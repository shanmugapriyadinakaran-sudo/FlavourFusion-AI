"""
FlavorFusion AI — Culinary Recipe Generation Service
Generates authentic recipes from selected ingredients.
Supports optional Gemini LLM integration with an intelligent,
rule-based culinary synthesis engine fallback grounded in authentic gastronomy.
"""

import os
from typing import List, Dict, Any, Optional
from app.models.entities import Ingredient
from app.schemas.all_schemas import (
    RecipeGenerateRequest, RecipeResponse, RecipeIngredientItem, NeededIngredientItem, IngredientInput
)
from app.core.config import settings

class RecipeEngine:
    def __init__(self, db_session):
        self.db = db_session
        self.api_key = settings.GEMINI_API_KEY

    def generate_recipe(self, request: RecipeGenerateRequest) -> RecipeResponse:
        """
        Generates a structured culinary recipe tailored to selected ingredients,
        servings, prep style, and meal type.
        """
        ingredients = request.ingredients or []
        if not ingredients:
            raise ValueError("At least one ingredient is required to generate a recipe.")

        servings = max(request.servings, 1)

        # Scale ingredient quantities for requested servings
        scaled_ingredients: List[RecipeIngredientItem] = []
        allergens: List[str] = []

        for item in ingredients:
            name = item.name.strip().title()
            # Fetch allergen info from db
            db_ing = self.db.query(Ingredient).filter(Ingredient.name.ilike(name)).first()
            if db_ing:
                for a in (db_ing.allergens or []):
                    if a not in allergens:
                        allergens.append(a)

            unit_str = (item.unit or "g").strip()
            # Special scaling for pieces / pcs
            if unit_str.lower() in ["piece", "pieces", "pc", "pcs"]:
                scaled_qty = float(max(1, round((item.quantity or 1.0) * (servings / 2.0))))
            else:
                scaled_qty = round((item.quantity or 100.0) * (servings / 2.0), 1)

            scaled_ingredients.append(
                RecipeIngredientItem(
                    name=name,
                    quantity=scaled_qty,
                    unit=unit_str,
                    notes=f"Preparation: {item.preparation_method}" if item.preparation_method else None
                )
            )

        # Check if LLM integration is available
        if self.api_key:
            try:
                return self._generate_with_gemini(request, scaled_ingredients, allergens)
            except Exception as e:
                print(f"Gemini API recipe generation unavailable ({str(e)}); falling back to Culinary Engine.")

        return self._generate_with_culinary_engine(request, scaled_ingredients, allergens)

    def _generate_with_culinary_engine(
        self,
        request: RecipeGenerateRequest,
        ingredients: List[RecipeIngredientItem],
        allergens: List[str]
    ) -> RecipeResponse:
        """
        Intelligent culinary synthesis engine that formulates realistic, technique-driven
        recipes with kitchen tools, exact pantry additions, and detailed steps.
        """
        names = [x.name for x in ingredients]
        names_lower = [n.lower() for n in names]
        names_str = " ".join(names_lower)
        servings = request.servings

        # --- Ingredient Classification ---
        has_seafood = any(x in names_str for x in ["salmon", "shrimp", "tuna", "cod", "prawn", "crab"])
        has_meat = any(x in names_str for x in ["chicken", "bacon", "beef", "pork", "turkey", "lamb", "duck"])
        has_grain_pasta = any(x in names_str for x in ["rice", "pasta", "spaghetti", "penne", "noodle", "quinoa", "risotto", "couscous", "bread", "brioche", "sourdough"])
        has_dairy_fat = any(x in names_str for x in ["butter", "ghee", "curd", "yogurt", "cream", "cheese", "cheddar", "parmesan", "mozzarella", "feta"])
        has_tart_fresh = any(x in names_str for x in ["apple", "green apple", "lemon", "lime", "watermelon", "feta", "avocado", "cucumber", "balsamic vinegar", "strawberry"])
        has_sweet_dessert = any(x in names_str for x in ["vanilla", "dark chocolate", "chocolate", "honey", "mango", "maple syrup", "cinnamon"])
        has_wok_asian = any(x in names_str for x in ["soy sauce", "ginger", "sesame", "tofu", "broccoli", "bok choy"])
        has_curry_masala = any(x in names_str for x in ["cardamom", "cumin", "roasted cumin", "chana", "chickpea", "paneer", "garam masala", "turmeric"])

        # =========================================================================
        # ARCHETYPE 1: Pan-Seared Seafood with Citrus-Herb Reduction
        # =========================================================================
        if has_seafood:
            title = f"Pan-Seared Crispy {' & '.join(names[:2])} with Citrus-Herb Beurre Blanc"
            cuisine = request.cuisine if request.cuisine != "Fusion" else "French-Mediterranean"
            meal_type = "Dinner"
            prep_time = 10 if not request.prefer_quick else 5
            cook_time = 12 if not request.prefer_quick else 8
            difficulty = "Medium"

            summary = (
                f"Fresh {names[0]} pan-seared to develop a crisp golden crust, gently basted with "
                f"foaming butter, garlic aromatics, and finished with bright citrus and herbs ({', '.join(names[1:3])})."
            )

            required_tools = [
                "12-inch Heavy Stainless Steel or Cast Iron Skillet",
                "Slotted Fish Spatula",
                "Chef's Knife & Cutting Board",
                "Instant-Read Digital Thermometer",
                "Small Heavy Saucepan"
            ]

            needed_ingredients = [
                NeededIngredientItem(name="Extra Virgin Olive Oil", amount="1.5 tbsp", purpose="High-smoke point fat for searing"),
                NeededIngredientItem(name="Unsalted European Butter", amount="25g (approx. 2 tbsp)", purpose="Pan basting (arrosé) for nutty richness"),
                NeededIngredientItem(name="Fresh Garlic Cloves", amount="2 cloves, crushed", purpose="Aromatic skillet perfume"),
                NeededIngredientItem(name="Kosher Flaky Sea Salt", amount="1 tsp", purpose="Surface seasoning & moisture control"),
                NeededIngredientItem(name="Freshly Cracked Black Pepper", amount="1/2 tsp", purpose="Piquant savory balance")
            ]

            steps = [
                f"Pat {names[0]} thoroughly dry with paper towels to eliminate surface moisture for a golden crust; season both sides evenly with kosher salt and cracked pepper.",
                f"Place a 12-inch heavy skillet over medium-high heat. Add 1.5 tbsp olive oil and heat until shimmering and faintly smoking.",
                f"Carefully lay {names[0]} into the pan away from you. Press down gently with a fish spatula for 10 seconds to ensure full surface contact; sear undisturbed for 4-5 minutes until a crisp crust forms.",
                f"Gently flip over. Lower heat to medium and add butter, crushed garlic, and {', '.join(names[1:2]) if len(names) > 1 else 'fresh herbs'} to the skillet.",
                f"Tilt the pan slightly and continuously spoon the foaming melted butter over the seafood for 2-3 minutes until glistening and cooked to 140°F internal temperature.",
                f"Remove from heat immediately, squeeze fresh citrus over the pan, and rest on warm plates for 2 minutes before serving."
            ]

            missing_ingredients = ["Fresh capers (for briny pop)", "Microgreens or watercress garnish"]
            substitutions = ["Avocado oil in place of olive oil", "Ghee in place of butter for lactose sensitivity"]

        # =========================================================================
        # ARCHETYPE 2: Skillet-Roasted Poultry / Meat with Pan Jus
        # =========================================================================
        elif has_meat:
            title = f"Skillet-Roasted {' & '.join(names[:2])} with Pan-Dripping Herb Jus"
            cuisine = request.cuisine if request.cuisine != "Fusion" else "Contemporary Bistro"
            meal_type = "Dinner"
            prep_time = 12 if not request.prefer_quick else 6
            cook_time = 18 if not request.prefer_quick else 12
            difficulty = "Medium"

            summary = (
                f"Juicy pan-seared {names[0]} with a deep Maillard caramelized crust, simmered and basted "
                f"in rendered pan drippings with {', '.join(names[1:3])}."
            )

            required_tools = [
                "12-inch Heavy Bottom Skillet",
                "Silicone-Tipped Kitchen Tongs",
                "Wood Cutting Board & Chef's Knife",
                "Instant-Read Meat Thermometer"
            ]

            needed_ingredients = [
                NeededIngredientItem(name="Neutral High-Heat Oil (Avocado/Grapeseed)", amount="2 tbsp", purpose="Searing without burning"),
                NeededIngredientItem(name="Kosher Salt", amount="1 tsp", purpose="Essential protein dry-brine"),
                NeededIngredientItem(name="Freshly Ground Black Pepper", amount="1/2 tsp", purpose="Savory crust pungency"),
                NeededIngredientItem(name="Unsalted Butter", amount="1.5 tbsp", purpose="Finishing emulsification"),
                NeededIngredientItem(name="Warm Vegetable or Chicken Stock", amount="60 ml (1/4 cup)", purpose="Pan deglazing & sauce foundation")
            ]

            steps = [
                f"Trim and pat {names[0]} completely dry; season liberally with kosher salt and freshly cracked pepper on all sides.",
                f"Heat cooking oil in a heavy skillet over medium-high flame until hot and shimmering.",
                f"Add {names[0]} and sear undisturbed for 5-6 minutes until deeply browned and releasing naturally from the pan surface.",
                f"Turn over, add butter and {', '.join(names[1:3])}, and baste repeatedly with pan juices over medium heat.",
                f"Deglaze the pan with 1/4 cup warm broth, scraping the browned fond from the bottom of the skillet into a glossy pan sauce.",
                f"Transfer to a carving board and allow to rest for 4-5 minutes to allow juices to redistribute before slicing."
            ]

            missing_ingredients = ["Dijon mustard (1 tsp for pan sauce body)", "Fresh parsley sprigs"]
            substitutions = ["Boneless chicken thighs for chicken breasts", "Olive oil in place of butter"]

        # =========================================================================
        # ARCHETYPE 3: Hand-Tossed Pasta, Scented Pilaf or Grain Risotto
        # =========================================================================
        elif has_grain_pasta or ("tomato" in names_str and "basil" in names_str):
            grain_name = next((n for n in names if any(g in n.lower() for g in ["rice", "pasta", "quinoa", "bread"])), "Penne")
            title = f"Artisanal {grain_name} with {' & '.join([n for n in names if n != grain_name][:2])}"
            cuisine = request.cuisine if request.cuisine != "Fusion" else ("Italian Regional" if "pasta" in names_str or "tomato" in names_str else "Mediterranean")
            meal_type = "Dinner"
            prep_time = 10
            cook_time = 15
            difficulty = "Easy"

            summary = (
                f"Al dente grains tossed in an emulsified sauce created from starchy cooking water, "
                f"cold-pressed oil, and the vibrant aromatic flavors of {', '.join(names[:3])}."
            )

            required_tools = [
                "6-Quart Pasta Pot or Deep Dutch Oven",
                "12-inch Deep Sauté Pan",
                "Stainless Steel Colander / Strainer",
                "Wooden Deglazing Spoon",
                "Microplane Cheese Grater"
            ]

            needed_ingredients = [
                NeededIngredientItem(name="Extra Virgin Olive Oil", amount="2.5 tbsp", purpose="Sauce base & emulsion foundation"),
                NeededIngredientItem(name="Coarse Sea Salt", amount="1.5 tbsp", purpose="For boiling pasta/grain water"),
                NeededIngredientItem(name="Reserved Starchy Cooking Water", amount="60 ml (1/4 cup)", purpose="Liquid for creamy emulsification"),
                NeededIngredientItem(name="Minced Garlic or Shallots", amount="2 cloves", purpose="Sweet allium background note"),
                NeededIngredientItem(name="Freshly Ground Black Pepper", amount="1/2 tsp", purpose="Aromatic spice contrast")
            ]

            steps = [
                f"Bring 4 quarts of filtered water to a rolling boil in a stockpot. Season with 1.5 tbsp coarse salt until tasting lightly of the sea.",
                f"Add grains/pasta and cook until strictly al dente according to package instructions, testing for a slight resistant bite at the core.",
                f"Meanwhile, heat 2.5 tbsp olive oil in a deep sauté pan over medium-low heat. Add minced garlic and aromatics ({', '.join(names[:2])}), sweating gently for 2 minutes without browning.",
                f"Carefully ladle 1/4 cup of the starchy boiling cooking water from the pot directly into the sauté pan to build an emulsion.",
                f"Drain pasta and immediately transfer it into the simmering sauce. Toss vigorously over medium heat for 90 seconds ('mantecatura') until the sauce turns glossy and clings tightly.",
                f"Remove from heat, fold in remaining fresh herbs or cheese ({', '.join(names[2:4]) if len(names) > 2 else 'fresh garnishes'}), and serve in warm bowls."
            ]

            missing_ingredients = ["Freshly grated Parmigiano-Reggiano", "Crushed red pepper chili flakes"]
            substitutions = ["Gluten-free brown rice pasta", "Nutritional yeast for dairy-free cheese alternative"]

        # =========================================================================
        # ARCHETYPE 4: High-Heat Wok Stir-Fry / Asian Glaze
        # =========================================================================
        elif has_wok_asian:
            title = f"High-Heat Wok-Charred {' & '.join(names[:2])} with Toasted Sesame Glaze"
            cuisine = request.cuisine if request.cuisine != "Fusion" else "Pan-Asian Fusion"
            meal_type = "Dinner"
            prep_time = 10
            cook_time = 8
            difficulty = "Easy"

            summary = (
                f"Blistered at high heat to achieve authentic wok hei smoky edges, glazed with savory soy, "
                f"fresh gingerol warmth, and toasted sesame aromatics ({', '.join(names[:3])})."
            )

            required_tools = [
                "14-inch Carbon Steel Wok or Cast Iron Skillet",
                "Wok Spatula / Slotted Turner",
                "Chef's Knife & Cutting Board",
                "Small Whisk for Slurry"
            ]

            needed_ingredients = [
                NeededIngredientItem(name="Toasted Sesame Oil", amount="1.5 tbsp", purpose="Finishing aromatic luster"),
                NeededIngredientItem(name="High-Smoke Point Peanut or Avocado Oil", amount="2 tbsp", purpose="High heat searing"),
                NeededIngredientItem(name="Low-Sodium Soy Sauce or Tamari", amount="2 tbsp", purpose="Fermented savory umami base"),
                NeededIngredientItem(name="Cornstarch Slurry", amount="1 tsp cornstarch + 2 tbsp water", purpose="Glossy sauce cling"),
                NeededIngredientItem(name="Fresh Scallions", amount="2 stalks, cut on bias", purpose="Crisp fresh allium finish")
            ]

            steps = [
                f"Slice all ingredients ({', '.join(names)}) into uniform bite-sized pieces so they cook evenly in under 4 minutes.",
                f"Place wok over maximum flame until wisps of white smoke appear. Swirl cooking oil around the wok perimeter.",
                f"Add primary ingredients ({names[0]}) and spread into a single layer; sear undisturbed for 60 seconds to blister edges.",
                f"Toss vigorously, then add aromatics ({', '.join(names[1:3])}) and stir-fry continuously for 90 seconds.",
                f"Pour soy sauce and whisked cornstarch slurry around the sizzling outer edge of the wok; toss rapidly as the glaze turns glossy and coats every morsel.",
                f"Drizzle toasted sesame oil over the top and serve piping hot with steamed jasmine rice or noodles."
            ]

            missing_ingredients = ["Toasted white sesame seeds", "Red bird's eye chili"]
            substitutions = ["Coconut aminos in place of soy sauce", "Tofu in place of animal proteins"]

        # =========================================================================
        # ARCHETYPE 5: Aromatic Simmered Curry / Rich Kadai Masala
        # =========================================================================
        elif has_curry_masala:
            title = f"Slow-Simmered Royal {' & '.join(names[:2])} Kadai Masala"
            cuisine = request.cuisine if request.cuisine != "Fusion" else "Traditional Indian"
            meal_type = "Dinner"
            prep_time = 15
            cook_time = 20
            difficulty = "Medium"

            summary = (
                f"A deeply fragrant, slow-bloomed spiced curry marrying whole roasted aromatics with "
                f"a rich velvety gravy base ({', '.join(names[:3])})."
            )

            required_tools = [
                "Heavy-Bottomed Dutch Oven or Deep Kadai",
                "Chef's Knife & Wooden Spatula",
                "Stone Mortar & Pestle",
                "Ladle"
            ]

            needed_ingredients = [
                NeededIngredientItem(name="Pure Desi Ghee or Cold-Pressed Mustard Oil", amount="2 tbsp", purpose="Blooming whole spices (tadka)"),
                NeededIngredientItem(name="Fine Sea Salt", amount="1 tsp", purpose="Seasoning and moisture extraction"),
                NeededIngredientItem(name="Finely Diced Yellow Onion", amount="1 medium (approx. 100g)", purpose="Sweet caramelized base"),
                NeededIngredientItem(name="Ground Turmeric & Garam Masala", amount="1/2 tsp each", purpose="Warm color and aromatic depth"),
                NeededIngredientItem(name="Warm Filtered Water or Broth", amount="180 ml (3/4 cup)", purpose="Simmering gravy liquid")
            ]

            steps = [
                f"Heat ghee in a heavy Dutch oven over medium heat. Lightly crush whole spices in a mortar and bloom in hot ghee for 40 seconds until fragrant ('tadka').",
                f"Add diced onions with a pinch of salt; sauté slowly for 8-10 minutes, stirring frequently until deeply golden-brown.",
                f"Stir in minced ginger/garlic and powdered spices; cook for 1 minute until the raw fragrance turns nutty.",
                f"Add primary ingredients ({', '.join(names[:2])}) and fold through the spiced base, coating thoroughly ('bhunao').",
                f"Pour in warm water or broth, bring to a gentle simmer, cover, and cook on low heat for 12-15 minutes until tender and oil separates at the rim.",
                f"Finish with crushed green cardamom or fresh cilantro, rest covered for 3 minutes, and serve with warm roti or basmati rice."
            ]

            missing_ingredients = ["Fresh coriander / cilantro leaves", "Kasuri methi (crushed dried fenugreek leaves)"]
            substitutions = ["Coconut oil in place of ghee for vegan", "Paneer or tofu interchangeably"]

        # =========================================================================
        # ARCHETYPE 6: Chilled Parfait, Confection or Dessert Ambrosia
        # =========================================================================
        elif has_sweet_dessert or (request.prefer_no_cook and "curd" in names_str):
            title = f"Artisan Chilled {' & '.join(names[:2])} Ambrosia Coupes"
            cuisine = request.cuisine if request.cuisine != "Fusion" else "Contemporary Patisserie"
            meal_type = "Dessert / Sweet Treat"
            prep_time = 10
            cook_time = 0 if request.prefer_no_cook else 5
            difficulty = "Easy"

            summary = (
                f"A luxurious chilled confection layering creamy emulsified textures with "
                f"concentrated fruit essences and warm spice notes ({', '.join(names[:3])})."
            )

            required_tools = [
                "Balloon Whisk or Hand Mixer",
                "Chilled Glass Serving Coupes / Ramekins",
                "Silicone Folding Spatula",
                "Stone Mortar & Pestle"
            ]

            needed_ingredients = [
                NeededIngredientItem(name="Pure Vanilla Bean Extract", amount="1/2 tsp", purpose="Warm sweet aromatic lift"),
                NeededIngredientItem(name="Maldon Flaky Sea Salt", amount="1/4 tsp", purpose="Salt-sweet flavor catalyst"),
                NeededIngredientItem(name="Roasted Crushed Pistachios or Almonds", amount="2 tbsp", purpose="Textural artisan crunch"),
                NeededIngredientItem(name="Organic Honey or Agave Nectar", amount="1 tbsp", purpose="Natural glaze and shine")
            ]

            steps = [
                f"In a chilled glass bowl, gently whisk the base cream/curd ({names[0]}) with vanilla and natural sweetener until velvety smooth.",
                f"Lightly bruise spices or prepare fruit reductions ({', '.join(names[1:3])}) to release concentrated aromatic volatile oils.",
                f"Gently fold two-thirds of the aromatics into the whipped base, preserving a marbled, cloud-like texture.",
                f"Portion evenly into {servings} chilled coupe glasses or dessert ramekins.",
                f"Chill in the refrigerator for at least 15 minutes to allow flavors to harmonize and set.",
                f"Before serving, crown with the reserved toppings, crushed pistachios, and a delicate pinch of flaky sea salt."
            ]

            missing_ingredients = ["Fresh mint leaves (for aromatic bouquet)", "Edible silver or gold leaf (optional presentation)"]
            substitutions = ["Greek yogurt in place of curd", "Maple syrup in place of honey"]

        # =========================================================================
        # ARCHETYPE 7: Crisp Bistro Salad / Crudo / Carpaccio
        # =========================================================================
        elif has_tart_fresh or request.prefer_no_cook:
            title = f"Shaved {' & '.join(names[:2])} Bistro Carpaccio with Citrus Emulsion"
            cuisine = request.cuisine if request.cuisine != "Fusion" else "Mediterranean-Bistro"
            meal_type = "Light Lunch / Starter"
            prep_time = 10
            cook_time = 0
            difficulty = "Easy"

            summary = (
                f"A vibrant, crisp salad featuring paper-thin shaved {names[0]} paired with "
                f"savory crumbly textures and a cold-pressed citrus vinaigrette ({', '.join(names[1:3])})."
            )

            required_tools = [
                "Mandoline Slicer or Sharp Chef's Knife",
                "Small Glass Whisking Bowl",
                "Large Chilled Ceramic Platter",
                "Salad Tongs"
            ]

            needed_ingredients = [
                NeededIngredientItem(name="Cold-Pressed Extra Virgin Olive Oil", amount="2 tbsp", purpose="Vinaigrette body & lipid mouthfeel"),
                NeededIngredientItem(name="Fresh Lemon or Lime Juice", amount="1.5 tbsp", purpose="Bright malic/citric acid cleanse"),
                NeededIngredientItem(name="Flaky Sea Salt", amount="1/2 tsp", purpose="Osmotic crisping & seasoning"),
                NeededIngredientItem(name="Freshly Cracked Pink Peppercorns", amount="1/4 tsp", purpose="Mild floral heat"),
                NeededIngredientItem(name="Toasted Walnuts or Pumpkin Seeds", amount="2 tbsp", purpose="Crunch contrast")
            ]

            steps = [
                f"Using a mandoline or razor-sharp chef's knife, shave {names[0]} into paper-thin ribbons or delicate bite-sized discs.",
                f"In a small glass bowl, whisk together extra virgin olive oil, fresh citrus juice, sea salt, and cracked pink pepper until emulsified.",
                f"Arrange shaved {names[0]} and companion ingredients ({', '.join(names[1:3])}) in an overlapping pattern across a chilled platter.",
                f"Lightly spoon the citrus emulsion over the arrangement just before serving to maintain maximum crispness.",
                f"Scatter toasted nuts or seeds over top and serve immediately as a refreshing palate stimulator."
            ]

            missing_ingredients = ["Baby wild arugula / rocket", "Aged balsamic drizzle"]
            substitutions = ["Apple cider vinegar in place of fresh citrus", "Pecorino in place of cheddar/feta"]

        # =========================================================================
        # ARCHETYPE 8: Gourmet Pan-Roasted Sauté & Reduction Glaze (Default)
        # =========================================================================
        else:
            title = f"Gourmet Pan-Roasted {' & '.join(names[:2])} with Herb Glaze"
            cuisine = request.cuisine or "Contemporary Fusion"
            meal_type = request.meal_type or "Dinner"
            prep_time = 10 if not request.prefer_quick else 5
            cook_time = 14 if not request.prefer_quick else 8
            difficulty = "Easy"

            summary = (
                f"Artisan skillet preparation harmonizing {', '.join(names)} through "
                f"gentle high-heat searing, aromatic blooming, and balanced pan deglazing."
            )

            required_tools = [
                "12-inch Heavy Bottom Skillet",
                "Chef's Knife & Cutting Board",
                "Wooden Deglazing Spoon",
                "Measuring Spoons"
            ]

            needed_ingredients = [
                NeededIngredientItem(name="Extra Virgin Olive Oil or Butter", amount="2 tbsp", purpose="Searing fat & browning catalyst"),
                NeededIngredientItem(name="Kosher Salt", amount="1 tsp", purpose="Essential flavor amplifier"),
                NeededIngredientItem(name="Freshly Cracked Black Pepper", amount="1/2 tsp", purpose="Savory warmth"),
                NeededIngredientItem(name="Filtered Water or Stock", amount="60 ml (1/4 cup)", purpose="Pan deglazing liquid"),
                NeededIngredientItem(name="Minced Garlic", amount="1 clove", purpose="Aromatic background note")
            ]

            steps = [
                f"Prep all ingredients ({', '.join(names)}), slicing dense items into uniform pieces for consistent cooking.",
                f"Heat 2 tbsp olive oil or butter in a heavy skillet over medium-high heat until shimmering.",
                f"Add primary ingredients ({names[0]}) and sear undisturbed for 4 minutes until golden-brown edges develop.",
                f"Add companion ingredients ({', '.join(names[1:3])}) and minced garlic; sauté for 3 minutes while stirring gently.",
                f"Pour in 1/4 cup broth or water, scraping the caramelized browned bits from the pan bottom into a glossy glaze.",
                f"Season to taste with kosher salt and black pepper; portion onto warm dinner plates and serve immediately."
            ]

            missing_ingredients = ["Freshly chopped chives or parsley", "A squeeze of fresh lemon juice"]
            substitutions = ["Avocado oil in place of butter", "Tamari in place of salt for savory umami boost"]

        return RecipeResponse(
            title=title,
            summary=summary,
            cuisine=cuisine,
            meal_type=meal_type,
            prep_time_mins=prep_time,
            cook_time_mins=cook_time,
            servings=servings,
            difficulty=difficulty,
            ingredients_list=ingredients,
            steps=steps,
            missing_ingredients=missing_ingredients,
            substitutions=substitutions,
            allergens=allergens,
            required_tools=required_tools,
            needed_ingredients=needed_ingredients,
            generation_mode="Curated Culinary Engine (Deterministic Recipe Formulation)"
        )

    def _generate_with_gemini(
        self,
        request: RecipeGenerateRequest,
        ingredients: List[RecipeIngredientItem],
        allergens: List[str]
    ) -> RecipeResponse:
        import httpx
        import json

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={self.api_key}"
        ing_text = ", ".join([f"{i.quantity} {i.unit} {i.name}" for i in ingredients])

        prompt = (
            f"You are a master chef. Generate a delicious, realistic recipe using these primary ingredients: {ing_text}. "
            f"Cuisine: {request.cuisine}. Meal type: {request.meal_type}. Servings: {request.servings}. "
            f"Prefer quick: {request.prefer_quick}. Prefer no-cook: {request.prefer_no_cook}. "
            f"Respond strictly in valid JSON format with keys: "
            f"title (string), summary (string), prep_time_mins (int), cook_time_mins (int), difficulty (string), "
            f"required_tools (array of strings, e.g. ['12-inch Cast Iron Skillet', 'Chef Knife']), "
            f"needed_ingredients (array of objects with 'name', 'amount', 'purpose'), "
            f"steps (array of detailed step-by-step culinary instructions with exact temperatures and times), "
            f"missing_ingredients (array of strings for optional garnishes), substitutions (array of strings)."
        )

        resp = httpx.post(url, json={"contents": [{"parts": [{"text": prompt}]}]}, timeout=12.0)
        resp.raise_for_status()
        data = resp.json()
        raw_text = data["candidates"][0]["content"]["parts"][0]["text"].strip()
        if raw_text.startswith("```"):
            raw_text = raw_text.split("\n", 1)[1].rsplit("```", 1)[0].strip()
        parsed = json.loads(raw_text)

        needed_items = []
        for n in parsed.get("needed_ingredients", []):
            if isinstance(n, dict):
                needed_items.append(NeededIngredientItem(
                    name=n.get("name", "Pantry Staple"),
                    amount=n.get("amount", "As needed"),
                    purpose=n.get("purpose", "Seasoning")
                ))

        return RecipeResponse(
            title=parsed.get("title", "Gourmet Culinary Formulation"),
            summary=parsed.get("summary", ""),
            cuisine=request.cuisine or "Fusion",
            meal_type=request.meal_type or "Dinner",
            prep_time_mins=parsed.get("prep_time_mins", 15),
            cook_time_mins=parsed.get("cook_time_mins", 20),
            servings=request.servings,
            difficulty=parsed.get("difficulty", "Medium"),
            ingredients_list=ingredients,
            steps=parsed.get("steps", []),
            missing_ingredients=parsed.get("missing_ingredients", []),
            substitutions=parsed.get("substitutions", []),
            allergens=allergens,
            required_tools=parsed.get("required_tools", ["Chef's Knife", "Heavy Skillet", "Prep Bowls"]),
            needed_ingredients=needed_items,
            generation_mode="LLM (Google Gemini Flash API)"
        )
