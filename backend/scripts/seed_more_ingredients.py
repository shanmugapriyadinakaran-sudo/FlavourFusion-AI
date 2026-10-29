"""
Script to expand FlavorFusion AI ingredient database with essential culinary ingredients:
Green Apple, Salt, Black Salt, Butter, Parmesan, Mozzarella, Cheddar, Egg, Chicken, Salmon,
Shrimp, Tofu, Bacon, Watermelon, Pineapple, Banana, Orange, Peach, Blueberry, Raspberry, Fig,
Carrot, Potato, Sweet Potato, Eggplant, Zucchini, Beetroot, Asparagus, Cauliflower, Broccoli,
Corn, Shallot, Scallions, Rosemary, Thyme, Oregano, Dill, Rice Vinegar, Apple Cider Vinegar,
Dijon Mustard, Maple Syrup, Brown Sugar, Tahini, Miso Paste, Sesame Oil, Smoked Paprika,
Cayenne Pepper, Wasabi, Gochujang, Ricotta, Goat Cheese, Brie, Greek Yogurt, Whole Milk,
Oat Milk, Pasta, Sourdough Bread, Oats, Quinoa, Lentils, Walnuts, Peanuts.
"""

from typing import List, Dict, Any
from app.database.session import SessionLocal
from app.models.entities import Ingredient, IngredientFlavorProfile, IngredientPairingEvidence

