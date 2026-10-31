"""
Comprehensive Culinary Seed Dataset for FlavorFusion AI
Includes 65+ ingredients with chemical aroma profiles, 6 basic taste metrics,
allergens, cuisine tags, and verified pairing evidence.
"""

import os
import sys

# Ensure backend root is on sys.path
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from typing import List, Dict, Any
from app.database.session import SessionLocal, engine, Base
from app.models.entities import (
    Ingredient,
    IngredientFlavorProfile,
    IngredientPairingEvidence,
    User,
    UserPreference
)
from app.core.security import get_password_hash

INGREDIENTS_DATA: List[Dict[str, Any]] = [
    # Fruits
    {
        "name": "Mango",
        "slug": "mango",
        "category": "Produce",
        "description": "Sweet, tropical stone fruit with juicy floral notes and rich carotenoid depth.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Southeast Asian", "Tropical", "Mexican"],
        "flavor_profile": {
            "sweet": 8.5, "salty": 0.0, "sour": 3.2, "bitter": 0.5, "umami": 0.8, "spicy": 0.0, "intensity": 7.5,
            "primary_aromas": ["Fruity", "Floral", "Tropical", "Sweet"],
            "texture_profile": ["Juicy", "Soft", "Fibrous"],
            "dominant_compounds": ["Myrcene", "Ocimene", "Ethyl butyrate"]
        }
    },
    {
        "name": "Lime",
        "slug": "lime",
        "category": "Produce",
        "description": "Zesty, sharp citrus with high citric acid content and terpene-rich peel oils.",
        "default_unit": "ml",
        "allergens": [],
        "cuisines": ["Mexican", "Southeast Asian", "Indian", "Global"],
        "flavor_profile": {
            "sweet": 1.5, "salty": 0.0, "sour": 9.2, "bitter": 3.0, "umami": 0.2, "spicy": 0.0, "intensity": 8.5,
            "primary_aromas": ["Citrus", "Sharp", "Fresh", "Zesty"],
            "texture_profile": ["Liquid", "Juicy"],
            "dominant_compounds": ["Limonene", "Citral", "Terpinolene"]
        }
    },
    {
        "name": "Lemon",
        "slug": "lemon",
        "category": "Produce",
        "description": "Bright, aromatic yellow citrus essential for acidic balancing and brightening flavors.",
        "default_unit": "ml",
        "allergens": [],
        "cuisines": ["Mediterranean", "Global", "Middle Eastern", "Indian"],
        "flavor_profile": {
            "sweet": 2.0, "salty": 0.0, "sour": 9.0, "bitter": 2.5, "umami": 0.2, "spicy": 0.0, "intensity": 8.0,
            "primary_aromas": ["Citrus", "Crisp", "Floral", "Zesty"],
            "texture_profile": ["Liquid", "Juicy"],
            "dominant_compounds": ["Limonene", "Citronellal", "Pinene"]
        }
    },
    {
        "name": "Apple",
        "slug": "apple",
        "category": "Produce",
        "description": "Crisp orchard fruit balancing malic acid and fructose.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["European", "American", "Global"],
        "flavor_profile": {
            "sweet": 7.0, "salty": 0.0, "sour": 4.5, "bitter": 0.5, "umami": 0.5, "spicy": 0.0, "intensity": 5.5,
            "primary_aromas": ["Fruity", "Fresh", "Green"],
            "texture_profile": ["Crisp", "Juicy", "Crunchy"],
            "dominant_compounds": ["Hexyl acetate", "Ethyl 2-methylbutyrate"]
        }
    },
    {
        "name": "Strawberry",
        "slug": "strawberry",
        "category": "Produce",
        "description": "Fragrant berry featuring dynamic furaneol sweetness and ester aromatics.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Global", "European", "American"],
        "flavor_profile": {
            "sweet": 7.5, "salty": 0.0, "sour": 5.0, "bitter": 0.5, "umami": 0.8, "spicy": 0.0, "intensity": 6.8,
            "primary_aromas": ["Berry", "Fruity", "Floral", "Sweet"],
            "texture_profile": ["Juicy", "Tender", "Seedy"],
            "dominant_compounds": ["Furaneol", "Methyl cinnamate"]
        }
    },
    {
        "name": "Pomegranate",
        "slug": "pomegranate",
        "category": "Produce",
        "description": "Ruby-red arils full of tart polyphenols and sweet berry undertones.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Middle Eastern", "Indian", "Mediterranean"],
        "flavor_profile": {
            "sweet": 6.5, "salty": 0.0, "sour": 6.5, "bitter": 2.0, "umami": 0.5, "spicy": 0.0, "intensity": 6.5,
            "primary_aromas": ["Tart", "Fruity", "Tannic"],
            "texture_profile": ["Crunchy", "Juicy"],
            "dominant_compounds": ["Ellagic acid", "Hexanal"]
        }
    },
    {
        "name": "Tamarind",
        "slug": "tamarind",
        "category": "Produce",
        "description": "Tart, sour-sweet fruit pod containing high tartaric acid, vital in South Asian and Southeast Asian curries and chutneys.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Southeast Asian", "Mexican"],
        "flavor_profile": {
            "sweet": 4.5, "salty": 0.0, "sour": 8.5, "bitter": 1.0, "umami": 2.5, "spicy": 0.0, "intensity": 8.5,
            "primary_aromas": ["Sour", "Fruity", "Caramelized", "Earthy"],
            "texture_profile": ["Sticky", "Thick", "Fibrous"],
            "dominant_compounds": ["Tartaric acid", "Furfural"]
        }
    },
    {
        "name": "Avocado",
        "slug": "avocado",
        "category": "Produce",
        "description": "Rich, creamy fruit packed with oleic monounsaturated fatty acids and subtle grassy notes.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Mexican", "Latin American", "Global"],
        "flavor_profile": {
            "sweet": 1.0, "salty": 0.2, "sour": 0.5, "bitter": 1.0, "umami": 4.5, "spicy": 0.0, "intensity": 4.5,
            "primary_aromas": ["Nutty", "Grassy", "Rich", "Green"],
            "texture_profile": ["Creamy", "Smooth", "Buttery"],
            "dominant_compounds": ["Nonenal", "Oleic acid"]
        }
    },
    {
        "name": "Tomato",
        "slug": "tomato",
        "category": "Produce",
        "description": "Umami powerhouse loaded with free glutamates, malic and citric acids.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Italian", "Indian", "Mediterranean", "Mexican", "Global"],
        "flavor_profile": {
            "sweet": 4.0, "salty": 0.2, "sour": 5.5, "bitter": 1.0, "umami": 7.5, "spicy": 0.0, "intensity": 6.5,
            "primary_aromas": ["Fruity", "Earthy", "Green", "Fresh"],
            "texture_profile": ["Juicy", "Soft"],
            "dominant_compounds": ["Glutamate", "cis-3-Hexenal", "beta-Damascenone"]
        }
    },
    {
        "name": "Coconut",
        "slug": "coconut",
        "category": "Produce",
        "description": "Nutty, sweet flesh with lactone-driven creamy richness.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Southeast Asian", "Caribbean", "Tropical"],
        "flavor_profile": {
            "sweet": 5.0, "salty": 0.2, "sour": 0.5, "bitter": 0.5, "umami": 2.5, "spicy": 0.0, "intensity": 6.0,
            "primary_aromas": ["Nutty", "Sweet", "Creamy", "Lactonic"],
            "texture_profile": ["Crunchy", "Fibrous", "Rich"],
            "dominant_compounds": ["delta-Octalactone", "delta-Decalactone"]
        }
    },

    # Dairy & Cultured
    {
        "name": "Curd",
        "slug": "curd",
        "category": "Dairy",
        "description": "Traditional Indian yogurt / dahi fermented with lactic acid bacteria; creamy, cooling, and gently tangy.",
        "default_unit": "g",
        "allergens": ["Dairy"],
        "cuisines": ["Indian", "Middle Eastern", "Mediterranean"],
        "flavor_profile": {
            "sweet": 2.5, "salty": 0.5, "sour": 6.8, "bitter": 0.5, "umami": 3.8, "spicy": 0.0, "intensity": 6.2,
            "primary_aromas": ["Lactic", "Fresh", "Tangy", "Creamy"],
            "texture_profile": ["Creamy", "Smooth", "Cool"],
            "dominant_compounds": ["Lactic acid", "Diacetyl", "Acetaldehyde"]
        }
    },
    {
        "name": "Paneer",
        "slug": "paneer",
        "category": "Dairy",
        "description": "Fresh, non-melting South Asian curd cheese with a clean milky profile.",
        "default_unit": "g",
        "allergens": ["Dairy"],
        "cuisines": ["Indian"],
        "flavor_profile": {
            "sweet": 2.0, "salty": 0.5, "sour": 1.2, "bitter": 0.2, "umami": 4.0, "spicy": 0.0, "intensity": 4.0,
            "primary_aromas": ["Milky", "Fresh", "Mild"],
            "texture_profile": ["Soft", "Firm", "Spongy"],
            "dominant_compounds": ["Milk proteins", "Butyric acid"]
        }
    },
    {
        "name": "Ghee",
        "slug": "ghee",
        "category": "Dairy",
        "description": "Clarified butter simmered to caramelize milk solids, giving an intense nutty, toasted aroma.",
        "default_unit": "g",
        "allergens": ["Dairy"],
        "cuisines": ["Indian", "Middle Eastern"],
        "flavor_profile": {
            "sweet": 2.0, "salty": 0.0, "sour": 0.0, "bitter": 0.0, "umami": 3.5, "spicy": 0.0, "intensity": 7.5,
            "primary_aromas": ["Nutty", "Toasted", "Buttery", "Caramelized"],
            "texture_profile": ["Liquid", "Rich", "Silky"],
            "dominant_compounds": ["Lactones", "Diacetyl", "Methyl ketones"]
        }
    },
    {
        "name": "Heavy Cream",
        "slug": "heavy-cream",
        "category": "Dairy",
        "description": "High fat dairy cream that coats the palate, softens high acidity and rounds out sharp spices.",
        "default_unit": "ml",
        "allergens": ["Dairy"],
        "cuisines": ["French", "Indian", "Global"],
        "flavor_profile": {
            "sweet": 3.0, "salty": 0.2, "sour": 0.2, "bitter": 0.0, "umami": 2.5, "spicy": 0.0, "intensity": 5.0,
            "primary_aromas": ["Creamy", "Milky", "Sweet"],
            "texture_profile": ["Creamy", "Velvety", "Rich"],
            "dominant_compounds": ["Diacetyl", "Milk fats"]
        }
    },
    {
        "name": "Feta Cheese",
        "slug": "feta-cheese",
        "category": "Dairy",
        "description": "Brined crumbly curd cheese delivering salty, tangy, punchy herbaceous contrast.",
        "default_unit": "g",
        "allergens": ["Dairy"],
        "cuisines": ["Greek", "Mediterranean"],
        "flavor_profile": {
            "sweet": 0.5, "salty": 8.5, "sour": 6.0, "bitter": 1.0, "umami": 6.5, "spicy": 0.0, "intensity": 7.8,
            "primary_aromas": ["Briny", "Pungent", "Lactic", "Tangy"],
            "texture_profile": ["Crumbly", "Creamy", "Firm"],
            "dominant_compounds": ["Caproic acid", "Sodium chloride"]
        }
    },
    {
        "name": "Coconut Milk",
        "slug": "coconut-milk",
        "category": "Pantry",
        "description": "Silky dairy-free extract from coconut meat providing rich medium-chain triglycerides.",
        "default_unit": "ml",
        "allergens": [],
        "cuisines": ["Southeast Asian", "South Indian", "Caribbean"],
        "flavor_profile": {
            "sweet": 4.0, "salty": 0.2, "sour": 0.2, "bitter": 0.0, "umami": 2.8, "spicy": 0.0, "intensity": 6.0,
            "primary_aromas": ["Coconut", "Sweet", "Creamy", "Tropical"],
            "texture_profile": ["Smooth", "Liquid", "Creamy"],
            "dominant_compounds": ["delta-Lactones", "Lauric acid"]
        }
    },

    # Spices & Aromatics
    {
        "name": "Cardamom",
        "slug": "cardamom",
        "category": "Spice",
        "description": "The 'Queen of Spices' boasting cineole, terpinyl acetate, and eucalyptus-floral warmth.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Middle Eastern", "Scandinavian"],
        "flavor_profile": {
            "sweet": 3.5, "salty": 0.0, "sour": 0.5, "bitter": 2.0, "umami": 0.0, "spicy": 4.5, "intensity": 8.8,
            "primary_aromas": ["Eucalyptus", "Warm Spice", "Floral", "Citrus", "Resinous"],
            "texture_profile": ["Powder", "Granular"],
            "dominant_compounds": ["1,8-Cineole", "alpha-Terpinyl acetate", "Linalool"]
        }
    },
    {
        "name": "Roasted Cumin",
        "slug": "roasted-cumin",
        "category": "Spice",
        "description": "Pan-toasted cumin seeds that release pyrazines, delivering an earthy, smoky, savory depth.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Mexican", "Middle Eastern"],
        "flavor_profile": {
            "sweet": 1.0, "salty": 0.0, "sour": 0.5, "bitter": 3.0, "umami": 3.5, "spicy": 3.0, "intensity": 8.0,
            "primary_aromas": ["Smoky", "Earthy", "Warm Spice", "Nutty"],
            "texture_profile": ["Granular", "Crisp"],
            "dominant_compounds": ["Cuminaldehyde", "Pyrazines", "Terpenes"]
        }
    },
    {
        "name": "Mint",
        "slug": "mint",
        "category": "Herb",
        "description": "Spearmint and peppermint herb loaded with menthol providing cooling sensations and herbal brightness.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Middle Eastern", "Mediterranean", "Southeast Asian"],
        "flavor_profile": {
            "sweet": 1.5, "salty": 0.0, "sour": 0.2, "bitter": 2.0, "umami": 0.2, "spicy": 2.0, "intensity": 7.5,
            "primary_aromas": ["Cooling", "Herbal", "Fresh", "Peppery"],
            "texture_profile": ["Delicate", "Leafy"],
            "dominant_compounds": ["Menthol", "Carvone", "Limonene"]
        }
    },
    {
        "name": "Cilantro",
        "slug": "cilantro",
        "category": "Herb",
        "description": "Fresh coriander greens with aldehyde-rich citrus-herbal freshness.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Mexican", "Southeast Asian"],
        "flavor_profile": {
            "sweet": 0.5, "salty": 0.0, "sour": 1.0, "bitter": 2.5, "umami": 0.5, "spicy": 1.5, "intensity": 6.8,
            "primary_aromas": ["Citrus", "Herbal", "Pungent", "Green"],
            "texture_profile": ["Leafy", "Crisp"],
            "dominant_compounds": ["(E)-2-Decenal", "Linalool"]
        }
    },
    {
        "name": "Basil",
        "slug": "basil",
        "category": "Herb",
        "description": "Sweet Mediterranean herb loaded with eugenol and estragole notes resembling anise and clove.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Italian", "Mediterranean", "French"],
        "flavor_profile": {
            "sweet": 2.5, "salty": 0.0, "sour": 0.2, "bitter": 2.0, "umami": 0.8, "spicy": 2.0, "intensity": 7.0,
            "primary_aromas": ["Anise", "Herbal", "Sweet", "Floral", "Pungent"],
            "texture_profile": ["Delicate", "Leafy"],
            "dominant_compounds": ["Eugenol", "Estragole", "Linalool"]
        }
    },
    {
        "name": "Ginger",
        "slug": "ginger",
        "category": "Spice",
        "description": "Pungent rhizome containing gingerols that transform into aromatic shogaols when cooked.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Chinese", "Southeast Asian", "Global"],
        "flavor_profile": {
            "sweet": 2.0, "salty": 0.0, "sour": 1.0, "bitter": 2.0, "umami": 0.5, "spicy": 7.8, "intensity": 8.5,
            "primary_aromas": ["Pungent", "Peppery", "Citrus", "Warm Spice"],
            "texture_profile": ["Fibrous", "Juicy", "Crisp"],
            "dominant_compounds": ["Gingerol", "Zingiberene", "Shogaol"]
        }
    },
    {
        "name": "Garlic",
        "slug": "garlic",
        "category": "Spice",
        "description": "Allium bulb loaded with allicin; sharp and pungent raw, sweet, mellow, and deeply savory cooked.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Global", "Italian", "Indian", "Chinese", "Mediterranean"],
        "flavor_profile": {
            "sweet": 3.0, "salty": 0.0, "sour": 0.2, "bitter": 2.0, "umami": 7.0, "spicy": 6.5, "intensity": 8.5,
            "primary_aromas": ["Sulfur", "Pungent", "Savory", "Warm"],
            "texture_profile": ["Crisp", "Firm", "Smooth (roasted)"],
            "dominant_compounds": ["Allicin", "Diallyl disulfide"]
        }
    },
    {
        "name": "Cinnamon",
        "slug": "cinnamon",
        "category": "Spice",
        "description": "Aromatic tree bark with cinnamaldehyde providing woody, sweet warmth.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Middle Eastern", "Mexican", "Baking"],
        "flavor_profile": {
            "sweet": 5.0, "salty": 0.0, "sour": 0.2, "bitter": 1.5, "umami": 0.0, "spicy": 4.5, "intensity": 8.2,
            "primary_aromas": ["Warm Spice", "Woody", "Sweet"],
            "texture_profile": ["Powder", "Bark"],
            "dominant_compounds": ["Cinnamaldehyde", "Eugenol"]
        }
    },
    {
        "name": "Saffron",
        "slug": "saffron",
        "category": "Spice",
        "description": "The world's most prized spice stigmas featuring safranal and crocin: metallic honey and hay notes.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Persian", "Spanish", "Mediterranean"],
        "flavor_profile": {
            "sweet": 2.0, "salty": 0.0, "sour": 0.2, "bitter": 3.0, "umami": 0.5, "spicy": 1.0, "intensity": 9.0,
            "primary_aromas": ["Hay", "Honey", "Floral", "Metallic", "Earthy"],
            "texture_profile": ["Delicate Thread"],
            "dominant_compounds": ["Safranal", "Crocin", "Picrocrocin"]
        }
    },
    {
        "name": "Chili Pepper",
        "slug": "chili-pepper",
        "category": "Spice",
        "description": "Fiery pod rich in capsaicin that binds to TRPV1 heat receptors.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Mexican", "Thai", "Sichuan"],
        "flavor_profile": {
            "sweet": 1.5, "salty": 0.0, "sour": 0.5, "bitter": 1.5, "umami": 1.0, "spicy": 9.5, "intensity": 9.2,
            "primary_aromas": ["Pungent", "Fruity", "Smoky", "Green"],
            "texture_profile": ["Crisp", "Crunchy"],
            "dominant_compounds": ["Capsaicin", "Dihydrocapsaicin"]
        }
    },
    {
        "name": "Black Pepper",
        "slug": "black-pepper",
        "category": "Spice",
        "description": "Dried berries delivering sharp piperine pungency and terpene pine notes.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Global", "Indian", "French"],
        "flavor_profile": {
            "sweet": 0.2, "salty": 0.0, "sour": 0.2, "bitter": 3.5, "umami": 0.5, "spicy": 7.0, "intensity": 7.5,
            "primary_aromas": ["Peppery", "Woody", "Pine", "Sharp"],
            "texture_profile": ["Granular"],
            "dominant_compounds": ["Piperine", "Pinene", "Limonene"]
        }
    },
    {
        "name": "Turmeric",
        "slug": "turmeric",
        "category": "Spice",
        "description": "Vibrant golden rhizome containing curcumin; earthy, slightly bitter and musky warm.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Southeast Asian"],
        "flavor_profile": {
            "sweet": 0.5, "salty": 0.0, "sour": 0.2, "bitter": 4.5, "umami": 0.5, "spicy": 3.0, "intensity": 6.8,
            "primary_aromas": ["Earthy", "Woody", "Mustard", "Warm"],
            "texture_profile": ["Powder", "Root"],
            "dominant_compounds": ["Curcumin", "Turmerone", "Zingiberene"]
        }
    },
    {
        "name": "Star Anise",
        "slug": "star-anise",
        "category": "Spice",
        "description": "Star-shaped pod dominated by anethole providing sweet licorice warmth.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Chinese", "Vietnamese", "Indian"],
        "flavor_profile": {
            "sweet": 6.0, "salty": 0.0, "sour": 0.0, "bitter": 2.0, "umami": 0.0, "spicy": 3.5, "intensity": 8.5,
            "primary_aromas": ["Anise", "Licorice", "Sweet", "Woody"],
            "texture_profile": ["Hard Pod", "Powder"],
            "dominant_compounds": ["Anethole", "Estragole"]
        }
    },
    {
        "name": "Cloves",
        "slug": "cloves",
        "category": "Spice",
        "description": "Intensely aromatic flower buds loaded with eugenol.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Middle Eastern", "European"],
        "flavor_profile": {
            "sweet": 2.0, "salty": 0.0, "sour": 0.0, "bitter": 4.0, "umami": 0.0, "spicy": 6.0, "intensity": 9.5,
            "primary_aromas": ["Warm Spice", "Medicinal", "Woody", "Numbing"],
            "texture_profile": ["Hard Bud", "Powder"],
            "dominant_compounds": ["Eugenol", "Caryophyllene"]
        }
    },
    {
        "name": "Nutmeg",
        "slug": "nutmeg",
        "category": "Spice",
        "description": "Grated seed with sabinene and myristicin providing comforting sweet woody spice.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "French", "Dutch", "Baking"],
        "flavor_profile": {
            "sweet": 3.5, "salty": 0.0, "sour": 0.0, "bitter": 2.5, "umami": 0.0, "spicy": 3.5, "intensity": 7.5,
            "primary_aromas": ["Nutty", "Woody", "Sweet", "Warm Spice"],
            "texture_profile": ["Powder"],
            "dominant_compounds": ["Myristicin", "Sabinene", "Elemicin"]
        }
    },
    {
        "name": "Curry Leaves",
        "slug": "curry-leaves",
        "category": "Herb",
        "description": "Aromatic foliage essential to South Indian tempering (tadka) with a nutty, herbal, citrus aroma.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["South Indian", "Sri Lankan"],
        "flavor_profile": {
            "sweet": 0.5, "salty": 0.0, "sour": 0.2, "bitter": 3.0, "umami": 1.0, "spicy": 2.0, "intensity": 8.0,
            "primary_aromas": ["Nutty", "Citrus", "Herbal", "Pungent"],
            "texture_profile": ["Leafy", "Crisp (fried)"],
            "dominant_compounds": ["Caryophyllene", "Pinene", "Mahanimbine"]
        }
    },

    # Sweeteners, Oils & Condiments
    {
        "name": "Honey",
        "slug": "honey",
        "category": "Pantry",
        "description": "Floral nectar containing fructose, glucose, and phenolics that add smooth natural sweetness.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Global", "Mediterranean", "Middle Eastern", "Indian"],
        "flavor_profile": {
            "sweet": 9.5, "salty": 0.0, "sour": 1.0, "bitter": 0.0, "umami": 0.5, "spicy": 0.0, "intensity": 7.8,
            "primary_aromas": ["Floral", "Caramelized", "Sweet", "Fruity"],
            "texture_profile": ["Viscous", "Syrupy", "Smooth"],
            "dominant_compounds": ["Fructose", "Phenylacetic acid", "Phenethyl alcohol"]
        }
    },
    {
        "name": "Jaggery",
        "slug": "jaggery",
        "category": "Pantry",
        "description": "Unrefined cane sugar rich in molasses minerals with deep caramel-earthy tones.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Southeast Asian"],
        "flavor_profile": {
            "sweet": 8.8, "salty": 0.5, "sour": 0.8, "bitter": 1.0, "umami": 1.5, "spicy": 0.0, "intensity": 8.0,
            "primary_aromas": ["Caramelized", "Molasses", "Earthy", "Warm"],
            "texture_profile": ["Solid", "Crumbly"],
            "dominant_compounds": ["Sucrose", "Pyrazines", "Phenols"]
        }
    },
    {
        "name": "Soy Sauce",
        "slug": "soy-sauce",
        "category": "Pantry",
        "description": "Fermented soybean liquid delivering intense salty, amino acid umami depth.",
        "default_unit": "ml",
        "allergens": ["Soy", "Gluten"],
        "cuisines": ["Japanese", "Chinese", "Asian Fusion"],
        "flavor_profile": {
            "sweet": 1.5, "salty": 9.5, "sour": 2.0, "bitter": 0.5, "umami": 9.5, "spicy": 0.0, "intensity": 8.5,
            "primary_aromas": ["Fermented", "Savory", "Toasted", "Malty"],
            "texture_profile": ["Liquid"],
            "dominant_compounds": ["Monosodium glutamate", "HEMF", "Isovaleric acid"]
        }
    },
    {
        "name": "Balsamic Vinegar",
        "slug": "balsamic-vinegar",
        "category": "Pantry",
        "description": "Aged cooked grape must with complex acetic acidity balanced by caramelized fruit sweetness.",
        "default_unit": "ml",
        "allergens": [],
        "cuisines": ["Italian", "Mediterranean"],
        "flavor_profile": {
            "sweet": 6.0, "salty": 0.2, "sour": 8.0, "bitter": 0.5, "umami": 2.0, "spicy": 0.0, "intensity": 7.5,
            "primary_aromas": ["Woody", "Fruity", "Acetic", "Caramelized"],
            "texture_profile": ["Syrupy", "Liquid"],
            "dominant_compounds": ["Acetic acid", "Furanones", "Oak vanillin"]
        }
    },
    {
        "name": "Olive Oil",
        "slug": "olive-oil",
        "category": "Pantry",
        "description": "Extra virgin cold-pressed oil with oleocanthal pepperiness and green artichoke notes.",
        "default_unit": "ml",
        "allergens": [],
        "cuisines": ["Mediterranean", "Italian", "Spanish", "Global"],
        "flavor_profile": {
            "sweet": 0.5, "salty": 0.0, "sour": 0.2, "bitter": 3.0, "umami": 2.0, "spicy": 2.5, "intensity": 6.0,
            "primary_aromas": ["Grassy", "Peppery", "Fruity", "Green"],
            "texture_profile": ["Silky", "Smooth", "Liquid"],
            "dominant_compounds": ["Oleocanthal", "Hexanal"]
        }
    },

    # Nuts & Seeds
    {
        "name": "Pistachio",
        "slug": "pistachio",
        "category": "Pantry",
        "description": "Vibrant emerald nut with gentle pine, sweetness, and delicate crunch.",
        "default_unit": "g",
        "allergens": ["Nuts"],
        "cuisines": ["Middle Eastern", "Indian", "Mediterranean"],
        "flavor_profile": {
            "sweet": 3.5, "salty": 0.2, "sour": 0.0, "bitter": 0.8, "umami": 3.2, "spicy": 0.0, "intensity": 5.5,
            "primary_aromas": ["Nutty", "Sweet", "Pine", "Delicate"],
            "texture_profile": ["Crunchy", "Crisp"],
            "dominant_compounds": ["Pinene", "Terpinolene", "Pyrazines"]
        }
    },
    {
        "name": "Almonds",
        "slug": "almonds",
        "category": "Pantry",
        "description": "Benzaldehyde-rich nuts offering clean, pleasant crunch and marzipan notes.",
        "default_unit": "g",
        "allergens": ["Nuts"],
        "cuisines": ["Global", "Indian", "Middle Eastern", "Spanish"],
        "flavor_profile": {
            "sweet": 3.0, "salty": 0.0, "sour": 0.0, "bitter": 1.2, "umami": 2.8, "spicy": 0.0, "intensity": 5.0,
            "primary_aromas": ["Nutty", "Toasted", "Marzipan", "Woody"],
            "texture_profile": ["Crunchy", "Firm"],
            "dominant_compounds": ["Benzaldehyde", "Pyrazines"]
        }
    },
    {
        "name": "Cashews",
        "slug": "cashews",
        "category": "Pantry",
        "description": "Buttery, sweet crescent nuts that blend into velvety gravies and desserts.",
        "default_unit": "g",
        "allergens": ["Nuts"],
        "cuisines": ["Indian", "Southeast Asian", "Vegan Cuisine"],
        "flavor_profile": {
            "sweet": 4.0, "salty": 0.2, "sour": 0.0, "bitter": 0.2, "umami": 3.5, "spicy": 0.0, "intensity": 5.2,
            "primary_aromas": ["Buttery", "Sweet", "Nutty", "Creamy"],
            "texture_profile": ["Tender-Crisp", "Creamy"],
            "dominant_compounds": ["Lactones", "Alkylphenols"]
        }
    },
    {
        "name": "Sesame Seeds",
        "slug": "sesame-seeds",
        "category": "Pantry",
        "description": "Tiny seeds rich in sesamol and pyrazines providing warm toasted nuttiness.",
        "default_unit": "g",
        "allergens": ["Sesame"],
        "cuisines": ["Asian", "Middle Eastern", "Indian"],
        "flavor_profile": {
            "sweet": 1.5, "salty": 0.0, "sour": 0.0, "bitter": 2.0, "umami": 3.8, "spicy": 0.0, "intensity": 6.8,
            "primary_aromas": ["Nutty", "Toasted", "Earthy"],
            "texture_profile": ["Crunchy", "Tiny"],
            "dominant_compounds": ["Sesamol", "2-Acetyl-1-pyrroline"]
        }
    },

    # Vegetables & Fungi
    {
        "name": "Onion",
        "slug": "onion",
        "category": "Produce",
        "description": "Foundational culinary allium. Pungent when raw, intensely sweet and savory when caramelized.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Global"],
        "flavor_profile": {
            "sweet": 4.5, "salty": 0.0, "sour": 0.5, "bitter": 1.5, "umami": 5.5, "spicy": 4.5, "intensity": 7.0,
            "primary_aromas": ["Pungent", "Sulfur", "Savory", "Sweet"],
            "texture_profile": ["Crisp (raw)", "Tender (cooked)"],
            "dominant_compounds": ["Propanethial S-oxide", "Dipropyl disulfide"]
        }
    },
    {
        "name": "Mushroom",
        "slug": "mushroom",
        "category": "Produce",
        "description": "Fungal treasure laden with octen-3-ol and guanylate for earthy umami explosion.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Global", "French", "Japanese", "Italian"],
        "flavor_profile": {
            "sweet": 1.0, "salty": 0.2, "sour": 0.2, "bitter": 1.0, "umami": 8.8, "spicy": 0.0, "intensity": 7.5,
            "primary_aromas": ["Earthy", "Woody", "Savory", "Fungal"],
            "texture_profile": ["Tender", "Meaty", "Juicy"],
            "dominant_compounds": ["1-Octen-3-ol", "Guanylic acid"]
        }
    },
    {
        "name": "Spinach",
        "slug": "spinach",
        "category": "Produce",
        "description": "Leafy green loaded with iron, chlorophyll, and subtle earthy mineral tones.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Mediterranean", "Global"],
        "flavor_profile": {
            "sweet": 1.0, "salty": 0.2, "sour": 0.2, "bitter": 3.0, "umami": 4.0, "spicy": 0.0, "intensity": 4.5,
            "primary_aromas": ["Green", "Earthy", "Mineral"],
            "texture_profile": ["Tender", "Leafy"],
            "dominant_compounds": ["Hexanal", "Oxalic acid"]
        }
    },
    {
        "name": "Bell Pepper",
        "slug": "bell-pepper",
        "category": "Produce",
        "description": "Sweet, crisp capsicum with methoxypyrazines lending characteristic fresh green aroma.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Mexican", "Mediterranean", "Asian Fusion"],
        "flavor_profile": {
            "sweet": 5.0, "salty": 0.0, "sour": 1.0, "bitter": 1.5, "umami": 1.5, "spicy": 0.5, "intensity": 5.5,
            "primary_aromas": ["Green", "Fresh", "Fruity", "Crisp"],
            "texture_profile": ["Crisp", "Crunchy", "Juicy"],
            "dominant_compounds": ["2-Isobutyl-3-methoxypyrazine"]
        }
    },
    {
        "name": "Cucumber",
        "slug": "cucumber",
        "category": "Produce",
        "description": "Ultra-refreshing, nonadienal-driven cool vegetable, ideal for raitas and salads.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Mediterranean", "Global"],
        "flavor_profile": {
            "sweet": 1.5, "salty": 0.0, "sour": 0.5, "bitter": 0.8, "umami": 0.5, "spicy": 0.0, "intensity": 3.5,
            "primary_aromas": ["Cooling", "Melon", "Fresh", "Watery"],
            "texture_profile": ["Crunchy", "Juicy", "Crisp"],
            "dominant_compounds": ["(E,Z)-3,6-Nonadien-1-ol"]
        }
    },

    # Desserts & Indulgence
    {
        "name": "Dark Chocolate",
        "slug": "dark-chocolate",
        "category": "Pantry",
        "description": "Rich fermented cacao solids boasting polyphenols, theobromine, pyrazines, and fruit acidity.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Baking", "Mexican", "Desserts"],
        "flavor_profile": {
            "sweet": 3.5, "salty": 0.0, "sour": 2.5, "bitter": 7.5, "umami": 2.0, "spicy": 0.0, "intensity": 8.5,
            "primary_aromas": ["Roasty", "Earthy", "Fruity", "Woody", "Bittersweet"],
            "texture_profile": ["Snap", "Smooth (melting)"],
            "dominant_compounds": ["Theobromine", "Isovaleric acid", "Tetramethylpyrazine"]
        }
    },
    {
        "name": "Coffee",
        "slug": "coffee",
        "category": "Pantry",
        "description": "Roasted coffee bean infusion loaded with furfurylthiol and chlorogenic acids.",
        "default_unit": "ml",
        "allergens": [],
        "cuisines": ["Global"],
        "flavor_profile": {
            "sweet": 0.5, "salty": 0.0, "sour": 3.0, "bitter": 8.0, "umami": 2.0, "spicy": 0.0, "intensity": 8.8,
            "primary_aromas": ["Roasty", "Smoky", "Caramelized", "Earthy"],
            "texture_profile": ["Liquid"],
            "dominant_compounds": ["2-Furfurylthiol", "Pyrazines", "Caffeine"]
        }
    },
    {
        "name": "Vanilla",
        "slug": "vanilla",
        "category": "Spice",
        "description": "Cured orchid pod providing pure comforting vanillin, amplifying perceived sweetness.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Global", "Baking", "Desserts"],
        "flavor_profile": {
            "sweet": 4.5, "salty": 0.0, "sour": 0.0, "bitter": 1.0, "umami": 0.0, "spicy": 0.0, "intensity": 8.0,
            "primary_aromas": ["Sweet", "Warm", "Floral", "Caramelized"],
            "texture_profile": ["Extract / Pod"],
            "dominant_compounds": ["Vanillin", "4-Hydroxybenzaldehyde"]
        }
    },
    {
        "name": "Basmati Rice",
        "slug": "basmati-rice",
        "category": "Grain",
        "description": "Aromatic long-grain rice scented with 2-acetyl-1-pyrroline (pandan/popcorn fragrance).",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Middle Eastern"],
        "flavor_profile": {
            "sweet": 2.0, "salty": 0.0, "sour": 0.0, "bitter": 0.0, "umami": 2.0, "spicy": 0.0, "intensity": 3.5,
            "primary_aromas": ["Popcorn", "Pandan", "Nutty", "Floral"],
            "texture_profile": ["Fluffy", "Tender", "Grainy"],
            "dominant_compounds": ["2-Acetyl-1-pyrroline"]
        }
    },
    {
        "name": "Chickpeas",
        "slug": "chickpeas",
        "category": "Legume",
        "description": "Hearty garbanzo legumes delivering nutty, starchy body and rich plant protein.",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Middle Eastern", "Mediterranean"],
        "flavor_profile": {
            "sweet": 2.0, "salty": 0.2, "sour": 0.2, "bitter": 1.0, "umami": 4.5, "spicy": 0.0, "intensity": 4.5,
            "primary_aromas": ["Nutty", "Earthy", "Grainy"],
            "texture_profile": ["Creamy (mashed)", "Firm", "Starchy"],
            "dominant_compounds": ["Pyrazines", "Hexanal"]
        }
    }
]

