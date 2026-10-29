import datetime
from sqlalchemy import (
    Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Text, JSON
)
from sqlalchemy.orm import relationship
from app.database.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    # Relationships
    preferences = relationship("UserPreference", back_populates="user", uselist=False, cascade="all, delete-orphan")
    predictions = relationship("Prediction", back_populates="user", cascade="all, delete-orphan")
    saved_combinations = relationship("SavedCombination", back_populates="user", cascade="all, delete-orphan")
    recipes = relationship("Recipe", back_populates="user", cascade="all, delete-orphan")
    ratings = relationship("UserRating", back_populates="user", cascade="all, delete-orphan")


class UserPreference(Base):
    __tablename__ = "user_preferences"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    
    # JSON arrays/objects
    preferred_cuisines = Column(JSON, default=list)  # ["Indian", "Mediterranean", "Italian", ...]
    favorite_ingredients = Column(JSON, default=list)  # ["Mango", "Cardamom", "Garlic", ...]
    disliked_ingredients = Column(JSON, default=list)  # ["Cilantro", "Bitter Gourd", ...]
    texture_preferences = Column(JSON, default=list)  # ["Creamy", "Crispy", "Smooth"]
    aroma_preferences = Column(JSON, default=list)  # ["Citrus", "Herbal", "Warm Spice"]
    
    # Specific attributes
    spice_tolerance = Column(Integer, default=3)  # 1 to 5 scale
    sweet_affinity = Column(Integer, default=3)  # 1 to 5
    sour_affinity = Column(Integer, default=3)   # 1 to 5
    bitter_affinity = Column(Integer, default=2) # 1 to 5
    umami_affinity = Column(Integer, default=4)  # 1 to 5
    salty_affinity = Column(Integer, default=3)  # 1 to 5
    
    dietary_preferences = Column(JSON, default=list)  # ["Vegetarian", "Vegan", "Gluten-Free", ...]
    allergies = Column(JSON, default=list)  # Hard exclusions: ["Dairy", "Nuts", "Gluten", "Shellfish", ...]
    budget_preference = Column(String(50), default="Moderate")  # "Budget", "Moderate", "Gourmet"
    prep_time_preference = Column(Integer, default=30)  # minutes
    adventurousness = Column(Integer, default=3)  # 1 (classic) to 5 (radical experimental)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    user = relationship("User", back_populates="preferences")


class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True, nullable=False)
    slug = Column(String(100), unique=True, index=True, nullable=False)
    category = Column(String(50), index=True, nullable=False)  # "Produce", "Spice", "Dairy", "Pantry", etc.
    description = Column(Text, nullable=True)
    image_url = Column(String(500), nullable=True)
    default_unit = Column(String(20), default="g")
    allergens = Column(JSON, default=list)  # ["Dairy", "Nuts", etc.]
    cuisines = Column(JSON, default=list)  # ["Indian", "Global", etc.]
    is_curated = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationships
    flavor_profile = relationship("IngredientFlavorProfile", back_populates="ingredient", uselist=False, cascade="all, delete-orphan")


class IngredientFlavorProfile(Base):
    __tablename__ = "ingredient_flavor_profiles"

    id = Column(Integer, primary_key=True, index=True)
    ingredient_id = Column(Integer, ForeignKey("ingredients.id"), unique=True, nullable=False)
    
    # 0 to 10 scale for 6 basic tastes
    sweet = Column(Float, default=0.0)
    salty = Column(Float, default=0.0)
    sour = Column(Float, default=0.0)
    bitter = Column(Float, default=0.0)
    umami = Column(Float, default=0.0)
    spicy = Column(Float, default=0.0)
    
    intensity = Column(Float, default=5.0)  # 1 to 10 overall flavor strength
    
    # Aromas: dict or list of {aroma: score} e.g. {"fruity": 8, "floral": 4}
    primary_aromas = Column(JSON, default=list)  # ["Fruity", "Floral", "Warm Spice"]
    texture_profile = Column(JSON, default=list)  # ["Juicy", "Soft", "Smooth"]
    dominant_compounds = Column(JSON, default=list)  # ["Limonene", "Eugenol", "Vanillin", ...]
    
    ingredient = relationship("Ingredient", back_populates="flavor_profile")


class IngredientPairingEvidence(Base):
    __tablename__ = "ingredient_pairing_evidence"

    id = Column(Integer, primary_key=True, index=True)
    ingredient_a_name = Column(String(100), index=True, nullable=False)
    ingredient_b_name = Column(String(100), index=True, nullable=False)
    affinity_score = Column(Float, default=70.0)  # 0 to 100
    shared_compounds = Column(JSON, default=list)  # ["Terpene", "Linalool"]
    culinary_evidence = Column(Text, nullable=True)  # "Classic North Indian lassi and dessert combination"
    source = Column(String(100), default="Curated Culinary Knowledge Base")
    is_experimental = Column(Boolean, default=False)


