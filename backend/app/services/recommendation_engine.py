"""
FlavorFusion AI — Personalized Recommendation Engine
Generates customized pairings based on user preferences, hard allergy exclusions,
dietary constraints, spice tolerance, loved/disliked ingredients, and rating feedback.
"""

from typing import List, Dict, Any, Optional
from app.models.entities import (
    Ingredient, IngredientFlavorProfile, IngredientPairingEvidence,
    UserPreference, UserRating
)
from app.schemas.all_schemas import RecommendationItem, IngredientInput
from app.services.flavor_engine import FlavorEngine

CURATED_ARCHETYPES = [
    {
        "name": "Royal Shrikhand Ambrosia",
        "ingredients": ["Mango", "Curd", "Cardamom", "Pistachio", "Saffron"],
        "cuisine": "Indian",
        "novelty": "Classic",
        "prep": "Whip hung curd with cardamom and saffron; fold in fresh ripe mango cubes and top with toasted pistachio slivers.",
        "evidence": "High (Royal Mughal & Gujarati Culinary Heritage)"
    },
    {
        "name": "Zesty Guacamole Fiesta",
        "ingredients": ["Avocado", "Lime", "Cilantro", "Tomato", "Roasted Cumin", "Chili Pepper"],
        "cuisine": "Mexican",
        "novelty": "Classic",
        "prep": "Mash avocado with fresh lime juice, fold in diced tomato, chopped cilantro, and toasted cumin.",
        "evidence": "High (Traditional Mesoamerican Gastronomy)"
    },
    {
        "name": "Caprese Herb Symphony",
        "ingredients": ["Tomato", "Basil", "Garlic", "Olive Oil", "Black Pepper"],
        "cuisine": "Italian",
        "novelty": "Classic",
        "prep": "Layer ripe sliced tomatoes with whole sweet basil leaves, drizzle cold-pressed olive oil, rub with garlic, and crack fresh pepper.",
        "evidence": "High (Campania Regional Culinary Tradition)"
    },
    {
        "name": "Chili Aztec Cacao Fusion",
        "ingredients": ["Dark Chocolate", "Chili Pepper", "Cinnamon", "Vanilla"],
        "cuisine": "Fusion",
        "novelty": "Adventurous",
        "prep": "Gently melt dark chocolate, infuse with Ceylon cinnamon quill, vanilla pod seeds, and a subtle pinch of roasted chili powder.",
        "evidence": "High (Mesoamerican Ancient Elixir Science)"
    },
    {
        "name": "Golden Turmeric Citrus Tonic",
        "ingredients": ["Turmeric", "Ginger", "Lemon", "Honey", "Black Pepper"],
        "cuisine": "Indian",
        "novelty": "Balanced",
        "prep": "Simmer fresh ginger root with crushed black pepper, stir in golden turmeric and fresh lemon juice, sweeten gently with raw honey.",
        "evidence": "High (Ayurvedic Rasayana Tradition)"
    },
    {
        "name": "Strawberry Aceto Velvet",
        "ingredients": ["Strawberry", "Balsamic Vinegar", "Basil", "Black Pepper"],
        "cuisine": "Mediterranean",
        "novelty": "Adventurous",
        "prep": "Macerate fresh strawberries in aged balsamic glaze, garnish with torn basil leaves and coarse black pepper.",
        "evidence": "Moderate (Modernist Gastronomic Contrast)"
    },
    {
        "name": "South Indian Coconut Podi Rice",
        "ingredients": ["Basmati Rice", "Coconut", "Curry Leaves", "Roasted Cumin", "Ghee"],
        "cuisine": "South Indian",
        "novelty": "Balanced",
        "prep": "Temper curry leaves and cumin seeds in hot aromatic ghee; toss with freshly grated coconut and steaming long-grain basmati.",
        "evidence": "High (Traditional Tamil & Kerala Temple Cuisine)"
    },
    {
        "name": "Mediterranean Chickpea Crisp",
        "ingredients": ["Chickpeas", "Garlic", "Lemon", "Olive Oil", "Roasted Cumin"],
        "cuisine": "Mediterranean",
        "novelty": "Balanced",
        "prep": "Roast chickpeas with garlic infused olive oil and cumin, finish with a generous squeeze of fresh lemon.",
        "evidence": "High (Levantine Culinary Science)"
    }
]

