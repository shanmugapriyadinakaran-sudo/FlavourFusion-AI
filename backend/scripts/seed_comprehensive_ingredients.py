"""
FlavorFusion AI — Comprehensive Ingredient Catalog Seed Script
Adds chocolate variety, ice cream variety, baking needs, pizza & dough,
stuffing & fillings, meats, Chinese ingredients, Italian, Spanish,
noodles, pasta, sauce variety, vanilla extract, and more.
"""

import sys
import os

backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from app.database.session import SessionLocal
from app.models.entities import Ingredient, IngredientFlavorProfile, IngredientPairingEvidence

NEW_INGREDIENTS = [
    # ----------------- CHOCOLATE VARIETY -----------------
    {
        "name": "Milk Chocolate",
        "category": "Sweets & Desserts",
        "description": "Smooth, creamy confectionery made of cocoa solids, cocoa butter, milk solids, and sucrose.",
        "image_url": "https://images.unsplash.com/photo-1549007994-cb92caebd54b?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": ["Dairy"],
        "cuisines": ["Global", "European", "American"],
        "sweet": 7.8, "salty": 1.2, "sour": 0.5, "bitter": 2.2, "umami": 1.5, "spicy": 0.0, "intensity": 6.5,
        "primary_aromas": ["Sweet", "Caramelized", "Dairy"],
        "texture_profile": ["Creamy", "Melting", "Velvety"],
        "dominant_compounds": ["Vanillin", "Delta-Decalactone", "Tetramethylpyrazine", "Theobromine"]
    },
    {
        "name": "White Chocolate",
        "category": "Sweets & Desserts",
        "description": "Rich confection of pure deodorized cocoa butter, milk solids, and fragrant vanilla aroma.",
        "image_url": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": ["Dairy"],
        "cuisines": ["European", "Global"],
        "sweet": 8.5, "salty": 0.8, "sour": 0.2, "bitter": 0.0, "umami": 0.8, "spicy": 0.0, "intensity": 6.0,
        "primary_aromas": ["Vanilla", "Milky", "Sweet"],
        "texture_profile": ["Buttery", "Velvety", "Smooth"],
        "dominant_compounds": ["Vanillin", "Diacetyl", "Cocoa Butter Triglycerides", "Delta-Octalactone"]
    },
    {
        "name": "Dark Chocolate 85%",
        "category": "Sweets & Desserts",
        "description": "High-cacao bittersweet chocolate featuring deep roasted polyphenols, earthy bitterness, and faint fruit acidity.",
        "image_url": "https://images.unsplash.com/photo-1511381939415-e44015466834?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["European", "Mesoamerican", "Global"],
        "sweet": 2.2, "salty": 0.2, "sour": 2.5, "bitter": 8.5, "umami": 3.0, "spicy": 0.0, "intensity": 9.0,
        "primary_aromas": ["Roasted", "Earthy", "Woody", "Cocoa"],
        "texture_profile": ["Firm", "Snap", "Melting"],
        "dominant_compounds": ["Theobromine", "Tetramethylpyrazine", "Phenylethyl Alcohol", "Isovaleric Acid", "Furfuryl Alcohol"]
    },
    {
        "name": "Cocoa Powder",
        "category": "Pantry",
        "description": "Pure unsweetened Dutch-processed cocoa powder with intense concentrated chocolate essence.",
        "image_url": "https://images.unsplash.com/photo-1541592106381-b31e9677c0e5?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tbsp",
        "allergens": [],
        "cuisines": ["Global", "European"],
        "sweet": 0.5, "salty": 0.2, "sour": 1.8, "bitter": 8.8, "umami": 2.5, "spicy": 0.0, "intensity": 8.5,
        "primary_aromas": ["Deep Roasted", "Earthy", "Chocolate"],
        "texture_profile": ["Powdery", "Dry"],
        "dominant_compounds": ["Tetramethylpyrazine", "Theobromine", "Furfuryl Alcohol", "Pyrroles"]
    },
    {
        "name": "Cacao Nibs",
        "category": "Pantry",
        "description": "Crushed roasted fermented pure cacao beans with a nutty, satisfying artisan crunch.",
        "image_url": "https://images.unsplash.com/photo-1587132137056-bfbf0166836e?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Mesoamerican", "Global"],
        "sweet": 0.8, "salty": 0.1, "sour": 3.2, "bitter": 8.0, "umami": 2.0, "spicy": 0.0, "intensity": 8.2,
        "primary_aromas": ["Nutty", "Roasted", "Fruity", "Earthy"],
        "texture_profile": ["Crunchy", "Brittle"],
        "dominant_compounds": ["Theobromine", "Pyrazines", "Polyphenols", "Flavan-3-ols"]
    },

    # ----------------- ICE CREAM VARIETY -----------------
    {
        "name": "Vanilla Ice Cream",
        "category": "Sweets & Desserts",
        "description": "Classic frozen dairy dessert infused with cured Madagascar bourbon vanilla beans and egg yolk custard.",
        "image_url": "https://images.unsplash.com/photo-1570197788417-0e82375c9371?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": ["Dairy", "Eggs"],
        "cuisines": ["Global", "French", "American"],
        "sweet": 7.5, "salty": 0.8, "sour": 0.2, "bitter": 0.0, "umami": 1.0, "spicy": 0.0, "intensity": 6.2,
        "primary_aromas": ["Vanilla", "Sweet Cream", "Custard"],
        "texture_profile": ["Frozen", "Velvety", "Melting"],
        "dominant_compounds": ["Vanillin", "Diacetyl", "Delta-Decalactone", "Ethyl Vanillin"]
    },
    {
        "name": "Chocolate Ice Cream",
        "category": "Sweets & Desserts",
        "description": "Rich frozen custard blending heavy dairy cream with melted dark chocolate and Dutch cocoa.",
        "image_url": "https://images.unsplash.com/photo-1563805042-7684c019e1cb?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": ["Dairy"],
        "cuisines": ["Global", "American", "Italian"],
        "sweet": 6.8, "salty": 0.7, "sour": 0.3, "bitter": 3.5, "umami": 1.8, "spicy": 0.0, "intensity": 7.0,
        "primary_aromas": ["Cocoa", "Sweet Dairy", "Caramel"],
        "texture_profile": ["Frozen", "Creamy", "Dense"],
        "dominant_compounds": ["Theobromine", "Pyrazines", "Vanillin", "Lactones"]
    },
    {
        "name": "Strawberry Ice Cream",
        "category": "Sweets & Desserts",
        "description": "Sweet berry churned cream infused with macerated summer strawberry puree.",
        "image_url": "https://images.unsplash.com/photo-1587314168485-3236d6710814?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": ["Dairy"],
        "cuisines": ["Global", "American"],
        "sweet": 7.2, "salty": 0.5, "sour": 2.8, "bitter": 0.0, "umami": 0.5, "spicy": 0.0, "intensity": 6.5,
        "primary_aromas": ["Fruity", "Berry", "Creamy"],
        "texture_profile": ["Frozen", "Smooth", "Fruity"],
        "dominant_compounds": ["Furaneol", "Ethyl Butyrate", "Methyl Cinnamate", "Delta-Decalactone"]
    },
    {
        "name": "Matcha Ice Cream",
        "category": "Sweets & Desserts",
        "description": "Japanese ceremonial green tea gelato with nuanced grassy astringency and sweet cream balance.",
        "image_url": "https://images.unsplash.com/photo-1505394033641-40c6ad1178d7?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": ["Dairy"],
        "cuisines": ["Japanese", "East Asian"],
        "sweet": 5.5, "salty": 0.4, "sour": 0.8, "bitter": 4.5, "umami": 3.0, "spicy": 0.0, "intensity": 7.2,
        "primary_aromas": ["Grassy", "Earthy", "Herbaceous", "Sweet Dairy"],
        "texture_profile": ["Silky", "Frozen", "Smooth"],
        "dominant_compounds": ["L-Theanine", "Epigallocatechin Gallate (EGCG)", "Hexenal", "Dimethyl Sulfide"]
    },
    {
        "name": "Pistachio Gelato",
        "category": "Sweets & Desserts",
        "description": "Sicilian-style slow-churned gelato made from roasted Bronte pistachio paste.",
        "image_url": "https://images.unsplash.com/photo-1560008581-09826d1de69e?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": ["Dairy", "Tree Nuts"],
        "cuisines": ["Italian", "Mediterranean"],
        "sweet": 6.2, "salty": 1.2, "sour": 0.2, "bitter": 1.5, "umami": 2.2, "spicy": 0.0, "intensity": 7.5,
        "primary_aromas": ["Nutty", "Floral", "Sweet Cream"],
        "texture_profile": ["Dense", "Velvety", "Elastic"],
        "dominant_compounds": ["Benzaldehyde", "Alpha-Pinene", "Limonene", "Lactones"]
    },

    # ----------------- BAKING NEEDS & EXTRACTS -----------------
    {
        "name": "Pure Vanilla Extract",
        "category": "Pantry",
        "description": "Concentrated pure extract derived from cured Bourbon vanilla beans in ethanol solution.",
        "image_url": "https://images.unsplash.com/photo-1608686207856-001b95cf60ca?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tsp",
        "allergens": [],
        "cuisines": ["Global", "French", "American"],
        "sweet": 5.0, "salty": 0.0, "sour": 0.8, "bitter": 2.0, "umami": 0.0, "spicy": 0.0, "intensity": 8.8,
        "primary_aromas": ["Vanilla", "Woody", "Sweet"],
        "texture_profile": ["Liquid"],
        "dominant_compounds": ["Vanillin", "4-Hydroxybenzaldehyde", "Guaiacol", "Anisyl Alcohol"]
    },
    {
        "name": "All-Purpose Flour",
        "category": "Pantry",
        "description": "Milled wheat flour containing medium gluten content (10-12%), essential for breads, sauces, and baking.",
        "image_url": "https://images.unsplash.com/photo-1627485937980-221c88ac04f9?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": ["Gluten"],
        "cuisines": ["Global"],
        "sweet": 1.5, "salty": 0.1, "sour": 0.2, "bitter": 0.5, "umami": 1.0, "spicy": 0.0, "intensity": 2.5,
        "primary_aromas": ["Grainy", "Earthy", "Neutral"],
        "texture_profile": ["Powdery", "Starchy"],
        "dominant_compounds": ["Amylose", "Amylopectin", "Glutenin", "Gliadin"]
    },
    {
        "name": "Brown Sugar",
        "category": "Pantry",
        "description": "Refined sucrose crystals blended with natural cane molasses for deep caramel-toffee complexity.",
        "image_url": "https://images.unsplash.com/photo-1607672632458-9fe566786c7f?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Global", "American", "British"],
        "sweet": 9.2, "salty": 0.6, "sour": 0.4, "bitter": 1.0, "umami": 0.8, "spicy": 0.0, "intensity": 7.5,
        "primary_aromas": ["Molasses", "Caramel", "Toffee"],
        "texture_profile": ["Granular", "Moist"],
        "dominant_compounds": ["Maltol", "Furans", "Sotolon", "Cyclotene"]
    },
    {
        "name": "Baking Powder",
        "category": "Pantry",
        "description": "Double-acting chemical leavening agent releasing carbon dioxide gas under moisture and oven heat.",
        "image_url": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tsp",
        "allergens": [],
        "cuisines": ["Global"],
        "sweet": 0.0, "salty": 5.0, "sour": 2.5, "bitter": 3.0, "umami": 0.0, "spicy": 0.0, "intensity": 4.5,
        "primary_aromas": ["Neutral", "Mineral"],
        "texture_profile": ["Powdery"],
        "dominant_compounds": ["Sodium Bicarbonate", "Monocalcium Phosphate", "Sodium Acid Pyrophosphate"]
    },
    {
        "name": "Active Dry Yeast",
        "category": "Pantry",
        "description": "Dormant Saccharomyces cerevisiae granules that ferment sugars into ethanol and carbon dioxide.",
        "image_url": "https://images.unsplash.com/photo-1549845003-328fc09fad6e?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tsp",
        "allergens": [],
        "cuisines": ["Global", "European"],
        "sweet": 0.2, "salty": 0.2, "sour": 1.5, "bitter": 2.2, "umami": 4.0, "spicy": 0.0, "intensity": 5.5,
        "primary_aromas": ["Yeasty", "Fermented", "Bready"],
        "texture_profile": ["Granular"],
        "dominant_compounds": ["Glutathione", "Ergosterol", "Yeast Esters", "Succinic Acid"]
    },
    {
        "name": "Cornstarch",
        "category": "Pantry",
        "description": "Pure refined carbohydrate starch extracted from maize, used for silky translucent sauces and baking tenderness.",
        "image_url": "https://images.unsplash.com/photo-1627485937980-221c88ac04f9?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tbsp",
        "allergens": [],
        "cuisines": ["Global", "Chinese", "American"],
        "sweet": 0.5, "salty": 0.0, "sour": 0.0, "bitter": 0.0, "umami": 0.2, "spicy": 0.0, "intensity": 1.5,
        "primary_aromas": ["Neutral", "Starchy"],
        "texture_profile": ["Ultra-fine Powder", "Silky Slurry"],
        "dominant_compounds": ["Amylose", "Amylopectin"]
    },

    # ----------------- PIZZA & DOUGH -----------------
    {
        "name": "Pizza Dough",
        "category": "Bakery & Dough",
        "description": "Slow-fermented artisan dough with high-protein 00 wheat flour, active yeast, extra virgin olive oil, and sea salt.",
        "image_url": "https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": ["Gluten"],
        "cuisines": ["Italian", "American"],
        "sweet": 1.8, "salty": 3.5, "sour": 1.8, "bitter": 0.4, "umami": 2.5, "spicy": 0.0, "intensity": 4.5,
        "primary_aromas": ["Fermented Wheat", "Yeasty", "Toasted Hearth"],
        "texture_profile": ["Elastic", "Chewy", "Airy Crumb"],
        "dominant_compounds": ["Ethanol", "Lactic Acid", "Gluten Polymers", "Diacetyl"]
    },
    {
        "name": "Puff Pastry",
        "category": "Bakery & Dough",
        "description": "French laminated dough crafted by repeatedly folding cold European butter between flour sheets for hundreds of flaky layers.",
        "image_url": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=600&q=80",
        "default_unit": "piece",
        "allergens": ["Gluten", "Dairy"],
        "cuisines": ["French", "European"],
        "sweet": 2.0, "salty": 2.2, "sour": 0.2, "bitter": 0.2, "umami": 1.8, "spicy": 0.0, "intensity": 6.0,
        "primary_aromas": ["Rich Butter", "Toasted Pastry", "Golden Flake"],
        "texture_profile": ["Flaky", "Crisp", "Light"],
        "dominant_compounds": ["Diacetyl", "Butyric Acid", "Delta-Lactones", "Maillard Pyrazines"]
    },
    {
        "name": "Sourdough Starter",
        "category": "Bakery & Dough",
        "description": "Wild fermented culture of symbiotic wild yeast and lactic acid bacteria generating distinctive tangy artisan complexity.",
        "image_url": "https://images.unsplash.com/photo-1589367920969-ab8e050bbb04?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": ["Gluten"],
        "cuisines": ["European", "American"],
        "sweet": 1.0, "salty": 0.2, "sour": 6.8, "bitter": 1.2, "umami": 3.0, "spicy": 0.0, "intensity": 7.0,
        "primary_aromas": ["Sour", "Acetic", "Fruity Ferment", "Bready"],
        "texture_profile": ["Spongy", "Bubbling", "Viscous"],
        "dominant_compounds": ["Acetic Acid", "Lactic Acid", "Ethanol", "Isoamyl Alcohol"]
    },
    {
        "name": "Pie Crust",
        "category": "Bakery & Dough",
        "description": "Tender, short artisan pastry enriched with chilled butter or lard for sweet and savory pies.",
        "image_url": "https://images.unsplash.com/photo-1519869325930-281384150729?auto=format&fit=crop&w=600&q=80",
        "default_unit": "piece",
        "allergens": ["Gluten", "Dairy"],
        "cuisines": ["American", "British", "French"],
        "sweet": 1.8, "salty": 2.5, "sour": 0.1, "bitter": 0.1, "umami": 1.2, "spicy": 0.0, "intensity": 5.0,
        "primary_aromas": ["Baked Butter", "Toasted Wheat"],
        "texture_profile": ["Crumbly", "Flaky", "Short"],
        "dominant_compounds": ["Diacetyl", "Lactones", "Furans"]
    },

    # ----------------- STUFFINGS & FILLINGS -----------------
    {
        "name": "Panko Breadcrumbs",
        "category": "Pantry",
        "description": "Japanese crustless-baked bread flakes resulting in an ultra-light, airy, shatteringly crisp fried coating.",
        "image_url": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": ["Gluten"],
        "cuisines": ["Japanese", "Global"],
        "sweet": 1.0, "salty": 1.0, "sour": 0.1, "bitter": 0.2, "umami": 1.2, "spicy": 0.0, "intensity": 2.8,
        "primary_aromas": ["Toasted Bread", "Neutral"],
        "texture_profile": ["Shatteringly Crisp", "Airy"],
        "dominant_compounds": ["Wheat Starch", "Maillard Furans"]
    },
    {
        "name": "Mushroom Duxelles",
        "category": "Produce",
        "description": "Finely minced mushrooms, shallots, garlic, and fresh thyme slow-sautéed in butter into an intense umami paste.",
        "image_url": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": ["Dairy"],
        "cuisines": ["French", "Continental"],
        "sweet": 2.0, "salty": 3.0, "sour": 0.8, "bitter": 1.5, "umami": 8.5, "spicy": 0.2, "intensity": 8.5,
        "primary_aromas": ["Earthy", "Woodland", "Brown Butter", "Herbaceous"],
        "texture_profile": ["Paste", "Rustic Mince"],
        "dominant_compounds": ["1-Octen-3-ol", "Glutamic Acid", "Allicin", "Thymol", "Diacetyl"]
    },
    {
        "name": "Herb Stuffing",
        "category": "Pantry",
        "description": "Seasoned artisanal bread croutons tossed with sage, thyme, celery, onions, and rich stock.",
        "image_url": "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": ["Gluten"],
        "cuisines": ["American", "British"],
        "sweet": 2.2, "salty": 4.5, "sour": 0.5, "bitter": 1.2, "umami": 5.8, "spicy": 0.5, "intensity": 6.8,
        "primary_aromas": ["Sage", "Thyme", "Roasted Onion", "Savoury Broth"],
        "texture_profile": ["Moist", "Tender", "Crisp Edges"],
        "dominant_compounds": ["Thujone", "Thymol", "Allicin", "Glutamic Acid"]
    },

    # ----------------- MEATS & CHARCUTERIE -----------------
    {
        "name": "Beef Tenderloin",
        "category": "Meat & Seafood",
        "description": "The most tender cut of beef, lean and fine-grained, rich in savory heme iron and succulence.",
        "image_url": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["French", "American", "Global"],
        "sweet": 0.8, "salty": 1.5, "sour": 0.8, "bitter": 0.5, "umami": 8.8, "spicy": 0.0, "intensity": 8.5,
        "primary_aromas": ["Meaty", "Heme", "Roasted"],
        "texture_profile": ["Melt-in-mouth Tender", "Succulent"],
        "dominant_compounds": ["Inosine Monophosphate (IMP)", "Myoglobin", "Carnitine", "4-Methyloctanoic Acid"]
    },
    {
        "name": "Ground Beef",
        "category": "Meat & Seafood",
        "description": "Minced 80/20 chuck beef with balanced fat ratio for burgers, ragù bolognese, and savory fillings.",
        "image_url": "https://images.unsplash.com/photo-1588168333986-5078d3ae3976?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Global", "Italian", "American", "Mexican"],
        "sweet": 0.5, "salty": 1.8, "sour": 0.5, "bitter": 0.5, "umami": 8.2, "spicy": 0.0, "intensity": 8.0,
        "primary_aromas": ["Savory Meat", "Rich Lipid", "Caramelized"],
        "texture_profile": ["Juicy", "Ground Mince"],
        "dominant_compounds": ["Glutamic Acid", "Inosine Monophosphate", "Pyrazines", "Oleic Acid"]
    },
    {
        "name": "Pork Belly",
        "category": "Meat & Seafood",
        "description": "Richly marbled cut with alternating layers of succulent pork muscle and silky rendered fat.",
        "image_url": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Chinese", "Korean", "American", "European"],
        "sweet": 1.5, "salty": 1.8, "sour": 0.4, "bitter": 0.2, "umami": 8.5, "spicy": 0.0, "intensity": 8.8,
        "primary_aromas": ["Pork Fat", "Savory Umami", "Caramelized"],
        "texture_profile": ["Crispy Skin", "Tender Melting Fat"],
        "dominant_compounds": ["Oleic Acid", "Linoleic Acid", "Inosinate", "Pyrazines"]
    },
    {
        "name": "Spanish Chorizo",
        "category": "Meat & Seafood",
        "description": "Cured Spanish pork sausage heavily seasoned with smoked Pimentón de la Vera paprika and garlic.",
        "image_url": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Spanish", "Mexican", "Mediterranean"],
        "sweet": 1.8, "salty": 6.8, "sour": 2.2, "bitter": 1.0, "umami": 8.2, "spicy": 5.5, "intensity": 9.2,
        "primary_aromas": ["Smoky Paprika", "Garlic", "Cured Pork"],
        "texture_profile": ["Firm", "Chewy", "Fat-marbled"],
        "dominant_compounds": ["Guaiacol", "Capsanthin", "Allicin", "Glutamate", "Lactic Acid"]
    },
    {
        "name": "Prosciutto di Parma",
        "category": "Meat & Seafood",
        "description": "King of Italian dry-cured hams, aged for 18-24 months with sea salt into translucent, buttery ribbons.",
        "image_url": "https://images.unsplash.com/photo-1529042410759-befb1204b468?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Italian", "European"],
        "sweet": 2.5, "salty": 7.2, "sour": 1.0, "bitter": 0.5, "umami": 9.5, "spicy": 0.0, "intensity": 8.8,
        "primary_aromas": ["Aged Umami", "Cured Sweet Pork", "Saline"],
        "texture_profile": ["Silky", "Melting", "Paper-thin"],
        "dominant_compounds": ["Free Glutamic Acid", "Hexanal", "3-Methylbutanal", "Diacetyl"]
    },
    {
        "name": "Pancetta",
        "category": "Meat & Seafood",
        "description": "Italian salt-cured, pepper-rolled pork belly adding essential unctuous richness to carbonara and ragù.",
        "image_url": "https://images.unsplash.com/photo-1529042410759-befb1204b468?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Italian"],
        "sweet": 1.0, "salty": 6.5, "sour": 0.8, "bitter": 0.5, "umami": 8.5, "spicy": 1.5, "intensity": 8.2,
        "primary_aromas": ["Black Pepper", "Cured Pork", "Saline"],
        "texture_profile": ["Crispy Lardons", "Melting Fat"],
        "dominant_compounds": ["Piperine", "Inosinic Acid", "Oleic Triglycerides", "Hexanal"]
    },
    {
        "name": "Lamb Chops",
        "category": "Meat & Seafood",
        "description": "Tender cutlet with rich gamey nuance, beautifully paired with rosemary, mint, and garlic.",
        "image_url": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=600&q=80",
        "default_unit": "piece",
        "allergens": [],
        "cuisines": ["Mediterranean", "Middle Eastern", "British"],
        "sweet": 0.8, "salty": 1.5, "sour": 0.8, "bitter": 0.5, "umami": 8.8, "spicy": 0.0, "intensity": 8.6,
        "primary_aromas": ["Gamey", "Herbal Pasture", "Rich Savory"],
        "texture_profile": ["Tender", "Juicy", "Searing Bone"],
        "dominant_compounds": ["Branched-chain Fatty Acids", "Carnitine", "Inosinate", "Sulfur Peptides"]
    },
    {
        "name": "Turkey Breast",
        "category": "Meat & Seafood",
        "description": "Lean, high-protein white meat with clean savory poultry flavor and fine grain.",
        "image_url": "https://images.unsplash.com/photo-1588168333986-5078d3ae3976?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["American", "Global"],
        "sweet": 0.5, "salty": 1.2, "sour": 0.4, "bitter": 0.2, "umami": 7.2, "spicy": 0.0, "intensity": 6.0,
        "primary_aromas": ["Clean Poultry", "Light Savory"],
        "texture_profile": ["Lean", "Fine Grain", "Tender"],
        "dominant_compounds": ["Inosine Monophosphate", "Anserine", "Glutamate"]
    },
    {
        "name": "Salami",
        "category": "Meat & Seafood",
        "description": "Fermented and air-dried seasoned pork sausage laced with peppercorns, garlic, and wine.",
        "image_url": "https://images.unsplash.com/photo-1529042410759-befb1204b468?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Italian", "European"],
        "sweet": 1.2, "salty": 7.0, "sour": 3.0, "bitter": 0.8, "umami": 8.8, "spicy": 2.0, "intensity": 8.5,
        "primary_aromas": ["Fermented Lactic", "Peppery", "Garlic"],
        "texture_profile": ["Firm", "Chewy"],
        "dominant_compounds": ["Lactic Acid", "Piperine", "Allicin", "Diacetyl", "Glutamic Acid"]
    },

    # ----------------- CHINESE INGREDIENTS -----------------
    {
        "name": "Shaoxing Wine",
        "category": "Sauces & Condiments",
        "description": "Traditional Chinese fermented glutinous rice wine essential for deglazing woks and braising meats.",
        "image_url": "https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tbsp",
        "allergens": [],
        "cuisines": ["Chinese"],
        "sweet": 3.2, "salty": 2.5, "sour": 2.8, "bitter": 2.0, "umami": 6.5, "spicy": 0.0, "intensity": 7.0,
        "primary_aromas": ["Fermented Rice", "Nutty Sherry", "Earthy"],
        "texture_profile": ["Liquid"],
        "dominant_compounds": ["Ethyl Lactate", "Glutamic Acid", "Benzaldehyde", "Phenylethyl Alcohol"]
    },
    {
        "name": "Oyster Sauce",
        "category": "Sauces & Condiments",
        "description": "Thick, dark savory sauce prepared from caramelized oyster extract reduction with deep umami sweetness.",
        "image_url": "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tbsp",
        "allergens": ["Shellfish"],
        "cuisines": ["Chinese", "Cantonese", "Southeast Asian"],
        "sweet": 5.0, "salty": 7.5, "sour": 0.8, "bitter": 0.5, "umami": 9.5, "spicy": 0.0, "intensity": 9.0,
        "primary_aromas": ["Caramelized Marine", "Glutamate Rich", "Molasses"],
        "texture_profile": ["Thick", "Syrupy", "Velvety"],
        "dominant_compounds": ["Free Glutamic Acid", "Inosinic Acid", "Caramel Pyrazines", "Taurine"]
    },
    {
        "name": "Hoisin Sauce",
        "category": "Sauces & Condiments",
        "description": "Fragrant Chinese glaze combining fermented soybean paste, star anise, garlic, red chili, and sweet sugar.",
        "image_url": "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tbsp",
        "allergens": ["Soy"],
        "cuisines": ["Chinese", "Vietnamese"],
        "sweet": 7.2, "salty": 6.0, "sour": 1.5, "bitter": 0.8, "umami": 7.5, "spicy": 1.5, "intensity": 8.5,
        "primary_aromas": ["Star Anise", "Fermented Soy", "Sweet Molasses"],
        "texture_profile": ["Glossy", "Thick"],
        "dominant_compounds": ["Anethole", "Glutamic Acid", "Allicin", "Capsaicin"]
    },
    {
        "name": "Szechuan Peppercorns",
        "category": "Spices & Seasoning",
        "description": "Citrusy pink husks of prickly ash producing an unmistakable electrifying tingling numbness (mala).",
        "image_url": "https://images.unsplash.com/photo-1596040033229-a9821ebd058d?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tsp",
        "allergens": [],
        "cuisines": ["Chinese", "Sichuan"],
        "sweet": 1.0, "salty": 0.0, "sour": 2.5, "bitter": 3.0, "umami": 1.0, "spicy": 7.0, "intensity": 9.5,
        "primary_aromas": ["Citrus Pine", "Woody", "Tingling Paresthesia"],
        "texture_profile": ["Husk", "Numbing Buzz"],
        "dominant_compounds": ["Hydroxy-alpha-sanshool", "Myrcene", "Limonene", "Linalool"]
    },
    {
        "name": "Five Spice Powder",
        "category": "Spices & Seasoning",
        "description": "Iconic Chinese spice blend uniting star anise, clove, Chinese cinnamon, fennel seed, and Szechuan pepper.",
        "image_url": "https://images.unsplash.com/photo-1596040033229-a9821ebd058d?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tsp",
        "allergens": [],
        "cuisines": ["Chinese", "Taiwanese", "Vietnamese"],
        "sweet": 4.5, "salty": 0.0, "sour": 1.0, "bitter": 3.0, "umami": 2.0, "spicy": 5.0, "intensity": 9.0,
        "primary_aromas": ["Star Anise", "Warm Clove", "Sweet Cinnamon"],
        "texture_profile": ["Fine Powder"],
        "dominant_compounds": ["Anethole", "Cinnamaldehyde", "Eugenol", "Estragole", "Sanshool"]
    },
    {
        "name": "Bok Choy",
        "category": "Produce",
        "description": "Tender Chinese cabbage with crisp white juicy stalks and tender deep-green nutrient-dense leaves.",
        "image_url": "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=600&q=80",
        "default_unit": "piece",
        "allergens": [],
        "cuisines": ["Chinese", "East Asian"],
        "sweet": 2.5, "salty": 0.5, "sour": 0.5, "bitter": 1.8, "umami": 2.2, "spicy": 0.5, "intensity": 4.0,
        "primary_aromas": ["Fresh Green", "Mustardy Glucosinolate"],
        "texture_profile": ["Crisp Stalk", "Tender Leaf"],
        "dominant_compounds": ["Glucobrassicin", "Hexenal", "Dimethyl Sulfide"]
    },
    {
        "name": "Shiitake Mushrooms",
        "category": "Produce",
        "description": "Savory East Asian mushrooms packed with high concentrations of natural ribonucleotides and earthy lenthionine.",
        "image_url": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Chinese", "Japanese", "East Asian"],
        "sweet": 1.5, "salty": 0.8, "sour": 0.8, "bitter": 1.2, "umami": 9.2, "spicy": 0.0, "intensity": 8.5,
        "primary_aromas": ["Deep Forest Umami", "Earthy", "Sulfury Smoke"],
        "texture_profile": ["Velvety", "Meaty", "Chewy Cap"],
        "dominant_compounds": ["Lenthionine", "Guanosine Monophosphate (GMP)", "Glutamic Acid", "1-Octen-3-ol"]
    },
    {
        "name": "Dark Soy Sauce",
        "category": "Sauces & Condiments",
        "description": "Aged, thick Chinese soy sauce brewed with molasses for deep mahogany color and rounded caramelized richness.",
        "image_url": "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tbsp",
        "allergens": ["Soy", "Gluten"],
        "cuisines": ["Chinese", "East Asian"],
        "sweet": 4.5, "salty": 7.5, "sour": 1.5, "bitter": 1.0, "umami": 9.2, "spicy": 0.0, "intensity": 9.0,
        "primary_aromas": ["Molasses Caramel", "Fermented Umami", "Toasted Yeast"],
        "texture_profile": ["Viscous Liquid"],
        "dominant_compounds": ["Glutamic Acid", "4-Hydroxy-2,5-dimethyl-3(2H)-furanone", "Caramel Pyrazines"]
    },
    {
        "name": "Sesame Oil",
        "category": "Sauces & Condiments",
        "description": "Aromatic amber oil pressed from toasted sesame seeds, delivering instant nutty roasted fragrance.",
        "image_url": "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tsp",
        "allergens": ["Sesame"],
        "cuisines": ["Chinese", "Korean", "Japanese", "East Asian"],
        "sweet": 1.0, "salty": 0.0, "sour": 0.0, "bitter": 0.5, "umami": 3.0, "spicy": 0.0, "intensity": 8.5,
        "primary_aromas": ["Toasted Nutty", "Roasted Sesame", "Rich Warm"],
        "texture_profile": ["Silky Oil"],
        "dominant_compounds": ["Sesamol", "Sesamolin", "2-Acetylpyrazine", "2-Ethyl-3-methylpyrazine"]
    },

    # ----------------- ITALIAN SPECIALTIES -----------------
    {
        "name": "San Marzano Tomatoes",
        "category": "Produce",
        "description": "Volcanic soil Campania plum tomatoes known worldwide for low acidity, high natural sweetness, and thick flesh.",
        "image_url": "https://images.unsplash.com/photo-1592924357228-91a4daadcfea?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Italian"],
        "sweet": 5.8, "salty": 0.4, "sour": 4.0, "bitter": 0.2, "umami": 8.8, "spicy": 0.0, "intensity": 7.5,
        "primary_aromas": ["Sun-ripened Tomato", "Sweet Herb", "Earthy Mineral"],
        "texture_profile": ["Meaty", "Dense Pulp"],
        "dominant_compounds": ["Glutamic Acid", "Lycopene", "Beta-Damascenone", "Citric Acid"]
    },
    {
        "name": "Pecorino Romano",
        "category": "Dairy",
        "description": "Ancient hard sheep's milk cheese from Lazio, aged to sharp, salty, piquant crystalline perfection.",
        "image_url": "https://images.unsplash.com/photo-1452195100486-9cc805987862?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": ["Dairy"],
        "cuisines": ["Italian", "Roman"],
        "sweet": 0.5, "salty": 8.5, "sour": 2.5, "bitter": 1.2, "umami": 9.2, "spicy": 2.5, "intensity": 9.2,
        "primary_aromas": ["Sharp Sheep Milk", "Saline Piquant", "Aged Butyric"],
        "texture_profile": ["Hard Granular", "Crystalline"],
        "dominant_compounds": ["Caproic Acid", "Caprylic Acid", "Butyric Acid", "Free Amino Acids"]
    },
    {
        "name": "Mascarpone",
        "category": "Dairy",
        "description": "Decadent triple-cream Italian cheese with 60-75% butterfat, creating velvety tiramisu and silky sauces.",
        "image_url": "https://images.unsplash.com/photo-1559561853-08451507cbe7?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": ["Dairy"],
        "cuisines": ["Italian", "French"],
        "sweet": 4.5, "salty": 0.8, "sour": 1.2, "bitter": 0.0, "umami": 2.2, "spicy": 0.0, "intensity": 6.8,
        "primary_aromas": ["Sweet Cream", "Milky", "Fresh Butter"],
        "texture_profile": ["Velvety", "Dense Spreadable", "Silky"],
        "dominant_compounds": ["Diacetyl", "Delta-Decalactone", "Milk Fat Globules"]
    },
    {
        "name": "Ricotta Cheese",
        "category": "Dairy",
        "description": "Mild, naturally sweet Italian whey curd cheese essential for cannoli, lasagna, and ravioli fillings.",
        "image_url": "https://images.unsplash.com/photo-1559561853-08451507cbe7?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": ["Dairy"],
        "cuisines": ["Italian"],
        "sweet": 3.8, "salty": 1.2, "sour": 1.5, "bitter": 0.0, "umami": 2.5, "spicy": 0.0, "intensity": 4.5,
        "primary_aromas": ["Fresh Milk", "Sweet Curd"],
        "texture_profile": ["Granular", "Soft", "Creamy"],
        "dominant_compounds": ["Lactic Acid", "Diacetyl", "Whey Protein"]
    },
    {
        "name": "Arborio Rice",
        "category": "Grains & Pasta",
        "description": "Short-grain Italian rice with high amylopectin content that releases starch during cooking into a creamy risotto.",
        "image_url": "https://images.unsplash.com/photo-1586201375761-83865001e31c?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Italian"],
        "sweet": 1.5, "salty": 0.1, "sour": 0.1, "bitter": 0.1, "umami": 1.5, "spicy": 0.0, "intensity": 2.5,
        "primary_aromas": ["Clean Starch", "Grain"],
        "texture_profile": ["Plump Pearl", "Creamy Coating", "Al Dente Core"],
        "dominant_compounds": ["Amylopectin", "Amylose"]
    },
    {
        "name": "Polenta",
        "category": "Grains & Pasta",
        "description": "Northern Italian coarse-ground yellow flint corn cooked into a warm golden porridge or pan-seared cakes.",
        "image_url": "https://images.unsplash.com/photo-1586201375761-83865001e31c?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Italian"],
        "sweet": 3.0, "salty": 0.2, "sour": 0.2, "bitter": 0.5, "umami": 1.8, "spicy": 0.0, "intensity": 4.2,
        "primary_aromas": ["Sweet Corn", "Toasted Grain"],
        "texture_profile": ["Creamy Grain", "Coarse Grit"],
        "dominant_compounds": ["Zeaxanthin", "Pyrazines", "Corn Starch"]
    },
    {
        "name": "Pine Nuts",
        "category": "Pantry",
        "description": "Delicate Mediterranean stone pine seeds rich in pinolenic acid, forming the backbone of classic Pesto Genovese.",
        "image_url": "https://images.unsplash.com/photo-1509358271058-acd22cc93898?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": ["Tree Nuts"],
        "cuisines": ["Italian", "Mediterranean", "Middle Eastern"],
        "sweet": 3.2, "salty": 0.2, "sour": 0.2, "bitter": 0.8, "umami": 3.5, "spicy": 0.0, "intensity": 6.0,
        "primary_aromas": ["Resinous Pine", "Sweet Nutty", "Toasted Butter"],
        "texture_profile": ["Soft Tender Nut", "Buttery"],
        "dominant_compounds": ["Pinolenic Acid", "Alpha-Pinene", "Terpenes", "Pyrazines"]
    },
    {
        "name": "Dried Oregano",
        "category": "Spices & Seasoning",
        "description": "Mediterranean aromatic herb whose drying process intensifies savory thymol and carvacrol pizza notes.",
        "image_url": "https://images.unsplash.com/photo-1596040033229-a9821ebd058d?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tsp",
        "allergens": [],
        "cuisines": ["Italian", "Greek", "Mexican"],
        "sweet": 1.2, "salty": 0.0, "sour": 0.8, "bitter": 4.5, "umami": 1.5, "spicy": 3.0, "intensity": 8.0,
        "primary_aromas": ["Pungent Herbal", "Woody", "Peppery"],
        "texture_profile": ["Flaked Leaves"],
        "dominant_compounds": ["Carvacrol", "Thymol", "P-Cymene", "Gamma-Terpinene"]
    },

    # ----------------- SPANISH SPECIALTIES -----------------
    {
        "name": "Spanish Saffron",
        "category": "Spices & Seasoning",
        "description": "Crimson stigmas of Crocus sativus from La Mancha, prized for its golden crocin color and warm safranal fragrance.",
        "image_url": "https://images.unsplash.com/photo-1596040033229-a9821ebd058d?auto=format&fit=crop&w=600&q=80",
        "default_unit": "pinch",
        "allergens": [],
        "cuisines": ["Spanish", "Persian", "Indian"],
        "sweet": 2.0, "salty": 0.0, "sour": 0.5, "bitter": 5.0, "umami": 1.5, "spicy": 0.5, "intensity": 9.5,
        "primary_aromas": ["Warm Honey-Hay", "Metallic Iodine", "Floral Scent"],
        "texture_profile": ["Delicate Threads"],
        "dominant_compounds": ["Safranal", "Crocin", "Picrocrocin"]
    },
    {
        "name": "Smoked Paprika",
        "category": "Spices & Seasoning",
        "description": "Pimentón de la Vera slowly oak-smoked over holm oak fires for deep Spanish paella, chorizo, and tapas dishes.",
        "image_url": "https://images.unsplash.com/photo-1596040033229-a9821ebd058d?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tsp",
        "allergens": [],
        "cuisines": ["Spanish", "Hungarian"],
        "sweet": 3.0, "salty": 0.2, "sour": 1.0, "bitter": 2.0, "umami": 2.5, "spicy": 3.5, "intensity": 8.8,
        "primary_aromas": ["Oak Woodsmoke", "Earthy Sweet Pepper"],
        "texture_profile": ["Fine Scarlet Powder"],
        "dominant_compounds": ["Guaiacol", "Syringol", "Capsanthin", "Pyrazines"]
    },
    {
        "name": "Manchego Cheese",
        "category": "Dairy",
        "description": "Protected DO sheep's milk cheese from La Mancha with characteristic herringbone rind and nutty piquant finish.",
        "image_url": "https://images.unsplash.com/photo-1452195100486-9cc805987862?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": ["Dairy"],
        "cuisines": ["Spanish"],
        "sweet": 1.8, "salty": 6.8, "sour": 2.0, "bitter": 0.8, "umami": 8.5, "spicy": 0.5, "intensity": 8.2,
        "primary_aromas": ["Sheep Milk", "Toasted Pecan", "Butyric Saline"],
        "texture_profile": ["Firm", "Flaky Crystalline"],
        "dominant_compounds": ["Caproic Acid", "Butyric Acid", "Free Glutamate", "Ketones"]
    },
    {
        "name": "Bomba Paella Rice",
        "category": "Grains & Pasta",
        "description": "Short-grain round Spanish rice capable of absorbing 3 times its volume in seafood stock without bursting.",
        "image_url": "https://images.unsplash.com/photo-1586201375761-83865001e31c?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Spanish"],
        "sweet": 1.2, "salty": 0.1, "sour": 0.1, "bitter": 0.1, "umami": 1.2, "spicy": 0.0, "intensity": 2.5,
        "primary_aromas": ["Neutral Grain", "Starch"],
        "texture_profile": ["Plump Pearl", "Firm Non-sticky", "Socarrat Crisp"],
        "dominant_compounds": ["Amylose", "Amylopectin"]
    },
    {
        "name": "Sherry Vinegar",
        "category": "Sauces & Condiments",
        "description": "Aged solera Spanish wine vinegar from Jerez with rich oak barrel woodiness and assertive acidity.",
        "image_url": "https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tbsp",
        "allergens": [],
        "cuisines": ["Spanish"],
        "sweet": 2.5, "salty": 0.4, "sour": 8.8, "bitter": 0.5, "umami": 2.0, "spicy": 0.0, "intensity": 8.5,
        "primary_aromas": ["Oak Wood", "Nutty Acetic", "Dried Fruit"],
        "texture_profile": ["Liquid"],
        "dominant_compounds": ["Acetic Acid", "Whisky Lactones", "Ethyl Acetate"]
    },

    # ----------------- NOODLES & PASTA -----------------
    {
        "name": "Spaghetti",
        "category": "Grains & Pasta",
        "description": "Classic cylindrical strand pasta extruded from 100% durum wheat semolina for al dente elasticity.",
        "image_url": "https://images.unsplash.com/photo-1551183053-bf91a1d81141?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": ["Gluten"],
        "cuisines": ["Italian", "Global"],
        "sweet": 1.2, "salty": 0.2, "sour": 0.1, "bitter": 0.2, "umami": 1.2, "spicy": 0.0, "intensity": 3.0,
        "primary_aromas": ["Semolina Wheat", "Toasted Grain"],
        "texture_profile": ["Al Dente Firm", "Smooth Strand"],
        "dominant_compounds": ["Durum Wheat Gluten", "Amylose Starch"]
    },
    {
        "name": "Fettuccine",
        "category": "Grains & Pasta",
        "description": "Flat, thick ribbon pasta crafted with fresh eggs, famous for clinging to rich cream and ragù sauces.",
        "image_url": "https://images.unsplash.com/photo-1551183053-bf91a1d81141?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": ["Gluten", "Eggs"],
        "cuisines": ["Italian", "Roman"],
        "sweet": 1.5, "salty": 0.3, "sour": 0.1, "bitter": 0.2, "umami": 2.0, "spicy": 0.0, "intensity": 3.5,
        "primary_aromas": ["Egg Yolk", "Durum Wheat"],
        "texture_profile": ["Broad Ribbon", "Tender Elastic"],
        "dominant_compounds": ["Lutein", "Wheat Glutenin", "Ovalbumin"]
    },
    {
        "name": "Penne Rigate",
        "category": "Grains & Pasta",
        "description": "Tubular extruded pasta with diagonal cuts and ridges designed to trap chunky sauces and pestos inside.",
        "image_url": "https://images.unsplash.com/photo-1551183053-bf91a1d81141?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": ["Gluten"],
        "cuisines": ["Italian"],
        "sweet": 1.2, "salty": 0.2, "sour": 0.1, "bitter": 0.2, "umami": 1.2, "spicy": 0.0, "intensity": 3.0,
        "primary_aromas": ["Semolina Wheat"],
        "texture_profile": ["Ridged Tube", "Chewy Al Dente"],
        "dominant_compounds": ["Durum Gluten", "Wheat Starch"]
    },
    {
        "name": "Ramen Noodles",
        "category": "Grains & Pasta",
        "description": "Japanese alkaline wheat noodles made with kansui mineral water for distinct yellow hue, springy chew, and broth resilience.",
        "image_url": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": ["Gluten"],
        "cuisines": ["Japanese"],
        "sweet": 1.0, "salty": 1.2, "sour": 0.2, "bitter": 0.5, "umami": 2.0, "spicy": 0.0, "intensity": 4.5,
        "primary_aromas": ["Alkaline Kansui", "Wheat Grain"],
        "texture_profile": ["Springy", "Chewy Bouncy"],
        "dominant_compounds": ["Potassium Carbonate", "Sodium Carbonate", "Gluten Network"]
    },
    {
        "name": "Udon Noodles",
        "category": "Grains & Pasta",
        "description": "Thick, soft Japanese wheat noodles prized for their soothing pillowy bounce in hot dashi broth.",
        "image_url": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": ["Gluten"],
        "cuisines": ["Japanese"],
        "sweet": 1.0, "salty": 0.8, "sour": 0.1, "bitter": 0.1, "umami": 1.2, "spicy": 0.0, "intensity": 3.0,
        "primary_aromas": ["Clean Wheat", "Starch"],
        "texture_profile": ["Thick Cylindrical", "Pillowy Chewy"],
        "dominant_compounds": ["Wheat Starch", "Gluten Matrix"]
    },
    {
        "name": "Rice Vermicelli",
        "category": "Grains & Pasta",
        "description": "Thin, delicate Asian rice noodles that cook in boiling water in 2 minutes for spring rolls and stir-fries.",
        "image_url": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Vietnamese", "Chinese", "Thai"],
        "sweet": 0.8, "salty": 0.1, "sour": 0.1, "bitter": 0.0, "umami": 0.8, "spicy": 0.0, "intensity": 2.0,
        "primary_aromas": ["Clean Rice"],
        "texture_profile": ["Delicate", "Translucent Slender"],
        "dominant_compounds": ["Rice Amylose"]
    },
    {
        "name": "Potato Gnocchi",
        "category": "Grains & Pasta",
        "description": "Tender Italian dumplings made of riced russet potatoes, egg, and flour, shaped with fork ridges to capture sauce.",
        "image_url": "https://images.unsplash.com/photo-1551183053-bf91a1d81141?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": ["Gluten", "Eggs"],
        "cuisines": ["Italian"],
        "sweet": 1.5, "salty": 1.5, "sour": 0.2, "bitter": 0.1, "umami": 2.2, "spicy": 0.0, "intensity": 4.0,
        "primary_aromas": ["Cooked Potato", "Toasted Butter"],
        "texture_profile": ["Pillowy Soft", "Tender Dumpling"],
        "dominant_compounds": ["Potato Amylopectin", "Wheat Protein"]
    },

    # ----------------- SAUCE VARIETY -----------------
    {
        "name": "Pesto Genovese",
        "category": "Sauces & Condiments",
        "description": "Ligurian emulsion of sweet Genovese basil leaves, toasted pine nuts, garlic, extra virgin olive oil, and aged Parmigiano.",
        "image_url": "https://images.unsplash.com/photo-1596797038530-2c107229654b?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tbsp",
        "allergens": ["Dairy", "Tree Nuts"],
        "cuisines": ["Italian"],
        "sweet": 1.5, "salty": 5.5, "sour": 1.0, "bitter": 1.8, "umami": 7.5, "spicy": 1.0, "intensity": 8.8,
        "primary_aromas": ["Fresh Basil Eugenol", "Garlic Allicin", "Aged Cheese"],
        "texture_profile": ["Coarse Emulsion", "Glossy Oil Herb Paste"],
        "dominant_compounds": ["Eugenol", "Linalool", "Allicin", "Pinolenic Acid", "Glutamate"]
    },
    {
        "name": "Marinara Sauce",
        "category": "Sauces & Condiments",
        "description": "Slow-simmered Southern Italian sauce of San Marzano plum tomatoes, garlic, extra virgin olive oil, and torn basil.",
        "image_url": "https://images.unsplash.com/photo-1572441713132-c542fc4fe282?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": [],
        "cuisines": ["Italian", "American-Italian"],
        "sweet": 4.5, "salty": 4.2, "sour": 4.2, "bitter": 0.5, "umami": 7.8, "spicy": 0.2, "intensity": 7.0,
        "primary_aromas": ["Simmered Tomato", "Garlic Confit", "Sweet Basil"],
        "texture_profile": ["Chunky Smooth", "Glossy Sauce"],
        "dominant_compounds": ["Glutamic Acid", "Lycopene", "Allicin", "Eugenol", "Citric Acid"]
    },
    {
        "name": "Bechamel Sauce",
        "category": "Sauces & Condiments",
        "description": "One of French culinary mother sauces, combining white butter-flour roux and whole milk scented with nutmeg.",
        "image_url": "https://images.unsplash.com/photo-1559561853-08451507cbe7?auto=format&fit=crop&w=600&q=80",
        "default_unit": "g",
        "allergens": ["Dairy", "Gluten"],
        "cuisines": ["French", "Italian", "Greek"],
        "sweet": 3.0, "salty": 3.2, "sour": 0.2, "bitter": 0.2, "umami": 3.0, "spicy": 0.5, "intensity": 6.0,
        "primary_aromas": ["Warm Nutmeg", "Sweet Dairy Butter", "Cooked Roux"],
        "texture_profile": ["Velvety", "Coat-the-spoon Cream"],
        "dominant_compounds": ["Myristicin", "Diacetyl", "Delta-Decalactone", "Lactic Acid"]
    },
    {
        "name": "Hollandaise Sauce",
        "category": "Sauces & Condiments",
        "description": "Rich French warm emulsion of egg yolks, melted clarified butter, and fresh lemon juice.",
        "image_url": "https://images.unsplash.com/photo-1525351484163-7529414344d8?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tbsp",
        "allergens": ["Dairy", "Eggs"],
        "cuisines": ["French"],
        "sweet": 1.0, "salty": 3.0, "sour": 5.2, "bitter": 0.2, "umami": 3.5, "spicy": 0.5, "intensity": 7.8,
        "primary_aromas": ["Clarified Butter", "Bright Lemon", "Warm Egg"],
        "texture_profile": ["Airy Emulsion", "Velvety Gloss"],
        "dominant_compounds": ["Citric Acid", "Limonene", "Lecithin", "Diacetyl", "Butyric Acid"]
    },
    {
        "name": "Sriracha Sauce",
        "category": "Sauces & Condiments",
        "description": "Fermented red jalapeño chili sauce with garlic, vinegar, and sweet cane sugar for immediate bright kick.",
        "image_url": "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tbsp",
        "allergens": [],
        "cuisines": ["Thai", "Vietnamese", "American"],
        "sweet": 4.5, "salty": 5.5, "sour": 4.8, "bitter": 0.5, "umami": 4.0, "spicy": 7.8, "intensity": 8.8,
        "primary_aromas": ["Fermented Red Chili", "Garlic", "Tangy Vinegar"],
        "texture_profile": ["Smooth Condiment Paste"],
        "dominant_compounds": ["Capsaicin", "Allicin", "Acetic Acid", "Lactic Acid"]
    },
    {
        "name": "Chimichurri",
        "category": "Sauces & Condiments",
        "description": "Argentine vibrant green steak sauce combining finely chopped flat parsley, oregano, garlic, red wine vinegar, and olive oil.",
        "image_url": "https://images.unsplash.com/photo-1596797038530-2c107229654b?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tbsp",
        "allergens": [],
        "cuisines": ["Argentine", "South American"],
        "sweet": 0.5, "salty": 4.2, "sour": 6.5, "bitter": 2.2, "umami": 2.5, "spicy": 3.0, "intensity": 8.5,
        "primary_aromas": ["Fresh Parsley Apiol", "Tangy Vinegar", "Raw Garlic"],
        "texture_profile": ["Coarse Vinaigrette", "Oil Infused"],
        "dominant_compounds": ["Apiol", "Carvacrol", "Allicin", "Acetic Acid", "Oleic Acid"]
    },
    {
        "name": "Teriyaki Sauce",
        "category": "Sauces & Condiments",
        "description": "Japanese glaze of brewed soy sauce, mirin sweet rice wine, sake, fresh ginger, and brown sugar reduction.",
        "image_url": "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tbsp",
        "allergens": ["Soy", "Gluten"],
        "cuisines": ["Japanese"],
        "sweet": 7.5, "salty": 6.8, "sour": 1.0, "bitter": 0.5, "umami": 8.5, "spicy": 1.0, "intensity": 8.5,
        "primary_aromas": ["Caramelized Mirin", "Fermented Soy", "Warm Gingerol"],
        "texture_profile": ["Glossy Glaze", "Syrupy"],
        "dominant_compounds": ["Glutamic Acid", "Gingerol", "Maltol", "Ethanol"]
    },
    {
        "name": "Tahini",
        "category": "Sauces & Condiments",
        "description": "Velvety Middle Eastern paste made from 100% stone-ground hulled sesame seeds.",
        "image_url": "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tbsp",
        "allergens": ["Sesame"],
        "cuisines": ["Middle Eastern", "Mediterranean"],
        "sweet": 1.2, "salty": 0.8, "sour": 0.5, "bitter": 3.8, "umami": 4.5, "spicy": 0.0, "intensity": 7.5,
        "primary_aromas": ["Roasted Sesame", "Earthy Nutty"],
        "texture_profile": ["Thick Creamy Paste"],
        "dominant_compounds": ["Sesamin", "Sesamolin", "Pyrazines", "Oleic Acid"]
    },
    {
        "name": "Gochujang",
        "category": "Sauces & Condiments",
        "description": "Fundamental Korean fermented condiment paste of sun-dried red chili peppers, glutinous rice, fermented soybeans, and salt.",
        "image_url": "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tbsp",
        "allergens": ["Soy"],
        "cuisines": ["Korean"],
        "sweet": 6.0, "salty": 6.8, "sour": 1.8, "bitter": 1.2, "umami": 8.8, "spicy": 7.5, "intensity": 9.2,
        "primary_aromas": ["Fermented Chili", "Sweet Rice Malt", "Deep Savory"],
        "texture_profile": ["Dense Sticky Paste"],
        "dominant_compounds": ["Capsaicin", "Glutamic Acid", "Meju Peptides", "Maltose"]
    },
    {
        "name": "BBQ Sauce",
        "category": "Sauces & Condiments",
        "description": "Sweet, smoky American barbecue sauce with tomato paste, brown sugar molasses, hickory woodsmoke, cider vinegar, and spices.",
        "image_url": "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?auto=format&fit=crop&w=600&q=80",
        "default_unit": "tbsp",
        "allergens": [],
        "cuisines": ["American", "Southern BBQ"],
        "sweet": 7.5, "salty": 5.5, "sour": 5.0, "bitter": 0.8, "umami": 5.5, "spicy": 3.2, "intensity": 8.8,
        "primary_aromas": ["Hickory Smoke", "Sweet Molasses", "Tangy Tomato"],
        "texture_profile": ["Thick Glossy Sauce"],
        "dominant_compounds": ["Guaiacol", "Syringol", "Acetic Acid", "Lycopene", "Maltol"]
    }
]

