"""
FlavorFusion AI — Comprehensive Indian Cuisine, Veggies & Fruits Expansion
Seeds:
- South Indian staples (Curry leaves, Mustard seeds, Hing, Urad dal, Chana dal, Toor dal, Methi seeds, Sambar powder, Rasam powder, Dosa batter, Coconut oil, Fresh coconut, Drumstick, Idli podi)
- North Indian staples (Kasuri methi, Garam masala, Amchur, Cumin seeds, Black cardamom, Cloves, Mustard oil, Chaat masala, Rajma, Kashmiri chili, Fennel seeds, Bay leaf)
- Comprehensive Fruits (Papaya, Guava, Lychee, Jackfruit, Custard apple, Fig, Pineapple, Banana, Orange, Kiwi, Grapes, Dragonfruit)
- Comprehensive Vegetables (Okra, Bitter gourd, Bottle gourd, Ridge gourd, Brinjal, Spinach, Fresh methi, Cauliflower, Green peas, Carrot, Radish, Beetroot, Capsicum, Cabbage, Pumpkin)
- Normalizes categories so Explorer can easily filter Vegetables and Fruits cleanly.
"""

import sys
import os

backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from app.database.session import SessionLocal
from app.models.entities import Ingredient, IngredientFlavorProfile, IngredientPairingEvidence

