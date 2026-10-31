from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field

# ----------------- Auth & User Schemas -----------------
class UserBase(BaseModel):
    email: str
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str = Field(..., min_length=6)

class UserLogin(BaseModel):
    email: str
    password: str

class UserResponse(UserBase):
    id: int
    is_active: bool
    is_admin: bool

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse

# ----------------- User Preferences -----------------
class UserPreferenceBase(BaseModel):
    preferred_cuisines: List[str] = []
    favorite_ingredients: List[str] = []
    disliked_ingredients: List[str] = []
    texture_preferences: List[str] = []
    aroma_preferences: List[str] = []
    spice_tolerance: int = Field(default=3, ge=0, le=5)
    sweet_affinity: int = Field(default=3, ge=0, le=5)
    sour_affinity: int = Field(default=3, ge=0, le=5)
    bitter_affinity: int = Field(default=2, ge=0, le=5)
    umami_affinity: int = Field(default=4, ge=0, le=5)
    salty_affinity: int = Field(default=3, ge=0, le=5)
    dietary_preferences: List[str] = []
    allergies: List[str] = []
    budget_preference: str = "Moderate"
    prep_time_preference: int = 30
    adventurousness: int = Field(default=3, ge=1, le=5)

class UserPreferenceUpdate(UserPreferenceBase):
    pass

