from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.entities import Recipe, Prediction, User
from app.schemas.all_schemas import (
    RecipeGenerateRequest, RecipeResponse, RecipeIngredientItem, NeededIngredientItem
)
from app.services.recipe_engine import RecipeEngine
from app.api.deps import get_current_user_optional, get_current_user
from app.data.curated_recipes import CURATED_RECIPE_CATALOG

router = APIRouter(prefix="/recipes", tags=["Recipe Generator"])

@router.get("/catalog", response_model=List[RecipeResponse])
def get_recipe_catalog(
    q: Optional[str] = None,
    cuisine: Optional[str] = None,
    meal_type: Optional[str] = None,
    difficulty: Optional[str] = None,
    current_user: Optional[User] = Depends(get_current_user_optional),
    db: Session = Depends(get_db)
):
    """
    Searchable Catalog of Curated Iconic Recipes.
    Filters by text search (q), cuisine, meal_type, and difficulty.
    Includes ingredients, tools, vessels, and step-by-step preparation.
    """
    results = []
    
    # Check which recipes this user has saved or wishlisted in DB
    user_saved_titles = set()
    user_wishlist_titles = set()
    if current_user:
        user_recipes = db.query(Recipe).filter(Recipe.user_id == current_user.id).all()
        for r in user_recipes:
            if r.is_saved:
                user_saved_titles.add(r.title.lower().strip())
            if r.is_wishlisted:
                user_wishlist_titles.add(r.title.lower().strip())

    for item in CURATED_RECIPE_CATALOG:
        # Search query filter
        if q:
            query = q.lower().strip()
            title_match = query in item["title"].lower()
            summary_match = query in item.get("summary", "").lower()
            cuisine_match = query in item.get("cuisine", "").lower()
            ing_match = any(query in ing["name"].lower() for ing in item.get("ingredients_list", []))
            tool_match = any(query in t.lower() for t in item.get("required_tools", []))
            vessel_match = any(query in v.lower() for v in item.get("required_vessels", []))
            if not (title_match or summary_match or cuisine_match or ing_match or tool_match or vessel_match):
                continue

        # Cuisine filter
        if cuisine and cuisine.lower() != "all" and item.get("cuisine", "").lower() != cuisine.lower():
            continue

        # Meal type filter
        if meal_type and meal_type.lower() != "all" and item.get("meal_type", "").lower() != meal_type.lower():
            continue

        # Difficulty filter
        if difficulty and difficulty.lower() != "all" and item.get("difficulty", "").lower() != difficulty.lower():
            continue

        t_lower = item["title"].lower().strip()
        is_saved = t_lower in user_saved_titles
        is_wishlisted = t_lower in user_wishlist_titles

        ing_items = [RecipeIngredientItem(**i) for i in item.get("ingredients_list", [])]
        needed_items = [NeededIngredientItem(**n) for n in item.get("needed_ingredients", [])]

        results.append(
            RecipeResponse(
                id=item["id"],
                title=item["title"],
                summary=item.get("summary", ""),
                cuisine=item.get("cuisine", "Fusion"),
                meal_type=item.get("meal_type", "Dinner"),
                prep_time_mins=item.get("prep_time_mins", 15),
                cook_time_mins=item.get("cook_time_mins", 20),
                servings=item.get("servings", 2),
                difficulty=item.get("difficulty", "Medium"),
                ingredients_list=ing_items,
                steps=item.get("steps", []),
                missing_ingredients=item.get("missing_ingredients", []),
                substitutions=item.get("substitutions", []),
                allergens=item.get("allergens", []),
                required_tools=item.get("required_tools", []),
                required_vessels=item.get("required_vessels", []),
                needed_ingredients=needed_items,
                generation_mode=item.get("generation_mode", "Master Chef Curated"),
                is_saved=is_saved,
                is_wishlisted=is_wishlisted
            )
        )

    return results

