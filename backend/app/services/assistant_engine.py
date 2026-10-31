"""
FlavorFusion AI — Advanced Culinary AI Assistant Engine ("Chef Fusion AI")
Provides witty culinary intelligence, food chemistry science, emergency kitchen fixes,
flavor illusion explanations (e.g. Soy Sauce + Vanilla = Salted Caramel), ingredient substitutions,
and delivers interactive pairings ready to load into the Flavor Lab.
"""

from typing import List, Dict, Any, Optional
import re
from app.core.config import settings
from app.schemas.all_schemas import AssistantChatResponse, SuggestedPairingItem

KNOWLEDGE_CARDS = [
    # 1. Vanilla + Soy Sauce (Salted Caramel)
    {
        "keywords": ["vanilla", "soy sauce", "caramel", "toffee", "ice cream"],
        "reply": (
            "Bro, the Vanilla Ice Cream + Soy Sauce hack is literal culinary alchemy! 🤯🍨\n\n"
            "Here's the chemistry: when high-glutamate fermented soy sauce (umami + sodium) touches cold dairy fats and vanillin, "
            "your tongue's sodium channels physically suppress perceived bitterness while elevating perceived sweetness. "
            "Your brain is tricked into tasting rich, slow-simmered **Artisan Salted Caramel & Toasted Toffee**!\n\n"
            "Pro tip: 2 scoops of rich vanilla ice cream + 1/2 tsp of premium dark soy sauce + toasted sesame seeds = 10/10 viral banger."
        ),
        "pairings": [
            SuggestedPairingItem(
                title="Kyoto Salted Caramel Sundae",
                ingredients=["Vanilla", "Soy Sauce"],
                tastes_like="Rich Salted Caramel & Toasted Toffee",
                reason="Sodium suppresses bitterness while free glutamates amplify vanillin sweetness."
            )
        ],
        "vibe": "Unhinged Genius 🔥"
    },
    # 2. Too Salty Fix
    {
        "keywords": ["too salty", "oversalted", "salty food", "fix salt", "salty soup"],
        "reply": (
            "Don't panic! Food chemistry can save your dish from a salt disaster: 🧂✨\n\n"
            "1. **Acid & Fat Counterbalance**: Add a splash of fresh lemon juice, unseasoned rice vinegar, or cream/coconut milk. Acidity and fat distract the sodium receptors on your tongue.\n"
            "2. **Dilution with Starch**: Drop in peeled raw potato chunks while simmering (they absorb salty liquid) or add unsalted broth/water.\n"
            "3. **Sweetness Touch**: A tiny pinch of brown sugar or honey rounds out sharp sodium edges.\n"
            "Never toss the dish — balance is all about receptor competition!"
        ),
        "pairings": [
            SuggestedPairingItem(
                title="Balanced Umami Broth",
                ingredients=["Lime", "Curd", "Cumin"],
                tastes_like="Smooth Tangy Buffer",
                reason="Acids and lactic dairy effectively buffer intense salinity."
            )
        ],
        "vibe": "Kitchen Lifesaver 🛟"
    },
    # 3. Too Sour / Too Acidic Fix
    {
        "keywords": ["too sour", "too acidic", "sour sauce", "acidic tomato", "fix sour"],
        "reply": (
            "Over-acidic dish? Here is the molecular trick chefs use: 🍅🧪\n\n"
            "1. **Baking Soda Reaction (The Nuclear Option)**: Add just 1/8 tsp of baking soda. You'll see it fizz as sodium bicarbonate neutralizes citric and malic acids chemically!\n"
            "2. **Fat Buffer**: Stir in cold butter, heavy cream, mascarpone, or olive oil. Lipids coat the tongue and mute sour astringency.\n"
            "3. **Slow Caramelization**: Add caramelized onions or a touch of honey rather than raw granulated sugar."
        ),
        "pairings": [
            SuggestedPairingItem(
                title="Velvety Pomodoro Buffer",
                ingredients=["Tomato", "Olive Oil", "Garlic", "Basil"],
                tastes_like="Sweet Sun-Ripened Marinara",
                reason="Lipids in olive oil coat the tongue, buffering raw tomato malic acid."
            )
        ],
        "vibe": "Molecular Chemistry 🧪"
    },
    # 4. Too Spicy / Hot Fix
    {
        "keywords": ["too spicy", "too hot", "burning", "chili heat", "fix spicy", "spicy food"],
        "reply": (
            "Tongue on fire? Water will only spread the pain! Here's how capsaicin actually works: 🌶️🔥\n\n"
            "Capsaicin is a non-polar hydrophobic molecule that binds tightly to your TRPV1 pain receptors. To unbind it:\n"
            "1. **Dairy Casein**: Drink whole milk, eat curd/yogurt, or add sour cream. Casein acts like detergent to wash away capsaicin!\n"
            "2. **Fats & Oils**: Peanut butter, avocado, or sesame oil dissolve the oily capsaicin.\n"
            "3. **Sugar & Acid**: Fresh lime juice plus a dash of sugar blocks heat signaling to the brain."
        ),
        "pairings": [
            SuggestedPairingItem(
                title="Cooling Spiced Raita",
                ingredients=["Curd", "Mint", "Roasted Cumin"],
                tastes_like="Chilled Refreshing Lactic Cloud",
                reason="Casein proteins strip capsaicin from pain receptors while menthol cools."
            )
        ],
        "vibe": "Tongue Extinguisher 🚒"
    },
    # 5. Strawberry + Balsamic Vinegar
    {
        "keywords": ["strawberry", "strawberries", "balsamic", "vinegar"],
        "reply": (
            "Strawberries + Balsamic Vinegar is classic Italian gastronomy that blows minds! 🍓🍾\n\n"
            "Fresh strawberries are packed with furanones and ethyl esters. When paired with the acetic acid and wood-barrel tannins of aged balsamic, "
            "it breaks down the berry cell walls, intensifies their natural sweetness, and tricks your brain into tasting **Macerated Plum & Blackberry Jam**!\n"
            "Grind a touch of black pepper on top to activate piperine warmth."
        ),
        "pairings": [
            SuggestedPairingItem(
                title="Balsamic Macerated Strawberries",
                ingredients=["Strawberry", "Balsamic Vinegar", "Black Pepper"],
                tastes_like="Macerated Plum & Rich Blackberry Jam",
                reason="Acetic acid releases locked fruit esters, simulating slow-cooked preserves."
            )
        ],
        "vibe": "Artisan Slap 🤌"
    },
    # 6. Mango + Curd + Cardamom (Shrikhand)
    {
        "keywords": ["mango", "curd", "yogurt", "lassi", "shrikhand", "cardamom"],
        "reply": (
            "Ah, the royal Mughal and Gujarati masterpiece! 🥭✨\n\n"
            "Mango's tropical sweetness can feel cloying alone, but cultured curd provides lactic acid that tightens the finish. "
            "Add green cardamom (containing cineole and terpinyl acetate), and it instantly bridges into **Luxurious Kesariya Shrikhand** or a velvety cloud lassi! "
            "Top tier combo backed by centuries of culinary heritage."
        ),
        "pairings": [
            SuggestedPairingItem(
                title="Royal Kesariya Shrikhand",
                ingredients=["Mango", "Curd", "Cardamom", "Pistachio", "Honey"],
                tastes_like="Velvety Tropical Mousse with Cardamom Warmth",
                reason="Lactic acid cuts mango fructose while cardamom cineole bridges fruit volatiles."
            )
        ],
        "vibe": "Royal Heritage 👑"
    },
    # 7. Watermelon + Feta + Mint
    {
        "keywords": ["watermelon", "feta", "cheese", "mint"],
        "reply": (
            "Watermelon + Feta + Mint is the ultimate Mediterranean summer power move! 🍉🧀🌿\n\n"
            "Watermelon is 92% water with gentle citrulline sweetness. Sheep's milk feta brings intense brine and rich lipids, "
            "creating an immediate sweet-salty hyper-contrast. Fresh mint leaves bring menthol, cooling the palate between each bite."
        ),
        "pairings": [
            SuggestedPairingItem(
                title="Mediterranean Watermelon Carpaccio",
                ingredients=["Watermelon", "Feta", "Mint", "Lime", "Black Pepper"],
                tastes_like="Crisp Saline Mediterranean Summer Cloud",
                reason="Briny sheep curds contrast cellular fruit hydration with crisp menthol aromatics."
            )
        ],
        "vibe": "Summer Aesthetic ☀️"
    },
    # 8. Dark Chocolate + Chili + Olive Oil
    {
        "keywords": ["chocolate", "dark chocolate", "cocoa", "chili", "chilli"],
        "reply": (
            "The ancient Aztec chocolate secret! 🍫🌶️\n\n"
            "Cacao contains theobromine and bitter polyphenols. Capsaicin from chili stimulates mild irritation, which causes your brain to release "
            "endorphins and dopamine. When emulsified with fruity extra virgin olive oil and flaky sea salt, the fats mute harsh bitterness and yield **Molten Aztec Ganache**!"
        ),
        "pairings": [
            SuggestedPairingItem(
                title="Aztec Spiced Ganache",
                ingredients=["Dark Chocolate", "Chili Pepper", "Olive Oil"],
                tastes_like="Smoky Molten Ganache with Lingering Warmth",
                reason="Capsaicin triggers endorphins while oil lipids coat polyphenols."
            )
        ],
        "vibe": "Dopamine Bomb ⚡"
    },
    # 9. Substitutions
    {
        "keywords": ["substitute", "substitution", "replace", "alternative"],
        "reply": (
            "Need a smart ingredient swap? Here are the gold-standard culinary substitutions: 🔄🍳\n\n"
            "• **1 Egg in Baking**: 1/4 cup applesauce, 1/2 mashed ripe banana, or 1 tbsp ground flaxseed + 3 tbsp water.\n"
            "• **Buttermilk**: 1 cup milk + 1 tbsp lemon juice or white vinegar (let sit 5 mins).\n"
            "• **Heavy Cream**: Full-fat coconut cream OR milk + melted butter (3:1 ratio).\n"
            "• **White Wine in Cooking**: Chicken/vegetable broth + a squeeze of fresh lemon juice.\n"
            "• **Soy Sauce (Gluten-Free)**: Tamari or Coconut Aminos."
        ),
        "pairings": [
            SuggestedPairingItem(
                title="Universal Pantry Swap",
                ingredients=["Lime", "Honey", "Olive Oil"],
                tastes_like="Bright Balanced Emulsion",
                reason="Clean simple emulsification adaptable to any cuisine."
            )
        ],
        "vibe": "Pantry Wizard 🧙‍♂️"
    },
    # 10. Midnight Snack / Quick Craving
    {
        "keywords": ["midnight", "snack", "hungry", "quick", "craving", "late night", "fast food"],
        "reply": (
            "Say less! Late-night cravings demand maximum umami with zero cleanup. 🌙✨\n\n"
            "Top 3 rapid hacks:\n"
            "1. **Midnight Citrus Guacamole**: Mashed avocado + squeeze of lime + roasted cumin + sea salt on toast. Ready in 2 minutes.\n"
            "2. **Honey Cardamom Yogurt Cloud**: Thick Greek curd + drizzle of honey + cracked cardamom + crushed pistachios.\n"
            "3. **The 5-Min Toffee Trick**: Vanilla ice cream + drizzle of soy sauce + pinch of toasted sesame."
        ),
        "pairings": [
            SuggestedPairingItem(
                title="Midnight Citrus Guac Toast",
                ingredients=["Avocado", "Lime", "Roasted Cumin", "Chili Pepper"],
                tastes_like="Creamy Zesty Guacamole",
                reason="High healthy oleic fats balanced by bright citric acid."
            )
        ],
        "vibe": "Midnight Savior 🌙"
    },
    # 11. Maillard Reaction & Searing Science
    {
        "keywords": ["maillard", "sear", "searing", "caramelization", "browning", "crust"],
        "reply": (
            "The Maillard reaction is the single greatest chemical phenomenon in cooking! 🥩🍳\n\n"
            "Occurring above 285°F (140°C), reducing sugars react with amino acids to produce hundreds of new flavor compounds called **pyrazines, furanones, and thiophenes**. "
            "That's why roasted cumin tastes smoky, seared steak tastes savory, and toasted bread smells irresistible! "
            "Always pat your ingredients completely dry before searing so surface moisture doesn't boil instead of brown."
        ),
        "pairings": [
            SuggestedPairingItem(
                title="High-Maillard Roasted Aromatics",
                ingredients=["Garlic", "Roasted Cumin", "Black Pepper", "Olive Oil"],
                tastes_like="Deep Roasted Nutty Umami",
                reason="Pyrazine creation via dry-heat amino acid reduction."
            )
        ],
        "vibe": "Pure Science 🧬"
    },
    # 12. Salmon & Seafood Pairings
    {
        "keywords": ["salmon", "fish", "seafood", "shrimp", "tuna"],
        "reply": (
            "Seafood chemistry is all about balancing rich omega-3 lipids and delicate protein structures! 🐟🍋\n\n"
            "1. **Citrus & Acid**: Lemon, lime, or capers neutralize fishy trimethylamine (TMA) and cut through rich fatty salmon.\n"
            "2. **Herbal Monoterpenes**: Dill, basil, and parsley bring refreshing carvone and apiol notes that lighten the bite.\n"
            "3. **Umami Glazes**: Miso, soy, and honey create a glossy caramel crust under heat."
        ),
        "pairings": [
            SuggestedPairingItem(
                title="Citrus Dill Salmon Glaze",
                ingredients=["Lime", "Honey", "Olive Oil", "Black Pepper"],
                tastes_like="Zesty Honey-Glazed Marine Perfection",
                reason="Citric acid cuts fish lipids while honey creates glossy pan glaze."
            )
        ],
        "vibe": "Chef's Catch 🌊"
    },
    # 13. Chicken & Poultry Pairings
    {
        "keywords": ["chicken", "poultry", "turkey"],
        "reply": (
            "Chicken is the ultimate blank culinary canvas! 🍗🌿\n\n"
            "Because chicken meat is rich in inosine monophosphate (an umami synergist), pairing it with glutamates (garlic, tomato, parmesan, mushrooms) "
            "multiplies the perceived savoriness by up to **8 times**! Brighten with rosemary, lemon, and a cracked black pepper crust."
        ),
        "pairings": [
            SuggestedPairingItem(
                title="Tuscan Garlic Lemon Medley",
                ingredients=["Garlic", "Lime", "Olive Oil", "Black Pepper"],
                tastes_like="Sun-Kissed Rustic Umami",
                reason="Nucleotide-glutamate synergy amplifies savory chicken perception."
            )
        ],
        "vibe": "Dinner Winner 🏆"
    },
    # 14. Coffee Pairings & Science
    {
        "keywords": ["coffee", "espresso", "latte", "caffeine"],
        "reply": (
            "Coffee isn't just a drink — it's a sensory powerhouse! ☕✨\n\n"
            "1. **Cardamom Coffee (Middle Eastern Classic)**: Cardamom's eucalyptus-like cineole cuts dark roast bitterness while adding cooling floral aromatics.\n"
            "2. **Dark Chocolate Mocha**: Shared pyrazines and diketopiperazines build deep roasted dessert notes.\n"
            "3. **Orange & Espresso (Espresso Romano)**: Citric acid balances natural coffee acidity and lifts heavy crema."
        ),
        "pairings": [
            SuggestedPairingItem(
                title="Cardamom Spiced Espresso Fusion",
                ingredients=["Cardamom", "Vanilla", "Dark Chocolate"],
                tastes_like="Velvet Spiced Mocha",
                reason="Shared pyrazines and terpinyl acetate round out roasted coffee bitterness."
            )
        ],
        "vibe": "Barista Alchemy ☕"
    },
    # 15. Green Apple Pairings
    {
        "keywords": ["green apple", "granny smith", "tart apple"],
        "reply": (
            "Green apples (Granny Smith) are a food scientist's dream! 🍏✨\n\n"
            "Unlike sweet red apples, green apples are loaded with **malic acid** and fresh green hexanal volatiles. "
            "That razor-sharp malic acid cuts right through rich dairy fats and cured meats!\n\n"
            "Elite pairings:\n"
            "• **Sharp Cheddar or Brie**: The classic Anglo-French bistro pairing — creamy fat + tart crunch.\n"
            "• **Pork & Bacon**: High acid cuts through unctuous pork belly lipids.\n"
            "• **Walnuts & Celery (Waldorf)**: Tannic nut skins softened by crisp juicy fruit."
        ),
        "pairings": [
            SuggestedPairingItem(
                title="Green Apple & Aged Cheddar Tartlet",
                ingredients=["Green Apple", "Cheddar", "Honey", "Walnuts"],
                tastes_like="Artisan Orchard Crunch & Toffee",
                reason="Malic acid cuts sharp cheddar dairy fats while honey rounds the finish."
            )
        ],
        "vibe": "Orchard Chemistry 🍏"
    },
    # 16. Salt Science
    {
        "keywords": ["salt", "sea salt", "flaky salt", "why salt", "salt science"],
        "reply": (
            "Salt (NaCl) isn't just a seasoning — it's the master controller of human taste perception! 🧂🔬\n\n"
            "1. **Bitterness Suppression**: Sodium ions physically bind to human bitter taste receptors on the tongue, turning down bitter signals to the brain.\n"
            "2. **Sweetness & Umami Amplification**: By suppressing bitterness, natural sweetness and savoriness shine twice as bright. That's why salted caramel, salted dark chocolate, and salted watermelon taste godly!\n"
            "3. **Volatile Aroma Release**: Salt reduces water activity, forcing aromatic organic flavor compounds into vapor phase so you smell and taste food faster."
        ),
        "pairings": [
            SuggestedPairingItem(
                title="Salted Dark Cacao Alchemy",
                ingredients=["Salt", "Dark Chocolate", "Vanilla"],
                tastes_like="Gourmet Salted Fudge Truffle",
                reason="Sodium ions block bitter receptors to unveil pure cacao sweetness."
            )
        ],
        "vibe": "Master Flavor Enhancer 🧂"
    },
    # 17. South Indian Tadka & Tempering Science
    {
        "keywords": ["tadka", "tempering", "curry leaves", "mustard seeds", "hing", "asafoetida", "south indian"],
        "reply": (
            "Tadka (or *Thalithal* in Tamil, *Popu* in Telugu) is masterclass fat-soluble extraction! 🍃🥥\n\n"
            "1. **Mustard Seed Physics**: When black mustard seeds crackle in hot oil (~180°C), thermal shock breaks their hulls, releasing sinigrin and enzymatically converting it to pungent, nutty **allyl isothiocyanate**.\n"
            "2. **Curry Leaf Terpenes**: Fresh curry leaves contain volatile beta-caryophyllene, alpha-pinene, and linalool. These aroma compounds are hydrophobic (oil-soluble); plunging them into hot ghee or coconut oil binds these terpenes directly into the cooking fat, perfuming the entire dish!\n"
            "3. **Asafoetida (Hing) Magic**: Raw hing smells sulfurous and sharp, but cooking it in fat instantly unlocks pleasant roasted-garlic and leek umami notes from ferulic acid."
        ),
        "pairings": [
            SuggestedPairingItem(
                title="Grandmother's Royal Tadka",
                ingredients=["Curry Leaves", "Mustard Seeds", "Asafoetida", "Ghee"],
                tastes_like="Nutty Crackling Aromatic Emulsion",
                reason="Hot fat extracts volatile terpenes and blooms sinigrin into savory nuttiness."
            )
        ],
        "vibe": "Tadka Virtuoso 🍃"
    },
    # 18. North Indian Bhunao & Makhani Science
    {
        "keywords": ["bhunao", "makhani", "paneer butter masala", "shahi paneer", "butter chicken", "kasuri methi", "north indian"],
        "reply": (
            "The magic of North Indian gravies lies in the ancient technique of **Bhunao** and the secret compound **Sotolon**! 🍛👑\n\n"
            "• **The Bhunao Process**: Sautéing onion-ginger-garlic paste and tomatoes on low heat until water fully evaporates and free oil separates. This triggers non-enzymatic caramelization and high Maillard reactions without scorching.\n"
            "• **Kasuri Methi (The Restaurant Secret)**: Dried fenugreek leaves contain an extraordinarily potent lactone called **sotolon**. Even in parts-per-billion concentrations, sotolon imparts a rich maple-sweet, warm herbal finish that separates roadside dhabas and 5-star hotels from ordinary curries!"
        ),
        "pairings": [
            SuggestedPairingItem(
                title="Imperial Shahi Makhani Foundation",
                ingredients=["Tomato", "Paneer", "Butter", "Kasuri Methi", "Garam Masala"],
                tastes_like="Silky Sweet-Savory Royal Tomato Velvet",
                reason="Bhunao caramelization meets sotolon fenugreek lactones."
            )
        ],
        "vibe": "Mughlai Royalty 👑"
    },
    # 19. South Indian Fermentation Science (Dosa & Idli)
    {
        "keywords": ["dosa", "idli", "batter", "fermentation", "urad dal", "crispy dosa", "ghee roast"],
        "reply": (
            "Dosa and Idli batter is one of the world's most sophisticated wild lactic acid fermentations! 🥞🔬\n\n"
            "• **Microbial Alchemy**: Wild microorganisms (*Leuconostoc mesenteroides* and *Lactobacillus fermentum*) naturally present on urad dal skins ferment starches into lactic acid (giving signature tang) and carbon dioxide (aerating the batter into a fluffy sponge).\n"
            "• **Surface Maillard Crisp**: When ladlefuls of fermented batter hit a smoking cast-iron tawa with ghee, the acidic sugars undergo instantaneous Maillard reactions, creating the wafer-thin, golden-brown lattice characteristic of a crispy Ghee Roast Dosa!"
        ),
        "pairings": [
            SuggestedPairingItem(
                title="Crispy Ghee Roast Duo",
                ingredients=["Idli Dosa Batter", "Ghee", "Curry Leaves", "Mustard Seeds"],
                tastes_like="Shatteringly Crisp Golden Tang with Ghee Diacetyl",
                reason="Lactic acid tang crisped with clarified butterfat Maillard browning."
            )
        ],
        "vibe": "Fermentation Gold 🥞"
    },
    # 20. Rasam & Sambar Chemistry
    {
        "keywords": ["rasam", "sambar", "toor dal", "milagu", "drumstick"],
        "reply": (
            "Rasam and Sambar are centuries-old Ayurvedic digestive wonders engineered through taste balance! 🥣🌿\n\n"
            "• **Tartaric Acid from Tamarind**: Tamarind pulp brings sharp tartaric acid that cuts through heavy lentil starches and tenderizes fibrous vegetables like drumstick.\n"
            "• **Piperine & Cumin Thermogenesis**: In Chettinad Pepper Rasam (*Milagu Rasam*), piperine from black pepper and cuminaldehyde stimulate salivary and gastric enzymes, warming the body and soothing colds instantly."
        ),
        "pairings": [
            SuggestedPairingItem(
                title="Chettinad Healing Rasam",
                ingredients=["Black Pepper", "Garlic", "Cumin Seeds", "Curry Leaves", "Ghee"],
                tastes_like="Fiery Citrus-Pepper Warming Nectar",
                reason="Piperine and allicin stimulate thermogenesis and awaken taste receptors."
            )
        ],
        "vibe": "Ayurvedic Elixir 🥣"
    },
    # 21. Indian Street Chaat 5-Point Balance
    {
        "keywords": ["chaat", "amchur", "chaat masala", "kala namak", "black salt", "guava chaat", "papdi"],
        "reply": (
            "Indian Chaat is the ultimate sensory explosion because it hits all 5 human taste receptors at maximum intensity! 💥🍈\n\n"
            "1. **Sour**: Amchur (sun-dried raw mango) & tamarind citric/tartaric acids.\n"
            "2. **Sweet**: Jaggery or sweet fruit esters (like fresh pink guava or ripe mango).\n"
            "3. **Spicy**: Green chili capsaicin and black pepper piperine.\n"
            "4. **Salty**: Mineral table salt.\n"
            "5. **Sulfurous Umami**: **Kala Namak** (Himalayan black salt) contains sodium sulfide and iron minerals that create a savory egg-like, gamey umami kick that makes street chaat downright addictive!"
        ),
        "pairings": [
            SuggestedPairingItem(
                title="Street-Style Spiced Guava Chaat",
                ingredients=["Guava", "Chaat Masala", "Lime", "Chili Pepper"],
                tastes_like="Electric Sweet-Tart-Spicy Crunch",
                reason="5-point taste axis: fruit fructose balanced by amchur acid and black salt sulfur."
            )
        ],
        "vibe": "Street Food Explosion 💥"
    }
]