EXPANDED_INGREDIENTS: List[Dict[str, Any]] = [
    # 1. Green Apple
    {
        "name": "Green Apple",
        "slug": "green-apple",
        "category": "Produce",
        "description": "Crisp, tart Granny Smith apple rich in vibrant malic acid and fresh hexanal green notes.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["European", "American", "Global"],
        "flavor_profile": {
            "sweet": 5.0, "salty": 0.0, "sour": 7.8, "bitter": 1.2, "umami": 0.3, "spicy": 0.0, "intensity": 6.8,
            "primary_aromas": ["Fruity", "Crisp", "Tart", "Green"],
            "texture_profile": ["Crisp", "Crunchy", "Juicy"],
            "dominant_compounds": ["Malic Acid", "Hexanal", "Ethyl 2-methylbutyrate"]
        }
    },
    # 2. Salt / Sea Salt
    {
        "name": "Salt",
        "slug": "salt",
        "category": "Pantry",
        "description": "Pure mineral sodium chloride, the fundamental taste amplifier that suppresses bitterness and elevates sweetness and umami.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Global"],
        "flavor_profile": {
            "sweet": 0.0, "salty": 10.0, "sour": 0.0, "bitter": 0.0, "umami": 1.0, "spicy": 0.0, "intensity": 9.5,
            "primary_aromas": ["Mineral", "Clean"],
            "texture_profile": ["Granular", "Crystalline"],
            "dominant_compounds": ["Sodium Chloride"]
        }
    },
    # 3. Black Salt (Kala Namak)
    {
        "name": "Black Salt",
        "slug": "black-salt",
        "category": "Spice",
        "description": "Volcanic rock salt with pungent hydrogen sulfide sulfurous aroma essential for Indian chaats and street foods.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "South Asian"],
        "flavor_profile": {
            "sweet": 0.0, "salty": 8.5, "sour": 1.0, "bitter": 0.5, "umami": 4.5, "spicy": 0.0, "intensity": 8.5,
            "primary_aromas": ["Sulfurous", "Pungent", "Savory"],
            "texture_profile": ["Powdered", "Granular"],
            "dominant_compounds": ["Sodium Chloride", "Sodium Sulfide", "Iron Sulfide"]
        }
    },
    # 4. Butter
    {
        "name": "Butter",
        "slug": "butter",
        "category": "Dairy",
        "description": "Cultured or sweet cream churned fat rich in diacetyl and butyric esters, providing luxurious mouthfeel.",
        "default_unit": "g",
        "allergens": ["Dairy"],
        "cuisines": ["French", "European", "American", "Global"],
        "flavor_profile": {
            "sweet": 2.5, "salty": 1.8, "sour": 1.0, "bitter": 0.0, "umami": 2.5, "spicy": 0.0, "intensity": 6.5,
            "primary_aromas": ["Buttery", "Creamy", "Lactic", "Nutty"],
            "texture_profile": ["Melting", "Rich", "Velvety"],
            "dominant_compounds": ["Diacetyl", "Acetoin", "Butyric acid"]
        }
    },
    # 5. Parmesan
    {
        "name": "Parmesan",
        "slug": "parmesan",
        "category": "Dairy",
        "description": "Aged hard Italian cheese packed with concentrated natural monosodium glutamate (MSG) crystals and sharp savory umami.",
        "default_unit": "g",
        "allergens": ["Dairy"],
        "cuisines": ["Italian", "European", "Global"],
        "flavor_profile": {
            "sweet": 0.8, "salty": 7.5, "sour": 2.5, "bitter": 1.0, "umami": 9.5, "spicy": 0.0, "intensity": 8.8,
            "primary_aromas": ["Cheesy", "Savory", "Nutty", "Sharp"],
            "texture_profile": ["Crystalline", "Hard", "Crumbly"],
            "dominant_compounds": ["Glutamate", "Isovaleric acid", "Methional"]
        }
    },
    # 6. Mozzarella
    {
        "name": "Mozzarella",
        "slug": "mozzarella",
        "category": "Dairy",
        "description": "Delicate, fresh stretched-curd cheese with high moisture and milky mild sweetness.",
        "default_unit": "g",
        "allergens": ["Dairy"],
        "cuisines": ["Italian", "Mediterranean"],
        "flavor_profile": {
            "sweet": 3.0, "salty": 3.0, "sour": 2.0, "bitter": 0.0, "umami": 4.0, "spicy": 0.0, "intensity": 4.5,
            "primary_aromas": ["Milky", "Fresh", "Lactic"],
            "texture_profile": ["Elastic", "Soft", "Creamy"],
            "dominant_compounds": ["Lactic acid", "Diacetyl"]
        }
    },
    # 7. Cheddar
    {
        "name": "Cheddar",
        "slug": "cheddar",
        "category": "Dairy",
        "description": "Aged semi-hard cow's milk cheese balancing sharp lactic acid, buttery richness, and savory bite.",
        "default_unit": "g",
        "allergens": ["Dairy"],
        "cuisines": ["British", "American", "Global"],
        "flavor_profile": {
            "sweet": 1.0, "salty": 6.5, "sour": 4.0, "bitter": 1.5, "umami": 8.0, "spicy": 0.0, "intensity": 7.8,
            "primary_aromas": ["Sharp", "Buttery", "Aged", "Lactic"],
            "texture_profile": ["Firm", "Smooth", "Crumbly"],
            "dominant_compounds": ["Diacetyl", "Butyric acid", "Methional"]
        }
    },
    # 8. Egg
    {
        "name": "Egg",
        "slug": "egg",
        "category": "Dairy",
        "description": "Complete culinary staple providing lecithin emulsification, savory yolk lipids, and albumen protein binding.",
        "default_unit": "unit",
        "allergens": ["Eggs"],
        "cuisines": ["Global"],
        "flavor_profile": {
            "sweet": 1.0, "salty": 1.5, "sour": 0.2, "bitter": 0.0, "umami": 5.5, "spicy": 0.0, "intensity": 5.0,
            "primary_aromas": ["Savory", "Sulfuric", "Rich"],
            "texture_profile": ["Custardy", "Silky", "Soft"],
            "dominant_compounds": ["Lecithin", "Sulfides", "Amino acids"]
        }
    },
    # 9. Chicken Breast
    {
        "name": "Chicken Breast",
        "slug": "chicken-breast",
        "category": "Produce",
        "description": "Lean poultry protein abundant in inosine monophosphate (IMP) that synergizes with plant glutamates.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Global"],
        "flavor_profile": {
            "sweet": 0.5, "salty": 1.5, "sour": 0.5, "bitter": 0.2, "umami": 6.5, "spicy": 0.0, "intensity": 5.5,
            "primary_aromas": ["Meaty", "Savory", "Mild"],
            "texture_profile": ["Firm", "Tender", "Fibrous"],
            "dominant_compounds": ["Inosine monophosphate", "Anserine"]
        }
    },
    # 10. Salmon
    {
        "name": "Salmon",
        "slug": "salmon",
        "category": "Produce",
        "description": "Rich anadromous oily fish rich in heart-healthy omega-3 fatty acids and oceanic umami.",
        "default_unit": "g",
        "allergens": ["Fish"],
        "cuisines": ["Nordic", "Japanese", "Global"],
        "flavor_profile": {
            "sweet": 1.2, "salty": 3.0, "sour": 0.5, "bitter": 0.5, "umami": 7.5, "spicy": 0.0, "intensity": 7.0,
            "primary_aromas": ["Marine", "Fatty", "Savory", "Smoky"],
            "texture_profile": ["Flaky", "Tender", "Velvety"],
            "dominant_compounds": ["Omega-3 fatty acids", "Trimethylamine oxide", "Glutamate"]
        }
    },
    # 11. Shrimp
    {
        "name": "Shrimp",
        "slug": "shrimp",
        "category": "Produce",
        "description": "Sweet and succulent crustacean with high natural glycine and adenosine monophosphate.",
        "default_unit": "g",
        "allergens": ["Shellfish"],
        "cuisines": ["Asian", "Mediterranean", "Latin American", "Global"],
        "flavor_profile": {
            "sweet": 4.5, "salty": 4.0, "sour": 0.5, "bitter": 0.2, "umami": 7.2, "spicy": 0.0, "intensity": 6.8,
            "primary_aromas": ["Sweet Marine", "Briny", "Shellfish"],
            "texture_profile": ["Snap", "Succulent", "Tender"],
            "dominant_compounds": ["Glycine", "Betaine", "Adenosine monophosphate"]
        }
    },
    # 12. Tofu
    {
        "name": "Tofu",
        "slug": "tofu",
        "category": "Legume",
        "description": "Coagulated soy milk curd with delicate subtle nutty flavor and sponge-like sauce absorption.",
        "default_unit": "g",
        "allergens": ["Soy"],
        "cuisines": ["East Asian", "Southeast Asian", "Global Vegan"],
        "flavor_profile": {
            "sweet": 1.5, "salty": 0.2, "sour": 0.5, "bitter": 0.5, "umami": 3.0, "spicy": 0.0, "intensity": 3.0,
            "primary_aromas": ["Beany", "Clean", "Mild"],
            "texture_profile": ["Silken", "Soft", "Firm"],
            "dominant_compounds": ["Isoflavones", "Hexanal"]
        }
    },
    # 13. Bacon
    {
        "name": "Bacon",
        "slug": "bacon",
        "category": "Pantry",
        "description": "Cured and hardwood-smoked pork belly with explosive crispy crunch and umami-smoke richness.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["American", "British", "Global"],
        "flavor_profile": {
            "sweet": 1.5, "salty": 8.0, "sour": 0.5, "bitter": 0.2, "umami": 8.8, "spicy": 0.0, "intensity": 8.5,
            "primary_aromas": ["Smoky", "Cured", "Meaty", "Savory"],
            "texture_profile": ["Crispy", "Fatty", "Crunchy"],
            "dominant_compounds": ["Guaiacol", "Furans", "Glutamate"]
        }
    },
    # 14. Watermelon
    {
        "name": "Watermelon",
        "slug": "watermelon",
        "category": "Produce",
        "description": "Refreshing summer melon with 92% hydration, citrulline, and crisp aquatic sweetness.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Mediterranean", "Global", "American"],
        "flavor_profile": {
            "sweet": 7.2, "salty": 0.0, "sour": 1.5, "bitter": 0.2, "umami": 0.2, "spicy": 0.0, "intensity": 5.2,
            "primary_aromas": ["Fruity", "Aquatic", "Fresh", "Green"],
            "texture_profile": ["Juicy", "Crisp", "Hydrating"],
            "dominant_compounds": ["Cis-6-nonenal", "Citrulline", "Lycopene"]
        }
    },
    # 15. Pineapple
    {
        "name": "Pineapple",
        "slug": "pineapple",
        "category": "Produce",
        "description": "Tropical bromelain-rich fruit bursting with punchy sweet-sour esters and caramelized potential.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Tropical", "Latin American", "Southeast Asian"],
        "flavor_profile": {
            "sweet": 8.0, "salty": 0.0, "sour": 6.5, "bitter": 0.5, "umami": 0.5, "spicy": 0.0, "intensity": 8.0,
            "primary_aromas": ["Tropical", "Fruity", "Ester", "Bright"],
            "texture_profile": ["Fibrous", "Juicy", "Crisp"],
            "dominant_compounds": ["Ethyl butyrate", "Allyl hexanoate", "Bromelain"]
        }
    },
    # 16. Banana
    {
        "name": "Banana",
        "slug": "banana",
        "category": "Produce",
        "description": "Starchy and creamy tropical fruit dominated by iconic isoamyl acetate notes.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Tropical", "Global"],
        "flavor_profile": {
            "sweet": 8.0, "salty": 0.0, "sour": 1.8, "bitter": 0.2, "umami": 0.8, "spicy": 0.0, "intensity": 6.8,
            "primary_aromas": ["Fruity", "Sweet", "Creamy", "Tropical"],
            "texture_profile": ["Creamy", "Soft", "Dense"],
            "dominant_compounds": ["Isoamyl acetate", "Eugenol", "Fructose"]
        }
    },
    # 17. Orange
    {
        "name": "Orange",
        "slug": "orange",
        "category": "Produce",
        "description": "Sun-ripened citrus balancing sweet fructose with bright citric acid and limonene zest.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Mediterranean", "Global", "American"],
        "flavor_profile": {
            "sweet": 7.5, "salty": 0.0, "sour": 5.5, "bitter": 1.0, "umami": 0.5, "spicy": 0.0, "intensity": 6.8,
            "primary_aromas": ["Citrus", "Sweet", "Fruity", "Floral"],
            "texture_profile": ["Juicy", "Pulpy", "Segmented"],
            "dominant_compounds": ["Limonene", "Octanal", "Citric acid"]
        }
    },
    # 18. Peach
    {
        "name": "Peach",
        "slug": "peach",
        "category": "Produce",
        "description": "Velvety stone fruit abundant in lactones, yielding floral and sweet honeyed notes.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["European", "American", "Asian"],
        "flavor_profile": {
            "sweet": 8.0, "salty": 0.0, "sour": 4.0, "bitter": 0.2, "umami": 0.4, "spicy": 0.0, "intensity": 6.5,
            "primary_aromas": ["Fruity", "Floral", "Lactone", "Honey"],
            "texture_profile": ["Velvety", "Soft", "Juicy"],
            "dominant_compounds": ["Gamma-decalactone", "Linalool", "Benzaldehyde"]
        }
    },
    # 19. Blueberry
    {
        "name": "Blueberry",
        "slug": "blueberry",
        "category": "Produce",
        "description": "Deep blue woodland berry pairing sweet floral tannins with gentle astringency.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["North American", "European", "Global"],
        "flavor_profile": {
            "sweet": 7.0, "salty": 0.0, "sour": 4.2, "bitter": 1.0, "umami": 0.3, "spicy": 0.0, "intensity": 6.0,
            "primary_aromas": ["Berry", "Woody", "Floral", "Sweet"],
            "texture_profile": ["Plump", "Juicy", "Tender"],
            "dominant_compounds": ["Anthocyanins", "Linalool", "Eucalyptol"]
        }
    },
    # 20. Raspberry
    {
        "name": "Raspberry",
        "slug": "raspberry",
        "category": "Produce",
        "description": "Fragrant aggregate berry with signature raspberry ketone and bright citric zing.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["European", "American"],
        "flavor_profile": {
            "sweet": 6.5, "salty": 0.0, "sour": 6.8, "bitter": 0.8, "umami": 0.2, "spicy": 0.0, "intensity": 7.2,
            "primary_aromas": ["Berry", "Floral", "Tart", "Perfumed"],
            "texture_profile": ["Delicate", "Seedy", "Juicy"],
            "dominant_compounds": ["Raspberry ketone", "Alpha-ionone", "Beta-ionone"]
        }
    },
    # 21. Fig
    {
        "name": "Fig",
        "slug": "fig",
        "category": "Produce",
        "description": "Ancient syconium fruit offering deep honey sweetness, tiny crunchy seeds, and floral wine notes.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Mediterranean", "Middle Eastern"],
        "flavor_profile": {
            "sweet": 8.8, "salty": 0.2, "sour": 1.5, "bitter": 0.5, "umami": 1.2, "spicy": 0.0, "intensity": 7.0,
            "primary_aromas": ["Honey", "Floral", "Wine", "Earthy"],
            "texture_profile": ["Soft", "Seedy", "Jammy"],
            "dominant_compounds": ["Linalool", "Benzaldehyde", "Fructose"]
        }
    },
    # 22. Carrot
    {
        "name": "Carrot",
        "slug": "carrot",
        "category": "Produce",
        "description": "Crunchy sweet root vegetable rich in earthy carotene and terpene sweetness.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Global"],
        "flavor_profile": {
            "sweet": 5.5, "salty": 0.5, "sour": 1.0, "bitter": 0.8, "umami": 1.5, "spicy": 0.0, "intensity": 5.2,
            "primary_aromas": ["Earthy", "Sweet", "Root", "Green"],
            "texture_profile": ["Crisp", "Crunchy", "Dense"],
            "dominant_compounds": ["Beta-carotene", "Terpinolene", "Caryophyllene"]
        }
    },
    # 23. Potato
    {
        "name": "Potato",
        "slug": "potato",
        "category": "Produce",
        "description": "Starchy tuber foundational to global culinary traditions, soaking up fats, herbs, and seasonings.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Global"],
        "flavor_profile": {
            "sweet": 2.0, "salty": 0.2, "sour": 0.2, "bitter": 0.2, "umami": 3.0, "spicy": 0.0, "intensity": 4.0,
            "primary_aromas": ["Earthy", "Starchy", "Comforting"],
            "texture_profile": ["Starchy", "Fluffy", "Crisp when fried"],
            "dominant_compounds": ["Amylose", "Amylopectin", "Methional"]
        }
    },
    # 24. Sweet Potato
    {
        "name": "Sweet Potato",
        "slug": "sweet-potato",
        "category": "Produce",
        "description": "Nutritious orange tuber that converts starches into maltose upon slow roasting.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["American", "Asian", "African", "Global"],
        "flavor_profile": {
            "sweet": 7.5, "salty": 0.2, "sour": 0.5, "bitter": 0.2, "umami": 2.0, "spicy": 0.0, "intensity": 6.2,
            "primary_aromas": ["Caramel", "Earthy", "Sweet", "Warm"],
            "texture_profile": ["Creamy", "Velvety", "Dense"],
            "dominant_compounds": ["Maltose", "Beta-carotene", "Furanones"]
        }
    },
    # 25. Eggplant
    {
        "name": "Eggplant",
        "slug": "eggplant",
        "category": "Produce",
        "description": "Sponge-textured nightshade that roasts and sautés into luscious silky umami.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Mediterranean", "Middle Eastern", "Indian", "Italian"],
        "flavor_profile": {
            "sweet": 2.5, "salty": 0.2, "sour": 1.0, "bitter": 2.5, "umami": 4.0, "spicy": 0.0, "intensity": 5.0,
            "primary_aromas": ["Vegetal", "Earthy", "Mild"],
            "texture_profile": ["Silky", "Spongy", "Melting"],
            "dominant_compounds": ["Chlorogenic acid", "Nasunin"]
        }
    },
    # 26. Zucchini
    {
        "name": "Zucchini",
        "slug": "zucchini",
        "category": "Produce",
        "description": "Tender summer squash with delicate green sweetness and crisp-tender flesh.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Italian", "French", "Mediterranean"],
        "flavor_profile": {
            "sweet": 3.0, "salty": 0.2, "sour": 1.2, "bitter": 0.5, "umami": 1.8, "spicy": 0.0, "intensity": 4.0,
            "primary_aromas": ["Green", "Fresh", "Vegetal"],
            "texture_profile": ["Tender", "Crisp", "Juicy"],
            "dominant_compounds": ["Hexanal", "Aldehydes"]
        }
    },
    # 27. Beetroot
    {
        "name": "Beetroot",
        "slug": "beetroot",
        "category": "Produce",
        "description": "Deep crimson root vegetable with unmistakable earthy geosmin aroma and high natural sucrose.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Eastern European", "Nordic", "Global"],
        "flavor_profile": {
            "sweet": 6.8, "salty": 0.8, "sour": 1.0, "bitter": 1.5, "umami": 1.8, "spicy": 0.0, "intensity": 6.5,
            "primary_aromas": ["Earthy", "Sweet", "Root", "Mineral"],
            "texture_profile": ["Dense", "Crisp", "Tender roasted"],
            "dominant_compounds": ["Geosmin", "Betanin", "Sucrose"]
        }
    },
    # 28. Asparagus
    {
        "name": "Asparagus",
        "slug": "asparagus",
        "category": "Produce",
        "description": "Elegant green spear with unique asparagusic acid, grassy sweetness, and sulfurous complexity.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["French", "European", "American"],
        "flavor_profile": {
            "sweet": 3.0, "salty": 0.5, "sour": 1.5, "bitter": 2.8, "umami": 4.5, "spicy": 0.0, "intensity": 6.2,
            "primary_aromas": ["Herbaceous", "Grassy", "Sulfurous", "Green"],
            "texture_profile": ["Crisp", "Snappy", "Tender"],
            "dominant_compounds": ["Asparagusic acid", "Methanethiol", "Pyrazines"]
        }
    },
    # 29. Cauliflower
    {
        "name": "Cauliflower",
        "slug": "cauliflower",
        "category": "Produce",
        "description": "Versatile cruciferous vegetable that develops deep nutty pyrazines when roasted or charred.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Middle Eastern", "European", "Global"],
        "flavor_profile": {
            "sweet": 3.5, "salty": 0.2, "sour": 0.8, "bitter": 2.0, "umami": 2.5, "spicy": 0.0, "intensity": 4.8,
            "primary_aromas": ["Nutty", "Brassica", "Mild"],
            "texture_profile": ["Crunchy", "Tender roasted", "Firm"],
            "dominant_compounds": ["Glucosinolates", "Dimethyl sulfide"]
        }
    },
    # 30. Broccoli
    {
        "name": "Broccoli",
        "slug": "broccoli",
        "category": "Produce",
        "description": "Green floret-dense brassica rich in sulforaphane, providing earthy crunch and savory depth.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Italian", "Asian", "American", "Global"],
        "flavor_profile": {
            "sweet": 2.8, "salty": 0.2, "sour": 1.0, "bitter": 3.2, "umami": 3.5, "spicy": 0.0, "intensity": 5.5,
            "primary_aromas": ["Green", "Brassica", "Earthy"],
            "texture_profile": ["Crisp", "Fibrous", "Firm"],
            "dominant_compounds": ["Sulforaphane", "Dimethyl trisulfide"]
        }
    },
    # 31. Corn
    {
        "name": "Corn",
        "slug": "corn",
        "category": "Produce",
        "description": "Plump golden kernels exploding with sweet starch and roasted popcorn-like pyrazine notes.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Mexican", "American", "Global"],
        "flavor_profile": {
            "sweet": 7.5, "salty": 0.5, "sour": 0.5, "bitter": 0.2, "umami": 2.2, "spicy": 0.0, "intensity": 6.0,
            "primary_aromas": ["Sweet Corn", "Grain", "Roasted"],
            "texture_profile": ["Juicy", "Popping", "Crunchy"],
            "dominant_compounds": ["Dimethyl sulfide", "Furans", "Sucrose"]
        }
    },
    # 32. Shallot
    {
        "name": "Shallot",
        "slug": "shallot",
        "category": "Produce",
        "description": "Aristocratic allium bridging the sharp sulfur of onions with subtle sweet garlic nuances.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["French", "Southeast Asian", "Global"],
        "flavor_profile": {
            "sweet": 4.5, "salty": 0.2, "sour": 1.0, "bitter": 1.5, "umami": 3.5, "spicy": 3.0, "intensity": 6.8,
            "primary_aromas": ["Allium", "Pungent", "Sweet", "Delicate"],
            "texture_profile": ["Crisp", "Tender softened"],
            "dominant_compounds": ["Allicin", "Dipropyl disulfide"]
        }
    },
    # 33. Scallions
    {
        "name": "Scallions",
        "slug": "scallions",
        "category": "Produce",
        "description": "Fresh bicolored allium stalks delivering crisp peppery sharpness in white stem and fresh grassiness in greens.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Chinese", "Japanese", "Korean", "Mexican", "Global"],
        "flavor_profile": {
            "sweet": 3.0, "salty": 0.2, "sour": 1.0, "bitter": 1.2, "umami": 2.5, "spicy": 3.5, "intensity": 6.2,
            "primary_aromas": ["Allium", "Grassy", "Fresh", "Sharp"],
            "texture_profile": ["Crisp", "Hollow", "Crunchy"],
            "dominant_compounds": ["Thiosulfinates", "Dipropyl disulfide"]
        }
    },
    # 34. Rosemary
    {
        "name": "Rosemary",
        "slug": "rosemary",
        "category": "Herb",
        "description": "Pungent Mediterranean needle herb saturated with camphor, pinene, and woody balsam.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Mediterranean", "Italian", "French"],
        "flavor_profile": {
            "sweet": 0.5, "salty": 0.0, "sour": 1.0, "bitter": 4.5, "umami": 0.8, "spicy": 2.0, "intensity": 8.5,
            "primary_aromas": ["Piney", "Woody", "Camphor", "Herbal"],
            "texture_profile": ["Needle", "Tough", "Aromatic"],
            "dominant_compounds": ["Alpha-pinene", "1,8-Cineole", "Camphor"]
        }
    },
    # 35. Thyme
    {
        "name": "Thyme",
        "slug": "thyme",
        "category": "Herb",
        "description": "Delicate sprig herb delivering foundational culinary warmth via antiseptic thymol.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["French", "Mediterranean", "American"],
        "flavor_profile": {
            "sweet": 0.5, "salty": 0.0, "sour": 1.0, "bitter": 3.5, "umami": 0.5, "spicy": 1.5, "intensity": 7.5,
            "primary_aromas": ["Herbal", "Warm", "Woody", "Earthy"],
            "texture_profile": ["Small Leaf", "Delicate"],
            "dominant_compounds": ["Thymol", "Carvacrol", "Cymene"]
        }
    },
    # 36. Oregano
    {
        "name": "Oregano",
        "slug": "oregano",
        "category": "Herb",
        "description": "Robust Mediterranean and Mexican mountain herb bursting with peppery carvacrol warmth.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Italian", "Greek", "Mexican"],
        "flavor_profile": {
            "sweet": 0.5, "salty": 0.0, "sour": 1.2, "bitter": 4.0, "umami": 0.5, "spicy": 2.5, "intensity": 8.0,
            "primary_aromas": ["Pungent", "Peppery", "Warm", "Herbal"],
            "texture_profile": ["Leafy", "Dry"],
            "dominant_compounds": ["Carvacrol", "Thymol", "Caryophyllene"]
        }
    },
    # 37. Dill
    {
        "name": "Dill",
        "slug": "dill",
        "category": "Herb",
        "description": "Feathery Nordic and Slavic herb featuring refreshing carvone, cutting through fatty fish and pickles.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Nordic", "Eastern European", "Greek"],
        "flavor_profile": {
            "sweet": 1.5, "salty": 0.0, "sour": 2.0, "bitter": 2.0, "umami": 0.2, "spicy": 0.5, "intensity": 7.0,
            "primary_aromas": ["Anise", "Herbal", "Fresh", "Sharp"],
            "texture_profile": ["Feathery", "Delicate"],
            "dominant_compounds": ["Carvone", "Limonene", "Anethofuran"]
        }
    },
    # 38. Rice Vinegar
    {
        "name": "Rice Vinegar",
        "slug": "rice-vinegar",
        "category": "Pantry",
        "description": "Mild, mellow Asian fermented vinegar with soft acidity and subtle rice sweetness.",
        "default_unit": "ml",
        "allergens": [],
        "cuisines": ["Japanese", "Chinese", "Korean"],
        "flavor_profile": {
            "sweet": 3.5, "salty": 0.2, "sour": 7.5, "bitter": 0.5, "umami": 1.5, "spicy": 0.0, "intensity": 6.8,
            "primary_aromas": ["Acidic", "Fermented", "Clean"],
            "texture_profile": ["Liquid"],
            "dominant_compounds": ["Acetic acid", "Lactic acid"]
        }
    },
    # 39. Apple Cider Vinegar
    {
        "name": "Apple Cider Vinegar",
        "slug": "apple-cider-vinegar",
        "category": "Pantry",
        "description": "Fermented apple must vinegar with rich malic tartness and probiotic woody depth.",
        "default_unit": "ml",
        "allergens": [],
        "cuisines": ["American", "European", "Global"],
        "flavor_profile": {
            "sweet": 2.5, "salty": 0.0, "sour": 8.5, "bitter": 0.8, "umami": 0.5, "spicy": 0.0, "intensity": 7.5,
            "primary_aromas": ["Fruity", "Vinegar", "Sharp", "Fermented"],
            "texture_profile": ["Liquid"],
            "dominant_compounds": ["Acetic acid", "Malic acid"]
        }
    },
    # 40. Dijon Mustard
    {
        "name": "Dijon Mustard",
        "slug": "dijon-mustard",
        "category": "Pantry",
        "description": "Sharp French condiment made from brown mustard seeds and white wine, delivering sinus-clearing pungency.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["French", "European"],
        "flavor_profile": {
            "sweet": 1.0, "salty": 5.5, "sour": 6.5, "bitter": 2.5, "umami": 2.0, "spicy": 6.0, "intensity": 8.0,
            "primary_aromas": ["Sharp", "Wine", "Pungent", "Sulfur"],
            "texture_profile": ["Smooth", "Pasty"],
            "dominant_compounds": ["Allyl isothiocyanate", "Sinigrin"]
        }
    },
    # 41. Maple Syrup
    {
        "name": "Maple Syrup",
        "slug": "maple-syrup",
        "category": "Pantry",
        "description": "Pure boiled sugar maple sap rich in sotolon, fenugreek-like aromatics, and wood caramel.",
        "default_unit": "ml",
        "allergens": [],
        "cuisines": ["North American"],
        "flavor_profile": {
            "sweet": 9.2, "salty": 0.0, "sour": 0.5, "bitter": 0.5, "umami": 0.5, "spicy": 0.0, "intensity": 7.8,
            "primary_aromas": ["Caramel", "Woody", "Sweet", "Vanilla"],
            "texture_profile": ["Viscous", "Syrupy", "Smooth"],
            "dominant_compounds": ["Sotolon", "Vanillin", "Sucrose"]
        }
    },
    # 42. Brown Sugar
    {
        "name": "Brown Sugar",
        "slug": "brown-sugar",
        "category": "Pantry",
        "description": "Sucrose crystals coated in natural cane molasses, lending deep toffee undertones.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Global"],
        "flavor_profile": {
            "sweet": 9.0, "salty": 0.2, "sour": 0.2, "bitter": 0.5, "umami": 0.2, "spicy": 0.0, "intensity": 7.5,
            "primary_aromas": ["Molasses", "Caramel", "Sweet"],
            "texture_profile": ["Granular", "Moist"],
            "dominant_compounds": ["Sucrose", "Furfural"]
        }
    },
    # 43. Tahini
    {
        "name": "Tahini",
        "slug": "tahini",
        "category": "Pantry",
        "description": "Velvety toasted sesame seed paste providing nutty bitterness, rich fats, and savory depth.",
        "default_unit": "g",
        "allergens": ["Sesame"],
        "cuisines": ["Middle Eastern", "Mediterranean"],
        "flavor_profile": {
            "sweet": 1.5, "salty": 1.0, "sour": 1.0, "bitter": 4.5, "umami": 5.0, "spicy": 0.0, "intensity": 7.2,
            "primary_aromas": ["Nutty", "Roasted", "Sesame"],
            "texture_profile": ["Paste", "Oily", "Thick"],
            "dominant_compounds": ["Sesamol", "Sesamolin", "Pyrazines"]
        }
    },
    # 44. Miso Paste
    {
        "name": "Miso Paste",
        "slug": "miso-paste",
        "category": "Pantry",
        "description": "Traditional Japanese koji-fermented soybean paste overflowing with deep savory glutamates.",
        "default_unit": "g",
        "allergens": ["Soy"],
        "cuisines": ["Japanese", "East Asian"],
        "flavor_profile": {
            "sweet": 2.5, "salty": 7.5, "sour": 2.0, "bitter": 1.0, "umami": 9.8, "spicy": 0.0, "intensity": 8.8,
            "primary_aromas": ["Fermented", "Umami", "Yeasty", "Salty"],
            "texture_profile": ["Paste", "Dense"],
            "dominant_compounds": ["Glutamate", "Isovaleric acid", "Succinic acid"]
        }
    },
    # 45. Sesame Oil
    {
        "name": "Sesame Oil",
        "slug": "sesame-oil",
        "category": "Pantry",
        "description": "Dark pressed roasted sesame finishing oil packing intense smoky pyrazine aroma.",
        "default_unit": "ml",
        "allergens": ["Sesame"],
        "cuisines": ["East Asian", "Korean", "Chinese"],
        "flavor_profile": {
            "sweet": 0.8, "salty": 0.0, "sour": 0.2, "bitter": 1.5, "umami": 4.0, "spicy": 0.0, "intensity": 8.5,
            "primary_aromas": ["Toasted", "Nutty", "Smoky"],
            "texture_profile": ["Oily", "Smooth"],
            "dominant_compounds": ["Pyrazines", "Guaiacol", "Sesamol"]
        }
    },
    # 46. Smoked Paprika
    {
        "name": "Smoked Paprika",
        "slug": "smoked-paprika",
        "category": "Spice",
        "description": "Oak-wood smoke cured sweet red peppers ground into deep scarlet savory powder.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Spanish", "Hungarian", "Mediterranean"],
        "flavor_profile": {
            "sweet": 4.0, "salty": 0.2, "sour": 1.0, "bitter": 1.5, "umami": 3.0, "spicy": 2.5, "intensity": 7.5,
            "primary_aromas": ["Smoky", "Earthy", "Woody", "Sweet"],
            "texture_profile": ["Powder"],
            "dominant_compounds": ["Guaiacol", "Capsanthin", "Pyrazines"]
        }
    },
    # 47. Cayenne Pepper
    {
        "name": "Cayenne Pepper",
        "slug": "cayenne-pepper",
        "category": "Spice",
        "description": "Finely milled pure pungent chili powder providing clean, fast-acting capsaicin heat.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Global", "Creole", "Indian"],
        "flavor_profile": {
            "sweet": 0.5, "salty": 0.0, "sour": 0.5, "bitter": 1.5, "umami": 1.0, "spicy": 9.5, "intensity": 9.0,
            "primary_aromas": ["Pungent", "Hot", "Pepper"],
            "texture_profile": ["Powder"],
            "dominant_compounds": ["Capsaicin", "Dihydrocapsaicin"]
        }
    },
    # 48. Wasabi
    {
        "name": "Wasabi",
        "slug": "wasabi",
        "category": "Spice",
        "description": "Freshly grated Japanese rhizome delivering explosive, volatile, vaporous nasal heat.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Japanese"],
        "flavor_profile": {
            "sweet": 2.0, "salty": 0.0, "sour": 1.0, "bitter": 2.0, "umami": 2.0, "spicy": 8.8, "intensity": 8.8,
            "primary_aromas": ["Pungent", "Nasal", "Green", "Sharp"],
            "texture_profile": ["Grated Paste"],
            "dominant_compounds": ["Allyl isothiocyanate", "6-MITC"]
        }
    },
    # 49. Gochujang
    {
        "name": "Gochujang",
        "slug": "gochujang",
        "category": "Pantry",
        "description": "Korean fermented red chili paste balancing sticky glutinous rice sweetness with spicy depth.",
        "default_unit": "g",
        "allergens": ["Soy"],
        "cuisines": ["Korean"],
        "flavor_profile": {
            "sweet": 6.5, "salty": 6.0, "sour": 1.8, "bitter": 1.0, "umami": 7.8, "spicy": 7.0, "intensity": 8.5,
            "primary_aromas": ["Fermented", "Chili", "Sweet", "Pungent"],
            "texture_profile": ["Sticky Paste", "Smooth"],
            "dominant_compounds": ["Capsaicin", "Fermented sugars", "Glutamate"]
        }
    },
    # 50. Ricotta
    {
        "name": "Ricotta",
        "slug": "ricotta",
        "category": "Dairy",
        "description": "Gentle sweet Italian whey cheese with delicate granular curds and sweet milky freshness.",
        "default_unit": "g",
        "allergens": ["Dairy"],
        "cuisines": ["Italian", "Mediterranean"],
        "flavor_profile": {
            "sweet": 4.5, "salty": 2.0, "sour": 1.5, "bitter": 0.0, "umami": 3.0, "spicy": 0.0, "intensity": 4.0,
            "primary_aromas": ["Milky", "Sweet", "Fresh Whey"],
            "texture_profile": ["Creamy", "Granular", "Light"],
            "dominant_compounds": ["Lactose", "Lactic acid"]
        }
    },
    # 51. Goat Cheese
    {
        "name": "Goat Cheese",
        "slug": "goat-cheese",
        "category": "Dairy",
        "description": "Tangy chèvre with signature caprylic acid rustic bite and creamy chalky texture.",
        "default_unit": "g",
        "allergens": ["Dairy"],
        "cuisines": ["French", "Mediterranean"],
        "flavor_profile": {
            "sweet": 1.5, "salty": 5.0, "sour": 6.5, "bitter": 1.0, "umami": 5.5, "spicy": 0.0, "intensity": 7.5,
            "primary_aromas": ["Goaty", "Sharp", "Earthy", "Lactic"],
            "texture_profile": ["Chalky", "Creamy", "Crumbly"],
            "dominant_compounds": ["Caprylic acid", "Caproic acid", "Diacetyl"]
        }
    },
    # 52. Brie
    {
        "name": "Brie",
        "slug": "brie",
        "category": "Dairy",
        "description": "Velvety soft-ripened cow's milk cheese boasting a bloomy rind with mushroom and buttery cream.",
        "default_unit": "g",
        "allergens": ["Dairy"],
        "cuisines": ["French", "European"],
        "flavor_profile": {
            "sweet": 2.0, "salty": 4.5, "sour": 2.0, "bitter": 1.0, "umami": 7.0, "spicy": 0.0, "intensity": 7.0,
            "primary_aromas": ["Mushroom", "Buttery", "Earthy", "Creamy"],
            "texture_profile": ["Gooey", "Melting", "Velvety"],
            "dominant_compounds": ["1-octen-3-ol", "Diacetyl", "Ammonia notes"]
        }
    },
    # 53. Greek Yogurt
    {
        "name": "Greek Yogurt",
        "slug": "greek-yogurt",
        "category": "Dairy",
        "description": "Triple-strained thick yogurt packed with protein and invigorating lactic acid tartness.",
        "default_unit": "g",
        "allergens": ["Dairy"],
        "cuisines": ["Greek", "Mediterranean", "Middle Eastern"],
        "flavor_profile": {
            "sweet": 2.5, "salty": 1.5, "sour": 6.8, "bitter": 0.5, "umami": 3.5, "spicy": 0.0, "intensity": 6.5,
            "primary_aromas": ["Lactic", "Tangy", "Milky"],
            "texture_profile": ["Dense", "Thick", "Creamy"],
            "dominant_compounds": ["Lactic acid", "Acetaldehyde", "Diacetyl"]
        }
    },
    # 54. Whole Milk
    {
        "name": "Whole Milk",
        "slug": "whole-milk",
        "category": "Dairy",
        "description": "Fresh whole dairy milk delivering natural lactose sweetness, butterfat emulsion, and liquid richness.",
        "default_unit": "ml",
        "allergens": ["Dairy"],
        "cuisines": ["Global"],
        "flavor_profile": {
            "sweet": 4.0, "salty": 1.0, "sour": 0.5, "bitter": 0.0, "umami": 2.0, "spicy": 0.0, "intensity": 3.8,
            "primary_aromas": ["Milky", "Sweet", "Creamy"],
            "texture_profile": ["Liquid", "Smooth"],
            "dominant_compounds": ["Lactose", "Butyric esters"]
        }
    },
    # 55. Oat Milk
    {
        "name": "Oat Milk",
        "slug": "oat-milk",
        "category": "Dairy",
        "description": "Enzymatically hydrolyzed oat beverage with pleasant cereal sweetness and creamy plant body.",
        "default_unit": "ml",
        "allergens": [],
        "cuisines": ["Global Modern"],
        "flavor_profile": {
            "sweet": 4.8, "salty": 0.5, "sour": 0.2, "bitter": 0.2, "umami": 1.2, "spicy": 0.0, "intensity": 4.0,
            "primary_aromas": ["Cereal", "Toasty", "Sweet", "Oat"],
            "texture_profile": ["Smooth", "Liquid"],
            "dominant_compounds": ["Maltose", "Vanillin", "Beta-glucans"]
        }
    },
    # 56. Pasta
    {
        "name": "Pasta",
        "slug": "pasta",
        "category": "Grain",
        "default_unit": "g",
        "allergens": ["Gluten"],
        "cuisines": ["Italian", "Global"],
        "flavor_profile": {
            "sweet": 2.0, "salty": 0.5, "sour": 0.2, "bitter": 0.2, "umami": 2.0, "spicy": 0.0, "intensity": 3.5,
            "primary_aromas": ["Wheat", "Grain", "Neutral"],
            "texture_profile": ["Al Dente", "Chewy", "Firm"],
            "dominant_compounds": ["Semolina starch", "Gluten"]
        }
    },
    # 57. Sourdough Bread
    {
        "name": "Sourdough Bread",
        "slug": "sourdough-bread",
        "category": "Grain",
        "default_unit": "g",
        "allergens": ["Gluten"],
        "cuisines": ["European", "American", "Artisan"],
        "flavor_profile": {
            "sweet": 2.0, "salty": 3.0, "sour": 5.5, "bitter": 1.2, "umami": 3.5, "spicy": 0.0, "intensity": 6.8,
            "primary_aromas": ["Yeasty", "Sour", "Roasted Crust", "Grain"],
            "texture_profile": ["Crusty", "Chewy", "Airy"],
            "dominant_compounds": ["Lactic acid", "Acetic acid", "Pyrazines"]
        }
    },
    # 58. Oats
    {
        "name": "Oats",
        "slug": "oats",
        "category": "Grain",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Global"],
        "flavor_profile": {
            "sweet": 3.0, "salty": 0.0, "sour": 0.2, "bitter": 0.5, "umami": 1.5, "spicy": 0.0, "intensity": 4.2,
            "primary_aromas": ["Grain", "Toasted", "Nutty"],
            "texture_profile": ["Chewy", "Creamy cooked"],
            "dominant_compounds": ["Beta-glucan", "Avenanthramides"]
        }
    },
    # 59. Quinoa
    {
        "name": "Quinoa",
        "slug": "quinoa",
        "category": "Grain",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["South American", "Global Healthy"],
        "flavor_profile": {
            "sweet": 1.8, "salty": 0.2, "sour": 0.5, "bitter": 1.5, "umami": 2.2, "spicy": 0.0, "intensity": 4.5,
            "primary_aromas": ["Nutty", "Earthy", "Grain"],
            "texture_profile": ["Fluffy", "Popping", "Tender"],
            "dominant_compounds": ["Saponins", "Amino acids"]
        }
    },
    # 60. Lentils
    {
        "name": "Lentils",
        "slug": "lentils",
        "category": "Legume",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Middle Eastern", "French"],
        "flavor_profile": {
            "sweet": 2.0, "salty": 0.2, "sour": 0.5, "bitter": 1.0, "umami": 4.5, "spicy": 0.0, "intensity": 5.2,
            "primary_aromas": ["Earthy", "Nutty", "Mineral"],
            "texture_profile": ["Creamy", "Soft", "Dense"],
            "dominant_compounds": ["Legumin", "Glutamate"]
        }
    },
    # 61. Walnuts
    {
        "name": "Walnuts",
        "slug": "walnuts",
        "category": "Pantry",
        "description": "Rich wrinkly tree nut featuring tannic astringent skins and high omega-3 buttery meat.",
        "default_unit": "g",
        "allergens": ["Nuts"],
        "cuisines": ["European", "Middle Eastern", "American"],
        "flavor_profile": {
            "sweet": 2.0, "salty": 0.0, "sour": 0.5, "bitter": 4.0, "umami": 3.0, "spicy": 0.0, "intensity": 6.8,
            "primary_aromas": ["Nutty", "Woody", "Tannic", "Earth"],
            "texture_profile": ["Crunchy", "Meaty", "Oily"],
            "dominant_compounds": ["Alpha-linolenic acid", "Ellagitannins", "Juglone"]
        }
    },
    # 62. Peanuts
    {
        "name": "Peanuts",
        "slug": "peanuts",
        "category": "Legume",
        "description": "Underground legume nut providing legendary roasted pyrazine crunch and creamy butter potential.",
        "default_unit": "g",
        "allergens": ["Peanuts"],
        "cuisines": ["American", "Southeast Asian", "African", "Global"],
        "flavor_profile": {
            "sweet": 2.5, "salty": 0.5, "sour": 0.2, "bitter": 1.5, "umami": 4.5, "spicy": 0.0, "intensity": 7.0,
            "primary_aromas": ["Roasted", "Nutty", "Pyrazine", "Earthy"],
            "texture_profile": ["Crunchy", "Dense", "Rich"],
            "dominant_compounds": ["Pyrazines", "Resveratrol", "Oleic acid"]
        }
    }
]