@router.get("/catalog/{recipe_id}", response_model=RecipeResponse)
def get_catalog_recipe(
    recipe_id: int,
    current_user: Optional[User] = Depends(get_current_user_optional),
    db: Session = Depends(get_db)
):
    target = next((r for r in CURATED_RECIPE_CATALOG if r["id"] == recipe_id), None)
    if not target:
        raise HTTPException(status_code=404, detail="Catalog recipe not found.")

    is_saved = False
    is_wishlisted = False
    if current_user:
        rec = db.query(Recipe).filter(
            Recipe.user_id == current_user.id,
            Recipe.title == target["title"]
        ).first()
        if rec:
            is_saved = rec.is_saved or False
            is_wishlisted = rec.is_wishlisted or False

    ing_items = [RecipeIngredientItem(**i) for i in target.get("ingredients_list", [])]
    needed_items = [NeededIngredientItem(**n) for n in target.get("needed_ingredients", [])]

    return RecipeResponse(
        id=target["id"],
        title=target["title"],
        summary=target.get("summary", ""),
        cuisine=target.get("cuisine", "Fusion"),
        meal_type=target.get("meal_type", "Dinner"),
        prep_time_mins=target.get("prep_time_mins", 15),
        cook_time_mins=target.get("cook_time_mins", 20),
        servings=target.get("servings", 2),
        difficulty=target.get("difficulty", "Medium"),
        ingredients_list=ing_items,
        steps=target.get("steps", []),
        missing_ingredients=target.get("missing_ingredients", []),
        substitutions=target.get("substitutions", []),
        allergens=target.get("allergens", []),
        required_tools=target.get("required_tools", []),
        required_vessels=target.get("required_vessels", []),
        needed_ingredients=needed_items,
        generation_mode=target.get("generation_mode", "Master Chef Curated"),
        is_saved=is_saved,
        is_wishlisted=is_wishlisted
    )

@router.post("/generate", response_model=RecipeResponse)
def generate_recipe(
    request: RecipeGenerateRequest,
    current_user: Optional[User] = Depends(get_current_user_optional),
    db: Session = Depends(get_db)
):
    # If prediction_id is given and ingredients are empty, populate from prediction
    if request.prediction_id and not request.ingredients:
        pred = db.query(Prediction).filter(Prediction.id == request.prediction_id).first()
        if pred and pred.ingredients:
            from app.schemas.all_schemas import IngredientInput
            request.ingredients = [
                IngredientInput(
                    name=pi.ingredient_name,
                    quantity=pi.quantity,
                    unit=pi.unit,
                    preparation_method=pi.preparation_method
                ) for pi in pred.ingredients
            ]

    engine = RecipeEngine(db)
    try:
        response = engine.generate_recipe(request)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    # Persist the generated recipe
    recipe_record = Recipe(
        user_id=current_user.id if current_user else None,
        prediction_id=request.prediction_id,
        title=response.title,
        summary=response.summary,
        cuisine=response.cuisine,
        meal_type=response.meal_type,
        prep_time_mins=response.prep_time_mins,
        cook_time_mins=response.cook_time_mins,
        servings=response.servings,
        difficulty=response.difficulty,
        ingredients_list=[i.model_dump() for i in response.ingredients_list],
        steps=response.steps,
        missing_ingredients=response.missing_ingredients,
        substitutions=response.substitutions,
        allergens=response.allergens,
        required_tools=response.required_tools,
        needed_ingredients=[n.model_dump() for n in response.needed_ingredients],
        generation_mode=response.generation_mode,
        is_saved=False
    )
    db.add(recipe_record)
    db.commit()
    db.refresh(recipe_record)

    response.id = recipe_record.id
    return response