PAIRING_EVIDENCE_DATA = [
    {
        "a": "Mango", "b": "Curd",
        "score": 96.0,
        "shared": ["Lactic sweetness", "Terpenes"],
        "evidence": "Foundational synergy in Mango Lassi, Aamrakhand (Shrikhand). Creamy lactic acid cuts tropical mango sweetness while mango rounds lactic sharpness.",
        "source": "Traditional Indian Culinary Heritage & Food Chemistry"
    },
    {
        "a": "Mango", "b": "Cardamom",
        "score": 94.0,
        "shared": ["Terpinyl acetate", "Linalool", "Limonene"],
        "evidence": "Shared terpene and floral volatile compounds create immense harmony. Cineole in cardamom lifts mango aroma.",
        "source": "Flavor Chemistry GC-MS Aroma Analysis"
    },
    {
        "a": "Curd", "b": "Roasted Cumin",
        "score": 95.0,
        "shared": ["Pyrazines", "Acetaldehyde"],
        "evidence": "The quintessential Raita and Chaas pairing. Smoky roasted cuminaldehyde cuts smooth lactic acidity.",
        "source": "Ayurvedic Culinary Science"
    },
    {
        "a": "Mango", "b": "Mint",
        "score": 90.0,
        "shared": ["Limonene", "Myrcene", "Ocimene"],
        "evidence": "Refreshing contrast: cooling menthol and tropical fruit esters form an invigorating palate cleanser.",
        "source": "Modern Gastronomy & Cocktail Science"
    },
    {
        "a": "Mango", "b": "Lime",
        "score": 93.0,
        "shared": ["Limonene", "Citral"],
        "evidence": "Acid-sugar balance. Lime citric acid tightens dense mango fructose.",
        "source": "South East Asian & Latin American Culinary Practice"
    },
    {
        "a": "Curd", "b": "Honey",
        "score": 92.0,
        "shared": ["Floral volatiles", "Phenethyl alcohol"],
        "evidence": "Classic Mediterranean and Greek pairing. Fructose sweetness softens cultured dairy tang.",
        "source": "Mediterranean Diet Tradition"
    },
    {
        "a": "Tomato", "b": "Basil",
        "score": 98.0,
        "shared": ["Eugenol", "Hexanal", "Linalool"],
        "evidence": "World famous Caprese & Marinara pairing. Sweet herbal clove notes in basil amplify glutamic tomato savoriness.",
        "source": "Italian Culinary Science"
    },
    {
        "a": "Tomato", "b": "Garlic",
        "score": 95.0,
        "shared": ["Sulfur compounds", "Savory glutamates"],
        "evidence": "Savory allium sulfur bridges acid in tomato, producing intense umami depth.",
        "source": "Global Gastronomy"
    },
    {
        "a": "Dark Chocolate", "b": "Chili Pepper",
        "score": 88.0,
        "shared": ["Phenolic volatiles", "Capsaicin-Endorphin trigger"],
        "evidence": "Ancient Mesoamerican Aztec mole synergy. Capsaicin warmth accentuates rich roasted cacao theobromine.",
        "source": "Mesoamerican Culinary History"
    },
    {
        "a": "Dark Chocolate", "b": "Coffee",
        "score": 97.0,
        "shared": ["Pyrazines", "Furfuryl compounds", "Chlorogenic acid"],
        "evidence": "Identical roasting volatiles produce the ultimate mocha flavor profile.",
        "source": "Coffee & Chocolate Sensory Science"
    },
    {
        "a": "Strawberry", "b": "Balsamic Vinegar",
        "score": 91.0,
        "shared": ["Acetic esters", "Furaneol"],
        "evidence": "High gourmet pairing: acetic tartness paradoxically elevates human tongue perception of fruit sweetness.",
        "source": "Modernist Cuisine"
    },
    {
        "a": "Avocado", "b": "Lime",
        "score": 94.0,
        "shared": ["Terpenes", "Acid-fat balance"],
        "evidence": "Citric acid cuts rich monounsaturated oleic lipid coating on tongue while preventing enzymatic browning.",
        "source": "Mexican Culinary Science (Guacamole)"
    },
    {
        "a": "Apple", "b": "Cinnamon",
        "score": 98.0,
        "shared": ["Cinnamaldehyde", "Eugenol", "Fruit esters"],
        "evidence": "Warm woody aromatic compounds bind with malic fruit sweetness.",
        "source": "Pastry & Baking Flavor Pairings"
    },
    {
        "a": "Ginger", "b": "Honey",
        "score": 92.0,
        "shared": ["Warm aromatics", "Floral terpenes"],
        "evidence": "Gingerol pungency is rounded and coated by viscous honey sugars.",
        "source": "Global Beverage & Herbal Medicine"
    },
    {
        "a": "Cardamom", "b": "Pistachio",
        "score": 95.0,
        "shared": ["Pinene", "Terpinyl acetate"],
        "evidence": "Royal Mughal and Persian dessert foundation (Kulfi, Baklava, Halwa).",
        "source": "Persian & Mughal Culinary Records"
    }
]