def run_seed():
    db = SessionLocal()
    added_count = 0
    updated_count = 0

    print("Seeding comprehensive ingredients into flavorfusion.db...")

    for data in NEW_INGREDIENTS:
        name = data["name"].strip()
        slug = name.lower().replace(" ", "-").replace("'", "").replace("%", "pct")

        existing = db.query(Ingredient).filter(Ingredient.name.ilike(name)).first()
        if existing:
            # Update existing
            existing.category = data["category"]
            existing.description = data["description"]
            existing.image_url = data["image_url"]
            existing.default_unit = data["default_unit"]
            existing.allergens = data["allergens"]
            existing.cuisines = data["cuisines"]

            if existing.flavor_profile:
                fp = existing.flavor_profile
                fp.sweet = data["sweet"]
                fp.salty = data["salty"]
                fp.sour = data["sour"]
                fp.bitter = data["bitter"]
                fp.umami = data["umami"]
                fp.spicy = data["spicy"]
                fp.intensity = data["intensity"]
                fp.primary_aromas = data["primary_aromas"]
                fp.texture_profile = data["texture_profile"]
                fp.dominant_compounds = data["dominant_compounds"]
            else:
                fp = IngredientFlavorProfile(
                    ingredient_id=existing.id,
                    sweet=data["sweet"],
                    salty=data["salty"],
                    sour=data["sour"],
                    bitter=data["bitter"],
                    umami=data["umami"],
                    spicy=data["spicy"],
                    intensity=data["intensity"],
                    primary_aromas=data["primary_aromas"],
                    texture_profile=data["texture_profile"],
                    dominant_compounds=data["dominant_compounds"]
                )
                db.add(fp)
            updated_count += 1
        else:
            ing = Ingredient(
                name=name,
                slug=slug,
                category=data["category"],
                description=data["description"],
                image_url=data["image_url"],
                default_unit=data["default_unit"],
                allergens=data["allergens"],
                cuisines=data["cuisines"],
                is_curated=True
            )
            db.add(ing)
            db.flush()

            fp = IngredientFlavorProfile(
                ingredient_id=ing.id,
                sweet=data["sweet"],
                salty=data["salty"],
                sour=data["sour"],
                bitter=data["bitter"],
                umami=data["umami"],
                spicy=data["spicy"],
                intensity=data["intensity"],
                primary_aromas=data["primary_aromas"],
                texture_profile=data["texture_profile"],
                dominant_compounds=data["dominant_compounds"]
            )
            db.add(fp)
            added_count += 1

    db.commit()
    total_count = db.query(Ingredient).count()
    print(f"Seed complete: {added_count} new ingredients added, {updated_count} updated. Total ingredients in database: {total_count}")
    db.close()

if __name__ == "__main__":
    run_seed()