@router.get("/{recipe_id}", response_model=RecipeResponse)
def get_recipe(
    recipe_id: int,
    current_user: Optional[User] = Depends(get_current_user_optional),
    db: Session = Depends(get_db)
):
    r = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not r:
        # Check catalog
        cat = next((item for item in CURATED_RECIPE_CATALOG if item["id"] == recipe_id), None)
        if cat:
            is_s = False
            is_w = False
            if current_user:
                ur = db.query(Recipe).filter(Recipe.user_id == current_user.id, Recipe.title == cat["title"]).first()
                if ur:
                    is_s = ur.is_saved or False
                    is_w = ur.is_wishlisted or False
            return RecipeResponse(
                id=cat["id"],
                title=cat["title"],
                summary=cat.get("summary", ""),
                cuisine=cat.get("cuisine", "Fusion"),
                meal_type=cat.get("meal_type", "Dinner"),
                prep_time_mins=cat.get("prep_time_mins", 15),
                cook_time_mins=cat.get("cook_time_mins", 20),
                servings=cat.get("servings", 2),
                difficulty=cat.get("difficulty", "Medium"),
                ingredients_list=[RecipeIngredientItem(**i) for i in cat.get("ingredients_list", [])],
                steps=cat.get("steps", []),
                missing_ingredients=cat.get("missing_ingredients", []),
                substitutions=cat.get("substitutions", []),
                allergens=cat.get("allergens", []),
                required_tools=cat.get("required_tools", []),
                required_vessels=cat.get("required_vessels", []),
                needed_ingredients=[NeededIngredientItem(**n) for n in cat.get("needed_ingredients", [])],
                generation_mode=cat.get("generation_mode", "Master Chef Curated"),
                is_saved=is_s,
                is_wishlisted=is_w
            )
        raise HTTPException(status_code=404, detail="Recipe not found.")

    ing_items = [RecipeIngredientItem(**item) for item in (r.ingredients_list or [])]
    needed_items = [NeededIngredientItem(**item) for item in (r.needed_ingredients or [])]
    return RecipeResponse(
        id=r.id,
        title=r.title,
        summary=r.summary or "",
        cuisine=r.cuisine or "Fusion",
        meal_type=r.meal_type or "Dinner",
        prep_time_mins=r.prep_time_mins or 15,
        cook_time_mins=r.cook_time_mins or 20,
        servings=r.servings or 2,
        difficulty=r.difficulty or "Medium",
        ingredients_list=ing_items,
        steps=r.steps or [],
        missing_ingredients=r.missing_ingredients or [],
        substitutions=r.substitutions or [],
        allergens=r.allergens or [],
        required_tools=r.required_tools or [],
        required_vessels=getattr(r, "required_vessels", []) or [],
        needed_ingredients=needed_items,
        generation_mode=r.generation_mode or "Curated Culinary Engine",
        is_saved=r.is_saved or False,
        is_wishlisted=r.is_wishlisted or False
    )

