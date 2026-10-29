export interface FlavorProfileData {
  sweet: number;
  salty: number;
  sour: number;
  bitter: number;
  umami: number;
  spicy: number;
  intensity: number;
  primary_aromas: string[];
  texture_profile: string[];
  dominant_compounds: string[];
}

export interface Ingredient {
  id: number;
  name: string;
  slug: string;
  category: string;
  description?: string;
  image_url?: string;
  default_unit: string;
  allergens: string[];
  cuisines: string[];
  is_curated: boolean;
  flavor_profile?: FlavorProfileData;
}

export interface SelectedIngredient {
  name: string;
  quantity: number;
  unit: string;
  preparation_method: string;
  category?: string;
}

export interface PairwiseInteraction {
  ingredient_a: string;
  ingredient_b: string;
  affinity_score: number;
  reason: string;
  shared_compounds: string[];
  conflict?: string;
}

export interface RatioItem {
  ingredient: string;
  ratio: string;
  recommended_grams?: number;
}

export interface DishSuggestion {
  name: string;
  description: string;
  estimated_time_mins?: number;
  cook_time_mins?: number;
  vibe_tag?: string;
  difficulty?: string;
  meal_type?: string;
}

export interface CombinationAnalysis {
  id?: number;
  title: string;
  overall_compatibility: number;
  personalized_match?: number | null;
  tastes_like?: string;
  tastes_like_explanation?: string;
  vibe_check?: string;
  shared_molecules?: string[];
  shared_molecule_count?: number;
  molecular_taste_synthesis?: string;
  possible_dishes?: DishSuggestion[];
  taste_profile: {
    sweet: number;
    salty: number;
    sour: number;
    bitter: number;
    umami: number;
    spicy: number;
  };
  aroma_profile: Record<string, number>;
  texture_profile: Record<string, number>;
  interaction_notes: string[];
  pairwise_matrix: PairwiseInteraction[];
  flavor_conflicts: string[];
  suggested_ratios: RatioItem[];
  complementary_suggestions: string[];
  evidence_quality: string;
  uncertainty_score: number;
  explanation: string;
}

export interface VisionCandidate {
  ingredient_name: string;
  confidence: number;
  category: string;
  visual_cues: string[];
}

export interface VisionIdentifyResponse {
  candidates: VisionCandidate[];
  image_url?: string;
  provider_used: string;
  is_mock: boolean;
  message: string;
}

export interface RecipeIngredientItem {
  name: string;
  quantity: number;
  unit: string;
  notes?: string;
}

export interface NeededIngredientItem {
  name: string;
  amount: string;
  purpose?: string;
}

export interface Recipe {
  id?: number;
  title: string;
  summary: string;
  cuisine: string;
  meal_type: string;
  prep_time_mins: number;
  cook_time_mins: number;
  servings: number;
  difficulty: string;
  ingredients_list: RecipeIngredientItem[];
  steps: string[];
  missing_ingredients: string[];
  substitutions: string[];
  allergens: string[];
  required_tools?: string[];
  required_vessels?: string[];
  needed_ingredients?: NeededIngredientItem[];
  generation_mode: string;
  is_saved?: boolean;
  is_wishlisted?: boolean;
}

export interface RecommendationItem {
  combination_name: string;
  ingredients: string[];
  overall_compatibility: number;
  personalized_match: number;
  taste_profile: Record<string, number>;
  aroma_highlights: string[];
  explanation: string;
  suggested_preparation: string;
  potential_conflicts: string[];
  evidence_quality: string;
  cuisine_style: string;
  novelty: string;
}

export interface User {
  id: number;
  email: string;
  full_name?: string;
  is_active: boolean;
  is_admin: boolean;
}

export interface UserPreferences {
  preferred_cuisines: string[];
  favorite_ingredients: string[];
  disliked_ingredients: string[];
  texture_preferences: string[];
  aroma_preferences: string[];
  spice_tolerance: number;
  sweet_affinity: number;
  sour_affinity: number;
  bitter_affinity: number;
  umami_affinity: number;
  salty_affinity: number;
  dietary_preferences: string[];
  allergies: string[];
  budget_preference: string;
  prep_time_preference: number;
  adventurousness: number;
}

export interface SuggestedPairingItem {
  title: string;
  ingredients: string[];
  tastes_like?: string;
  reason?: string;
}

export interface AssistantChatRequest {
  message: string;
  current_ingredients?: string[];
}

export interface AssistantChatResponse {
  reply: string;
  suggested_pairings: SuggestedPairingItem[];
  vibe?: string;
}

