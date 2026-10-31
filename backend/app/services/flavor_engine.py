"""
FlavorFusion AI — Explainable Flavor Prediction Engine
Performs multi-ingredient taste profile prediction, aroma distribution,
pairwise interaction analysis, balance scoring, conflict detection,
and personalized preference matching.
"""

from typing import List, Dict, Any, Optional, Tuple
import math
from app.models.entities import Ingredient, IngredientFlavorProfile, IngredientPairingEvidence, UserPreference
from app.schemas.all_schemas import (
    IngredientInput, CombinationAnalyzeResponse, PairwiseInteraction, RatioItem, DishSuggestion
)

EMERGENT_FLAVOR_SYNERGIES = [
    {
        "keys": {"vanilla", "soy sauce"},
        "tastes_like": "Rich Salted Caramel & Toasted Butterscotch 🍮",
        "explanation": "When glutamate-rich, salty fermented soy sauce marries with sweet aromatic vanillin and creamy fats, it produces the exact sensory illusion of deep caramelized sugar and buttery toffee on human tastebuds.",
        "vibe": "🤯 Unhinged Synergy (Literal Magic)",
        "dishes": [
            DishSuggestion(name="Kyoto Salted Caramel Sundae", description="Velvety vanilla ice cream or custard drizzled with reduced sweet-savory soy glaze and toasted sesame.", difficulty="Easy", cook_time_mins=5, vibe_tag="🔥 Viral Flavor Banger", meal_type="Dessert"),
            DishSuggestion(name="Miso-Soy Vanilla Glazed Brioche", description="Warm toasted brioche toast brushed with sweet soy caramel reduction.", difficulty="Easy", cook_time_mins=10, vibe_tag="✨ Chef's Secret", meal_type="Breakfast")
        ]
    },
    {
        "keys": {"green apple", "salt"},
        "tastes_like": "Crisp Juicy Malic Crunch & Explosive Orchard Sweetness 🍏🧂",
        "explanation": "Sodium ions selectively suppress perceived tongue astringency and trigger salivation, transforming sharp malic acid into an intensely sweet, refreshingly crisp orchard burst.",
        "vibe": "🍏 Pure Refreshing Crunch",
        "dishes": [
            DishSuggestion(name="Himalayan Salted Green Apple Carpaccio", description="Paper-thin shaved Granny Smith apple discs sprinkled with flaky sea salt and cracked pink peppercorn.", difficulty="Easy", cook_time_mins=5, vibe_tag="✨ 5-Minute Elegance", meal_type="Appetizer"),
            DishSuggestion(name="Salted Green Apple & Fennel Slaw", description="Julienned tart apple tossed with sea salt, olive oil, and lemon zest.", difficulty="Easy", cook_time_mins=8, vibe_tag="🥗 Crisp & Clean", meal_type="Salad")
        ]
    },
    {
        "keys": {"green apple", "cheddar"},
        "tastes_like": "Sharp Cheddar Orchard Crunch & Toffee Tart 🍏🧀",
        "explanation": "High malic acid in tart green apples cleanses dense dairy lipids, while butyric acid in sharp cheddar elevates perceived apple crispness into a savory-sweet artisan revelation.",
        "vibe": "🍏 Sophisticated Snack Banger",
        "dishes": [
            DishSuggestion(name="Artisan Cheddar & Green Apple Crostini", description="Toasted sourdough layered with melted aged cheddar and thinly shaved Granny Smith apple drizzled with honey.", difficulty="Easy", cook_time_mins=8, vibe_tag="✨ Bistro Classic", meal_type="Snack"),
            DishSuggestion(name="Shaved Apple & Cheddar Bistro Salad", description="Crisp green apple ribbons tossed with sharp cheddar cubes, toasted walnuts, and cider vinaigrette.", difficulty="Easy", cook_time_mins=10, vibe_tag="🥗 Clean Crunch", meal_type="Lunch")
        ]
    },
    {
        "keys": {"salt", "dark chocolate"},
        "tastes_like": "Gourmet Salted Dark Cacao & Fudge Truffle 🍫🧂",
        "explanation": "Sodium ions chemically block tongue bitterness receptors, letting theobromine and rich roasted cacao pyrazines burst into intense perceived chocolate fudge sweetness.",
        "vibe": "🍫 Certified S-Tier",
        "dishes": [
            DishSuggestion(name="Flaky Sea Salt Dark Chocolate Bark", description="Melted 70% dark chocolate sprinkled with Maldon flaky sea salt and toasted almonds.", difficulty="Easy", cook_time_mins=10, vibe_tag="✨ Viral Sweet-Savory", meal_type="Dessert"),
            DishSuggestion(name="Salted Espresso Mocha Truffles", description="Rich dark chocolate ganache infused with espresso and rolled in cocoa with a pinch of sea salt.", difficulty="Easy", cook_time_mins=15, vibe_tag="🌙 Midnight Luxury", meal_type="Dessert")
        ]
    },
    {
        "keys": {"watermelon", "feta cheese", "mint"},
        "tastes_like": "Mediterranean Sea Breeze & Chilled Melon Cloud 🍉",
        "explanation": "Aquatic cucurbitacin in chilled watermelon is magnified by the briny lactic salinity of sheep's milk feta, with cooling menthol vapors bridging the two.",
        "vibe": "🍉 Ultimate Summer Slap",
        "dishes": [
            DishSuggestion(name="Santorini Watermelon Feta Salad", description="Cubed chilled watermelon tossed with crumbled feta, torn fresh mint leaves, and a squeeze of lime.", difficulty="Easy", cook_time_mins=5, vibe_tag="⚡ 5-Minute Lifesaver", meal_type="Salad"),
            DishSuggestion(name="Mint-Melon Feta Skewers", description="Refreshing party skewers drizzled with aged balsamic reduction.", difficulty="Easy", cook_time_mins=8, vibe_tag="✨ Party Stunner", meal_type="Appetizer")
        ]
    },
    {
        "keys": {"salmon", "dill", "lemon"},
        "tastes_like": "Nordic Gravlax & Herb-Seared Marine Perfection 🐟🌿",
        "explanation": "Citric acid dissolves fishy trimethylamine while carvone and limonene monoterpenes slice through rich omega-3 marine lipids.",
        "vibe": "🌊 Michelin Seafood Flex",
        "dishes": [
            DishSuggestion(name="Pan-Seared Crispy Skin Salmon with Lemon-Dill", description="Golden pan-seared salmon finished with garlic-dill butter and charred lemon.", difficulty="Medium", cook_time_mins=15, vibe_tag="🔥 15-Minute Dinner", meal_type="Dinner"),
            DishSuggestion(name="Gravlax Style Salmon Tartare", description="Finely diced fresh salmon dressed with fresh dill, capers, lemon zest, and extra virgin olive oil.", difficulty="Easy", cook_time_mins=10, vibe_tag="✨ Raw Bar Elegance", meal_type="Appetizer")
        ]
    },
    {
        "keys": {"garlic", "butter"},
        "tastes_like": "French Beurre Maître d'Hôtel & Golden Roasted Confit 🧄🧈",
        "explanation": "Diacetyl and butyric dairy lipids encapsulate pungent allicin from garlic, mellowing sharp pungency into a silky, sweet, rich savory confit emulsion.",
        "vibe": "🧈 Pure Comfort & Culinary Fond",
        "dishes": [
            DishSuggestion(name="Garlic Butter Sautéed Skillet", description="Aromatic golden garlic melted into foaming butter for searing crusts or tossing vegetables.", difficulty="Easy", cook_time_mins=8, vibe_tag="✨ Chef's Staple", meal_type="Dinner"),
            DishSuggestion(name="Crispy Garlic Butter Crostini", description="Toasted artisan baguette brushed with slow-confit garlic butter and parsley.", difficulty="Easy", cook_time_mins=10, vibe_tag="🔥 Irresistible Starter", meal_type="Appetizer")
        ]
    },
    {
        "keys": {"mango", "curd", "cardamom"},
        "tastes_like": "Royal Kesariya Shrikhand & Velvet Tropical Mousse 🥭",
        "explanation": "Lactic acid cuts mango fructose richness while cineole and terpinyl acetate in cardamom lift the tropical esters into a decadent royal dessert profile.",
        "vibe": "👑 Royal Heritage Slap",
        "dishes": [
            DishSuggestion(name="Artisan Aamrakhand Parfait", description="Thick hung curd layered with ripe Alphonso purée, crushed green cardamom, and pistachios.", difficulty="Easy", cook_time_mins=15, vibe_tag="✨ 10/10 Comfort Food", meal_type="Dessert"),
            DishSuggestion(name="Mango Lassi Cloud Bowl", description="Whipped yogurt smoothie topped with roasted cumin seeds and fresh mint leaves.", difficulty="Easy", cook_time_mins=8, vibe_tag="⚡ Summer Essential", meal_type="Beverage")
        ]
    },
    {
        "keys": {"tomato", "basil", "garlic"},
        "tastes_like": "Sun-Drenched Neapolitan Pomodoro & Caprese Essence 🍅",
        "explanation": "Free glutamates in ripe tomatoes combine with eugenol/anise notes in sweet basil and allicin in garlic to generate the ultimate savory Italian umami harmony.",
        "vibe": "🤌 Nonna Approved (Absolute Perfection)",
        "dishes": [
            DishSuggestion(name="Rustic Bruschetta al Pomodoro", description="Crusty toasted sourdough rubbed with raw garlic, heaped with marinaded heirloom tomatoes and torn basil.", difficulty="Easy", cook_time_mins=10, vibe_tag="🔥 Dinner Party Stunner", meal_type="Appetizer"),
            DishSuggestion(name="Silky San Marzano Herb Emulsion", description="Slow-simmered tomato passata emulsified with cold-pressed olive oil.", difficulty="Medium", cook_time_mins=25, vibe_tag="✨ Pure Umami", meal_type="Dinner")
        ]
    },
    {
        "keys": {"dark chocolate", "chili pepper"},
        "tastes_like": "Mesoamerican Spiced Aztec Truffle & Warm Cacao 🍫🌶️",
        "explanation": "Capsaicin heat triggers human endorphin release while theobromine and roasted cacao pyrazines coat the palate, giving an intoxicating warm chocolate depth.",
        "vibe": "🌶️ Bold & Addictive",
        "dishes": [
            DishSuggestion(name="Aztec Spiced Hot Elixir", description="Thick drinking chocolate infused with Ceylon cinnamon, Mexican vanilla, and a gentle roasted chili kick.", difficulty="Easy", cook_time_mins=10, vibe_tag="🌙 Midnight Craving", meal_type="Beverage"),
            DishSuggestion(name="Spiced Cacao Ganache Tart", description="Bittersweet chocolate ganache dusted with chili flakes and flaky sea salt.", difficulty="Medium", cook_time_mins=30, vibe_tag="✨ Showstopper", meal_type="Dessert")
        ]
    },
    {
        "keys": {"strawberry", "balsamic vinegar"},
        "tastes_like": "Macerated Wild Blackberry Jam & Fig Glaze 🍓",
        "explanation": "Acetic acid in balsamic vinegar suppresses perceived astringency and amplifies human tongue sensitivity to fruit esters, making strawberries taste 3x sweeter and jammy.",
        "vibe": "🧠 Big Brain Gastronomy",
        "dishes": [
            DishSuggestion(name="Modena Glazed Strawberry Toast", description="Whipped ricotta or mascarpone on brioche topped with balsamic-macerated strawberries and cracked black pepper.", difficulty="Easy", cook_time_mins=8, vibe_tag="✨ Aesthetic Brunch", meal_type="Breakfast"),
            DishSuggestion(name="Warm Berry Balsamic Reduction", description="Gourmet coulis spooned over vanilla bean gelato or panna cotta.", difficulty="Easy", cook_time_mins=12, vibe_tag="🔥 Date Night Flex", meal_type="Dessert")
        ]
    },
    {
        "keys": {"avocado", "lime", "cilantro"},
        "tastes_like": "Bright Citrus Guacamole & Creamy Herb Dip 🥑",
        "explanation": "Citric acid cuts oleic monounsaturated lipids in avocado, while herbal decenal aldehydes in cilantro bring an ultra-fresh green bite.",
        "vibe": "🥑 S-Tier Freshness",
        "dishes": [
            DishSuggestion(name="Tableside Stone-Ground Guacamole", description="Chunky Hass avocado mashed with lime zest, serrano chili, and freshly plucked cilantro leaves.", difficulty="Easy", cook_time_mins=10, vibe_tag="🔥 Snack Perfection", meal_type="Snack"),
            DishSuggestion(name="Silky Cilantro Lime Crema", description="Blended avocado dressing with a dash of sea salt for tacos and bowls.", difficulty="Easy", cook_time_mins=5, vibe_tag="⚡ 5-Minute Meal Prep", meal_type="Condiment")
        ]
    },
    {
        "keys": {"coffee", "dark chocolate"},
        "tastes_like": "Velvety Espresso Mocha & Italian Tiramisu ☕",
        "explanation": "Identical roasted pyrazines and furfuryl volatiles cross-amplify bitterness and roasty aromatics into a luxurious cafe mocha profile.",
        "vibe": "⚡ Energy & Sophistication",
        "dishes": [
            DishSuggestion(name="Double Shot Mocha Affogato", description="Hot espresso poured over artisan dark chocolate gelato with shaved cacao.", difficulty="Easy", cook_time_mins=5, vibe_tag="✨ 3PM Pick-Me-Up", meal_type="Dessert"),
            DishSuggestion(name="Midnight Espresso Chocolate Bark", description="Snap-set dark chocolate studded with crushed espresso beans and sea salt.", difficulty="Easy", cook_time_mins=15, vibe_tag="🔥 Study Session Fuel", meal_type="Snack")
        ]
    },
    {
        "keys": {"apple", "cinnamon"},
        "tastes_like": "Warm Spiced Dutch Apple Strudel & Autumn Cider 🍏🥧",
        "explanation": "Cinnamaldehyde directly complements malic fruit esters, evoking the unmistakable sensory memory of freshly baked holiday pies.",
        "vibe": "🍂 Instant Cozy Fall Vibes",
        "dishes": [
            DishSuggestion(name="Caramelized Cinnamon Apple Skillet", description="Sliced orchard apples sautéed in brown butter and cinnamon until tender and golden.", difficulty="Easy", cook_time_mins=12, vibe_tag="✨ Pure Comfort", meal_type="Breakfast / Dessert"),
            DishSuggestion(name="Warm Spiced Mulled Cider", description="Pressed apple juice simmered with whole cinnamon bark, star anise, and orange peel.", difficulty="Easy", cook_time_mins=20, vibe_tag="❄️ Winter Warmth", meal_type="Beverage")
        ]
    },
    {
        "keys": {"bacon", "maple syrup"},
        "tastes_like": "Smoky Candied Maple Bacon & Savory Toffee 🥓🍁",
        "explanation": "Guaiacol smoke phenols and cured umami nitrites in bacon interlock with caramel pyrazines in maple syrup for the ultimate savory-sweet brunch indulgence.",
        "vibe": "🥓 Decadent Sweet-Savory Crunch",
        "dishes": [
            DishSuggestion(name="Slow-Crisped Candied Maple Bacon", description="Thick-cut smoked bacon oven-glazed with pure maple syrup and cracked black pepper.", difficulty="Easy", cook_time_mins=18, vibe_tag="✨ Brunch Showstopper", meal_type="Breakfast"),
            DishSuggestion(name="Maple Bacon Warm Brussels Sprouts", description="Pan-roasted charred sprouts tossed with crispy bacon lardons and maple glaze.", difficulty="Medium", cook_time_mins=15, vibe_tag="🔥 Bistro Favorite", meal_type="Dinner")
        ]
    },
    {
        "keys": {"peanut butter", "soy sauce"},
        "tastes_like": "Aromatic Bangkok Satay Glaze & Toasted Peanut Emulsion 🥜🥢",
        "explanation": "Roasted nutty pyrazines in peanut butter blend seamlessly with fermented glutamates and sodium in soy sauce, generating the foundational savoriness of Southeast Asian satay sauce.",
        "vibe": "🥢 Street Food Flavor Explosion",
        "dishes": [
            DishSuggestion(name="Warm Sesame Peanut Noodles", description="Hand-tossed noodles coated in a rich peanut butter, soy sauce, garlic, and chili dressing.", difficulty="Easy", cook_time_mins=12, vibe_tag="⚡ 10-Minute Comfort Food", meal_type="Lunch"),
            DishSuggestion(name="Thai Chicken Satay Skewers", description="Grilled chicken tenders glazed with warm peanut-soy emulsion and fresh lime.", difficulty="Medium", cook_time_mins=15, vibe_tag="🔥 Crowd Pleaser", meal_type="Dinner")
        ]
    },
    {
        "keys": {"coffee", "cardamom"},
        "tastes_like": "Warm Arabic Qahwa & Roasted Spiced Velvet ☕🌿",
        "explanation": "Dark roasted pyrazines and furans in coffee are lifted by the cool eucalyptol (cineole) and floral terpinyl acetate in cardamom, creating traditional Bedouin hospitality warmth.",
        "vibe": "☕ Aromatic Sensory Awakening",
        "dishes": [
            DishSuggestion(name="Traditional Cardamom Infused Qahwa", description="Lightly roasted coffee simmered gently with freshly crushed green cardamom pods.", difficulty="Easy", cook_time_mins=8, vibe_tag="✨ Cultural Classic", meal_type="Beverage"),
            DishSuggestion(name="Cardamom Espresso Panna Cotta", description="Silky coffee cream infused with crushed cardamom pods and vanilla.", difficulty="Medium", cook_time_mins=20, vibe_tag="🌙 Elegant Finish", meal_type="Dessert")
        ]
    },
    {
        "keys": {"chicken", "garlic", "rosemary"},
        "tastes_like": "Rustic Tuscan Herb-Roasted Poulet & Golden Jus 🍗🌿",
        "explanation": "Carnitine and Maillard amino-ketones in seared poultry meat absorb pinene terpenes from rosemary and allicin sweet confit from garlic, creating classic European hearth rotisserie flavors.",
        "vibe": "🍗 Sunday Roast Sensation",
        "dishes": [
            DishSuggestion(name="Crispy Rosemary Garlic Skillet Chicken", description="Pan-seared golden chicken cutlets basted with foaming rosemary-garlic butter.", difficulty="Medium", cook_time_mins=18, vibe_tag="🔥 20-Minute Masterpiece", meal_type="Dinner"),
            DishSuggestion(name="Roasted Garlic Herb Chicken Thighs", description="Crisp-skinned chicken thighs roasted over whole garlic cloves and fresh rosemary sprigs.", difficulty="Easy", cook_time_mins=35, vibe_tag="✨ Hearty Comfort", meal_type="Dinner")
        ]
    },
    {
        "keys": {"curry leaves", "mustard seeds", "coconut"},
        "tastes_like": "Aromatic South Indian Coastal Tadka & Coconut Tempering 🍃🥥",
        "explanation": "Popped black mustard seeds release pungent allyl isothiocyanate while hot coconut oil extracts lipid-soluble beta-caryophyllene from fresh curry leaves, creating the quintessential South Indian aromatic foundation.",
        "vibe": "🌴 Coastal Malabar Magic",
        "dishes": [
            DishSuggestion(name="Classic Kerala Coconut Aviyal or Poriyal", description="Fresh tender vegetables tossed in freshly grated coconut, tempered with crackling mustard seeds and fragrant curry leaves.", difficulty="Easy", cook_time_mins=15, vibe_tag="✨ Pure Tradition", meal_type="Side"),
            DishSuggestion(name="South Indian Coconut Chutney Tadka", description="Creamy ground coconut chutney finished with a sizzling tadka of mustard seeds, curry leaves, and dry red chili.", difficulty="Easy", cook_time_mins=8, vibe_tag="🔥 Breakfast Essential", meal_type="Condiment")
        ]
    },
    {
        "keys": {"toor dal", "curry leaves", "sambar powder"},
        "tastes_like": "Soul-Satisfying Authentic Madras Drumstick Sambar 🍲",
        "explanation": "Slow-stewed toor dal provides proteinaceous savory body, tamarind tartness balances the earthiness, and freshly bloomed sambar aromatics give comforting regional depth.",
        "vibe": "✨ South Indian Soul Food",
        "dishes": [
            DishSuggestion(name="Authentic Madras Drumstick Sambar", description="Slow-simmered yellow pigeon peas with drumsticks, shallots, tamarind, and aromatic sambar masala.", difficulty="Medium", cook_time_mins=30, vibe_tag="🔥 Feast Standard", meal_type="Dinner"),
            DishSuggestion(name="Mini Sambar Vada Dunk", description="Golden crispy medu vadas soaked in piping hot fragrant Madras sambar topped with ghee.", difficulty="Medium", cook_time_mins=25, vibe_tag="✨ Cafe Classic", meal_type="Breakfast")
        ]
    },
    {
        "keys": {"black pepper", "garlic", "cumin"},
        "tastes_like": "Zesty Chettinad Pepper Rasam & Digestive Tonic 🥣",
        "explanation": "Piperine in crushed black peppercorns combines synergistically with garlic allicin and cuminaldehyde, producing a soothing digestive broth that awakens the palate and clears the senses.",
        "vibe": "🌿 Ancient Herbal Remedy",
        "dishes": [
            DishSuggestion(name="Chettinad Milagu Poondu Rasam", description="Spicy and tangy black pepper-garlic soup tempered with cumin and curry leaves in hot ghee.", difficulty="Easy", cook_time_mins=15, vibe_tag="✨ Monsoon Comfort", meal_type="Soup"),
            DishSuggestion(name="Steamed Rice with Ghee & Hot Rasam", description="Piping hot jasmine or ponni rice mashed with A2 cow ghee and drenched in fiery pepper rasam.", difficulty="Easy", cook_time_mins=10, vibe_tag="❤️ Ultimate Comfort", meal_type="Lunch")
        ]
    },
    {
        "keys": {"paneer", "tomato", "kasuri methi"},
        "tastes_like": "Velvety Shahi Makhani Gravy with Fenugreek Aroma 🍛",
        "explanation": "Lycopene and umami-rich cooked tomatoes emulsified with butter provide a luxurious sweet-savory base, while crushed kasuri methi imparts sotolon lactones for that signature North Indian restaurant aroma.",
        "vibe": "👑 Royal Dawat Luxury",
        "dishes": [
            DishSuggestion(name="Delhi Shahi Paneer Butter Masala", description="Tender cottage cheese cubes simmered in a silky tomato, cashew, and butter gravy perfumed with crushed kasuri methi.", difficulty="Medium", cook_time_mins=25, vibe_tag="🔥 Restaurant Quality", meal_type="Dinner"),
            DishSuggestion(name="Smoky Paneer Tikka Lababdar", description="Charred tandoori paneer simmered with caramelized onions, tomatoes, and dried fenugreek leaves.", difficulty="Hard", cook_time_mins=35, vibe_tag="✨ Festive Star", meal_type="Dinner")
        ]
    },
    {
        "keys": {"idli dosa batter", "ghee"},
        "tastes_like": "Crispy Golden South Indian Ghee Roast Dosa 🥞",
        "explanation": "Fermented lactic acid batter undergoes rapid Maillard browning when poured on a blazing hot tawa; clarified butter fat (ghee) crisps the edges and infuses rich nutty diacetyl notes.",
        "vibe": "🔥 Tiffin Stall Legend",
        "dishes": [
            DishSuggestion(name="Crispy Ghee Roast Paper Dosa", description="Wafer-thin, lace-edged crepe roasted in pure golden ghee, served with coconut chutney and piping hot sambar.", difficulty="Medium", cook_time_mins=12, vibe_tag="✨ Morning Bliss", meal_type="Breakfast"),
            DishSuggestion(name="Ghee Podi Thatte Idli", description="Thick pillowy steamed rice cakes drenched in molten ghee and gunpowder roasted lentil spice mix.", difficulty="Easy", cook_time_mins=15, vibe_tag="🔥 South Indian Favorite", meal_type="Breakfast")
        ]
    },
    {
        "keys": {"rajma", "garam masala", "onion"},
        "tastes_like": "Hearty Punjabi Dhaba Style Rajma Masala 🍛",
        "explanation": "Slow-stewed red kidney beans release thick amylose starches that bind with caramelized onion-ginger bhunao and warming eugenol/cinnamon terpenes from garam masala.",
        "vibe": "❤️ Pure Punjabi Nostalgia",
        "dishes": [
            DishSuggestion(name="Dhaba Style Punjabi Rajma Chawal", description="Melt-in-mouth kidney beans simmered in a spiced onion-tomato gravy, served with fragrant cumin basmati rice.", difficulty="Medium", cook_time_mins=40, vibe_tag="🔥 Sunday Special", meal_type="Lunch"),
            DishSuggestion(name="Smoked Kashmiri Rajma Galouti", description="Silky spiced red kidney bean patties shallow-fried in ghee, served with mint chutney.", difficulty="Medium", cook_time_mins=25, vibe_tag="✨ Gourmet Starter", meal_type="Appetizer")
        ]
    },
    {
        "keys": {"guava", "chaat masala"},
        "tastes_like": "Sweet-Tangy Mumbai Street Cart Pink Guava Chaat 🍈✨",
        "explanation": "Tropical sweet esters in crunchy ripe guava are electrified by the tart malic amchur, pungent black salt (sulfur notes), and roasted cumin in chaat masala.",
        "vibe": "⚡ Mind-Blowing Sweet & Tangy",
        "dishes": [
            DishSuggestion(name="Street-Style Spiced Guava Wedges", description="Firm pink guava sliced into crescents, dusted generously with chaat masala, red chili, and a squeeze of fresh lime.", difficulty="Easy", cook_time_mins=5, vibe_tag="🔥 Instant Hit", meal_type="Snack"),
            DishSuggestion(name="Tropical Guava & Pomegranate Chaat", description="Chilled diced guava and ruby pomegranate jewels tossed with mint, amchur, and lemon juice.", difficulty="Easy", cook_time_mins=7, vibe_tag="✨ Refreshing Crunch", meal_type="Salad")
        ]
    },
    {
        "keys": {"okra", "amchur", "cumin"},
        "tastes_like": "Crispy Tart-Spiced Kurkuri Bhindi (Okra) 🌶️",
        "explanation": "Tart amchur (dried mango powder) breaks down okra mucilage upon cooking, while cumin pyrazines coat the crispy vegetable strips for zero-sliminess crunch.",
        "vibe": "💥 Irresistible Crisp Crunch",
        "dishes": [
            DishSuggestion(name="Crispy Kurkuri Bhindi Fries", description="Thinly julienned okra tossed with chickpea flour, cumin, and dry mango powder, flash-fried until ultra-crisp.", difficulty="Easy", cook_time_mins=15, vibe_tag="✨ Snack Addiction", meal_type="Snack"),
            DishSuggestion(name="North Indian Masala Bhindi Do Pyaza", description="Tender okra sautéed with double the onions, roasted cumin seeds, and a sharp amchur finish.", difficulty="Medium", cook_time_mins=20, vibe_tag="🔥 Home-Style Winner", meal_type="Side")
        ]
    }
]

