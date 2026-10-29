import os
import sys

# Ensure backend root directory is in sys.path
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database.session import SessionLocal
from app.models.entities import Ingredient, User

client = TestClient(app)

def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

# 1. Ingredient Search & Listing
def test_get_ingredients():
    response = client.get("/api/ingredients")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 10
    names = [i["name"] for i in data]
    assert "Mango" in names
    assert "Curd" in names

def test_search_ingredients():
    response = client.get("/api/ingredients/search?q=cardamom")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert data[0]["name"] == "Cardamom"

# 2. Multi-Ingredient Analysis (>2 and up to 30 ingredients)
def test_multi_ingredient_analysis_large_combination():
    # 7 ingredients test matching the prompt's example:
    # Mango, Curd, Honey, Cardamom, Mint, Lime, Roasted Cumin
    payload = {
        "title": "Royal Mango Medley",
        "ingredients": [
            {"name": "Mango", "quantity": 150.0, "unit": "g", "preparation_method": "Raw"},
            {"name": "Curd", "quantity": 100.0, "unit": "g", "preparation_method": "Raw"},
            {"name": "Honey", "quantity": 25.0, "unit": "g", "preparation_method": "Raw"},
            {"name": "Cardamom", "quantity": 3.0, "unit": "g", "preparation_method": "Raw"},
            {"name": "Mint", "quantity": 5.0, "unit": "g", "preparation_method": "Raw"},
            {"name": "Lime", "quantity": 10.0, "unit": "ml", "preparation_method": "Raw"},
            {"name": "Roasted Cumin", "quantity": 2.0, "unit": "g", "preparation_method": "Roasted"}
        ]
    }
    response = client.post("/api/combinations/analyze", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["overall_compatibility"] >= 75.0
    assert "sweet" in data["taste_profile"]
    assert "sour" in data["taste_profile"]
    assert len(data["suggested_ratios"]) == 7
    assert len(data["pairwise_matrix"]) > 0

# 3. Validation: Minimum, Maximum, and Duplicate Handling
def test_minimum_ingredient_validation():
    response = client.post("/api/combinations/analyze", json={"ingredients": []})
    assert response.status_code == 400

def test_duplicate_ingredient_handling():
    payload = {
        "ingredients": [
            {"name": "Mango", "quantity": 100.0, "unit": "g", "preparation_method": "Raw"},
            {"name": "Mango", "quantity": 50.0, "unit": "g", "preparation_method": "Raw"},
            {"name": "Lime", "quantity": 10.0, "unit": "ml", "preparation_method": "Raw"}
        ]
    }
    response = client.post("/api/combinations/analyze", json=payload)
    assert response.status_code == 200
    data = response.json()
    # Duplicate warning should be recorded
    conflict_text = " ".join(data["flavor_conflicts"])
    assert "Duplicate ingredient 'Mango'" in conflict_text
    # Should only have 2 unique ratio items (Mango & Lime)
    assert len(data["suggested_ratios"]) == 2

def test_missing_flavor_profile_handling():
    # Combination with an unknown custom ingredient
    payload = {
        "ingredients": [
            {"name": "Dragonfruit Essence", "quantity": 50.0, "unit": "g", "preparation_method": "Raw"},
            {"name": "Lime", "quantity": 10.0, "unit": "ml", "preparation_method": "Raw"}
        ]
    }
    response = client.post("/api/combinations/analyze", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "Exploratory" in data["evidence_quality"]
    assert data["uncertainty_score"] > 20.0

# 4. Authentication & Authorization
def test_auth_workflow():
    # Register test user
    test_email = "testchef@flavorfusion.ai"
    reg_resp = client.post("/api/auth/register", json={
        "email": test_email,
        "password": "ChefPassword123!",
        "full_name": "Test Chef"
    })
    # Should be 200 or 400 if already exists
    if reg_resp.status_code == 200:
        token = reg_resp.json()["access_token"]
    else:
        login_resp = client.post("/api/auth/login", json={
            "email": test_email,
            "password": "ChefPassword123!"
        })
        assert login_resp.status_code == 200
        token = login_resp.json()["access_token"]

    # Verify protected /me endpoint
    headers = {"Authorization": f"Bearer {token}"}
    me_resp = client.get("/api/auth/me", headers=headers)
    assert me_resp.status_code == 200
    assert me_resp.json()["email"] == test_email

# 5. Personalized Recommendations & Hard Allergy Exclusions
def test_allergy_hard_exclusion():
    # Log in as demo user
    login_resp = client.post("/api/auth/login", json={
        "email": "gourmet@flavorfusion.ai",
        "password": "Gourmet123!"
    })
    token = login_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Set allergy to "Dairy"
    client.put("/api/users/preferences", json={
        "preferred_cuisines": ["Indian"],
        "allergies": ["Dairy"],
        "favorite_ingredients": ["Mango"]
    }, headers=headers)

    # Analyze combo containing Curd (Dairy)
    combo_resp = client.post("/api/combinations/analyze", json={
        "ingredients": [
            {"name": "Mango", "quantity": 100.0, "unit": "g"},
            {"name": "Curd", "quantity": 100.0, "unit": "g"}
        ]
    }, headers=headers)
    assert combo_resp.status_code == 200
    data = combo_resp.json()
    # Personalized match MUST be 0.0 due to hard allergy constraint!
    assert data["personalized_match"] == 0.0
    assert any("ALLERGY" in c.upper() for c in data["flavor_conflicts"])

    # Reset allergy
    client.put("/api/users/preferences", json={
        "preferred_cuisines": ["Indian"],
        "allergies": [],
        "favorite_ingredients": ["Mango", "Cardamom"]
    }, headers=headers)

# 6. Recipe Generation
def test_recipe_generation():
    payload = {
        "ingredients": [
            {"name": "Mango", "quantity": 150.0, "unit": "g"},
            {"name": "Curd", "quantity": 100.0, "unit": "g"},
            {"name": "Cardamom", "quantity": 2.0, "unit": "g"}
        ],
        "servings": 4,
        "prefer_no_cook": True
    }
    response = client.post("/api/recipes/generate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["servings"] == 4
    assert len(data["steps"]) >= 3
    assert "generation_mode" in data

# 7. Image Upload Validation
def test_image_upload_invalid_type():
    files = {"file": ("test.txt", b"not an image", "text/plain")}
    response = client.post("/api/vision/identify", files=files)
    assert response.status_code == 400

def test_image_upload_valid_synthetic_image():
    from PIL import Image
    import io
    img = Image.new("RGB", (64, 64), color=(255, 200, 0)) # golden yellow
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)

    files = {"file": ("mango_sample.png", buf.getvalue(), "image/png")}
    response = client.post("/api/vision/identify", files=files)
    assert response.status_code == 200
    data = response.json()
    assert "candidates" in data
    detected_names = [c["ingredient_name"] for c in data["candidates"]]
    assert "Mango" in detected_names
    assert data["is_mock"] is False

# 8. Emergent Flavor Illusion (Vanilla + Soy Sauce = Salted Caramel)
def test_flavor_illusion_synergy():
    payload = {
        "title": "Vanilla Soy Illusion Test",
        "ingredients": [
            {"name": "Vanilla", "quantity": 100.0, "unit": "g"},
            {"name": "Soy Sauce", "quantity": 15.0, "unit": "ml"}
        ]
    }
    response = client.post("/api/combinations/analyze", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "Salted Caramel" in data["tastes_like"]
    assert "caramel" in data["tastes_like_explanation"].lower() or "sodium" in data["tastes_like_explanation"].lower() or "glutamate" in data["tastes_like_explanation"].lower()
    assert len(data["possible_dishes"]) >= 1
    assert any("Caramel" in d["name"] for d in data["possible_dishes"])

# 9. Recipe Wishlisting
def test_recipe_wishlist():
    # Login
    login_resp = client.post("/api/auth/login", json={
        "email": "gourmet@flavorfusion.ai",
        "password": "Gourmet123!"
    })
    token = login_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Generate recipe
    recipe_resp = client.post("/api/recipes/generate", json={
        "ingredients": [
            {"name": "Vanilla", "quantity": 100.0, "unit": "g"},
            {"name": "Soy Sauce", "quantity": 15.0, "unit": "ml"}
        ],
        "servings": 2
    }, headers=headers)
    assert recipe_resp.status_code == 200
    recipe_id = recipe_resp.json()["id"]

    # Toggle Wishlist
    wish_resp = client.post(f"/api/recipes/{recipe_id}/wishlist", headers=headers)
    assert wish_resp.status_code == 200
    assert wish_resp.json()["is_wishlisted"] is True

    # Verify in wishlist endpoint
    list_resp = client.get("/api/recipes/user/wishlist", headers=headers)
    assert list_resp.status_code == 200
    wishlist_ids = [r["id"] for r in list_resp.json()]
    assert recipe_id in wishlist_ids

# 10. AI Assistant Chat
def test_ai_assistant_chat():
    payload = {
        "message": "Why does vanilla ice cream and soy sauce taste like caramel?",
        "current_ingredients": ["Vanilla", "Soy Sauce"]
    }
    response = client.post("/api/assistant/chat", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "Salted Caramel" in data["reply"] or "caramel" in data["reply"].lower()
    assert len(data["suggested_pairings"]) >= 1
    assert data["suggested_pairings"][0]["ingredients"] == ["Vanilla", "Soy Sauce"]

# 11. Molecular Volatile Synthesis Test
def test_molecular_volatiles_synthesis():
    payload = {
        "title": "Molecular Test Tomato Basil Garlic",
        "ingredients": [
            {"name": "Tomato", "quantity": 100.0, "unit": "g"},
            {"name": "Basil", "quantity": 10.0, "unit": "g"},
            {"name": "Garlic", "quantity": 15.0, "unit": "g"}
        ]
    }
    response = client.post("/api/combinations/analyze", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "shared_molecules" in data
    assert "shared_molecule_count" in data
    assert data["shared_molecule_count"] >= 1
    assert data["molecular_taste_synthesis"] is not None
    assert len(data["molecular_taste_synthesis"]) > 20
    # Must not contain placeholder brackets
    assert "{" not in data["tastes_like"]

# 12. Recipe Catalog Search & Equipment
def test_recipe_catalog_search():
    # Search for pizza
    response = client.get("/api/recipes/catalog?q=pizza")
    assert response.status_code == 200
    catalog = response.json()
    assert len(catalog) >= 1
    pizza = catalog[0]
    assert "Pizza" in pizza["title"]
    assert len(pizza["required_tools"]) >= 1
    assert len(pizza["required_vessels"]) >= 1
    assert len(pizza["steps"]) >= 3
    assert len(pizza["ingredients_list"]) >= 3

if __name__ == "__main__":
    print("Testing health check...")
    test_health_check()
    print("Testing get ingredients...")
    test_get_ingredients()
    print("Testing search ingredients...")
    test_search_ingredients()
    print("Testing multi ingredient analysis...")
    test_multi_ingredient_analysis_large_combination()
    print("Testing minimum ingredient validation...")
    test_minimum_ingredient_validation()
    print("Testing duplicate ingredient handling...")
    test_duplicate_ingredient_handling()
    print("Testing missing flavor profile handling...")
    test_missing_flavor_profile_handling()
    print("Testing auth workflow...")
    test_auth_workflow()
    print("Testing allergy hard exclusion...")
    test_allergy_hard_exclusion()
    print("Testing recipe generation...")
    test_recipe_generation()
    print("Testing image upload invalid type...")
    test_image_upload_invalid_type()
    print("Testing image upload valid synthetic image...")
    test_image_upload_valid_synthetic_image()
    print("Testing flavor illusion synergy...")
    test_flavor_illusion_synergy()
    print("Testing recipe wishlist...")
    test_recipe_wishlist()
    print("Testing AI assistant chat...")
    test_ai_assistant_chat()
    print("Testing molecular volatiles synthesis...")
    test_molecular_volatiles_synthesis()
    print("Testing recipe catalog search...")
    test_recipe_catalog_search()
    print("ALL TESTS PASSED SUCCESSFULLY!")