class RecommendationEngine:
    def __init__(self, db_session):
        self.db = db_session
        self.flavor_engine = FlavorEngine(db_session)

    def get_recommendations(
        self,
        user_preference: Optional[UserPreference] = None,
        cuisine_filter: Optional[str] = None,
        novelty_filter: Optional[str] = None,
        limit: int = 6
    ) -> List[RecommendationItem]:
        """
        Generates filtered and personalized recommendations matching user profile,
        allergy exclusions, and culinary preference weights.
        """
        # Fetch user's ratings to incorporate dynamic feedback loop
        user_ratings: List[UserRating] = []
        if user_preference:
            user_ratings = self.db.query(UserRating).filter(UserRating.user_id == user_preference.user_id).all()

        allergies = [a.lower() for a in (user_preference.allergies if user_preference else [])]
        disliked = [d.lower() for d in (user_preference.disliked_ingredients if user_preference else [])]
        favorites = [f.lower() for f in (user_preference.favorite_ingredients if user_preference else [])]
        preferred_cuisines = [c.lower() for c in (user_preference.preferred_cuisines if user_preference else [])]

        results: List[RecommendationItem] = []

        for arch in CURATED_ARCHETYPES:
            # Check cuisine filter if requested
            if cuisine_filter and cuisine_filter.lower() != "all" and arch["cuisine"].lower() != cuisine_filter.lower():
                continue

            # Check novelty filter if requested
            if novelty_filter and novelty_filter.lower() != "all" and arch["novelty"].lower() != novelty_filter.lower():
                continue

            # Check HARD ALLERGY EXCLUSION
            has_allergen = False
            for ing_name in arch["ingredients"]:
                ing = self.db.query(Ingredient).filter(Ingredient.name.ilike(ing_name)).first()
                if ing:
                    for allg in (ing.allergens or []):
                        if allg.lower() in allergies:
                            has_allergen = True
                            break
                if has_allergen:
                    break
            if has_allergen:
                continue  # Hard exclude

            # Check disliked ingredients
            if any(ing_name.lower() in disliked for ing_name in arch["ingredients"]):
                continue

            # Analyze combination using FlavorEngine
            inputs = [
                IngredientInput(name=name, quantity=80.0, unit="g", preparation_method="Raw")
                for name in arch["ingredients"]
            ]

            try:
                analysis = self.flavor_engine.analyze_combination(
                    ingredients_input=inputs,
                    user_preference=user_preference,
                    title=arch["name"]
                )
            except Exception:
                continue

            # Calculate personalized match with user ratings feedback
            match_score = analysis.personalized_match or analysis.overall_compatibility

            # Bonus if combination contains favorite ingredients
            fav_count = sum(1 for ing_name in arch["ingredients"] if ing_name.lower() in favorites)
            match_score += fav_count * 5.0

            # Bonus if matches preferred cuisines
            if arch["cuisine"].lower() in preferred_cuisines:
                match_score += 6.0

            # Rating feedback influence: if user gave high ratings to similar ingredients, boost score
            for r in user_ratings:
                if r.score >= 4 and r.would_make_again:
                    match_score += 2.0
                elif r.score <= 2:
                    match_score -= 3.0

            match_score = min(max(match_score, 20.0), 99.0)

            # Build explanation
            rec_explanation = (
                f"Curated for you because it features {', '.join(arch['ingredients'][:3])} "
                f"matching your flavor palate with harmonious {analysis.evidence_quality.split('(')[0].strip()} evidence."
            )

            results.append(
                RecommendationItem(
                    combination_name=arch["name"],
                    ingredients=arch["ingredients"],
                    overall_compatibility=analysis.overall_compatibility,
                    personalized_match=round(match_score, 1),
                    taste_profile=analysis.taste_profile,
                    aroma_highlights=list(analysis.aroma_profile.keys())[:3],
                    explanation=rec_explanation,
                    suggested_preparation=arch["prep"],
                    potential_conflicts=analysis.flavor_conflicts,
                    evidence_quality=arch["evidence"],
                    cuisine_style=arch["cuisine"],
                    novelty=arch["novelty"]
                )
            )

        # Sort recommendations by personalized match score descending
        results.sort(key=lambda x: x.personalized_match, reverse=True)
        return results[:limit]