PREPARATION_MODIFIERS = {
    "Raw": {"sweet": 1.0, "sour": 1.0, "bitter": 1.0, "umami": 1.0, "spicy": 1.0, "aroma_decay": 1.0},
    "Roasted": {"sweet": 1.2, "sour": 0.85, "bitter": 0.9, "umami": 1.25, "spicy": 0.9, "aroma_decay": 1.1},
    "Sautéed": {"sweet": 1.15, "sour": 0.9, "bitter": 0.9, "umami": 1.2, "spicy": 0.95, "aroma_decay": 1.05},
    "Cooked": {"sweet": 1.05, "sour": 0.9, "bitter": 0.85, "umami": 1.1, "spicy": 0.9, "aroma_decay": 0.95},
    "Boiled": {"sweet": 0.95, "sour": 0.9, "bitter": 0.8, "umami": 1.0, "spicy": 0.85, "aroma_decay": 0.85},
}

class FlavorEngine:
    def __init__(self, db_session):
        self.db = db_session

    def analyze_combination(
        self,
        ingredients_input: List[IngredientInput],
        user_preference: Optional[UserPreference] = None,
        title: Optional[str] = None
    ) -> CombinationAnalyzeResponse:
        """
        Analyzes 1 to 30+ ingredients dynamically.
        Computes basic taste radar values, aroma clusters, texture profile,
        pairwise affinity matrix, conflicts, balance score, and personalized match.
        """
        if not ingredients_input:
            raise ValueError("At least one ingredient must be provided for analysis.")

        if len(ingredients_input) > 35:
            raise ValueError("Maximum 35 ingredients allowed per analysis.")

        # 1. Ingredient Normalization & Duplicate Handling
        normalized_inputs: Dict[str, Dict[str, Any]] = {}
        duplicate_warnings: List[str] = []

        for item in ingredients_input:
            clean_name = item.name.strip().title()
            if clean_name in normalized_inputs:
                normalized_inputs[clean_name]["quantity"] += item.quantity
                duplicate_warnings.append(
                    f"Duplicate ingredient '{clean_name}' combined into total {normalized_inputs[clean_name]['quantity']}{item.unit}."
                )
            else:
                normalized_inputs[clean_name] = {
                    "name": clean_name,
                    "quantity": max(item.quantity, 1.0),
                    "unit": item.unit,
                    "prep": item.preparation_method or "Raw"
                }

        unique_items = list(normalized_inputs.values())
        total_quantity = sum(x["quantity"] for x in unique_items)

        # 2. Fetch Ingredient Metadata & Profiles
        ing_models: Dict[str, Ingredient] = {}
        missing_ingredients: List[str] = []

        for item in unique_items:
            name = item["name"]
            ing = self.db.query(Ingredient).filter(Ingredient.name.ilike(name)).first()
            if ing:
                ing_models[name] = ing
            else:
                missing_ingredients.append(name)

        # If an ingredient is missing from database, synthesize a baseline heuristic profile
        for missing_name in missing_ingredients:
            ing_models[missing_name] = Ingredient(
                name=missing_name,
                slug=missing_name.lower().replace(" ", "-"),
                category="General",
                description="Custom user ingredient with estimated culinary baseline.",
                allergens=[],
                is_curated=False
            )
            ing_models[missing_name].flavor_profile = IngredientFlavorProfile(
                sweet=3.0, salty=1.0, sour=1.0, bitter=1.0, umami=3.0, spicy=1.0, intensity=5.0,
                primary_aromas=["Earthy", "Fresh"],
                texture_profile=["Tender"],
                dominant_compounds=[]
            )

        # 3. Calculate Weighted Basic Taste Radar
        taste_totals = {"sweet": 0.0, "salty": 0.0, "sour": 0.0, "bitter": 0.0, "umami": 0.0, "spicy": 0.0}
        total_intensity_weighted = 0.0

        aroma_scores: Dict[str, float] = {}
        texture_scores: Dict[str, float] = {}

        for item in unique_items:
            name = item["name"]
            q = item["quantity"]
            weight = q / total_quantity
            prep = item["prep"]
            mods = PREPARATION_MODIFIERS.get(prep, PREPARATION_MODIFIERS["Raw"])

            fp = ing_models[name].flavor_profile
            if not fp:
                continue

            intensity = getattr(fp, "intensity", 5.0)
            # Intensity-adjusted weight: high-intensity spices have more sensory impact per gram
            sensory_weight = weight * (intensity / 5.0)
            total_intensity_weighted += sensory_weight

            taste_totals["sweet"] += fp.sweet * mods["sweet"] * sensory_weight
            taste_totals["salty"] += fp.salty * sensory_weight
            taste_totals["sour"] += fp.sour * mods["sour"] * sensory_weight
            taste_totals["bitter"] += fp.bitter * mods["bitter"] * sensory_weight
            taste_totals["umami"] += fp.umami * mods["umami"] * sensory_weight
            taste_totals["spicy"] += fp.spicy * mods["spicy"] * sensory_weight

            # Aromas
            for aroma in (fp.primary_aromas or []):
                aroma_scores[aroma] = aroma_scores.get(aroma, 0.0) + (sensory_weight * 10.0)

            # Textures
            for tex in (fp.texture_profile or []):
                texture_scores[tex] = texture_scores.get(tex, 0.0) + (weight * 100.0)

        # Normalize tastes to 0 - 10 scale
        div = max(total_intensity_weighted, 0.1)
        final_taste_profile = {
            k: round(min(max(v / div, 0.0), 10.0), 1)
            for k, v in taste_totals.items()
        }

        # Normalize aromas to top highlights
        total_aroma_sum = sum(aroma_scores.values()) or 1.0
        final_aroma_profile = {
            k: round((v / total_aroma_sum) * 100.0, 1)
            for k, v in sorted(aroma_scores.items(), key=lambda x: x[1], reverse=True)[:7]
        }

        final_texture_profile = {
            k: round(v, 1)
            for k, v in sorted(texture_scores.items(), key=lambda x: x[1], reverse=True)[:5]
        }

        # 4. Pairwise Interaction Evaluation
        pairwise_matrix: List[PairwiseInteraction] = []
        interaction_notes: List[str] = []
        conflicts: List[str] = list(duplicate_warnings)

        pair_scores = []
        n = len(unique_items)

        if n == 1:
            pair_scores.append(80.0)
            interaction_notes.append(f"Single ingredient baseline profile for {unique_items[0]['name']}.")
        else:
            for i in range(n):
                for j in range(i + 1, n):
                    name_a = unique_items[i]["name"]
                    name_b = unique_items[j]["name"]
                    ing_a = ing_models[name_a]
                    ing_b = ing_models[name_b]

                    pair_interaction = self._evaluate_pair(ing_a, ing_b, unique_items[i], unique_items[j])
                    pairwise_matrix.append(pair_interaction)
                    pair_scores.append(pair_interaction.affinity_score)

                    if pair_interaction.reason:
                        interaction_notes.append(pair_interaction.reason)
                    if pair_interaction.conflict:
                        conflicts.append(pair_interaction.conflict)

        # 5. Higher-Order Balance Analysis & Conflicts
        # Acid-Sweetness balance:
        sw = final_taste_profile["sweet"]
        so = final_taste_profile["sour"]
        if sw > 7.0 and so < 1.0:
            conflicts.append("High sweetness without balancing acidity may feel cloying or flat.")
        elif so > 7.5 and sw < 1.5:
            conflicts.append("Sharp acidity dominates; consider a pinch of sweetness or fat to soften the edge.")

        # Bitterness warning:
        if final_taste_profile["bitter"] > 6.5 and sw < 3.0 and final_taste_profile["salty"] < 3.0:
            conflicts.append("Prominent bitterness without adequate fat, salt, or sweetness to buffer.")

        # Extreme Heat:
        if final_taste_profile["spicy"] > 7.8 and "Dairy" not in [ing_models[x["name"]].category for x in unique_items]:
            conflicts.append("Very high pungency/heat; pair with a cooling element like curd, cucumber, or lime.")

        # 6. Overall Compatibility Calculation
        avg_pair_score = sum(pair_scores) / len(pair_scores) if pair_scores else 75.0
        
        # Balance score based on diversity of harmonized tastes
        taste_variance = sum(abs(v - 4.0) for v in final_taste_profile.values()) / 6.0
        balance_bonus = max(0.0, (6.0 - taste_variance) * 2.5)  # balanced profiles score up to +15

        conflict_penalty = min(len([c for c in conflicts if "Duplicate" not in c]) * 6.0, 30.0)
        overall_comp = min(max(avg_pair_score + balance_bonus - conflict_penalty, 25.0), 99.0)

        # 7. Personalized Match Score
        personalized_score = overall_comp
        if user_preference:
            personalized_score = self._compute_personalized_score(
                base_score=overall_comp,
                unique_items=unique_items,
                ing_models=ing_models,
                taste_profile=final_taste_profile,
                preference=user_preference,
                conflicts=conflicts
            )

        # 8. Suggested Ratios & Complementary Suggestions
        suggested_ratios = self._calculate_ratios(unique_items, ing_models, total_quantity)
        complementary_suggestions = self._find_complementary(unique_items, final_taste_profile, ing_models)

        # 9. Evidence Quality & Uncertainty
        evidence_quality, uncertainty = self._assess_evidence_quality(unique_items, missing_ingredients, pairwise_matrix)

        combo_title = title or self._generate_title(unique_items)

        # Explanation summary
        explanation = self._generate_explanation(
            unique_items, overall_comp, personalized_score, final_taste_profile, interaction_notes, conflicts
        )

        # 10. Emergent Flavor Illusion ("Tastes Like"), Molecular Volatiles & Dish Suggestions
        (
            tastes_like,
            tastes_like_exp,
            vibe_tag,
            possible_dishes,
            shared_molecules,
            shared_molecule_count,
            molecular_taste_synthesis
        ) = self._detect_emergent_flavor_and_dishes(
            unique_items, final_taste_profile, ing_models, pairwise_matrix
        )

        return CombinationAnalyzeResponse(
            title=combo_title,
            overall_compatibility=round(overall_comp, 1),
            personalized_match=round(personalized_score, 1) if user_preference else None,
            taste_profile=final_taste_profile,
            aroma_profile=final_aroma_profile,
            texture_profile=final_texture_profile,
            interaction_notes=interaction_notes[:6],
            pairwise_matrix=pairwise_matrix,
            flavor_conflicts=conflicts,
            suggested_ratios=suggested_ratios,
            complementary_suggestions=complementary_suggestions,
            evidence_quality=evidence_quality,
            uncertainty_score=round(uncertainty, 1),
            explanation=explanation,
            tastes_like=tastes_like,
            tastes_like_explanation=tastes_like_exp,
            vibe_check=vibe_tag,
            shared_molecules=shared_molecules,
            shared_molecule_count=shared_molecule_count,
            molecular_taste_synthesis=molecular_taste_synthesis,
            possible_dishes=possible_dishes
        )

    def _detect_emergent_flavor_and_dishes(
        self,
        unique_items: List[Dict[str, Any]],
        taste_profile: Dict[str, float],
        ing_models: Dict[str, Ingredient],
        pairwise_matrix: Optional[List[PairwiseInteraction]] = None
    ) -> Tuple[str, str, str, List[DishSuggestion], List[str], int, str]:
        """
        Analyzes volatile aroma molecules, receptor mechanisms, and emergent sensory illusions.
        Returns (tastes_like, explanation, vibe, dishes, shared_molecules, shared_molecule_count, molecular_synthesis).
        Never outputs raw placeholder concatenations like {names[0]} & {names[1]}.
        """
        names_raw = [x["name"].lower().strip() for x in unique_items]
        
        # 1. Collect volatile aroma molecules from database models
        compounds_by_ing: Dict[str, List[str]] = {}
        all_present_compounds: List[str] = []
        for item in unique_items:
            name = item["name"]
            ing = ing_models.get(name)
            comps = []
            if ing and ing.flavor_profile and ing.flavor_profile.dominant_compounds:
                comps = [c.strip() for c in ing.flavor_profile.dominant_compounds if c.strip()]
            compounds_by_ing[name] = comps
            all_present_compounds.extend(comps)

        # 2. Compute exact shared volatile molecules across ingredient pairs
        shared_compounds_set = set()
        if pairwise_matrix:
            for pair in pairwise_matrix:
                for sc in (pair.shared_compounds or []):
                    if sc and len(sc) > 1:
                        shared_compounds_set.add(sc.strip().title())

        # Directly intersect dominant compounds
        item_keys = list(compounds_by_ing.keys())
        for i in range(len(item_keys)):
            for j in range(i + 1, len(item_keys)):
                set_a = set(c.lower() for c in compounds_by_ing[item_keys[i]])
                set_b = set(c.lower() for c in compounds_by_ing[item_keys[j]])
                common = set_a.intersection(set_b)
                for c in common:
                    shared_compounds_set.add(c.title())
                # Check chemical family overlaps (e.g. pyrazine, vanillin, limonene, linalool, eugenol)
                for ca in compounds_by_ing[item_keys[i]]:
                    for cb in compounds_by_ing[item_keys[j]]:
                        ca_l = ca.lower()
                        cb_l = cb.lower()
                        if (ca_l in cb_l or cb_l in ca_l) and len(ca_l) >= 4:
                            shared_compounds_set.add(ca.title())

        # If sparse overlap, evaluate chemical bridge from functional active constituents
        if not shared_compounds_set and len(unique_items) >= 2:
            all_lower = " ".join([c.lower() for c in all_present_compounds] + names_raw)
            if any(k in all_lower for k in ["butter", "cream", "dairy", "cheese", "oil", "fat"]) and any(k in all_lower for k in ["citric", "malic", "lemon", "apple", "vinegar"]):
                shared_compounds_set.add("Ester-Lipid Solubilization Complex")
            if any(k in all_lower for k in ["garlic", "onion", "shallot", "allicin"]) and any(k in all_lower for k in ["rosemary", "thyme", "basil", "pepper"]):
                shared_compounds_set.add("Organosulfur-Terpene Resonance")
            if any(k in all_lower for k in ["soy sauce", "glutamate", "parmesan", "tomato"]) and any(k in all_lower for k in ["sugar", "vanilla", "honey", "caramel"]):
                shared_compounds_set.add("SGLT1 Sodium-Glucose Receptor Bridge")

        shared_molecules = sorted(list(shared_compounds_set))
        shared_molecule_count = len(shared_molecules)

        # 3. Receptor Dynamics & Molecular Taste Synthesis
        all_comp_str = " ".join([c.lower() for c in all_present_compounds] + [s.lower() for s in shared_molecules] + names_raw)
        receptor_notes = []

        if any(k in all_comp_str for k in ["vanillin", "4-hydroxybenzaldehyde"]):
            receptor_notes.append("Vanillin binds nasal olfactory OR51M1 GPCR receptors, providing warm confectionery sweetness and amplifying perceived creaminess.")
        if any(k in all_comp_str for k in ["eugenol", "cinnamaldehyde", "cardamom", "clove"]):
            receptor_notes.append("Phenylpropanoids (eugenol, cinnamaldehyde) cross-stimulate TRPV1 warmth channels and T1R3 sweet-taste receptors for comforting bakery spice.")
        if any(k in all_comp_str for k in ["glutamate", "glutamic", "inosinate"]) or taste_profile.get("umami", 0) > 4.2:
            receptor_notes.append("Free glutamates cooperatively activate the T1R1/T1R3 umami receptor heterodimer, producing intense salivation and savory depth.")
        if any(k in all_comp_str for k in ["limonene", "citral", "linalool", "terpinene"]):
            receptor_notes.append("Monoterpenes (limonene, citral) stimulate olfactory receptors, releasing vibrant, uplifting citrus top-notes that slice through heavy lipids.")
        if any(k in all_comp_str for k in ["allicin", "sulfur", "diallyl", "scallion", "garlic"]):
            receptor_notes.append("Organosulfur volatiles stimulate TRPA1 chemosensory receptors, unlocking deep savory allium warmth.")
        if any(k in all_comp_str for k in ["malic", "citric", "tartaric", "acetic"]) or taste_profile.get("sour", 0) > 3.0:
            receptor_notes.append("Organic acids stimulate OTOP1 proton channels, sharply clearing tongue fats and amplifying fruit ester perception.")
        if any(k in all_comp_str for k in ["pyrazine", "theobromine", "guaiacol", "roasted"]):
            receptor_notes.append("Alkylpyrazines and phenolic volatiles stimulate retronasal aroma pathways with roasted Maillard crust and toasted notes.")
        if any(k in all_comp_str for k in ["capsaicin", "chili", "hot"]) or taste_profile.get("spicy", 0) > 3.5:
            receptor_notes.append("Capsaicin selectively depolarizes TRPV1 nociceptive heat receptors, triggering pleasant warmth and endorphin release.")
        if any(k in all_comp_str for k in ["butyric", "lactone", "diacetyl", "cream", "butter"]):
            receptor_notes.append("Dairy lactones and short-chain fatty acids stimulate oral somatosensory mechanoreceptors for rich velvety mouthfeel.")

        if not receptor_notes:
            receptor_notes.append("Chemosensory receptors engage in balanced cross-adaptation, preventing palate fatigue while maintaining harmonious flavor layers.")

        if shared_molecule_count > 0:
            mol_prefix = f"Analyzing the volatilome reveals {shared_molecule_count} shared aroma molecules ({', '.join(shared_molecules[:4])}). "
        else:
            mol_prefix = "Analyzing the volatilome reveals a complementary, multi-receptor affinity bridge. "

        molecular_taste_synthesis = mol_prefix + " ".join(receptor_notes[:2])

        # 4. Check curated emergent synergies
        normalized_keys = set(names_raw)
        for n in names_raw:
            if "apple" in n:
                normalized_keys.add("apple")
                normalized_keys.add("green apple")
            if "salt" in n:
                normalized_keys.add("salt")
            if "feta" in n:
                normalized_keys.add("feta")
                normalized_keys.add("feta cheese")
            if "curd" in n or "yogurt" in n:
                normalized_keys.add("curd")
            if "cheddar" in n:
                normalized_keys.add("cheddar")
            if "vanilla" in n:
                normalized_keys.add("vanilla")
            if "soy" in n:
                normalized_keys.add("soy sauce")
            if "chicken" in n:
                normalized_keys.add("chicken")
            if "salmon" in n:
                normalized_keys.add("salmon")
            if "butter" in n:
                normalized_keys.add("butter")
            if "garlic" in n:
                normalized_keys.add("garlic")
            if "chocolate" in n:
                normalized_keys.add("dark chocolate")

        for syn in EMERGENT_FLAVOR_SYNERGIES:
            if syn["keys"].issubset(normalized_keys):
                return (
                    syn["tastes_like"],
                    syn["explanation"],
                    syn["vibe"],
                    syn["dishes"],
                    shared_molecules,
                    shared_molecule_count,
                    molecular_taste_synthesis
                )

        # 5. Dynamic Flavor Synthesis (No placeholder strings)
        sw = taste_profile.get("sweet", 0)
        um = taste_profile.get("umami", 0)
        so = taste_profile.get("sour", 0)
        sp = taste_profile.get("spicy", 0)
        sa = taste_profile.get("salty", 0)

        has_dairy = any(x in ["butter", "ghee", "curd", "cream", "mozzarella", "cheddar", "feta", "parmesan", "cheese", "mascarpone", "ricotta"] for x in names_raw)
        has_acid = any(x in ["lemon", "lime", "balsamic vinegar", "vinegar", "green apple", "tomato", "orange", "sherry vinegar"] for x in names_raw) or so > 3.5
        has_protein = any(x in ["chicken", "salmon", "shrimp", "bacon", "beef", "pork", "paneer", "tofu", "egg", "beef tenderloin", "prosciutto", "pancetta", "lamb chops"] for x in names_raw)
        has_allium = any(x in ["garlic", "onion", "shallot", "scallion"] for x in names_raw)
        has_herb = any(x in ["basil", "mint", "cilantro", "dill", "rosemary", "thyme", "oregano", "pesto genovese"] for x in names_raw)
        has_sweet = any(x in ["honey", "sugar", "dark chocolate", "white chocolate", "milk chocolate", "mango", "strawberry", "apple", "maple syrup", "banana", "vanilla ice cream", "chocolate ice cream", "brown sugar"] for x in names_raw) or sw > 4.5
        has_salt = any("salt" in x or "soy sauce" in x or "parmesan" in x or "pecorino" in x or "anchovy" in x for x in names_raw) or sa > 3.5
        has_chocolate = any("chocolate" in x or "cocoa" in x or "cacao" in x for x in names_raw)

        if has_sweet and has_salt:
            t_like = "Velvety Salted Butterscotch & Golden Caramelized Nectar 🍮🧂"
            exp = f"Sodium ions selectively stimulate SGLT1 glucose transporters, eliminating perceived bitterness and elevating sweetness into a deep toffee-caramel profile. {molecular_taste_synthesis}"
            vibe = "✨ Sweet-Savory Perfection"
            dishes = [
                DishSuggestion(name="Artisan Salt-Kissed Glazed Confection", description="Golden caramelized dessert tart topped with flaky sea salt and sweet nectar notes.", difficulty="Easy", cook_time_mins=12, vibe_tag="✨ Sweet-Savory Flex", meal_type="Dessert"),
                DishSuggestion(name="Warm Salted Butterscotch Toast", description="Toasted brioche brushed with savory-sweet glaze and crunchy toffee notes.", difficulty="Easy", cook_time_mins=8, vibe_tag="🔥 Snack Perfection", meal_type="Breakfast")
            ]
        elif has_dairy and (has_acid or "apple" in " ".join(names_raw)):
            t_like = "Crisp Malic Orchard Acidity Slicing Rich Artisan Dairy Lipids 🍏🧀"
            exp = f"High malic and citric organic acids swiftly dissolve tongue-coating dairy fats, creating a vibrant alternating rhythm between rich creamy mouthfeel and refreshingly tart, crisp crunch. {molecular_taste_synthesis}"
            vibe = "🍏 Bistro Precision Harmony"
            dishes = [
                DishSuggestion(name="Artisan Orchard Fruit & Cheese Crostini", description="Toasted sourdough layered with melted artisan cheese, thinly sliced tart fruit, and honey drizzle.", difficulty="Easy", cook_time_mins=8, vibe_tag="✨ Bistro Starter", meal_type="Snack"),
                DishSuggestion(name="Shaved Crisp Orchard Salad with Crumbled Cheese", description="Delicate ribbons of tart fruit tossed with crumbly artisan cheese and cold-pressed vinaigrette.", difficulty="Easy", cook_time_mins=10, vibe_tag="🥗 Clean Crunch", meal_type="Salad")
            ]
        elif (has_protein or has_dairy) and has_allium and has_herb:
            t_like = "Savory Tuscan Herb-Seared Confit with Golden Allium Pan Jus 🍗🌿"
            exp = f"Volatile allicin from crushed alliums and terpene hydrocarbons from fresh herbs dissolve into rendered fats, binding deeply with Maillard crusts for classic European hearth flavor. {molecular_taste_synthesis}"
            vibe = "🔥 Michelin Pan Roast"
            dishes = [
                DishSuggestion(name="Pan-Seared Golden Skillet Roast with Herb Butter", description="Crisp-seared savory skillet finished with foaming garlic-herb butter and aromatic pan jus.", difficulty="Medium", cook_time_mins=18, vibe_tag="🔥 15-Minute Dinner", meal_type="Dinner"),
                DishSuggestion(name="Slow-Braised Garlic & Herb Confit Skillet", description="Tender savory skillet deglazed with aromatic herb pan sauce.", difficulty="Easy", cook_time_mins=25, vibe_tag="✨ Hearty Comfort", meal_type="Dinner")
            ]
        elif um > 4.2 and ("soy sauce" in " ".join(names_raw) or "garlic" in " ".join(names_raw) or "ginger" in " ".join(names_raw)):
            t_like = "Deep Savory Wok-Charred Umami & Toasted Pyrazines 🥢"
            exp = f"High concentrations of glutamates and allicin compounds rapidly brown at high heat, developing deep caramelized Asian street food aromatics. {molecular_taste_synthesis}"
            vibe = "🥢 Pure Savory Umami"
            dishes = [
                DishSuggestion(name="High-Heat Wok-Seared Glazed Stir-Fry", description="Crisp seared ingredients tossed with savory aromatics, ginger-garlic reduction, and toasted sesame.", difficulty="Medium", cook_time_mins=12, vibe_tag="⚡ 10-Minute Meal", meal_type="Dinner"),
                DishSuggestion(name="Savory Caramelized Umami Rice Bowl", description="Steamed Jasmine rice bowl topped with savory caramelized reduction and fresh scallions.", difficulty="Easy", cook_time_mins=15, vibe_tag="🌿 Nutrient Rich", meal_type="Lunch")
            ]
        elif has_chocolate and (sp > 3.0 or "coffee" in " ".join(names_raw) or "cinnamon" in " ".join(names_raw)):
            t_like = "Velvety Aztec Cacao Truffle & Bittersweet Espresso Ganache 🍫"
            exp = f"Roasted pyrazines, theobromine, and warming spices create a luxurious dessert finish with enduring chocolate depth. {molecular_taste_synthesis}"
            vibe = "🍫 Gourmet Cacao Luxury"
            dishes = [
                DishSuggestion(name="Decadent Dark Cacao Ganache Tart", description="Bittersweet chocolate ganache dusted with warming spices and sea salt in an artisan crust.", difficulty="Medium", cook_time_mins=30, vibe_tag="✨ Showstopper", meal_type="Dessert"),
                DishSuggestion(name="Spiced Hot Aztec Cocoa Elixir", description="Thick velvet drinking chocolate infused with Ceylon cinnamon, pure vanilla, and a gentle kick.", difficulty="Easy", cook_time_mins=10, vibe_tag="🌙 Midnight Craving", meal_type="Beverage")
            ]
        elif has_herb and ("mint" in " ".join(names_raw) or "cucumber" in " ".join(names_raw) or "lime" in " ".join(names_raw)):
            t_like = "Chilled Botanical Menthol Quench & Refreshing Citrus Aqua 🌿🍋"
            exp = f"TRPM8 cold receptors triggered by herbal menthols and citrus monoterpenes deliver an instant sensation of crisp, thirst-quenching lightness. {molecular_taste_synthesis}"
            vibe = "🌿 Botanical Cleanse"
            dishes = [
                DishSuggestion(name="Chilled Botanical Citrus Carpaccio", description="Paper-thin cold slices dressed with fresh herbal oils, lime zest, and flaky sea salt.", difficulty="Easy", cook_time_mins=8, vibe_tag="✨ Clean Refreshment", meal_type="Appetizer"),
                DishSuggestion(name="Infused Fresh Herb & Citrus Cooler", description="Lightly crushed botanical elixir served over crystal ice with torn mint.", difficulty="Easy", cook_time_mins=5, vibe_tag="⚡ Summer Essential", meal_type="Beverage")
            ]
        elif sw > 5.0 and um > 4.0:
            t_like = "Caramelized Glazed Umami with Sweet Teriyaki Butterscotch 🍯"
            exp = f"The cross-activation of sweet sucrose receptors and umami glutamate channels mimics slow-caramelized roasted glaze. {molecular_taste_synthesis}"
            vibe = "🔥 High Umami Comfort"
            dishes = [
                DishSuggestion(name="Glazed Sweet-Savory Skillet Medley", description="Sautéed savory elements caramelized with rich sweet glaze and aromatic garnish.", difficulty="Easy", cook_time_mins=15, vibe_tag="✨ Weeknight Sensation", meal_type="Dinner"),
                DishSuggestion(name="Caramelized Sweet Umami Grain Bowl", description="Warm grain bowl finished with savory-sweet glaze and toasted seeds.", difficulty="Easy", cook_time_mins=20, vibe_tag="🌿 Nutrient Rich", meal_type="Lunch")
            ]
        elif sw > 5.5 and so > 3.5:
            t_like = "Vibrant Tropical Agrodolce & Sweet-Tart Nectar 🍋🥭"
            exp = f"High acid tightly balancing pronounced sweetness mimics tart tropical sorbet or Sicilian agrodolce. {molecular_taste_synthesis}"
            vibe = "⚡ Electric Zest"
            dishes = [
                DishSuggestion(name="Zesty Sweet-Tart Fruit & Herb Tartare", description="Cold-tossed diced fresh fruit dressed with sweet-and-sour citrus reduction.", difficulty="Easy", cook_time_mins=10, vibe_tag="✨ Refreshing Crudo", meal_type="Appetizer"),
                DishSuggestion(name="Chilled Citrus Agrodolce Coulis", description="Blended dessert nectar reduction drizzled over chilled crema or fruit.", difficulty="Easy", cook_time_mins=8, vibe_tag="🔥 Dessert Topper", meal_type="Dessert")
            ]
        elif sp > 4.0 and um > 4.0:
            t_like = "Szechuan Fiery Umami & Charred Chili Crisp 🌶️"
            exp = f"Capsaicin heat combined with rich amino acid umami evokes roasted chili oil and street food depth. {molecular_taste_synthesis}"
            vibe = "🌶️ Certified Fire"
            dishes = [
                DishSuggestion(name="Fiery Szechuan Chili Stir-Fry", description="Wok-tossed savory elements crisped with aromatic chili oil and crushed peppercorns.", difficulty="Medium", cook_time_mins=15, vibe_tag="🔥 15-Minute Dinner", meal_type="Dinner"),
                DishSuggestion(name="Spicy Roasted Chili Glaze Noodles", description="Glossy chili-garlic reduction tossed with tender noodles or crisp vegetables.", difficulty="Easy", cook_time_mins=10, vibe_tag="✨ Chef's Secret", meal_type="Lunch")
            ]
        else:
            t_like = "Harmonized Artisan Pan-Sear with Warm Roasted Volatiles & Savory Balance ✨"
            exp = f"The aromatic volatiles and natural culinary oils marry during cooking, creating balanced flavor layers without palate fatigue. {molecular_taste_synthesis}"
            vibe = "✨ Chef's Kiss"
            dishes = [
                DishSuggestion(name="Artisan Pan-Roasted Golden Skillet", description="Carefully seasoned ingredients sautéed to golden perfection with aromatics and olive oil.", difficulty="Easy", cook_time_mins=15, vibe_tag="✨ Flavor Harmony", meal_type="Dinner"),
                DishSuggestion(name="Fresh Bistro Platter with Herb Dressing", description="Crisp layered dish dressed with cold-pressed olive oil, herbs, and sea salt.", difficulty="Easy", cook_time_mins=10, vibe_tag="🌿 Clean Gastronomy", meal_type="Lunch")
            ]

        return (
            t_like,
            exp,
            vibe,
            dishes,
            shared_molecules,
            shared_molecule_count,
            molecular_taste_synthesis
        )

    def _evaluate_pair(
        self,
        ing_a: Ingredient,
        ing_b: Ingredient,
        item_a: Dict[str, Any],
        item_b: Dict[str, Any]
    ) -> PairwiseInteraction:
        """Evaluates pairwise affinity using curated evidence + chemical compound overlap."""
        name_a = ing_a.name
        name_b = ing_b.name

        # Check DB pairing evidence (both directions)
        evidence = self.db.query(IngredientPairingEvidence).filter(
            ((IngredientPairingEvidence.ingredient_a_name.ilike(name_a)) & (IngredientPairingEvidence.ingredient_b_name.ilike(name_b))) |
            ((IngredientPairingEvidence.ingredient_a_name.ilike(name_b)) & (IngredientPairingEvidence.ingredient_b_name.ilike(name_a)))
        ).first()

        if evidence:
            return PairwiseInteraction(
                ingredient_a=name_a,
                ingredient_b=name_b,
                affinity_score=evidence.affinity_score,
                reason=evidence.culinary_evidence or f"Curated pairing between {name_a} and {name_b}.",
                shared_compounds=evidence.shared_compounds or []
            )

        # Heuristic calculation if not explicitly curated
        fp_a = ing_a.flavor_profile
        fp_b = ing_b.flavor_profile

        shared_compounds = []
        if fp_a and fp_b and fp_a.dominant_compounds and fp_b.dominant_compounds:
            shared_compounds = list(set(fp_a.dominant_compounds).intersection(set(fp_b.dominant_compounds)))

        # Culinary balance heuristics:
        base_affinity = 70.0
        reason = ""
        conflict = None

        if shared_compounds:
            base_affinity += min(len(shared_compounds) * 8.0, 20.0)
            reason = f"Shared aroma volatile: {', '.join(shared_compounds[:3])} creates bridging harmony."

        if fp_a and fp_b:
            # Sweet + Acid harmony
            if (fp_a.sweet > 5.0 and fp_b.sour > 5.0) or (fp_a.sour > 5.0 and fp_b.sweet > 5.0):
                base_affinity += 8.0
                reason = reason or f"Classic sweet-acid balance between {name_a} and {name_b}."

            # Dairy + Acid curdling warning
            is_dairy_a = "Dairy" in (ing_a.allergens or []) or ing_a.category == "Dairy"
            is_dairy_b = "Dairy" in (ing_b.allergens or []) or ing_b.category == "Dairy"
            high_acid = (fp_a.sour > 7.0 or fp_b.sour > 7.0)

            if (is_dairy_a and fp_b.sour > 7.0) or (is_dairy_b and fp_a.sour > 7.0):
                if item_a.get("prep") in ["Cooked", "Boiled"] or item_b.get("prep") in ["Cooked", "Boiled"]:
                    conflict = f"Heat + High acid from {name_a if fp_a.sour > 7.0 else name_b} may curdle fresh dairy in {name_b if fp_a.sour > 7.0 else name_a}."
                    base_affinity -= 12.0

            # Umami + Salt / Savory synergy
            if fp_a.umami > 6.0 and fp_b.umami > 4.0:
                base_affinity += 6.0
                reason = reason or f"Glutamate-rich umami synergy between {name_a} and {name_b}."

        return PairwiseInteraction(
            ingredient_a=name_a,
            ingredient_b=name_b,
            affinity_score=round(min(max(base_affinity, 35.0), 98.0), 1),
            reason=reason or f"Compatible culinary combination between {name_a} and {name_b}.",
            shared_compounds=shared_compounds,
            conflict=conflict
        )

    def _compute_personalized_score(
        self,
        base_score: float,
        unique_items: List[Dict[str, Any]],
        ing_models: Dict[str, Ingredient],
        taste_profile: Dict[str, float],
        preference: UserPreference,
        conflicts: List[str]
    ) -> float:
        """Calculates personalized match score based on user profile and hard allergy exclusions."""
        score = base_score

        # HARD ALLERGY EXCLUSIONS:
        user_allergies = [a.lower() for a in (preference.allergies or [])]
        for item in unique_items:
            ing = ing_models[item["name"]]
            for allergen in (ing.allergens or []):
                if allergen.lower() in user_allergies:
                    conflicts.append(f"CRITICAL ALLERGY SAFETY WARNING: Ingredient '{ing.name}' violates allergy constraint ({allergen})!")
                    return 0.0  # Hard zero for allergy safety

        # Disliked ingredients penalty
        disliked = [d.lower() for d in (preference.disliked_ingredients or [])]
        for item in unique_items:
            if item["name"].lower() in disliked:
                score -= 22.0
                conflicts.append(f"Contains '{item['name']}' which is marked in your disliked preferences.")

        # Favorite ingredients bonus
        favorites = [f.lower() for f in (preference.favorite_ingredients or [])]
        for item in unique_items:
            if item["name"].lower() in favorites:
                score += 8.0

        # Spice tolerance comparison
        user_spice = preference.spice_tolerance or 3
        actual_spice = taste_profile.get("spicy", 0.0)
        expected_spice = (user_spice / 5.0) * 10.0
        spice_diff = abs(actual_spice - expected_spice)
        if actual_spice > expected_spice + 2.5:
            score -= 10.0
            conflicts.append(f"Spiciness ({actual_spice}/10) exceeds your preference tolerance level.")
        elif spice_diff < 1.5:
            score += 5.0

        return min(max(score, 10.0), 99.0)

    def _calculate_ratios(
        self,
        unique_items: List[Dict[str, Any]],
        ing_models: Dict[str, Ingredient],
        total_quantity: float
    ) -> List[RatioItem]:
        """Provides balanced culinary ratio recommendations based on ingredient intensity."""
        ratios = []
        for item in unique_items:
            name = item["name"]
            ing = ing_models[name]
            fp = ing.flavor_profile
            intensity = getattr(fp, "intensity", 5.0)

            # Recommend lower percentages for potent spices and high percentages for base produce/dairy
            if intensity >= 8.0:
                recommended_pct = "3% – 8%"
            elif intensity >= 6.5:
                recommended_pct = "10% – 20%"
            else:
                recommended_pct = "35% – 60%"

            ratios.append(RatioItem(
                ingredient=name,
                ratio=recommended_pct,
                recommended_grams=round(item["quantity"], 1)
            ))
        return ratios

    def _find_complementary(
        self,
        unique_items: List[Dict[str, Any]],
        taste_profile: Dict[str, float],
        ing_models: Dict[str, Ingredient]
    ) -> List[str]:
        """Suggests 2-4 complementary ingredients to balance missing taste vectors or enrich texture."""
        existing_names = set(x["name"].lower() for x in unique_items)
        suggestions = []

        # If low acidity
        if taste_profile["sour"] < 2.5 and "lime" not in existing_names and "lemon" not in existing_names:
            suggestions.append("Lime (for bright citrus acidity to elevate aromas)")

        # If high sweetness + dairy but lacking spice
        if taste_profile["sweet"] > 5.5 and taste_profile["spicy"] < 2.0:
            if "cardamom" not in existing_names:
                suggestions.append("Cardamom (cineole warmth to cut sugar richness)")
            elif "roasted cumin" not in existing_names:
                suggestions.append("Roasted Cumin (smoky pyrazines for earthy counterpoint)")

        # If creamy but lacking crunch
        if "pistachio" not in existing_names and "almonds" not in existing_names:
            suggestions.append("Pistachio (for delicate crunch and pine-floral finish)")

        if "mint" not in existing_names and taste_profile["sweet"] > 4.0:
            suggestions.append("Mint (cooling menthol contrast)")

        if not suggestions:
            suggestions = ["Black Pepper", "Olive Oil", "Saffron"]

        return suggestions[:4]

    def _assess_evidence_quality(
        self,
        unique_items: List[Dict[str, Any]],
        missing_ingredients: List[str],
        pairwise_matrix: List[PairwiseInteraction]
    ) -> Tuple[str, float]:
        """Calculates evidence quality rating and uncertainty percentage."""
        if missing_ingredients:
            return "Exploratory (User Ingredients)", 35.0

        curated_count = sum(1 for p in pairwise_matrix if "Curated" in p.reason or "Traditional" in p.reason or len(p.shared_compounds) > 0)
        total_pairs = len(pairwise_matrix) or 1
        ratio = curated_count / total_pairs

        if ratio >= 0.7:
            return "High (Food Chemistry & Culinary Evidence)", 12.0
        elif ratio >= 0.4:
            return "Moderate (Volatile Compound Heuristics)", 24.0
        else:
            return "Exploratory (Novel Pairing Hypothesis)", 38.0

    def _generate_title(self, items: List[Dict[str, Any]]) -> str:
        names = [x["name"] for x in items]
        if len(names) <= 3:
            return " & ".join(names) + " Infusion"
        return f"{names[0]} & {names[1]} Medley ({len(names)} Ingredients)"

    def _generate_explanation(
        self,
        items: List[Dict[str, Any]],
        compatibility: float,
        personalized: Optional[float],
        tastes: Dict[str, float],
        notes: List[str],
        conflicts: List[str]
    ) -> str:
        names = ", ".join(x["name"] for x in items)
        status = "exceptional" if compatibility >= 85 else "harmonious" if compatibility >= 70 else "intriguing"

        text = f"This combination of {names} demonstrates an {status} culinary profile (Compatibility: {round(compatibility)}%). "
        
        dominant_tastes = sorted(tastes.items(), key=lambda x: x[1], reverse=True)
        top_two = [f"{k} ({v}/10)" for k, v in dominant_tastes[:2] if v > 2.0]
        if top_two:
            text += f"The sensory palate is primarily driven by {' and '.join(top_two)}. "

        if notes:
            text += f"Key flavor synergy: {notes[0]} "

        if conflicts:
            text += f"Keep in mind: {conflicts[0]} "

        return text