NEW_INDIAN_AND_PRODUCE = [
    # =========================================================================
    # SOUTH INDIAN SPECIALTIES
    # =========================================================================
    {
        "name": "Curry Leaves",
        "category": "Herbs",
        "description": "Essential South Indian aromatic leaf with intense citrus-pine herbal fragrance that blooms in hot tempering oil.",
        "image_url": "https://images.unsplash.com/photo-1615485290382-441e4d049cb5?auto=format&fit=crop&w=600&q=80",
        "default_unit": "leaves",
        "allergens": [],
        "cuisines": ["South Indian", "Indian", "Sri Lankan"],
        "sweet": 0.5, "salty": 0.0, "sour": 0.8, "bitter": 2.5, "umami": 1.5, "spicy": 0.5, "intensity": 7.5,
        "primary_aromas": ["Herbal", "Citrus", "Piney", "Warm Spice"],
        "texture_profile": ["Crisp", "Fragile"],
        "dominant_compounds": ["Beta-Caryophyllene", "Alpha-Pinene", "Linalool", "Sabinene"]
    },
    {
        "name": "Mustard Seeds",
        "category": "Spices & Seasonings",
        "description": "Tiny whole black mustard seeds that crackle in hot oil to release nutty, pungent allyl isothiocyanate aroma.",
        "image_url": "https://images.unsplash.com/photo-1615485290748-e215442531e2?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tsp",
        "allergens": ["Mustard"],
        "cuisines": ["South Indian", "North Indian", "Indian", "Bengali"],
        "sweet": 0.5, "salty": 0.0, "sour": 0.8, "bitter": 3.2, "umami": 1.2, "spicy": 4.5, "intensity": 7.5,
        "primary_aromas": ["Pungent", "Nutty", "Sulfurous", "Peppery"],
        "texture_profile": ["Crunchy", "Grainy"],
        "dominant_compounds": ["Sinigrin", "Allyl Isothiocyanate", "Limonene"]
    },
    {
        "name": "Asafoetida",
        "category": "Spices & Seasonings",
        "description": "Pungent dried ferula resin (Hing) that blooms in hot ghee into deep savory allium umami aroma, aiding digestion.",
        "image_url": "https://images.unsplash.com/photo-1596040033229-a9821ebd058d?auto=format&fit=crop&w=600&q=80",
        "default_unit": "pinch",
        "allergens": [],
        "cuisines": ["South Indian", "North Indian", "Indian"],
        "sweet": 0.0, "salty": 0.0, "sour": 0.5, "bitter": 3.0, "umami": 6.5, "spicy": 2.0, "intensity": 9.0,
        "primary_aromas": ["Savory Umami", "Allium", "Sulfurous", "Earthy"],
        "texture_profile": ["Powder"],
        "dominant_compounds": ["Ferulic Acid", "Diallyl Disulfide", "Umbelliferone", "Pinene"]
    },
    {
        "name": "Urad Dal",
        "category": "Grains & Lentils",
        "description": "Skinless split black gram providing mucilaginous body for fermented idli-dosa batter and golden crunchy tadka.",
        "image_url": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["South Indian", "North Indian", "Indian"],
        "sweet": 2.5, "salty": 0.2, "sour": 0.5, "bitter": 0.8, "umami": 4.5, "spicy": 0.0, "intensity": 5.0,
        "primary_aromas": ["Nutty", "Earthy", "Malty"],
        "texture_profile": ["Creamy", "Soft", "Crunchy when fried"],
        "dominant_compounds": ["Pyrazines", "Methionine", "Glutamic Acid"]
    },
    {
        "name": "Chana Dal",
        "category": "Grains & Lentils",
        "description": "Nutty split Bengal gram lentils that impart delightful golden crunch to South Indian tempering and body to vadas.",
        "image_url": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["South Indian", "North Indian", "Indian"],
        "sweet": 3.0, "salty": 0.2, "sour": 0.3, "bitter": 0.8, "umami": 4.2, "spicy": 0.0, "intensity": 5.0,
        "primary_aromas": ["Nutty", "Roasted", "Earthy"],
        "texture_profile": ["Firm", "Nutty Crunch"],
        "dominant_compounds": ["Alkylpyrazines", "Hexanal", "Vanillin traces"]
    },
    {
        "name": "Toor Dal",
        "category": "Grains & Lentils",
        "description": "Split yellow pigeon peas; the velvety, hearty legume foundation of South Indian Sambar and Rasam.",
        "image_url": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["South Indian", "North Indian", "Indian"],
        "sweet": 2.8, "salty": 0.2, "sour": 0.2, "bitter": 0.8, "umami": 4.8, "spicy": 0.0, "intensity": 5.2,
        "primary_aromas": ["Earthy", "Nutty", "Legume"],
        "texture_profile": ["Velvety", "Creamy", "Hearty"],
        "dominant_compounds": ["Glutamic Acid", "Pyrazines", "Legume Globulins"]
    },
    {
        "name": "Fenugreek Seeds",
        "category": "Spices & Seasonings",
        "description": "Golden Methi seeds containing sotolon; delivers signature bitter-maple depth to sambars, pickles, and tadka.",
        "image_url": "https://images.unsplash.com/photo-1596040033229-a9821ebd058d?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tsp",
        "allergens": [],
        "cuisines": ["South Indian", "North Indian", "Indian"],
        "sweet": 1.5, "salty": 0.0, "sour": 0.5, "bitter": 5.5, "umami": 2.0, "spicy": 1.5, "intensity": 7.5,
        "primary_aromas": ["Maple", "Curry", "Bitter", "Herbaceous"],
        "texture_profile": ["Hard", "Grainy"],
        "dominant_compounds": ["Sotolon", "Diosgenin", "Trigonelline"]
    },
    {
        "name": "Sambar Powder",
        "category": "Spices & Seasonings",
        "description": "Heritage South Indian roasted spice blend of coriander, cumin, toor dal, red chilies, fenugreek, and curry leaves.",
        "image_url": "https://images.unsplash.com/photo-1596040033229-a9821ebd058d?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tbsp",
        "allergens": [],
        "cuisines": ["South Indian", "Indian"],
        "sweet": 1.5, "salty": 0.5, "sour": 1.5, "bitter": 2.0, "umami": 5.0, "spicy": 5.5, "intensity": 8.5,
        "primary_aromas": ["Warm Spice", "Roasted Lentil", "Earthy", "Peppery"],
        "texture_profile": ["Fine Powder"],
        "dominant_compounds": ["Linalool", "Cuminaldehyde", "Capsaicin", "Curcumin", "Pyrazines"]
    },
    {
        "name": "Rasam Powder",
        "category": "Spices & Seasonings",
        "description": "Fiery, aromatic South Indian spice blend of cracked tellicherry black pepper, cumin, coriander, and red chilies.",
        "image_url": "https://images.unsplash.com/photo-1596040033229-a9821ebd058d?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tbsp",
        "allergens": [],
        "cuisines": ["South Indian", "Indian"],
        "sweet": 0.5, "salty": 0.5, "sour": 1.5, "bitter": 2.0, "umami": 4.5, "spicy": 6.5, "intensity": 8.8,
        "primary_aromas": ["Peppery", "Cumin", "Warm", "Pungent"],
        "texture_profile": ["Coarse Powder"],
        "dominant_compounds": ["Piperine", "Cuminaldehyde", "Linalool", "Capsaicin"]
    },
    {
        "name": "Idli Dosa Batter",
        "category": "Bakery & Dough",
        "description": "Naturally fermented stone-ground batter of rice and urad dal with airy lactic acid tang, producing crispy dosas and fluffy idlis.",
        "image_url": "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?auto=format&fit=crop&w=600&q=80",
        "default_unit": "ml",
        "allergens": [],
        "cuisines": ["South Indian", "Indian"],
        "sweet": 2.0, "salty": 0.8, "sour": 4.0, "bitter": 0.5, "umami": 4.2, "spicy": 0.0, "intensity": 6.0,
        "primary_aromas": ["Fermented", "Tangy", "Malty", "Cereal"],
        "texture_profile": ["Aerated Liquid", "Crisp when griddled", "Puffy when steamed"],
        "dominant_compounds": ["Lactic Acid", "Diacetyl", "Ethyl Acetate", "Carbon Dioxide"]
    },
    {
        "name": "Grated Fresh Coconut",
        "category": "Fruits",
        "description": "Sweet, juicy shredded coconut meat providing rich lauric fats and creamy sweetness to chutneys, avial, and poriyals.",
        "image_url": "https://images.unsplash.com/photo-1550989460-0adf9ea622e2?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["South Indian", "Coastal", "Indian", "Southeast Asian"],
        "sweet": 5.5, "salty": 0.5, "sour": 0.5, "bitter": 0.5, "umami": 2.0, "spicy": 0.0, "intensity": 6.0,
        "primary_aromas": ["Coconut", "Sweet", "Creamy", "Tropical"],
        "texture_profile": ["Moist", "Fibrous", "Tender"],
        "dominant_compounds": ["Delta-Octalactone", "Delta-Decalactone", "Lauric Acid"]
    },
    {
        "name": "Coconut Oil",
        "category": "Sauces & Condiments",
        "description": "Cold-pressed virgin coconut oil providing the iconic, sweet-scented tropical aroma of Kerala and South Indian tempering.",
        "image_url": "https://images.unsplash.com/photo-1526947425960-945c6e72858f?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tbsp",
        "allergens": [],
        "cuisines": ["South Indian", "Kerala", "Indian", "Coastal"],
        "sweet": 3.0, "salty": 0.0, "sour": 0.0, "bitter": 0.0, "umami": 1.0, "spicy": 0.0, "intensity": 7.0,
        "primary_aromas": ["Coconut", "Warm", "Toasted", "Sweet"],
        "texture_profile": ["Smooth Oil", "Velvety"],
        "dominant_compounds": ["Lauric Acid", "Caprylic Acid", "Lactones"]
    },
    {
        "name": "Drumstick",
        "category": "Vegetables",
        "description": "Ridged Moringa pods cooked in South Indian Sambar for their sweet, herbaceous savory pulp and tender edible seeds.",
        "image_url": "https://images.unsplash.com/photo-1615485290382-441e4d049cb5?auto=format&fit=crop&w=600&q=80",
        "default_unit": "piece",
        "allergens": [],
        "cuisines": ["South Indian", "Indian"],
        "sweet": 2.0, "salty": 0.0, "sour": 0.5, "bitter": 1.8, "umami": 3.5, "spicy": 1.0, "intensity": 6.0,
        "primary_aromas": ["Vegetal", "Herbal", "Sweet Green"],
        "texture_profile": ["Fibrous Exterior", "Gelatinous Pulp"],
        "dominant_compounds": ["Glucosinolates", "Hexanal", "Terpenes"]
    },
    {
        "name": "Idli Podi",
        "category": "Spices & Seasonings",
        "description": "Gunpowder spice; coarse South Indian blend of roasted lentils, sesame, dried red chilies, and asafoetida mixed with ghee.",
        "image_url": "https://images.unsplash.com/photo-1596040033229-a9821ebd058d?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tbsp",
        "allergens": ["Sesame"],
        "cuisines": ["South Indian", "Indian"],
        "sweet": 1.0, "salty": 3.5, "sour": 0.5, "bitter": 1.5, "umami": 6.0, "spicy": 6.0, "intensity": 8.5,
        "primary_aromas": ["Roasted", "Nutty", "Fiery", "Toasted Sesame"],
        "texture_profile": ["Coarse Grainy", "Crunchy"],
        "dominant_compounds": ["Roasted Pyrazines", "Capsaicin", "Sesamol", "Asafoetida Sulfur"]
    },

    # =========================================================================
    # NORTH INDIAN SPECIALTIES
    # =========================================================================
    {
        "name": "Kasuri Methi",
        "category": "Herbs",
        "description": "Dried fenugreek leaves crushed over curries to release sotolon; the secret fragrant soul of butter chicken and dal makhani.",
        "image_url": "https://images.unsplash.com/photo-1596040033229-a9821ebd058d?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tbsp",
        "allergens": [],
        "cuisines": ["North Indian", "Punjabi", "Mughlai"],
        "sweet": 1.0, "salty": 0.0, "sour": 0.5, "bitter": 3.0, "umami": 4.5, "spicy": 0.5, "intensity": 8.5,
        "primary_aromas": ["Maple", "Curry", "Herbaceous", "Nutty"],
        "texture_profile": ["Dried Flakes", "Crumbly"],
        "dominant_compounds": ["Sotolon", "Coumarin", "Beta-Pinene"]
    },
    {
        "name": "Garam Masala",
        "category": "Spices & Seasonings",
        "description": "Warm North Indian royal spice blend of cinnamon, black cardamom, cloves, mace, nutmeg, and cumin.",
        "image_url": "https://images.unsplash.com/photo-1596040033229-a9821ebd058d?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tsp",
        "allergens": [],
        "cuisines": ["North Indian", "Indian", "Mughlai", "Awadhi"],
        "sweet": 2.5, "salty": 0.0, "sour": 0.8, "bitter": 1.8, "umami": 3.0, "spicy": 5.5, "intensity": 9.0,
        "primary_aromas": ["Warm Spice", "Woody", "Sweet Aromatic", "Pungent"],
        "texture_profile": ["Fine Powder"],
        "dominant_compounds": ["Cinnamaldehyde", "Eugenol", "Cineole", "Myristicin", "Piperine"]
    },
    {
        "name": "Amchur",
        "category": "Spices & Seasonings",
        "description": "Dry green mango powder delivering clean, mouthwatering tartness without adding liquid to North Indian curries and chaat.",
        "image_url": "https://images.unsplash.com/photo-1596040033229-a9821ebd058d?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tsp",
        "allergens": [],
        "cuisines": ["North Indian", "Indian"],
        "sweet": 2.0, "salty": 0.0, "sour": 8.0, "bitter": 1.0, "umami": 1.5, "spicy": 0.0, "intensity": 7.5,
        "primary_aromas": ["Tart", "Fruity", "Citrus", "Sharp"],
        "texture_profile": ["Fine Powder"],
        "dominant_compounds": ["Citric Acid", "Malic Acid", "Ethyl Butyrate"]
    },
    {
        "name": "Cumin Seeds",
        "category": "Spices & Seasonings",
        "description": "Whole jeera seeds rich in cuminaldehyde, releasing an unmistakable earthy, nutty warmth when bloomed in ghee.",
        "image_url": "https://images.unsplash.com/photo-1596040033229-a9821ebd058d?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tsp",
        "allergens": [],
        "cuisines": ["North Indian", "South Indian", "Indian", "Middle Eastern", "Mexican"],
        "sweet": 1.2, "salty": 0.0, "sour": 0.5, "bitter": 2.2, "umami": 2.5, "spicy": 2.0, "intensity": 7.0,
        "primary_aromas": ["Earthy", "Warm", "Woody", "Nutty"],
        "texture_profile": ["Seed", "Crunchy"],
        "dominant_compounds": ["Cuminaldehyde", "Cymene", "Terpinene"]
    },
    {
        "name": "Black Cardamom",
        "category": "Spices & Seasonings",
        "description": "Large smoky pods (Badi Elaichi) dried over open flames, providing deep camphorous, cineole-rich fragrance to biryanis.",
        "image_url": "https://images.unsplash.com/photo-1596040033229-a9821ebd058d?auto=format&fit=crop&w=600&q=80",
        "default_unit": "piece",
        "allergens": [],
        "cuisines": ["North Indian", "Indian", "Himalayan"],
        "sweet": 1.0, "salty": 0.0, "sour": 0.5, "bitter": 2.5, "umami": 3.0, "spicy": 3.5, "intensity": 8.5,
        "primary_aromas": ["Smoky", "Camphorous", "Woody", "Resinous"],
        "texture_profile": ["Coarse Pod"],
        "dominant_compounds": ["1,8-Cineole", "Guaiacol", "Alpha-Terpineol"]
    },
    {
        "name": "Cloves",
        "category": "Spices & Seasonings",
        "description": "Whole laung buds packed with eugenol, delivering immense sweet-spicy warmth and gentle numbing depth.",
        "image_url": "https://images.unsplash.com/photo-1596040033229-a9821ebd058d?auto=format&fit=crop&w=600&q=80",
        "default_unit": "piece",
        "allergens": [],
        "cuisines": ["North Indian", "South Indian", "Indian", "Global"],
        "sweet": 3.0, "salty": 0.0, "sour": 0.5, "bitter": 3.0, "umami": 2.0, "spicy": 5.0, "intensity": 9.5,
        "primary_aromas": ["Warm Spice", "Sweet", "Pungent", "Medicinal"],
        "texture_profile": ["Dried Bud"],
        "dominant_compounds": ["Eugenol", "Eugenyl Acetate", "Beta-Caryophyllene"]
    },
    {
        "name": "Mustard Oil",
        "category": "Sauces & Condiments",
        "description": "Pungent cold-pressed raw mustard oil (Kachi Ghani) with eye-watering sharpness that mellows into savory gold when smoked.",
        "image_url": "https://images.unsplash.com/photo-1526947425960-945c6e72858f?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tbsp",
        "allergens": ["Mustard"],
        "cuisines": ["North Indian", "Punjabi", "Bengali"],
        "sweet": 0.5, "salty": 0.0, "sour": 0.5, "bitter": 2.5, "umami": 1.5, "spicy": 7.0, "intensity": 8.5,
        "primary_aromas": ["Pungent", "Wasabi-like", "Nutty", "Sulfurous"],
        "texture_profile": ["Golden Viscous Oil"],
        "dominant_compounds": ["Allyl Isothiocyanate", "Erucic Acid", "Sinigrin"]
    },
    {
        "name": "Chaat Masala",
        "category": "Spices & Seasonings",
        "description": "Tangy, sulfurous street-food finishing spice blend of Kala Namak (black salt), amchur, cumin, coriander, and ginger.",
        "image_url": "https://images.unsplash.com/photo-1596040033229-a9821ebd058d?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tsp",
        "allergens": [],
        "cuisines": ["North Indian", "Indian"],
        "sweet": 1.0, "salty": 5.0, "sour": 6.5, "bitter": 1.0, "umami": 6.0, "spicy": 4.0, "intensity": 8.8,
        "primary_aromas": ["Sulfurous", "Tangy", "Savory Umami", "Piquant"],
        "texture_profile": ["Fine Powder"],
        "dominant_compounds": ["Hydrogen Sulfide", "Cuminaldehyde", "Citric Acid", "Piperine"]
    },
    {
        "name": "Rajma",
        "category": "Grains & Lentils",
        "description": "Hearty red kidney beans slow-simmered with onion-tomato-ginger masala for classic Punjabi comfort.",
        "image_url": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["North Indian", "Punjabi"],
        "sweet": 2.5, "salty": 0.2, "sour": 0.2, "bitter": 0.8, "umami": 5.0, "spicy": 0.0, "intensity": 5.5,
        "primary_aromas": ["Earthy", "Nutty", "Legume"],
        "texture_profile": ["Creamy", "Hearty", "Meaty"],
        "dominant_compounds": ["Legume Globulins", "Glutamic Acid", "Pyrazines"]
    },
    {
        "name": "Kashmiri Red Chili",
        "category": "Spices & Seasonings",
        "description": "Famed mild chili providing radiant deep-red restaurant gravy coloration with gentle, fruity sweet warmth.",
        "image_url": "https://images.unsplash.com/photo-1596040033229-a9821ebd058d?auto=format&fit=crop&w=600&q=80",
        "default_unit": "piece",
        "allergens": [],
        "cuisines": ["North Indian", "Indian"],
        "sweet": 2.5, "salty": 0.0, "sour": 1.0, "bitter": 1.0, "umami": 2.0, "spicy": 3.5, "intensity": 6.5,
        "primary_aromas": ["Fruity", "Smoky", "Earthy", "Mild Heat"],
        "texture_profile": ["Wrinkled Pod"],
        "dominant_compounds": ["Capsanthin", "Capsorubin", "Mild Capsaicin"]
    },
    {
        "name": "Fennel Seeds",
        "category": "Spices & Seasonings",
        "description": "Sweet saunf seeds bursting with anethole; delivers refreshing licorice notes to Kashmiri curries and digestifs.",
        "image_url": "https://images.unsplash.com/photo-1596040033229-a9821ebd058d?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tsp",
        "allergens": [],
        "cuisines": ["North Indian", "Kashmiri", "Indian"],
        "sweet": 5.5, "salty": 0.0, "sour": 0.5, "bitter": 1.2, "umami": 1.0, "spicy": 1.5, "intensity": 7.0,
        "primary_aromas": ["Anise", "Sweet", "Herbaceous", "Refreshing"],
        "texture_profile": ["Seed", "Crunchy"],
        "dominant_compounds": ["Trans-Anethole", "Estragole", "Fenchone"]
    },
    {
        "name": "Bay Leaf",
        "category": "Herbs",
        "description": "Indian cassia leaf (Tej Patta) with sweet cinnamon-clove aromatic notes, distinct from Mediterranean bay leaves.",
        "image_url": "https://images.unsplash.com/photo-1596040033229-a9821ebd058d?auto=format&fit=crop&w=600&q=80",
        "default_unit": "leaves",
        "allergens": [],
        "cuisines": ["North Indian", "Indian", "Mughlai"],
        "sweet": 1.0, "salty": 0.0, "sour": 0.5, "bitter": 1.8, "umami": 2.0, "spicy": 2.0, "intensity": 6.5,
        "primary_aromas": ["Cinnamon", "Woody", "Warm Spice", "Balsamic"],
        "texture_profile": ["Dried Tough Leaf"],
        "dominant_compounds": ["Cinnamaldehyde", "Eugenol", "Linalool"]
    },

    # =========================================================================
    # COMPREHENSIVE FRUITS
    # =========================================================================
    {
        "name": "Papaya",
        "category": "Fruits",
        "description": "Sweet, buttery orange tropical fruit loaded with papain enzymes, subtle musky sweetness, and lush juiciness.",
        "image_url": "https://images.unsplash.com/photo-1517282009859-f000ec3b26fe?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Tropical", "Southeast Asian"],
        "sweet": 6.5, "salty": 0.0, "sour": 1.2, "bitter": 0.5, "umami": 1.0, "spicy": 0.0, "intensity": 5.5,
        "primary_aromas": ["Tropical", "Musky", "Floral", "Sweet"],
        "texture_profile": ["Soft", "Melting", "Succulent"],
        "dominant_compounds": ["Linalool", "Benzyl Isothiocyanate", "Papain"]
    },
    {
        "name": "Guava",
        "category": "Fruits",
        "description": "Crisp sweet-tart tropical fruit with fragrant floral caryophyllene aroma, iconic when eaten with red chili and black salt.",
        "image_url": "https://images.unsplash.com/photo-1536511135898-752b0d49281c?auto=format&fit=crop&w=600&q=80",
        "default_unit": "piece",
        "allergens": [],
        "cuisines": ["Indian", "Tropical", "Mexican"],
        "sweet": 6.0, "salty": 0.0, "sour": 3.5, "bitter": 1.0, "umami": 0.8, "spicy": 0.0, "intensity": 7.0,
        "primary_aromas": ["Floral", "Green", "Tropical", "Fruity"],
        "texture_profile": ["Crisp", "Grainy Core", "Crunchy"],
        "dominant_compounds": ["Beta-Caryophyllene", "Hexanal", "Ethyl Acetate"]
    },
    {
        "name": "Lychee",
        "category": "Fruits",
        "description": "Delicate translucent fruit bursting with floral rose-like sweetness, juicy acidity, and perfumed aroma.",
        "image_url": "https://images.unsplash.com/photo-1577234286642-fc512a5f8f11?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Asian", "Indian", "Tropical"],
        "sweet": 7.5, "salty": 0.0, "sour": 2.0, "bitter": 0.2, "umami": 0.5, "spicy": 0.0, "intensity": 7.0,
        "primary_aromas": ["Floral", "Rose", "Sweet", "Fruity"],
        "texture_profile": ["Translucent", "Juicy", "Gelatinous"],
        "dominant_compounds": ["Linalool", "Rose Oxide", "Geraniol"]
    },
    {
        "name": "Jackfruit",
        "category": "Fruits",
        "description": "Versatile giant tropical fruit; savory meaty texture when green (kathal), and lush honey-banana sweetness when ripe.",
        "image_url": "https://images.unsplash.com/photo-1596707328659-4fa2c66810c9?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["South Indian", "Indian", "Southeast Asian"],
        "sweet": 7.0, "salty": 0.0, "sour": 1.5, "bitter": 0.5, "umami": 3.0, "spicy": 0.0, "intensity": 7.5,
        "primary_aromas": ["Banana-Pineapple", "Tropical", "Ester", "Sweet"],
        "texture_profile": ["Fibrous", "Chewy", "Meaty"],
        "dominant_compounds": ["Isoamyl Acetate", "Ethyl Butyrate", "Propyl Isovalerate"]
    },
    {
        "name": "Custard Apple",
        "category": "Fruits",
        "description": "Velvety Sitaphal with intensely sweet, fragrant vanilla-pear pulp surrounding smooth dark seeds.",
        "image_url": "https://images.unsplash.com/photo-1587049352846-4a222e784d38?auto=format&fit=crop&w=600&q=80",
        "default_unit": "piece",
        "allergens": [],
        "cuisines": ["Indian", "Tropical"],
        "sweet": 8.5, "salty": 0.0, "sour": 1.0, "bitter": 0.2, "umami": 1.0, "spicy": 0.0, "intensity": 7.5,
        "primary_aromas": ["Vanilla", "Floral", "Sweet Custard", "Piney"],
        "texture_profile": ["Creamy", "Granular", "Melting"],
        "dominant_compounds": ["Alpha-Pinene", "Beta-Pinene", "Limonene", "Ethyl Esters"]
    },
    {
        "name": "Fig",
        "category": "Fruits",
        "description": "Plump fresh Anjeer with honeyed floral jamminess, chewy skin, and delightful crunchy seeds.",
        "image_url": "https://images.unsplash.com/photo-1601493700631-2b16ec4b4716?auto=format&fit=crop&w=600&q=80",
        "default_unit": "piece",
        "allergens": [],
        "cuisines": ["Mediterranean", "Indian", "Middle Eastern"],
        "sweet": 7.2, "salty": 0.1, "sour": 1.0, "bitter": 0.5, "umami": 1.5, "spicy": 0.0, "intensity": 6.0,
        "primary_aromas": ["Honey", "Berry", "Earthy", "Floral"],
        "texture_profile": ["Jammy", "Tender", "Seedy Crunch"],
        "dominant_compounds": ["Benzaldehyde", "Linalool", "Eugenol"]
    },
    {
        "name": "Pineapple",
        "category": "Fruits",
        "description": "Golden tropical fruit bursting with sweet-tart bromelain juice and high ethyl butyrate brightness.",
        "image_url": "https://images.unsplash.com/photo-1550258987-190a2d41a8ba?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Tropical", "Indian", "Southeast Asian"],
        "sweet": 7.8, "salty": 0.0, "sour": 4.5, "bitter": 0.2, "umami": 0.5, "spicy": 0.0, "intensity": 7.8,
        "primary_aromas": ["Tropical", "Sweet Fruity", "Ester", "Zesty"],
        "texture_profile": ["Fibrous", "Juicy", "Crisp"],
        "dominant_compounds": ["Ethyl Butyrate", "Bromelain", "Furaneol"]
    },
    {
        "name": "Banana",
        "category": "Fruits",
        "description": "Rich creamy fruit packed with potassium and isoamyl acetate aroma, beloved in desserts, smoothies, and savory roasts.",
        "image_url": "https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?auto=format&fit=crop&w=600&q=80",
        "default_unit": "piece",
        "allergens": [],
        "cuisines": ["Global", "Indian", "Tropical"],
        "sweet": 7.5, "salty": 0.0, "sour": 1.0, "bitter": 0.2, "umami": 1.0, "spicy": 0.0, "intensity": 6.0,
        "primary_aromas": ["Fruity Ester", "Creamy", "Sweet", "Vanilla-like"],
        "texture_profile": ["Creamy", "Soft", "Velvety"],
        "dominant_compounds": ["Isoamyl Acetate", "Eugenol", "Butyl Acetate"]
    },
    {
        "name": "Orange",
        "category": "Fruits",
        "description": "Juicy sweet citrus segment filled with sunshine, balanced citric acid, and uplifting limonene fragrance.",
        "image_url": "https://images.unsplash.com/photo-1547514701-42782101795e?auto=format&fit=crop&w=600&q=80",
        "default_unit": "piece",
        "allergens": [],
        "cuisines": ["Global", "Mediterranean"],
        "sweet": 6.5, "salty": 0.0, "sour": 4.2, "bitter": 0.8, "umami": 0.5, "spicy": 0.0, "intensity": 7.0,
        "primary_aromas": ["Citrus", "Sweet", "Zesty", "Fresh"],
        "texture_profile": ["Juicy", "Vesicular", "Tender"],
        "dominant_compounds": ["Limonene", "Citral", "Valencene"]
    },
    {
        "name": "Kiwi",
        "category": "Fruits",
        "description": "Vibrant emerald fruit with exhilarating electric acidity, delicate sweetness, and tender edible black seeds.",
        "image_url": "https://images.unsplash.com/photo-1585059895524-72359e06133a?auto=format&fit=crop&w=600&q=80",
        "default_unit": "piece",
        "allergens": [],
        "cuisines": ["Global", "New Zealand"],
        "sweet": 6.0, "salty": 0.0, "sour": 5.0, "bitter": 0.5, "umami": 0.5, "spicy": 0.0, "intensity": 7.2,
        "primary_aromas": ["Tart Green", "Tropical", "Fresh", "Zesty"],
        "texture_profile": ["Succulent", "Soft", "Popping Seeds"],
        "dominant_compounds": ["Ethyl Butyrate", "Actinidin", "Hexanal"]
    },
    {
        "name": "Grapes",
        "category": "Fruits",
        "description": "Crisp sweet berries packed with refreshing juice, natural tartaric acid, and subtle floral skin tannins.",
        "image_url": "https://images.unsplash.com/photo-1537640538966-79f369143f8f?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Global", "Mediterranean"],
        "sweet": 7.0, "salty": 0.0, "sour": 3.0, "bitter": 0.2, "umami": 0.5, "spicy": 0.0, "intensity": 6.0,
        "primary_aromas": ["Fruity", "Floral", "Sweet", "Wine-like"],
        "texture_profile": ["Taut Skin", "Bursting Juice", "Crisp"],
        "dominant_compounds": ["Tartaric Acid", "Methyl Anthranilate", "Linalool"]
    },
    {
        "name": "Dragonfruit",
        "category": "Fruits",
        "description": "Exotic Pitaya with speckled poppy-like seeds, refreshing mild melon sweetness, and vibrant natural pigments.",
        "image_url": "https://images.unsplash.com/photo-1527325678964-54921661f888?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Tropical", "Asian"],
        "sweet": 4.5, "salty": 0.0, "sour": 1.5, "bitter": 0.2, "umami": 0.5, "spicy": 0.0, "intensity": 4.5,
        "primary_aromas": ["Mild Melon", "Aquatic", "Fresh", "Subtle Sweet"],
        "texture_profile": ["Crunchy Seeds", "Gelatinous", "Juicy"],
        "dominant_compounds": ["Betacyanins", "Hexanal", "Limonene"]
    },

    # =========================================================================
    # COMPREHENSIVE VEGETABLES (VEGGIES)
    # =========================================================================
    {
        "name": "Okra",
        "category": "Vegetables",
        "description": "Tender green Bhindi pods; crisp and caramelized when stir-fried with dry spices or amchur.",
        "image_url": "https://images.unsplash.com/photo-1597362925123-77861d3fbac7?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Middle Eastern", "Southern US"],
        "sweet": 2.0, "salty": 0.0, "sour": 0.5, "bitter": 1.5, "umami": 3.0, "spicy": 0.0, "intensity": 5.0,
        "primary_aromas": ["Green Vegetal", "Earthy", "Grassy"],
        "texture_profile": ["Crisp Exterior", "Tender Core", "Crunchy Seeds"],
        "dominant_compounds": ["Mucilage Glycoproteins", "Hexanal", "Octenal"]
    },
    {
        "name": "Bitter Gourd",
        "category": "Vegetables",
        "description": "Warty green Karela rich in charantin; celebrated in Indian and Asian kitchens when balanced with tamarind, jaggery, or coconut.",
        "image_url": "https://images.unsplash.com/photo-1597362925123-77861d3fbac7?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Chinese", "Southeast Asian"],
        "sweet": 0.5, "salty": 0.0, "sour": 0.5, "bitter": 9.0, "umami": 2.0, "spicy": 0.0, "intensity": 9.0,
        "primary_aromas": ["Intensely Bitter", "Green", "Medicinal"],
        "texture_profile": ["Crunchy", "Firm", "Ridged"],
        "dominant_compounds": ["Charantin", "Momordicin", "Cucurbitacins"]
    },
    {
        "name": "Bottle Gourd",
        "category": "Vegetables",
        "description": "Mild, hydrating Lauki (Sorakkai); absorbs spices and lentils effortlessly in light cooling stews and dals.",
        "image_url": "https://images.unsplash.com/photo-1597362925123-77861d3fbac7?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Asian"],
        "sweet": 2.5, "salty": 0.0, "sour": 0.2, "bitter": 0.5, "umami": 2.0, "spicy": 0.0, "intensity": 3.5,
        "primary_aromas": ["Aquatic", "Mild Green", "Sweet Vegetal"],
        "texture_profile": ["Spongy", "Tender", "Hydrated"],
        "dominant_compounds": ["Cucurbitacins", "L-Choline", "Pectin"]
    },
    {
        "name": "Ridge Gourd",
        "category": "Vegetables",
        "description": "Sweet, tender Turai (Peerkangai); delicate green gourd perfect for light South Indian kootu or spiced dry stir-fries.",
        "image_url": "https://images.unsplash.com/photo-1597362925123-77861d3fbac7?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Asian"],
        "sweet": 3.0, "salty": 0.0, "sour": 0.2, "bitter": 0.5, "umami": 2.2, "spicy": 0.0, "intensity": 3.8,
        "primary_aromas": ["Sweet Vegetal", "Mild Green", "Fresh"],
        "texture_profile": ["Soft", "Melting", "Delicate"],
        "dominant_compounds": ["Luffein", "Riboflavin", "Pectin"]
    },
    {
        "name": "Brinjal",
        "category": "Vegetables",
        "description": "Glossy purple Baingan (Eggplant); acts as a savory umami sponge that melts into velvety richness in Baingan Bharta and Sambar.",
        "image_url": "https://images.unsplash.com/photo-1615485290382-441e4d049cb5?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Mediterranean", "Italian", "Middle Eastern"],
        "sweet": 2.0, "salty": 0.0, "sour": 0.5, "bitter": 2.5, "umami": 4.5, "spicy": 0.0, "intensity": 5.5,
        "primary_aromas": ["Earthy", "Savory", "Vegetal", "Faint Smoky"],
        "texture_profile": ["Spongy Raw", "Velvety Cooked", "Melting"],
        "dominant_compounds": ["Nasunin", "Chlorogenic Acid", "Guaiacol"]
    },
    {
        "name": "Spinach",
        "category": "Vegetables",
        "description": "Tender iron-rich Palak leaves; cooks down into velvety emerald puree for Palak Paneer, dals, and healthy bowls.",
        "image_url": "https://images.unsplash.com/photo-1576045057995-568f588f82fb?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Global", "Mediterranean"],
        "sweet": 1.5, "salty": 0.2, "sour": 0.5, "bitter": 2.0, "umami": 4.0, "spicy": 0.0, "intensity": 5.0,
        "primary_aromas": ["Earthy Green", "Iron-rich", "Mineral", "Fresh"],
        "texture_profile": ["Tender Leaf", "Silky when wilted"],
        "dominant_compounds": ["Oxalic Acid", "Chlorophyll", "Lutein", "Hexanal"]
    },
    {
        "name": "Cauliflower",
        "category": "Vegetables",
        "description": "Crisp brassica florets (Gobi); caramelizes beautifully with turmeric and cumin in Aloo Gobi and roast trays.",
        "image_url": "https://images.unsplash.com/photo-1568584711075-3d021a7c3ca3?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Global", "European"],
        "sweet": 3.0, "salty": 0.0, "sour": 0.5, "bitter": 1.5, "umami": 3.0, "spicy": 0.0, "intensity": 5.0,
        "primary_aromas": ["Nutty", "Sweet Brassica", "Earthy"],
        "texture_profile": ["Crisp Raw", "Tender-Crisp Roasted", "Soft Boiled"],
        "dominant_compounds": ["Glucosinolates", "Dimethyl Disulfide", "Sulforaphane"]
    },
    {
        "name": "Green Peas",
        "category": "Vegetables",
        "description": "Sweet green Matar gems bursting with sucrose and fresh grassy hexenal aroma, essential in Indian gravies and pulao.",
        "image_url": "https://images.unsplash.com/photo-1587735243615-c03f25aaff15?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Global", "British"],
        "sweet": 6.0, "salty": 0.0, "sour": 0.5, "bitter": 0.5, "umami": 3.5, "spicy": 0.0, "intensity": 5.5,
        "primary_aromas": ["Sweet Green", "Grassy", "Fresh", "Legume"],
        "texture_profile": ["Popping Skin", "Tender Creamy Core"],
        "dominant_compounds": ["Hexenal", "Pyrazines", "Sucrose"]
    },
    {
        "name": "Carrot",
        "category": "Vegetables",
        "description": "Crunchy sweet root rich in beta-carotene; stars in savory sambars, poriyals, and decadent winter Gajar ka Halwa.",
        "image_url": "https://images.unsplash.com/photo-1598170845058-32b9d6a5da37?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Global"],
        "sweet": 6.5, "salty": 0.1, "sour": 0.5, "bitter": 0.5, "umami": 2.0, "spicy": 0.0, "intensity": 5.5,
        "primary_aromas": ["Sweet Earthy", "Woody", "Terpene"],
        "texture_profile": ["Crisp Crunch", "Tender Cooked"],
        "dominant_compounds": ["Terpinolene", "Caryophyllene", "Beta-Carotene"]
    },
    {
        "name": "Radish",
        "category": "Vegetables",
        "description": "Crisp white Mooli (Mullangi) with peppery isothiocyanate bite that transforms into sweet, succulent umami when simmered in Sambar.",
        "image_url": "https://images.unsplash.com/photo-1597362925123-77861d3fbac7?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Asian", "Japanese"],
        "sweet": 2.0, "salty": 0.0, "sour": 0.5, "bitter": 2.0, "umami": 2.5, "spicy": 4.0, "intensity": 6.5,
        "primary_aromas": ["Peppery", "Pungent", "Sulfurous", "Crisp"],
        "texture_profile": ["Juicy Crunch", "Crisp"],
        "dominant_compounds": ["4-Methylthio-3-butenyl Isothiocyanate", "Sinigrin"]
    },
    {
        "name": "Beetroot",
        "category": "Vegetables",
        "description": "Vibrant ruby root vegetable with geosmin earthiness and deep natural sweetness, shining in South Indian poriyal and cutlets.",
        "image_url": "https://images.unsplash.com/photo-1597362925123-77861d3fbac7?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Global", "Eastern European"],
        "sweet": 6.0, "salty": 0.1, "sour": 0.5, "bitter": 0.8, "umami": 2.5, "spicy": 0.0, "intensity": 6.0,
        "primary_aromas": ["Earthy", "Sweet", "Root", "Beet"],
        "texture_profile": ["Dense Crunch", "Succulent Cooked"],
        "dominant_compounds": ["Geosmin", "Betanin", "Pyrazines"]
    },
    {
        "name": "Capsicum",
        "category": "Vegetables",
        "description": "Crisp green bell pepper with distinct pyrazine fresh aroma, essential in Indian Kadai gravies and stir-fries.",
        "image_url": "https://images.unsplash.com/photo-1563565375-f3fdfdbefa83?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Mexican", "Mediterranean"],
        "sweet": 4.5, "salty": 0.0, "sour": 1.0, "bitter": 1.5, "umami": 2.0, "spicy": 0.5, "intensity": 6.0,
        "primary_aromas": ["Green Bell", "Earthy", "Zesty", "Fresh"],
        "texture_profile": ["Crisp", "Juicy", "Crunchy"],
        "dominant_compounds": ["2-Methoxy-3-isobutylpyrazine", "Hexenal"]
    },
    {
        "name": "Cabbage",
        "category": "Vegetables",
        "description": "Crunchy layered brassica (Patta Gobi); quick-sautéed with mustard seeds, curry leaves, and coconut for delicious poriyal.",
        "image_url": "https://images.unsplash.com/photo-1597362925123-77861d3fbac7?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "Asian", "European"],
        "sweet": 3.5, "salty": 0.0, "sour": 0.5, "bitter": 1.5, "umami": 2.5, "spicy": 0.5, "intensity": 5.0,
        "primary_aromas": ["Sweet Brassica", "Green", "Peppery"],
        "texture_profile": ["Crisp", "Ribboned Crunch"],
        "dominant_compounds": ["Allyl Isothiocyanate", "Dimethyl Trisulfide"]
    },
    {
        "name": "Pumpkin",
        "category": "Vegetables",
        "description": "Golden Kaddu squash that caramelizes into velvety sweet richness in South Indian sambar, kootu, and North Indian curries.",
        "image_url": "https://images.unsplash.com/photo-1570586437263-ab629fccc818?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Indian", "American", "Global"],
        "sweet": 6.0, "salty": 0.0, "sour": 0.5, "bitter": 0.5, "umami": 2.5, "spicy": 0.0, "intensity": 5.5,
        "primary_aromas": ["Sweet Squash", "Earthy", "Caramelized"],
        "texture_profile": ["Firm Raw", "Meltingly Soft Cooked"],
        "dominant_compounds": ["Beta-Ionone", "Carotenoids", "Hexanal"]
    }
]