def seed_database():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        # 1. Seed Demo Admin & Test User
        admin_user = db.query(User).filter(User.email == "admin@flavorfusion.ai").first()
        if not admin_user:
            admin_user = User(
                email="admin@flavorfusion.ai",
                full_name="Chef Alexander (Admin)",
                hashed_password=get_password_hash("AdminPass123!"),
                is_admin=True,
                is_active=True
            )
            db.add(admin_user)
            db.commit()
            db.refresh(admin_user)

            # Default preferences for admin
            pref = UserPreference(
                user_id=admin_user.id,
                preferred_cuisines=["Indian", "Mediterranean", "Italian"],
                favorite_ingredients=["Mango", "Curd", "Cardamom", "Garlic"],
                disliked_ingredients=[],
                spice_tolerance=4,
                sweet_affinity=3,
                sour_affinity=4,
                dietary_preferences=["Omnivore"],
                allergies=[],
                adventurousness=4
            )
            db.add(pref)
            db.commit()

        # Seed standard demo user
        demo_user = db.query(User).filter(User.email == "gourmet@flavorfusion.ai").first()
        if not demo_user:
            demo_user = User(
                email="gourmet@flavorfusion.ai",
                full_name="Priya Sharma",
                hashed_password=get_password_hash("Gourmet123!"),
                is_admin=False,
                is_active=True
            )
            db.add(demo_user)
            db.commit()
            db.refresh(demo_user)

            pref = UserPreference(
                user_id=demo_user.id,
                preferred_cuisines=["Indian", "Fusion"],
                favorite_ingredients=["Mango", "Cardamom", "Mint", "Pistachio"],
                disliked_ingredients=["Bitter Gourd"],
                spice_tolerance=3,
                sweet_affinity=4,
                sour_affinity=3,
                dietary_preferences=["Vegetarian"],
                allergies=[],
                adventurousness=4
            )
            db.add(pref)
            db.commit()

        # 2. Seed Ingredients & Flavor Profiles
        try:
            from scripts.seed_more_ingredients import EXPANDED_INGREDIENTS
            all_ingredients = INGREDIENTS_DATA + EXPANDED_INGREDIENTS
        except Exception:
            all_ingredients = INGREDIENTS_DATA

        for item in all_ingredients:
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

        # 2b. Seed Comprehensive Ingredient Catalog (179 items)
        try:
            from scripts.seed_comprehensive_ingredients import NEW_INGREDIENTS
            for item in NEW_INGREDIENTS:
                existing = db.query(Ingredient).filter(Ingredient.name.ilike(item["name"])).first()
                if not existing:
                    ing = Ingredient(
                        name=item["name"],
                        slug=item["name"].lower().replace(" ", "-"),
                        category=item["category"],
                        description=item["description"],
                        image_url=item.get("image_url"),
                        default_unit=item.get("default_unit", "g"),
                        allergens=item.get("allergens", []),
                        cuisines=item.get("cuisines", []),
                        is_curated=True
                    )
                    db.add(ing)
                    db.flush()
                    fp = IngredientFlavorProfile(
                        ingredient_id=ing.id,
                        sweet=item["sweet"],
                        salty=item["salty"],
                        sour=item["sour"],
                        bitter=item["bitter"],
                        umami=item["umami"],
                        spicy=item["spicy"],
                        intensity=item["intensity"],
                        primary_aromas=item["primary_aromas"],
                        texture_profile=item["texture_profile"],
                        dominant_compounds=item["dominant_compounds"]
                    )
                    db.add(fp)
            db.commit()
        except Exception as ex_comp:
            print(f"Notice on seeding comprehensive catalog: {ex_comp}")

        # 2c. Seed Indian Cuisine (North & South) + Fruits & Veggies Expansion (221 items total)
        try:
            try:
                from scripts.seed_indian_and_produce import NEW_INDIAN_AND_PRODUCE
            except ImportError:
                from backend.scripts.seed_indian_and_produce import NEW_INDIAN_AND_PRODUCE
            for item in NEW_INDIAN_AND_PRODUCE:
                existing = db.query(Ingredient).filter(Ingredient.name.ilike(item["name"])).first()
                if not existing:
                    ing = Ingredient(
                        name=item["name"],
                        slug=item["name"].lower().replace(" ", "-"),
                        category=item["category"],
                        description=item["description"],
                        image_url=item.get("image_url"),
                        default_unit=item.get("default_unit", "g"),
                        allergens=item.get("allergens", []),
                        cuisines=item.get("cuisines", []),
                        is_curated=True
                    )
                    db.add(ing)
                    db.flush()
                    fp = IngredientFlavorProfile(
                        ingredient_id=ing.id,
                        sweet=item["sweet"],
                        salty=item["salty"],
                        sour=item["sour"],
                        bitter=item["bitter"],
                        umami=item["umami"],
                        spicy=item["spicy"],
                        intensity=item["intensity"],
                        primary_aromas=item["primary_aromas"],
                        texture_profile=item["texture_profile"],
                        dominant_compounds=item["dominant_compounds"]
                    )
                    db.add(fp)

            # Reclassify legacy 'Produce' into distinct Vegetables and Fruits
            FRUIT_NAMES = {"mango", "lime", "lemon", "apple", "green apple", "strawberry", "pomegranate", "watermelon", "orange", "banana", "peach", "blueberry", "raspberry", "papaya", "guava", "lychee", "jackfruit", "custard apple", "fig", "pineapple", "kiwi", "grapes", "dragonfruit"}
            all_ings = db.query(Ingredient).all()
            for ing in all_ings:
                n_lower = ing.name.lower()
                if ing.category == "Produce":
                    if n_lower in FRUIT_NAMES:
                        ing.category = "Fruits"
                    else:
                        ing.category = "Vegetables"
            db.commit()
        except Exception as ex_ind:
            print(f"Notice on seeding Indian and produce catalog: {ex_ind}")

        # 3. Seed Pairing Evidence
        try:
            from scripts.seed_more_ingredients import EXPANDED_PAIRINGS
            extra_pairings = [
                {"a": p["ing_a"], "b": p["ing_b"], "score": p["score"], "shared": p.get("compounds", []), "evidence": p.get("evidence"), "source": p.get("source", "Flavor Intelligence Base")}
                for p in EXPANDED_PAIRINGS
            ]
            all_pairings = PAIRING_EVIDENCE_DATA + extra_pairings
        except Exception:
            all_pairings = PAIRING_EVIDENCE_DATA

        for pe in all_pairings:
            existing = db.query(IngredientPairingEvidence).filter(
                IngredientPairingEvidence.ingredient_a_name == pe["a"],
                IngredientPairingEvidence.ingredient_b_name == pe["b"]
            ).first()
            if not existing:
                evidence = IngredientPairingEvidence(
                    ingredient_a_name=pe["a"],
                    ingredient_b_name=pe["b"],
                    affinity_score=pe["score"],
                    shared_compounds=pe["shared"],
                    culinary_evidence=pe["evidence"],
                    source=pe["source"]
                )
                db.add(evidence)
        db.commit()
        print("Database seeded successfully with users, ingredients, and pairing evidence!")
    except Exception as e:
        db.rollback()
        print(f"Error seeding database: {e}")
        raise e
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()