class AssistantEngine:
    def __init__(self):
        self.api_key = settings.GEMINI_API_KEY

    def chat(self, message: str, current_ingredients: Optional[List[str]] = None) -> AssistantChatResponse:
        cleaned = message.lower().strip()
        ing_list = current_ingredients or []

        # 1. Try Gemini API if key is configured
        if self.api_key:
            try:
                return self._chat_with_gemini(message, ing_list)
            except Exception as e:
                print(f"Gemini Assistant fallback: {e}")

        # 2. Match against extensive knowledge cards
        for card in KNOWLEDGE_CARDS:
            if any(k in cleaned for k in card["keywords"]):
                return AssistantChatResponse(
                    reply=card["reply"],
                    suggested_pairings=card["pairings"],
                    vibe=card.get("vibe", "Culinary Bestie 🔥")
                )

        # 3. Dynamic ingredient queries (e.g. "What can I make with green apple and cheddar?" or "I have avocado and tomato")
        common_ingredients = [
            # Fruits & Vegetables
            "green apple", "apple", "papaya", "guava", "lychee", "jackfruit", "custard apple",
            "fig", "pineapple", "banana", "orange", "kiwi", "grapes", "dragonfruit",
            "watermelon", "blueberry", "raspberry", "peach", "strawberry", "mango", "lemon", "lime",
            "okra", "bhindi", "bitter gourd", "karela", "bottle gourd", "lauki", "ridge gourd", "turai",
            "brinjal", "eggplant", "drumstick", "spinach", "palak", "fresh methi", "fenugreek",
            "cauliflower", "gobi", "green peas", "matar", "carrot", "gajar", "radish", "mooli",
            "beetroot", "capsicum", "bell pepper", "cabbage", "pumpkin", "potato", "sweet potato",
            "zucchini", "asparagus", "broccoli", "corn", "shallot", "scallions", "onion", "garlic", "ginger",
            # South & North Indian Staples
            "curry leaves", "mustard seeds", "asafoetida", "hing", "urad dal", "chana dal", "toor dal",
            "fenugreek seeds", "sambar powder", "rasam powder", "idli dosa batter", "coconut", "coconut oil",
            "kasuri methi", "garam masala", "amchur", "cumin seeds", "cumin", "black cardamom", "cardamom",
            "cloves", "mustard oil", "chaat masala", "rajma", "kashmiri red chili", "fennel seeds", "bay leaf",
            "paneer", "ghee", "curd", "yogurt", "tamarind", "black pepper", "coriander seeds",
            # Western / Global Basics
            "salt", "sea salt", "black salt", "cheddar", "butter", "parmesan", "mozzarella",
            "egg", "salmon", "shrimp", "bacon", "chicken", "beef", "pork",
            "rosemary", "thyme", "oregano", "basil", "dill", "cilantro", "mint",
            "maple syrup", "honey", "miso", "tahini", "walnuts", "pistachio", "peanuts",
            "dark chocolate", "vanilla", "soy sauce", "balsamic vinegar", "olive oil", "pasta"
        ]
        detected = [ing for ing in common_ingredients if ing in cleaned]

        if detected:
            names_title = [d.title() for d in detected]
            return AssistantChatResponse(
                reply=(
                    f"Chef's intuition tingling! 🧑‍🍳 With **{', '.join(names_title)}**, you've got the foundation of an incredible dish!\n\n"
                    f"To make it shine: balance the primary taste profile (sweetness vs acidity), add a toasted aromatic for depth, "
                    f"and finish with a texture contrast (like flaky salt, toasted seeds, or fresh herbs). "
                    f"Check out the formula below — you can load it directly into your Flavor Lab with 1 click!"
                ),
                suggested_pairings=[
                    SuggestedPairingItem(
                        title=f"{names_title[0]} Gourmet Synergy",
                        ingredients=names_title[:4],
                        tastes_like="Multi-Layered Harmonic Dish",
                        reason=f"Derived from your query for {', '.join(names_title)}."
                    )
                ],
                vibe="Chef Formulation 🧪"
            )

        # 4. Context-aware if user already has ingredients loaded in Flavor Lab
        if ing_list:
            ings_text = ", ".join(ing_list)
            return AssistantChatResponse(
                reply=(
                    f"Looking at your active Flavor Lab workspace ({ings_text}), you have a super vibrant formula! 🧪✨\n\n"
                    f"To elevate this combination:\n"
                    f"• **Acid-Base Balance**: If it's tasting rich, add a dash of citrus (Lime or Balsamic) to cut through heavy fats.\n"
                    f"• **Aromatic Bridges**: Add an aromatic like Cardamom, Basil, or Cumin to bridge volatile scent compounds.\n"
                    f"• **Umami Depth**: A tiny pinch of flaky sea salt will suppress any lingering bitterness."
                ),
                suggested_pairings=[
                    SuggestedPairingItem(
                        title=f"{ing_list[0]} Workspace Fusion",
                        ingredients=ing_list[:4],
                        tastes_like="Complex Gastronomic Alchemy",
                        reason="Optimized formulation from your active Flavor Lab."
                    )
                ],
                vibe="Flavor Alchemist ✨"
            )

        # 5. General intelligent culinary reply
        return AssistantChatResponse(
            reply=(
                f"Hey foodie! 👋 I'm **Chef Fusion AI**, your culinary chemistry bestie.\n\n"
                f"You can ask me anything about food science:\n"
                f"• *'Why does vanilla ice cream and soy sauce taste like caramel?'* 🍨\n"
                f"• *'How do I fix a dish that's too salty or too sour?'* 🧂\n"
                f"• *'What can I substitute for buttermilk or eggs?'* 🔄\n"
                f"• *'What pairs best with salmon, dark chocolate, or avocado?'* 🥑\n\n"
                f"What flavor mystery are you trying to crack today?"
            ),
            suggested_pairings=[
                SuggestedPairingItem(
                    title="The Salted Caramel Hack",
                    ingredients=["Vanilla", "Soy Sauce"],
                    tastes_like="Rich Salted Caramel & Toasted Toffee",
                    reason="Try the viral sweet-savory sensory illusion!"
                ),
                SuggestedPairingItem(
                    title="Royal Shrikhand Ambrosia",
                    ingredients=["Mango", "Curd", "Cardamom"],
                    tastes_like="Velvety Mango Mousse",
                    reason="Iconic Indian dessert synergy."
                )
            ],
            vibe="Culinary Bestie 🔥"
        )

    def _chat_with_gemini(self, message: str, current_ingredients: List[str]) -> AssistantChatResponse:
        import httpx
        import json

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={self.api_key}"
        system_prompt = (
            "You are Chef Fusion AI, an ultra-fun, knowledgeable expert in culinary chemistry. "
            "Explain flavor science, emergency cooking fixes (oversalted, too acidic, too spicy), substitutions, "
            "weird flavor illusions (e.g. vanilla ice cream + soy sauce = salted caramel), and suggest dishes. "
            "Keep responses concise, exciting, scientific, and use emojis. "
            "Respond in strictly valid JSON with keys: reply (string), vibe (string, e.g. 'Certified Banger 🔥'), "
            "suggested_pairings (array of objects with title, ingredients, tastes_like, reason)."
        )

        user_content = f"User asks: {message}. Current lab ingredients: {', '.join(current_ingredients) if current_ingredients else 'None'}."
        payload = {
            "contents": [
                {"role": "user", "parts": [{"text": system_prompt + "\n" + user_content}]}
            ]
        }
        res = httpx.post(url, json=payload, timeout=10.0)
        res.raise_for_status()
        data = res.json()
        raw = data["candidates"][0]["content"]["parts"][0]["text"].strip()
        if raw.startswith("```"):
            raw = raw.split("\n", 1)[1].rsplit("```", 1)[0].strip()
        parsed = json.loads(raw)

        pairings = [
            SuggestedPairingItem(
                title=p.get("title", "Chef's Pairing"),
                ingredients=p.get("ingredients", []),
                tastes_like=p.get("tastes_like", "Gourmet Symphony"),
                reason=p.get("reason", "")
            )
            for p in parsed.get("suggested_pairings", [])
        ]

        return AssistantChatResponse(
            reply=parsed.get("reply", "That sounds delicious!"),
            suggested_pairings=pairings,
            vibe=parsed.get("vibe", "Chef's Kiss ✨")
        )