FRUIT_NAMES = {
    "mango", "lime", "lemon", "apple", "strawberry", "pomegranate", "tamarind", "coconut", "watermelon",
    "orange", "banana", "pineapple", "grapes", "kiwi", "papaya", "guava", "lychee", "jackfruit",
    "custard apple", "fig", "dragonfruit", "grated fresh coconut"
}

VEGETABLE_NAMES = {
    "tomato", "avocado", "garlic", "onion", "shallot", "scallion", "ginger", "chili pepper",
    "potato", "bok choy", "shiitake mushrooms", "san marzano tomatoes", "okra", "bitter gourd",
    "bottle gourd", "ridge gourd", "brinjal", "spinach", "cauliflower", "green peas", "carrot",
    "radish", "beetroot", "capsicum", "cabbage", "pumpkin", "drumstick"
}

def seed_indian_and_produce():
    db = SessionLocal()
    print("Starting Indian cuisine, fruits & vegetables seeding...")
    
    try:
        # 1. Reclassify existing ingredients into clear "Fruits" and "Vegetables"
        all_ings = db.query(Ingredient).all()
        for ing in all_ings:
            name_l = ing.name.lower().strip()
            if name_l in FRUIT_NAMES:
                ing.category = "Fruits"
            elif name_l in VEGETABLE_NAMES:
                ing.category = "Vegetables"
            elif ing.category == "Produce":
                ing.category = "Vegetables"
        db.commit()
        print("Existing produce reclassified into Fruits & Vegetables!")

        # 2. Insert new ingredients
        added_count = 0
        for item in NEW_INDIAN_AND_PRODUCE:
            clean_name = item["name"].strip()
            existing = db.query(Ingredient).filter(Ingredient.name.ilike(clean_name)).first()
            if not existing:
                ing = Ingredient(
                    name=clean_name,
                    slug=clean_name.lower().replace(" ", "-"),
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
                added_count += 1
            else:
                # Update category and profile if needed
                existing.category = item["category"]
                if not existing.cuisines:
                    existing.cuisines = item.get("cuisines", [])
                if existing.flavor_profile:
                    existing.flavor_profile.dominant_compounds = item["dominant_compounds"]

        db.commit()
        print(f"Successfully added {added_count} new Indian, fruit & vegetable ingredients!")

        # Total counts
        total = db.query(Ingredient).count()
        print(f"Total ingredients in catalog now: {total}")

    except Exception as e:
        db.rollback()
        print(f"Error seeding Indian & produce data: {e}")
        raise e
    finally:
        db.close()

if __name__ == "__main__":
    seed_indian_and_produce()