class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)  # nullable for guest users
    title = Column(String(255), nullable=False)
    
    # Scores (0 to 100)
    overall_compatibility = Column(Float, nullable=False)
    personalized_match = Column(Float, nullable=True)
    
    # Detailed calculated profiles
    taste_profile = Column(JSON, nullable=False)  # {"sweet": 6.2, "sour": 3.1, ...}
    aroma_profile = Column(JSON, nullable=False)  # {"Fruity": 45, "Herbal": 20, ...}
    texture_profile = Column(JSON, nullable=False) # {"Creamy": 60, "Crunchy": 10, ...}
    
    # Explainable factors
    interaction_notes = Column(JSON, default=list)  # List of why pairings work
    flavor_conflicts = Column(JSON, default=list)  # Warnings / potential clashes
    suggested_ratios = Column(JSON, default=list)  # [{"ingredient": "Mango", "ratio": "60%"}]
    complementary_suggestions = Column(JSON, default=list)  # ["Pistachio", "Saffron"]
    evidence_quality = Column(String(50), default="High")  # "High", "Moderate", "Exploratory"
    uncertainty_score = Column(Float, default=15.0)  # 0 to 100
    tastes_like = Column(String(255), nullable=True)
    tastes_like_explanation = Column(Text, nullable=True)
    vibe_check = Column(String(100), default="✨ Chef's Kiss")
    shared_molecules = Column(JSON, default=list)
    shared_molecule_count = Column(Integer, default=0)
    molecular_taste_synthesis = Column(Text, nullable=True)
    possible_dishes = Column(JSON, default=list)
    
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="predictions")
    ingredients = relationship("PredictionIngredient", back_populates="prediction", cascade="all, delete-orphan")
    recipes = relationship("Recipe", back_populates="prediction")
    saved_as = relationship("SavedCombination", back_populates="prediction")


class PredictionIngredient(Base):
    __tablename__ = "prediction_ingredients"

    id = Column(Integer, primary_key=True, index=True)
    prediction_id = Column(Integer, ForeignKey("predictions.id"), nullable=False)
    ingredient_name = Column(String(100), nullable=False)
    quantity = Column(Float, default=100.0)
    unit = Column(String(20), default="g")
    preparation_method = Column(String(50), default="Raw")  # "Raw", "Cooked", "Roasted", "Sautéed", "Boiled"

    prediction = relationship("Prediction", back_populates="ingredients")


class SavedCombination(Base):
    __tablename__ = "saved_combinations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    prediction_id = Column(Integer, ForeignKey("predictions.id"), nullable=False)
    custom_title = Column(String(255), nullable=True)
    notes = Column(Text, nullable=True)
    tags = Column(JSON, default=list)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="saved_combinations")
    prediction = relationship("Prediction", back_populates="saved_as")


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    prediction_id = Column(Integer, ForeignKey("predictions.id"), nullable=True)
    title = Column(String(255), nullable=False)
    summary = Column(Text, nullable=True)
    cuisine = Column(String(100), default="Fusion")
    meal_type = Column(String(50), default="Dinner")  # "Breakfast", "Lunch", "Dinner", "Dessert", "Beverage"
    prep_time_mins = Column(Integer, default=15)
    cook_time_mins = Column(Integer, default=20)
    servings = Column(Integer, default=2)
    difficulty = Column(String(50), default="Medium")  # "Easy", "Medium", "Advanced"
    
    ingredients_list = Column(JSON, default=list)  # [{name, quantity, unit, optional}]
    steps = Column(JSON, default=list)  # ["Step 1...", "Step 2..."]
    missing_ingredients = Column(JSON, default=list)
    substitutions = Column(JSON, default=list)
    allergens = Column(JSON, default=list)
    required_tools = Column(JSON, default=list)  # ["12-inch Cast Iron Skillet", "Chef's Knife", ...]
    required_vessels = Column(JSON, default=list)  # ["Heavy-Bottom Pot", "Baking Sheet", ...]
    needed_ingredients = Column(JSON, default=list)  # [{"name": "Olive Oil", "amount": "2 tbsp", "purpose": "Cooking fat"}]
    generation_mode = Column(String(50), default="Curated Culinary Engine")  # "LLM (Gemini)" or "Curated Culinary Engine"
    is_saved = Column(Boolean, default=False)
    is_wishlisted = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="recipes")
    prediction = relationship("Prediction", back_populates="recipes")


class UserRating(Base):
    __tablename__ = "user_ratings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    combination_id = Column(Integer, ForeignKey("saved_combinations.id"), nullable=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"), nullable=True)
    score = Column(Integer, nullable=False)  # 1 to 5 stars
    comment = Column(Text, nullable=True)
    taste_feedback = Column(JSON, default=dict)  # {"too_sweet": false, "too_spicy": false, etc.}
    would_make_again = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="ratings")