EXPANDED_PAIRINGS = [
    {
        "ing_a": "Green Apple", "ing_b": "Cheddar", "score": 93.0,
        "compounds": ["Malic Acid", "Diacetyl", "Butyric Acid"],
        "evidence": "Legendary Anglo-American pairing: high malic acid cuts sharp aged cheddar dairy fat.",
        "source": "Culinary Chemistry Classics"
    },
    {
        "ing_a": "Green Apple", "ing_b": "Brie", "score": 91.0,
        "compounds": ["Malic Acid", "1-octen-3-ol", "Lactic Acid"],
        "evidence": "French bistro classic: crisp tart apple refreshes rich bloomy rind cheese.",
        "source": "French Gastronomic Compendium"
    },
    {
        "ing_a": "Green Apple", "ing_b": "Walnuts", "score": 88.0,
        "compounds": ["Tannins", "Hexanal", "Ellagitannins"],
        "evidence": "Waldorf Salad cornerstone: tart acidity softens tannic nut skins.",
        "source": "Waldorf Gastronomy"
    },
    {
        "ing_a": "Salt", "ing_b": "Dark Chocolate", "score": 96.0,
        "compounds": ["Sodium Chloride", "Theobromine", "Pyrazines"],
        "evidence": "Salt crystals suppress bitterness and explode perceived cocoa bean sweetness.",
        "source": "Molecular Gastronomy & Flavor Chemistry"
    },
    {
        "ing_a": "Salt", "ing_b": "Watermelon", "score": 94.0,
        "compounds": ["Sodium Chloride", "Citrulline", "Cis-6-nonenal"],
        "evidence": "Southern and Mediterranean tradition: a pinch of salt makes melon taste twice as sweet.",
        "source": "Sensory Food Science"
    },
    {
        "ing_a": "Watermelon", "ing_b": "Feta Cheese", "score": 95.0,
        "compounds": ["Cis-6-nonenal", "Lactic Acid", "Sodium"],
        "evidence": "Greek summer icon: crisp sweet water against crumbly salty brined sheep's curd.",
        "source": "Hellenic Culinary Tradition"
    },
    {
        "ing_a": "Tomato", "ing_b": "Mozzarella", "score": 97.0,
        "compounds": ["Glutamate", "Lactic Acid", "Diacetyl"],
        "evidence": "Caprese gold standard: umami tomato acid balanced by mild creamy buffalo milk curd.",
        "source": "Italian Culinary Heritage"
    },
    {
        "ing_a": "Salmon", "ing_b": "Dill", "score": 95.0,
        "compounds": ["Carvone", "Omega-3", "Limonene"],
        "evidence": "Nordic Gravlax tradition: carvone herb aromatics slice through dense salmon lipids.",
        "source": "Scandinavian Culinary Classics"
    },
    {
        "ing_a": "Bacon", "ing_b": "Maple Syrup", "score": 93.0,
        "compounds": ["Guaiacol", "Sotolon", "Furans"],
        "evidence": "North American diner classic: smoky savory bacon fat glazed with toffee maple sugars.",
        "source": "American Gastronomic Culture"
    },
    {
        "ing_a": "Parmesan", "ing_b": "Balsamic Vinegar", "score": 96.0,
        "compounds": ["Glutamate", "Acetic Acid", "Wood Tannins"],
        "evidence": "Emilia-Romagna holy grail: aged cheese nuggets drizzled with traditional Aceto Balsamico.",
        "source": "Italian Traditional Gastronomy"
    }
]