class UserPreferenceResponse(UserPreferenceBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True

# ----------------- Ingredient Schemas -----------------
class FlavorProfileData(BaseModel):
    sweet: float = Field(default=0.0, ge=0, le=10)
    salty: float = Field(default=0.0, ge=0, le=10)
    sour: float = Field(default=0.0, ge=0, le=10)
    bitter: float = Field(default=0.0, ge=0, le=10)
    umami: float = Field(default=0.0, ge=0, le=10)
    spicy: float = Field(default=0.0, ge=0, le=10)
    intensity: float = Field(default=5.0, ge=0, le=10)
    primary_aromas: List[str] = []
    texture_profile: List[str] = []
    dominant_compounds: List[str] = []

    class Config:
        from_attributes = True

class IngredientBase(BaseModel):
    name: str
    category: str
    description: Optional[str] = None
    image_url: Optional[str] = None
    default_unit: str = "g"
    allergens: List[str] = []
    cuisines: List[str] = []

class IngredientCreate(IngredientBase):
    flavor_profile: Optional[FlavorProfileData] = None

class IngredientResponse(IngredientBase):
    id: int
    slug: str
    is_curated: bool
    flavor_profile: Optional[FlavorProfileData] = None

    class Config:
        from_attributes = True

# ----------------- Flavor Lab & Combination Schemas -----------------
class IngredientInput(BaseModel):
    name: str
    quantity: float = Field(default=100.0, gt=0)
    unit: str = "g"
    preparation_method: str = "Raw"  # Raw, Cooked, Roasted, Sautéed, Boiled

class CombinationAnalyzeRequest(BaseModel):
    ingredients: List[IngredientInput]
    title: Optional[str] = None

class RatioItem(BaseModel):
    ingredient: str
    ratio: str
    recommended_grams: Optional[float] = None

class PairwiseInteraction(BaseModel):
    ingredient_a: str
    ingredient_b: str
    affinity_score: float
    reason: str
    shared_compounds: List[str] = []
    conflict: Optional[str] = None

class DishSuggestion(BaseModel):
    name: str
    description: str
    difficulty: str = "Easy"
    cook_time_mins: int = 15
    vibe_tag: str = "✨ Chef's Kiss"
    meal_type: str = "Snack / Dessert"

class CombinationAnalyzeResponse(BaseModel):
    id: Optional[int] = None
    title: str
    overall_compatibility: float
    personalized_match: Optional[float] = None
    taste_profile: Dict[str, float]  # sweet, salty, sour, bitter, umami, spicy
    aroma_profile: Dict[str, float]  # Fruity: 80, Herbal: 40, etc.
    texture_profile: Dict[str, float] # Creamy, Crunchy, etc.
    interaction_notes: List[str]
    pairwise_matrix: List[PairwiseInteraction] = []
    flavor_conflicts: List[str]
    suggested_ratios: List[RatioItem]
    complementary_suggestions: List[str]
    evidence_quality: str
    uncertainty_score: float
    explanation: str
    tastes_like: Optional[str] = None
    tastes_like_explanation: Optional[str] = None
    vibe_check: Optional[str] = None
    shared_molecules: List[str] = []
    shared_molecule_count: int = 0
    molecular_taste_synthesis: Optional[str] = None
    possible_dishes: List[DishSuggestion] = []

class CombinationSaveRequest(BaseModel):
    prediction_id: int
    custom_title: Optional[str] = None
    notes: Optional[str] = None
    tags: List[str] = []

class SavedCombinationResponse(BaseModel):
    id: int
    prediction_id: int
    custom_title: Optional[str] = None
    notes: Optional[str] = None
    tags: List[str] = []
    prediction: Optional[CombinationAnalyzeResponse] = None

# ----------------- Vision Schemas -----------------
class VisionCandidate(BaseModel):
    ingredient_name: str
    confidence: float
    category: str
    visual_cues: List[str] = []

class VisionIdentifyResponse(BaseModel):
    candidates: List[VisionCandidate]
    image_url: Optional[str] = None
    provider_used: str  # "Local Computer Vision Feature Model", "Google Gemini Vision API", etc.
    is_mock: bool = False
    message: str

class VisionConfirmRequest(BaseModel):
    confirmed_ingredients: List[str]

# ----------------- Recipe Schemas -----------------
class RecipeIngredientItem(BaseModel):
    name: str
    quantity: float
    unit: str
    notes: Optional[str] = None

class NeededIngredientItem(BaseModel):
    name: str
    amount: str
    purpose: Optional[str] = None

class RecipeGenerateRequest(BaseModel):
    ingredients: Optional[List[IngredientInput]] = None
    prediction_id: Optional[int] = None
    cuisine: Optional[str] = "Fusion"
    meal_type: Optional[str] = "Dinner"
    servings: int = Field(default=2, ge=1, le=12)
    prefer_quick: bool = False
    prefer_no_cook: bool = False
    dietary_constraints: List[str] = []

class RecipeResponse(BaseModel):
    id: Optional[int] = None
    title: str
    summary: str
    cuisine: str
    meal_type: str
    prep_time_mins: int
    cook_time_mins: int
    servings: int
    difficulty: str
    ingredients_list: List[RecipeIngredientItem]
    steps: List[str]
    missing_ingredients: List[str] = []
    substitutions: List[str] = []
    allergens: List[str] = []
    required_tools: List[str] = []
    required_vessels: List[str] = []
    needed_ingredients: List[NeededIngredientItem] = []
    generation_mode: str
    is_saved: bool = False
    is_wishlisted: bool = False

# ----------------- Assistant Schemas -----------------
class SuggestedPairingItem(BaseModel):
    title: str
    ingredients: List[str]
    tastes_like: str
    reason: str

class AssistantChatRequest(BaseModel):
    message: str
    current_ingredients: Optional[List[str]] = []
    history: Optional[List[Dict[str, str]]] = []

class AssistantChatResponse(BaseModel):
    reply: str
    suggested_pairings: List[SuggestedPairingItem] = []
    vibe: str = "Culinary Bestie"

# ----------------- Recommendation Schemas -----------------
class RecommendationItem(BaseModel):
    combination_name: str
    ingredients: List[str]
    overall_compatibility: float
    personalized_match: float
    taste_profile: Dict[str, float]
    aroma_highlights: List[str]
    explanation: str
    suggested_preparation: str
    potential_conflicts: List[str] = []
    evidence_quality: str
    cuisine_style: str
    novelty: str  # "Classic", "Balanced", "Adventurous"

class RecommendationFeedbackRequest(BaseModel):
    combination_name: str
    ingredients: List[str]
    score: int = Field(..., ge=1, le=5)
    comment: Optional[str] = None
    liked: bool = True

# ----------------- Rating Schemas -----------------
class RatingCreateRequest(BaseModel):
    score: int = Field(..., ge=1, le=5)
    comment: Optional[str] = None
    combination_id: Optional[int] = None
    recipe_id: Optional[int] = None
    taste_feedback: Dict[str, Any] = {}
    would_make_again: bool = True