@router.post("/{recipe_id}/save")
def toggle_save_recipe(
    recipe_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    r = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not r:
        cat = next((item for item in CURATED_RECIPE_CATALOG if item["id"] == recipe_id), None)
        if cat:
            r = db.query(Recipe).filter(Recipe.user_id == current_user.id, Recipe.title == cat["title"]).first()
            if not r:
                r = Recipe(
                    user_id=current_user.id,
                    title=cat["title"],
                    summary=cat.get("summary", ""),
                    cuisine=cat.get("cuisine", "Fusion"),
                    meal_type=cat.get("meal_type", "Dinner"),
                    prep_time_mins=cat.get("prep_time_mins", 15),
                    cook_time_mins=cat.get("cook_time_mins", 20),
                    servings=cat.get("servings", 2),
                    difficulty=cat.get("difficulty", "Medium"),
                    ingredients_list=cat.get("ingredients_list", []),
                    steps=cat.get("steps", []),
                    missing_ingredients=cat.get("missing_ingredients", []),
                    substitutions=cat.get("substitutions", []),
                    allergens=cat.get("allergens", []),
                    required_tools=cat.get("required_tools", []),
                    required_vessels=cat.get("required_vessels", []),
                    needed_ingredients=cat.get("needed_ingredients", []),
                    generation_mode=cat.get("generation_mode", "Master Chef Curated"),
                    is_saved=True,
                    is_wishlisted=False
                )
                db.add(r)
                db.commit()
                db.refresh(r)
                return {"id": r.id, "is_saved": True, "message": "Saved to library."}
        else:
            raise HTTPException(status_code=404, detail="Recipe not found.")

    r.user_id = current_user.id
    r.is_saved = not (r.is_saved or False)
    db.commit()
    return {"id": r.id, "is_saved": r.is_saved, "message": "Saved state updated."}

@router.post("/{recipe_id}/wishlist")
def toggle_wishlist_recipe(
    recipe_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    r = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not r:
        cat = next((item for item in CURATED_RECIPE_CATALOG if item["id"] == recipe_id), None)
        if cat:
            r = db.query(Recipe).filter(Recipe.user_id == current_user.id, Recipe.title == cat["title"]).first()
            if not r:
                r = Recipe(
                    user_id=current_user.id,
                    title=cat["title"],
                    summary=cat.get("summary", ""),
                    cuisine=cat.get("cuisine", "Fusion"),
                    meal_type=cat.get("meal_type", "Dinner"),
                    prep_time_mins=cat.get("prep_time_mins", 15),
                    cook_time_mins=cat.get("cook_time_mins", 20),
                    servings=cat.get("servings", 2),
                    difficulty=cat.get("difficulty", "Medium"),
                    ingredients_list=cat.get("ingredients_list", []),
                    steps=cat.get("steps", []),
                    missing_ingredients=cat.get("missing_ingredients", []),
                    substitutions=cat.get("substitutions", []),
                    allergens=cat.get("allergens", []),
                    required_tools=cat.get("required_tools", []),
                    required_vessels=cat.get("required_vessels", []),
                    needed_ingredients=cat.get("needed_ingredients", []),
                    generation_mode=cat.get("generation_mode", "Master Chef Curated"),
                    is_saved=False,
                    is_wishlisted=True
                )
                db.add(r)
                db.commit()
                db.refresh(r)
                return {"id": r.id, "is_wishlisted": True, "message": "Added to wishlist."}
        else:
            raise HTTPException(status_code=404, detail="Recipe not found.")

    r.user_id = current_user.id
    r.is_wishlisted = not (r.is_wishlisted or False)
    db.commit()
    return {"id": r.id, "is_wishlisted": r.is_wishlisted, "message": "Wishlist state updated."}

@router.get("/user/saved", response_model=List[RecipeResponse])
def get_saved_recipes(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    saved = db.query(Recipe).filter(Recipe.user_id == current_user.id, Recipe.is_saved == True).all()
    results = []
    for r in saved:
        ing_items = [RecipeIngredientItem(**item) for item in (r.ingredients_list or [])]
        needed_items = [NeededIngredientItem(**item) for item in (r.needed_ingredients or [])]
        results.append(
            RecipeResponse(
                id=r.id,
                title=r.title,
                summary=r.summary or "",
                cuisine=r.cuisine or "Fusion",
                meal_type=r.meal_type or "Dinner",
                prep_time_mins=r.prep_time_mins or 15,
                cook_time_mins=r.cook_time_mins or 20,
                servings=r.servings or 2,
                difficulty=r.difficulty or "Medium",
                ingredients_list=ing_items,
                steps=r.steps or [],
                missing_ingredients=r.missing_ingredients or [],
                substitutions=r.substitutions or [],
                allergens=r.allergens or [],
                required_tools=r.required_tools or [],
                needed_ingredients=needed_items,
                generation_mode=r.generation_mode or "Curated Culinary Engine",
                is_saved=True,
                is_wishlisted=r.is_wishlisted or False
            )
        )
    return results

@router.get("/user/wishlist", response_model=List[RecipeResponse])
def get_wishlisted_recipes(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    wishlisted = db.query(Recipe).filter(Recipe.user_id == current_user.id, Recipe.is_wishlisted == True).all()
    results = []
    for r in wishlisted:
        ing_items = [RecipeIngredientItem(**item) for item in (r.ingredients_list or [])]
        needed_items = [NeededIngredientItem(**item) for item in (r.needed_ingredients or [])]
        results.append(
            RecipeResponse(
                id=r.id,
                title=r.title,
                summary=r.summary or "",
                cuisine=r.cuisine or "Fusion",
                meal_type=r.meal_type or "Dinner",
                prep_time_mins=r.prep_time_mins or 15,
                cook_time_mins=r.cook_time_mins or 20,
                servings=r.servings or 2,
                difficulty=r.difficulty or "Medium",
                ingredients_list=ing_items,
                steps=r.steps or [],
                missing_ingredients=r.missing_ingredients or [],
                substitutions=r.substitutions or [],
                allergens=r.allergens or [],
                required_tools=r.required_tools or [],
                needed_ingredients=needed_items,
                generation_mode=r.generation_mode or "Curated Culinary Engine",
                is_saved=r.is_saved or False,
                is_wishlisted=True
            )
        )
    return results