def run_seed():
    db = SessionLocal()
    added_count = 0
    try:
        print("Seeding expanded ingredients into database...")
        for item in EXPANDED_INGREDIENTS:
            existing = db.query(Ingredient).filter(Ingredient.slug == item["slug"]).first()
            if not existing:
                ing = Ingredient(
                    name=item["name"],
                    slug=item["slug"],
                    category=item["category"],
                    description=item.get("description"),
                    default_unit=item.get("default_unit", "g"),
                    allergens=item.get("allergens", []),
                    cuisines=item.get("cuisines", []),
                    is_curated=True
                )
                db.add(ing)
                db.commit()
                db.refresh(ing)

                fp_data = item.get("flavor_profile", {})
                fp = IngredientFlavorProfile(
                    ingredient_id=ing.id,
                    sweet=fp_data.get("sweet", 0.0),
                    salty=fp_data.get("salty", 0.0),
                    sour=fp_data.get("sour", 0.0),
                    bitter=fp_data.get("bitter", 0.0),
                    umami=fp_data.get("umami", 0.0),
                    spicy=fp_data.get("spicy", 0.0),
                    intensity=fp_data.get("intensity", 5.0),
                    primary_aromas=fp_data.get("primary_aromas", []),
                    texture_profile=fp_data.get("texture_profile", []),
                    dominant_compounds=fp_data.get("dominant_compounds", [])
                )
                db.add(fp)
                db.commit()
                added_count += 1
                print(f" + Added {ing.name} ({ing.category})")

        print(f"\nAdded {added_count} new ingredients!")

        # Seed Pairings
        pairings_added = 0
        for p in EXPANDED_PAIRINGS:
            existing = db.query(IngredientPairingEvidence).filter(
                IngredientPairingEvidence.ingredient_a_name == p["ing_a"],
                IngredientPairingEvidence.ingredient_b_name == p["ing_b"]
            ).first()
            if not existing:
                ev = IngredientPairingEvidence(
                    ingredient_a_name=p["ing_a"],
                    ingredient_b_name=p["ing_b"],
                    affinity_score=p["score"],
                    shared_compounds=p.get("compounds", []),
                    culinary_evidence=p.get("evidence"),
                    source=p.get("source", "Flavor Intelligence Base"),
                    is_experimental=False
                )
                db.add(ev)
                # Bi-directional
                ev_rev = IngredientPairingEvidence(
                    ingredient_a_name=p["ing_b"],
                    ingredient_b_name=p["ing_a"],
                    affinity_score=p["score"],
                    shared_compounds=p.get("compounds", []),
                    culinary_evidence=p.get("evidence"),
                    source=p.get("source", "Flavor Intelligence Base"),
                    is_experimental=False
                )
                db.add(ev_rev)
                db.commit()
                pairings_added += 2
        print(f"Added {pairings_added} new pairing evidences!")

        total = db.query(Ingredient).count()
        print(f"Total ingredients now in database: {total}")

    except Exception as e:
        db.rollback()
        print(f"Error during seeding: {e}")
        raise
    finally:
        db.close()

if __name__ == "__main__":
    run_seed()
