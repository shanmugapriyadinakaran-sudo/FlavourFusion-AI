"""
Curated Recipe Catalog for FlavorFusion AI.
Provides a comprehensive library of iconic global recipes with required ingredients,
tools, vessels, and step-by-step preparation instructions.
"""

from typing import List, Dict, Any

CURATED_RECIPE_CATALOG: List[Dict[str, Any]] = [
    {
        "id": 101,
        "title": "Artisan Neapolitan Pizza Margherita",
        "summary": "Crisp blistered fermented crust topped with sweet San Marzano tomato sauce, melted fresh mozzarella, and aromatic torn basil.",
        "cuisine": "Italian",
        "meal_type": "Dinner",
        "prep_time_mins": 20,
        "cook_time_mins": 10,
        "servings": 2,
        "difficulty": "Medium",
        "ingredients_list": [
            {"name": "Pizza Dough", "quantity": 1.0, "unit": "piece", "notes": "Room temperature fermented dough ball"},
            {"name": "San Marzano Tomatoes", "quantity": 150.0, "unit": "g", "notes": "Hand-crushed with sea salt"},
            {"name": "Mozzarella", "quantity": 120.0, "unit": "g", "notes": "Torn fresh mozzarella balls, drained"},
            {"name": "Basil", "quantity": 8.0, "unit": "leaves", "notes": "Fresh Italian sweet basil"},
            {"name": "Olive Oil", "quantity": 1.5, "unit": "tbsp", "notes": "Extra virgin cold pressed"}
        ],
        "required_tools": ["Pizza Peel / Flat Baking Tray", "Pastry Brush", "Chef's Knife & Cutting Board", "Bench Scraper"],
        "required_vessels": ["Heavy Pizza Stone or Cast Iron Baking Steel", "Medium Mixing Bowl"],
        "steps": [
            "Preheat oven with pizza stone to maximum heat (250°C / 500°F) for at least 45 minutes.",
            "Gently stretch room-temperature pizza dough onto a floured surface from center outward, preserving an airy outer rim (cornicione).",
            "Ladle crushed San Marzano tomatoes in concentric circles over the base, leaving a 1/2-inch border.",
            "Scatter torn fresh mozzarella evenly across the sauce and drizzle with cold-pressed olive oil.",
            "Slide pizza onto blazing hot pizza stone. Bake for 7 to 9 minutes until the cheese bubbles and the crust develops charred leopard spots.",
            "Remove, immediately crown with freshly plucked sweet basil leaves, slice with pizza wheel, and serve piping hot."
        ],
        "allergens": ["Gluten", "Dairy"],
        "substitutions": ["Use Buffalo Mozzarella or vegan cashew mozzarella.", "Substitute ready puff pastry in a pinch."],
        "needed_ingredients": [
            {"name": "Extra Virgin Olive Oil", "amount": "1.5 tbsp", "purpose": "Drizzle over crust"},
            {"name": "Flaky Sea Salt", "amount": "1 pinch", "purpose": "Season tomatoes"}
        ],
        "generation_mode": "Master Chef Curated"
    },
    {
        "id": 102,
        "title": "Classic Roman Spaghetti Carbonara",
        "summary": "Silky emulsified pasta coated in rich egg yolks, toasted black pepper, and salty, crisp cured pork jowl without any cream.",
        "cuisine": "Italian",
        "meal_type": "Dinner",
        "prep_time_mins": 10,
        "cook_time_mins": 15,
        "servings": 2,
        "difficulty": "Medium",
        "ingredients_list": [
            {"name": "Spaghetti", "quantity": 200.0, "unit": "g", "notes": "Bronze-die extruded spaghetti"},
            {"name": "Pancetta", "quantity": 100.0, "unit": "g", "notes": "Diced into 1/4-inch lardons (or Guanciale)"},
            {"name": "Egg", "quantity": 3.0, "unit": "piece", "notes": "2 whole eggs + 1 yolk, room temperature"},
            {"name": "Pecorino Romano", "quantity": 50.0, "unit": "g", "notes": "Finely microplaned"},
            {"name": "Black Pepper", "quantity": 1.0, "unit": "tbsp", "notes": "Freshly cracked whole peppercorns"}
        ],
        "required_tools": ["Tongs", "Microplane / Fine Cheese Grater", "Whisk", "Chef's Knife"],
        "required_vessels": ["Large Pasta Stockpot", "12-inch Heavy Skillet", "Medium Ceramic Mixing Bowl"],
        "steps": [
            "Bring 4 liters of water to a rolling boil in stockpot; salt generously with coarse sea salt.",
            "In ceramic bowl, vigorously whisk eggs, egg yolk, and grated Pecorino Romano until a thick, uniform paste forms.",
            "In skillet over medium heat, render diced pancetta until golden and crisp around edges (about 6 minutes). Remove skillet from direct heat.",
            "Boil spaghetti until 2 minutes shy of al dente. Using tongs, transfer spaghetti directly into skillet with rendered fat.",
            "Ladle 1/3 cup starchy pasta water into skillet. Stir rapidly over very low residual heat to create an initial emulsified gloss.",
            "Pour egg and pecorino mixture over warm pasta, tossing continuously off direct heat so the residual heat cooks the eggs into a creamy sauce without curdling.",
            "Finish with generous freshly cracked black pepper and extra Pecorino Romano."
        ],
        "allergens": ["Gluten", "Dairy", "Eggs"],
        "substitutions": ["Use smoked bacon if pancetta is unavailable.", "Parmigiano Reggiano can replace Pecorino."],
        "needed_ingredients": [
            {"name": "Sea Salt", "amount": "2 tbsp", "purpose": "Salting pasta water"},
            {"name": "Starchy Pasta Cooking Water", "amount": "1/2 cup", "purpose": "Emulsifying sauce"}
        ],
        "generation_mode": "Master Chef Curated"
    },
    {
        "id": 103,
        "title": "Authentic Szechuan Kung Pao Chicken",
        "summary": "Tender velveted chicken cubes stir-fried with fragrant Szechuan peppercorns, roasted peanuts, scallions, and glossy sweet-sour-spicy sauce.",
        "cuisine": "Chinese",
        "meal_type": "Dinner",
        "prep_time_mins": 15,
        "cook_time_mins": 10,
        "servings": 3,
        "difficulty": "Medium",
        "ingredients_list": [
            {"name": "Chicken", "quantity": 350.0, "unit": "g", "notes": "Skinless boneless chicken thighs cut into 3/4-inch cubes"},
            {"name": "Szechuan Peppercorns", "quantity": 1.0, "unit": "tsp", "notes": "Lightly crushed to release citrus aroma"},
            {"name": "Chili Pepper", "quantity": 8.0, "unit": "piece", "notes": "Whole dried red chilies, deseeded"},
            {"name": "Peanuts", "quantity": 50.0, "unit": "g", "notes": "Roasted unsalted peanuts"},
            {"name": "Scallion", "quantity": 3.0, "unit": "piece", "notes": "Cut into 1-inch white and green batons"},
            {"name": "Garlic", "quantity": 3.0, "unit": "cloves", "notes": "Thinly sliced"},
            {"name": "Ginger", "quantity": 1.0, "unit": "tbsp", "notes": "Minced fresh ginger"},
            {"name": "Soy Sauce", "quantity": 2.0, "unit": "tbsp", "notes": "Divided between marinade and sauce"},
            {"name": "Shaoxing Wine", "quantity": 1.0, "unit": "tbsp", "notes": "Chinese cooking wine"},
            {"name": "Cornstarch", "quantity": 1.5, "unit": "tsp", "notes": "For velveting chicken"}
        ],
        "required_tools": ["Carbon Steel Wok or 12-inch High-Wall Skillet", "Wok Spatula / Chuan", "Chef's Knife & Cutting Board", "Small Prep Bowls"],
        "required_vessels": ["Carbon Steel Wok", "Small Sauce Bowl", "Prep Plates"],
        "steps": [
            "Toss chicken cubes with 1 tbsp soy sauce, Shaoxing wine, and cornstarch. Marinate for 15 minutes.",
            "Whisk sauce in a small bowl: 1 tbsp soy sauce, 1 tbsp Chinese black vinegar, 1 tsp sugar, and 1/2 tsp cornstarch dissolved in 2 tbsp water.",
            "Heat wok over high flame until smoking; swirl in 2 tbsp high-smoke oil.",
            "Add dried red chilies and Szechuan peppercorns; stir-fry for 20 seconds until dark red and fragrant (do not burn).",
            "Tumble in marinated chicken; spread across wok walls and sear undisturbed for 90 seconds, then toss until cooked through.",
            "Add sliced garlic, ginger, and scallion whites. Stir-fry for 30 seconds.",
            "Pour in prepared sauce; toss vigorously as it bubbles and coats every chicken cube in a glossy glaze.",
            "Turn off heat, fold in roasted peanuts and green scallion batons, and serve immediately with steamed Jasmine rice."
        ],
        "allergens": ["Soy", "Peanuts", "Gluten"],
        "substitutions": ["Firm tofu cubes or shrimp can replace chicken.", "Cashews can substitute peanuts."],
        "needed_ingredients": [
            {"name": "Cooking Oil", "amount": "2 tbsp", "purpose": "High-heat stir fry"},
            {"name": "Brown Sugar", "amount": "1 tsp", "purpose": "Sauce balance"}
        ],
        "generation_mode": "Master Chef Curated"
    },
    {
        "id": 104,
        "title": "Authentic Seafood & Saffron Paella Valenciana",
        "summary": "Golden Bomba rice infused with Spanish saffron threads, sweet paprika, tender shrimp, and rich shellfish broth with a crispy socarrat crust.",
        "cuisine": "Spanish",
        "meal_type": "Dinner",
        "prep_time_mins": 20,
        "cook_time_mins": 30,
        "servings": 4,
        "difficulty": "Advanced",
        "ingredients_list": [
            {"name": "Bomba Paella Rice", "quantity": 300.0, "unit": "g", "notes": "Spanish short-grain absorption rice"},
            {"name": "Spanish Saffron", "quantity": 1.0, "unit": "pinch", "notes": "Steeped in 2 tbsp warm broth"},
            {"name": "Shrimp", "quantity": 250.0, "unit": "g", "notes": "Jumbo peeled and deveined with tails on"},
            {"name": "Smoked Paprika", "quantity": 1.5, "unit": "tsp", "notes": "Pimentón de la Vera"},
            {"name": "Spanish Chorizo", "quantity": 80.0, "unit": "g", "notes": "Sliced into rounds"},
            {"name": "Tomato", "quantity": 2.0, "unit": "piece", "notes": "Grated fresh tomato pulp (sofrito)"},
            {"name": "Garlic", "quantity": 4.0, "unit": "cloves", "notes": "Minced"},
            {"name": "Lemon", "quantity": 1.0, "unit": "piece", "notes": "Cut into wedges for serving"}
        ],
        "required_tools": ["Wide Wooden Spoon", "Ladle", "Chef's Knife", "Citrus Juicer"],
        "required_vessels": ["14 to 16-inch Traditional Carbon Steel Paella Pan or Wide Cast Iron Pan", "Small Saucepan for Warm Broth"],
        "steps": [
            "Gently warm 800ml fish or chicken stock in a saucepan and steep crushed saffron threads for 10 minutes.",
            "Heat 3 tbsp olive oil in the wide paella pan over medium heat. Brown chorizo slices and sear shrimp for 1 minute per side; transfer to a plate.",
            "In same pan fat, sauté minced garlic and grated tomato pulp with smoked paprika for 5 minutes until darkened into a jammy sofrito.",
            "Add Bomba rice; stir for 2 minutes until translucent grains are coated in aromatic oil.",
            "Pour in saffron-infused warm broth. Distribute rice evenly across pan. DO NOT STIR RICE AFTER THIS POINT to allow starch structure to set.",
            "Simmer briskly on medium-high heat for 10 minutes, then reduce to low heat for 10 minutes until liquid is absorbed.",
            "Arrange seared shrimp over top. Increase heat to medium-high for 2 minutes until crackling sounds indicate the crispy bottom socarrat crust has formed.",
            "Cover with a clean kitchen towel off heat for 5 minutes. Garnish with lemon wedges and serve directly in the pan."
        ],
        "allergens": ["Shellfish"],
        "substitutions": ["Arborio rice can substitute if Bomba is unavailable.", "Chicken thighs and green beans for traditional land paella."],
        "needed_ingredients": [
            {"name": "Fish or Chicken Stock", "amount": "800 ml", "purpose": "Cooking rice"},
            {"name": "Extra Virgin Olive Oil", "amount": "3 tbsp", "purpose": "Sautéing sofrito"}
        ],
        "generation_mode": "Master Chef Curated"
    },
    {
        "id": 105,
        "title": "Pan-Seared Beef Tenderloin with Garlic Herb Butter",
        "summary": "Melt-in-your-mouth filet mignon steaks seared in cast iron with a deep caramelized crust, continuously basted with rosemary, thyme, and foaming butter.",
        "cuisine": "French",
        "meal_type": "Dinner",
        "prep_time_mins": 10,
        "cook_time_mins": 12,
        "servings": 2,
        "difficulty": "Medium",
        "ingredients_list": [
            {"name": "Beef Tenderloin", "quantity": 2.0, "unit": "piece", "notes": "6oz center-cut filet mignon steaks, room temp"},
            {"name": "Butter", "quantity": 50.0, "unit": "g", "notes": "Unsalted European high-fat butter"},
            {"name": "Garlic", "quantity": 4.0, "unit": "cloves", "notes": "Lightly crushed skin-on"},
            {"name": "Rosemary", "quantity": 2.0, "unit": "sprigs", "notes": "Fresh whole rosemary"},
            {"name": "Thyme", "quantity": 4.0, "unit": "sprigs", "notes": "Fresh garden thyme sprigs"},
            {"name": "Black Pepper", "quantity": 1.0, "unit": "tsp", "notes": "Coarsely ground"}
        ],
        "required_tools": ["Instant-Read Meat Thermometer", "Heavy-Duty Kitchen Tongs", "Large Metal Basting Spoon", "Cutting Board"],
        "required_vessels": ["12-inch Heavy Cast Iron Skillet", "Resting Board / Warm Plate"],
        "steps": [
            "Pat tenderloin dry with paper towels; season all sides generously with coarse sea salt and cracked black pepper 30 minutes before cooking.",
            "Heat cast iron skillet over high heat until smoking; add 1 tbsp neutral oil with high smoke point.",
            "Place steaks in skillet. Sear undisturbed for 2.5 minutes without moving until a deep mahogany crust forms.",
            "Flip steaks with tongs; sear reverse side for 2 minutes.",
            "Turn heat down to medium; add butter, crushed garlic cloves, rosemary, and thyme into the pan.",
            "Tilt skillet slightly toward you. Using large metal spoon, continuously baste foaming herb-infused butter over top of steaks for 2 minutes until internal temperature hits 52°C (125°F for medium-rare).",
            "Transfer steaks to warm cutting board. Pour remaining pan juices over steaks and rest for 7 minutes before carving thick medallions."
        ],
        "allergens": ["Dairy"],
        "substitutions": ["Ribeye or New York Strip steaks work equally well.", "Ghee can be used for dairy-sensitive diners."],
        "needed_ingredients": [
            {"name": "High-Smoke Neutral Oil", "amount": "1 tbsp", "purpose": "Initial high-heat sear"},
            {"name": "Coarse Sea Salt", "amount": "1 tsp", "purpose": "Dry-brine seasoning"}
        ],
        "generation_mode": "Master Chef Curated"
    },
    {
        "id": 106,
        "title": "Authentic Japanese Shoyu Ramen",
        "summary": "Springy ramen noodles bathed in a rich dashi-chicken broth with aromatic soy tare, tender chashu pork belly, soft-boiled ajitsuke egg, and scallions.",
        "cuisine": "Japanese",
        "meal_type": "Dinner",
        "prep_time_mins": 25,
        "cook_time_mins": 35,
        "servings": 2,
        "difficulty": "Advanced",
        "ingredients_list": [
            {"name": "Ramen Noodles", "quantity": 200.0, "unit": "g", "notes": "Fresh or dried alkaline ramen noodles"},
            {"name": "Pork Belly", "quantity": 200.0, "unit": "g", "notes": "Rolled and braised chashu slices"},
            {"name": "Egg", "quantity": 2.0, "unit": "piece", "notes": "Soft-boiled ramen eggs with jammy yolks"},
            {"name": "Soy Sauce", "quantity": 3.0, "unit": "tbsp", "notes": "Japanese shoyu tare base"},
            {"name": "Shiitake Mushrooms", "quantity": 4.0, "unit": "piece", "notes": "Sliced fresh or rehydrated dried"},
            {"name": "Scallion", "quantity": 2.0, "unit": "piece", "notes": "Finely curled green rings"},
            {"name": "Sesame Oil", "quantity": 1.0, "unit": "tsp", "notes": "Toasted finish oil"}
        ],
        "required_tools": ["Ramen Strainer / Spider Noodle Basket", "Ladle", "Chef's Knife", "Timer"],
        "required_vessels": ["Deep Stockpot for Broth", "Large Pot of Boiling Water for Noodles", "2 Heavy Ceramic Ramen Bowls"],
        "steps": [
            "In stockpot, simmer rich chicken and mushroom broth with sliced ginger, garlic, and shiitake caps for 30 minutes.",
            "Prepare tare: whisk soy sauce with 1 tsp mirin and a dash of dashi in bottom of each ramen bowl.",
            "Boil water in noodle pot. Drop ramen noodles and boil for exactly 90 to 120 seconds for firm 'katame' texture.",
            "Ladle 350ml steaming broth into each bowl over the tare; stir once with chopsticks to combine.",
            "Lift noodles with spider strainer, shake off excess water vigorously, and fold noodles neatly into broth.",
            "Top with seared pork belly slices, halved jammy soft-boiled eggs, sliced shiitake, and a mound of fresh scallions.",
            "Drizzle with a drop of toasted sesame oil and serve immediately while steaming hot."
        ],
        "allergens": ["Gluten", "Soy", "Eggs"],
        "substitutions": ["Chicken breast or pan-fried tofu can replace pork.", "Udon or soba can substitute ramen noodles."],
        "needed_ingredients": [
            {"name": "Chicken Stock", "amount": "750 ml", "purpose": "Ramen soup base"},
            {"name": "Water", "amount": "3 L", "purpose": "Boiling noodles"}
        ],
        "generation_mode": "Master Chef Curated"
    },
    {
        "id": 107,
        "title": "Creamy Tuscan Chicken Fettuccine Alfredo",
        "summary": "Al dente fettuccine ribbons coated in a luxurious emulsion of heavy cream, melted butter, aged Parmigiano Reggiano, and pan-seared golden chicken strips.",
        "cuisine": "Italian",
        "meal_type": "Dinner",
        "prep_time_mins": 10,
        "cook_time_mins": 15,
        "servings": 2,
        "difficulty": "Easy",
        "ingredients_list": [
            {"name": "Fettuccine", "quantity": 200.0, "unit": "g", "notes": "Egg fettuccine ribbons"},
            {"name": "Chicken", "quantity": 250.0, "unit": "g", "notes": "Boneless breast sliced into cutlets"},
            {"name": "Butter", "quantity": 40.0, "unit": "g", "notes": "European unsalted butter"},
            {"name": "Garlic", "quantity": 3.0, "unit": "cloves", "notes": "Minced"},
            {"name": "Parmesan", "quantity": 60.0, "unit": "g", "notes": "Aged Parmigiano Reggiano freshly grated"},
            {"name": "Heavy Cream", "quantity": 120.0, "unit": "ml", "notes": "Fresh whipping cream"},
            {"name": "Parsley", "quantity": 2.0, "unit": "tbsp", "notes": "Finely chopped flat-leaf Italian parsley"}
        ],
        "required_tools": ["Pasta Tongs", "Cheese Grater", "Whisk", "Chef's Knife"],
        "required_vessels": ["Large Pasta Stockpot", "12-inch Sauté Pan"],
        "steps": [
            "Boil fettuccine in salted water until al dente; reserve 1/2 cup pasta cooking water.",
            "Season chicken cutlets with salt and pepper. Sear in sauté pan with 1 tbsp olive oil over medium-high heat for 4 minutes per side until golden. Remove and slice into strips.",
            "In same pan, melt butter over medium heat. Sauté minced garlic for 45 seconds until fragrant without browning.",
            "Pour in heavy cream; bring to a gentle simmer for 2 minutes to thicken slightly.",
            "Turn heat to lowest setting; gradually whisk in freshly grated Parmesan in batches until sauce is velvety and smooth.",
            "Transfer hot fettuccine directly into sauce. Toss with tongs, adding a splash of reserved pasta water if needed to loosen.",
            "Top with sliced golden chicken strips, freshly cracked black pepper, and chopped Italian parsley."
        ],
        "allergens": ["Gluten", "Dairy"],
        "substitutions": ["Shrimp or sautéed mushrooms can replace chicken.", "Penne pasta can replace fettuccine."],
        "needed_ingredients": [
            {"name": "Black Pepper", "amount": "1/2 tsp", "purpose": "Seasoning"},
            {"name": "Olive Oil", "amount": "1 tbsp", "purpose": "Searing chicken"}
        ],
        "generation_mode": "Master Chef Curated"
    },
    {
        "id": 108,
        "title": "Velvety Mascarpone & Espresso Tiramisu",
        "summary": "Classic Italian no-bake dessert featuring crisp savoiardi ladyfingers soaked in dark espresso and layered with whipped mascarpone cream and raw cacao.",
        "cuisine": "Italian",
        "meal_type": "Dessert",
        "prep_time_mins": 25,
        "cook_time_mins": 0,
        "servings": 6,
        "difficulty": "Easy",
        "ingredients_list": [
            {"name": "Mascarpone", "quantity": 250.0, "unit": "g", "notes": "Chilled Italian mascarpone cheese"},
            {"name": "Coffee", "quantity": 200.0, "unit": "ml", "notes": "Freshly brewed strong espresso cooled to room temp"},
            {"name": "Cocoa Powder", "quantity": 2.0, "unit": "tbsp", "notes": "Dutch-process unsweetened cacao for dusting"},
            {"name": "Pure Vanilla Extract", "quantity": 1.0, "unit": "tsp", "notes": "Pure Madagascar vanilla"},
            {"name": "Sugar", "quantity": 60.0, "unit": "g", "notes": "Fine granulated sugar"},
            {"name": "Egg", "quantity": 2.0, "unit": "piece", "notes": "Separated into yolks and whites"}
        ],
        "required_tools": ["Electric Hand Mixer or Whisk", "Fine Mesh Sifter / Strainer", "Rubber Spatula"],
        "required_vessels": ["8x8-inch Glass Pyrex Dish or Ceramic Casserole", "2 Medium Glass Mixing Bowls"],
        "steps": [
            "In a bowl, beat egg yolks with sugar and vanilla extract until pale, thick, and ribbon-like (about 4 minutes).",
            "Gently fold mascarpone cheese into yolk mixture using a rubber spatula until completely lump-free and silky.",
            "In separate clean bowl, beat egg whites with a pinch of salt until stiff peaks form.",
            "Gently fold whipped egg whites into mascarpone cream in two batches to maintain maximum airiness.",
            "Pour cooled espresso into a shallow dish. Dip ladyfinger biscuits one by one for 1.5 seconds per side (do not over-saturate).",
            "Arrange a single layer of soaked ladyfingers tightly in bottom of glass dish. Spread half of mascarpone cream evenly over top.",
            "Repeat with a second layer of soaked ladyfingers and finish with remaining mascarpone cream smoothed with spatula.",
            "Refrigerate for at least 4 hours (ideally overnight). Dust generously with Dutch-process cocoa powder through a sifter just before slicing."
        ],
        "allergens": ["Dairy", "Eggs", "Gluten"],
        "substitutions": ["Heavy whipping cream can replace egg whites for pasteurized preparation.", "Decaf espresso can be used."],
        "needed_ingredients": [
            {"name": "Ladyfinger Biscuits (Savoiardi)", "amount": "20 pieces", "purpose": "Cake base layers"},
            {"name": "Salt", "amount": "1 pinch", "purpose": "Egg white stabilization"}
        ],
        "generation_mode": "Master Chef Curated"
    },
    {
        "id": 109,
        "title": "Sizzling Spanish Garlic Shrimp (Gambas al Ajillo)",
        "summary": "Plump wild shrimp flash-sautéed in sizzling extra virgin olive oil with heaps of golden slivered garlic, dry sherry, and chili flakes.",
        "cuisine": "Spanish",
        "meal_type": "Appetizer",
        "prep_time_mins": 10,
        "cook_time_mins": 6,
        "servings": 2,
        "difficulty": "Easy",
        "ingredients_list": [
            {"name": "Shrimp", "quantity": 300.0, "unit": "g", "notes": "Peeled, deveined, patted completely dry"},
            {"name": "Garlic", "quantity": 8.0, "unit": "cloves", "notes": "Thinly slivered with a sharp knife"},
            {"name": "Sherry Vinegar", "quantity": 1.0, "unit": "tbsp", "notes": "Or dry Spanish Fino Sherry"},
            {"name": "Chili Pepper", "quantity": 1.0, "unit": "piece", "notes": "Dried red chili pepper sliced or 1 tsp flakes"},
            {"name": "Smoked Paprika", "quantity": 0.5, "unit": "tsp", "notes": "Sweet Spanish pimentón"},
            {"name": "Parsley", "quantity": 2.0, "unit": "tbsp", "notes": "Fresh Italian flat-leaf parsley chopped"}
        ],
        "required_tools": ["Chef's Knife & Cutting Board", "Wooden Spoon", "Kitchen Tongs"],
        "required_vessels": ["Traditional Spanish Clay Cazuela or 10-inch Heavy Skillet"],
        "steps": [
            "Toss shrimp with a pinch of sea salt and smoked paprika; let stand for 5 minutes.",
            "Pour 1/3 cup extra virgin olive oil into skillet over medium-low heat. Add slivered garlic and sliced chili.",
            "Cook garlic gently for 2 to 3 minutes until pale golden and fragrant (do not let it brown or turn bitter).",
            "Increase heat to medium-high. Add shrimp in a single layer. Sear for 90 seconds until pink on underside.",
            "Flip shrimp with tongs; splash in sherry vinegar and cook for another 60 seconds until shrimp just turn opaque.",
            "Remove from heat immediately while oil is still bubbling vigorously. Scatter fresh chopped parsley over top.",
            "Serve sizzling hot straight to the table alongside warm crusty sourdough bread for dipping into the garlic-infused oil."
        ],
        "allergens": ["Shellfish"],
        "substitutions": ["White wine can substitute for sherry.", "Scallops or calamari can be prepared the same way."],
        "needed_ingredients": [
            {"name": "Extra Virgin Olive Oil", "amount": "1/3 cup", "purpose": "Sizzling cooking bath"},
            {"name": "Crusty Bread / Sourdough", "amount": "4 slices", "purpose": "Dipping oil"}
        ],
        "generation_mode": "Master Chef Curated"
    },
    {
        "id": 110,
        "title": "Fresh Tableside Stone-Ground Guacamole",
        "summary": "Rich creamy Hass avocados crushed with fragrant lime juice, diced jalapeño, fresh cilantro, and fine sea salt, served with warm tortilla chips.",
        "cuisine": "Mexican",
        "meal_type": "Snack",
        "prep_time_mins": 10,
        "cook_time_mins": 0,
        "servings": 4,
        "difficulty": "Easy",
        "ingredients_list": [
            {"name": "Avocado", "quantity": 3.0, "unit": "piece", "notes": "Ripe Hass avocados yielding to gentle pressure"},
            {"name": "Lime", "quantity": 2.0, "unit": "piece", "notes": "Juiced fresh"},
            {"name": "Cilantro", "quantity": 3.0, "unit": "tbsp", "notes": "Freshly chopped leaves and tender stems"},
            {"name": "Onion", "quantity": 0.5, "unit": "piece", "notes": "Finely diced white onion rinsed in cold water"},
            {"name": "Chili Pepper", "quantity": 1.0, "unit": "piece", "notes": "Jalapeño or serrano finely minced"},
            {"name": "Tomato", "quantity": 1.0, "unit": "piece", "notes": "Roma tomato, seeded and diced"}
        ],
        "required_tools": ["Chef's Knife & Cutting Board", "Citrus Juicer", "Fork or Potato Masher"],
        "required_vessels": ["Traditional Lava Stone Molcajete or Heavy Ceramic Bowl"],
        "steps": [
            "In molcajete or heavy bowl, grind 1 tbsp minced onion, 1 tsp minced jalapeño, 1 tbsp cilantro, and 1/2 tsp sea salt into a fragrant green paste.",
            "Halve avocados, remove pits, and scoop flesh into the bowl with a spoon.",
            "Squeeze fresh lime juice directly over the avocado flesh to preserve vibrant green color.",
            "Mash with a fork to your desired texture, keeping plenty of chunky rustic avocado pieces.",
            "Gently fold in remaining diced onion, diced seeded tomato, and fresh cilantro.",
            "Taste and adjust with a splash more lime juice or salt as needed. Serve immediately with warm tortilla chips."
        ],
        "allergens": [],
        "substitutions": ["Add roasted garlic for deeper allium flavor.", "Substitute pomegranate seeds for tomato for festive crunch."],
        "needed_ingredients": [
            {"name": "Flaky Sea Salt", "amount": "1 tsp", "purpose": "Seasoning"},
            {"name": "Crispy Tortilla Chips", "amount": "1 basket", "purpose": "Dipping"}
        ],
        "generation_mode": "Master Chef Curated"
    },
    {
        "id": 111,
        "title": "Decadent Molten Dark Chocolate Lava Cake",
        "summary": "Individual bittersweet cacao cakes with a delicate baked sponge exterior and a rich, flowing molten ganache center, dusted with sea salt and cocoa.",
        "cuisine": "French",
        "meal_type": "Dessert",
        "prep_time_mins": 15,
        "cook_time_mins": 12,
        "servings": 2,
        "difficulty": "Medium",
        "ingredients_list": [
            {"name": "Dark Chocolate 85%", "quantity": 100.0, "unit": "g", "notes": "Chopped fine"},
            {"name": "Butter", "quantity": 60.0, "unit": "g", "notes": "Unsalted high-fat butter"},
            {"name": "Egg", "quantity": 2.0, "unit": "piece", "notes": "1 whole egg + 1 yolk at room temp"},
            {"name": "Brown Sugar", "quantity": 35.0, "unit": "g", "notes": "Adds deep caramel undertone"},
            {"name": "All-Purpose Flour", "quantity": 2.0, "unit": "tbsp", "notes": "Sifted"},
            {"name": "Pure Vanilla Extract", "quantity": 0.5, "unit": "tsp", "notes": "Madagascar vanilla extract"},
            {"name": "Vanilla Ice Cream", "quantity": 2.0, "unit": "scoops", "notes": "For serving alongside warm cake"}
        ],
        "required_tools": ["Electric Hand Mixer or Whisk", "Heatproof Bowl & Saucepan (Bain-marie)", "Pastry Brush"],
        "required_vessels": ["Two 6oz Ceramic Ramekins", "Baking Sheet"],
        "steps": [
            "Preheat oven to 200°C (400°F). Brush ramekins with melted butter and dust inside with cocoa powder, tapping out excess.",
            "In heatproof bowl over a pot of barely simmering water, melt chopped dark chocolate and butter together until silky smooth. Remove to cool slightly.",
            "In separate bowl, whisk whole egg, egg yolk, brown sugar, and vanilla extract vigorously for 2 minutes until frothy and pale.",
            "Fold melted chocolate mixture into beaten eggs with a spatula.",
            "Gently fold in sifted flour just until no dry flour streaks remain (do not overmix).",
            "Divide batter evenly between prepared ramekins. Place ramekins on baking sheet.",
            "Bake for exactly 11 to 12 minutes until edges are set and center is still slightly soft to touch.",
            "Let cool for 1 minute. Run a thin knife around edges and invert onto dessert plates.",
            "Dust with cocoa powder, sprinkle with flaky sea salt, and crown with a cold scoop of vanilla ice cream."
        ],
        "allergens": ["Dairy", "Eggs", "Gluten"],
        "substitutions": ["Use gluten-free 1-to-1 baking flour.", "Milk chocolate can replace dark chocolate for a sweeter profile."],
        "needed_ingredients": [
            {"name": "Cocoa Powder", "amount": "1 tbsp", "purpose": "Dusting ramekins"},
            {"name": "Flaky Sea Salt", "amount": "1 pinch", "purpose": "Finishing contrast"}
        ],
        "generation_mode": "Master Chef Curated"
    },
    {
        "id": 112,
        "title": "Szechuan Spicy Dan Dan Noodles",
        "summary": "Tender noodles tossed in a fiery, fragrant sauce of toasted sesame paste, Szechuan chili oil, dark soy sauce, crispy minced pork, and crushed peanuts.",
        "cuisine": "Chinese",
        "meal_type": "Lunch",
        "prep_time_mins": 15,
        "cook_time_mins": 15,
        "servings": 2,
        "difficulty": "Medium",
        "ingredients_list": [
            {"name": "Udon Noodles", "quantity": 250.0, "unit": "g", "notes": "Or fresh Chinese wheat noodles"},
            {"name": "Ground Beef", "quantity": 150.0, "unit": "g", "notes": "Or ground pork belly"},
            {"name": "Tahini", "quantity": 2.0, "unit": "tbsp", "notes": "Chinese toasted sesame paste or tahini"},
            {"name": "Szechuan Peppercorns", "quantity": 1.0, "unit": "tsp", "notes": "Toasted and ground fine"},
            {"name": "Soy Sauce", "quantity": 2.0, "unit": "tbsp", "notes": "Dark soy sauce + light soy sauce blend"},
            {"name": "Bok Choy", "quantity": 2.0, "unit": "heads", "notes": "Halved lengthwise"},
            {"name": "Peanuts", "quantity": 30.0, "unit": "g", "notes": "Crushed roasted peanuts"},
            {"name": "Scallion", "quantity": 2.0, "unit": "piece", "notes": "Finely chopped"}
        ],
        "required_tools": ["Wok or Heavy Skillet", "Pasta Spider / Strainer", "Chef's Knife & Board"],
        "required_vessels": ["Carbon Steel Wok", "Noodle Stockpot", "2 Deep Ceramic Noodle Bowls"],
        "steps": [
            "In wok over medium-high heat, brown ground meat with 1 tsp dark soy sauce and five-spice until crispy and dark brown (about 6 minutes).",
            "Whisk sauce directly in bottoms of serving bowls: sesame paste/tahini, soy sauce, Szechuan pepper, chili oil, minced garlic, and a splash of hot broth.",
            "Boil noodles in stockpot until tender with slight chew. During last 30 seconds of cooking, drop halved bok choy into boiling water to blanch.",
            "Lift noodles and bok choy out with spider, draining well.",
            "Divide hot noodles into bowls directly over the sesame-chili sauce.",
            "Top with crispy browned meat, blanched bok choy, crushed roasted peanuts, and sliced scallions.",
            "Toss noodles thoroughly tableside to coat every strand in the spicy, creamy sesame-chili emulsion."
        ],
        "allergens": ["Gluten", "Soy", "Peanuts", "Sesame"],
        "substitutions": ["Shiitake mushrooms make an excellent vegetarian meat substitute.", "Ramen or spaghetti can substitute wheat noodles."],
        "needed_ingredients": [
            {"name": "Chili Oil", "amount": "2 tbsp", "purpose": "Aromatic heat"},
            {"name": "Broth or Noodle Water", "amount": "1/4 cup", "purpose": "Loosen sauce"}
        ],
        "generation_mode": "Master Chef Curated"
    },
    {
        "id": 113,
        "title": "Royal Kesariya Mango Shrikhand Parfait",
        "summary": "Silky strained Greek yogurt whipped with ripe Alphonso mango purée, fragrant green cardamom, toasted pistachios, and golden saffron threads.",
        "cuisine": "Indian",
        "meal_type": "Dessert",
        "prep_time_mins": 20,
        "cook_time_mins": 0,
        "servings": 4,
        "difficulty": "Easy",
        "ingredients_list": [
            {"name": "Curd", "quantity": 400.0, "unit": "g", "notes": "Greek yogurt or hung curd strained for 4 hours"},
            {"name": "Mango", "quantity": 250.0, "unit": "g", "notes": "Ripe sweet mango puréed smooth"},
            {"name": "Spanish Saffron", "quantity": 1.0, "unit": "pinch", "notes": "Steeped in 1 tbsp warm milk"},
            {"name": "Cardamom", "quantity": 0.5, "unit": "tsp", "notes": "Freshly ground green cardamom seeds"},
            {"name": "Brown Sugar", "quantity": 40.0, "unit": "g", "notes": "Or powdered cane sugar"},
            {"name": "Pistachio Gelato", "quantity": 2.0, "unit": "scoops", "notes": "Optional side or chopped toasted pistachios"}
        ],
        "required_tools": ["Cheesecloth or Nut Milk Bag", "Whisk or Food Processor", "Spatula"],
        "required_vessels": ["Fine Mesh Colander", "Large Glass Mixing Bowl", "4 Glass Dessert Cups"],
        "steps": [
            "Line colander with cheesecloth, place over bowl, and strain curd in refrigerator for 3 to 4 hours to remove whey, leaving thick creamy 'chakka'.",
            "In small ramekin, steep saffron threads in warm milk for 10 minutes until deep orange-gold.",
            "Transfer strained curd into glass bowl. Add powdered sugar, cardamom powder, and steeped saffron milk.",
            "Whisk vigorously for 3 minutes until smooth, glossy, and cloud-like.",
            "Gently fold in smooth ripe mango purée until a uniform golden swirl is achieved.",
            "Spoon into individual dessert glasses. Chill in refrigerator for at least 1 hour.",
            "Garnish with slivered raw pistachios and a single saffron thread before serving cool."
        ],
        "allergens": ["Dairy", "Nuts"],
        "substitutions": ["Coconut yogurt can replace dairy curd for vegan preparation.", "Frozen mango pulp can be used year-round."],
        "needed_ingredients": [
            {"name": "Milk", "amount": "1 tbsp", "purpose": "Saffron steeping"},
            {"name": "Shelled Pistachios", "amount": "2 tbsp", "purpose": "Topping garnish"}
        ],
        "generation_mode": "Master Chef Curated"
    },
    {
        "id": 114,
        "title": "Matcha Green Tea & White Chocolate Gelato Affogato",
        "summary": "Earthly ceremonial Japanese matcha gelato crowned with melted white chocolate curls and splashed with warm sweet vanilla espresso.",
        "cuisine": "Japanese",
        "meal_type": "Dessert",
        "prep_time_mins": 10,
        "cook_time_mins": 5,
        "servings": 2,
        "difficulty": "Easy",
        "ingredients_list": [
            {"name": "Matcha Ice Cream", "quantity": 2.0, "unit": "scoops", "notes": "Artisan ceremonial matcha gelato"},
            {"name": "White Chocolate", "quantity": 40.0, "unit": "g", "notes": "Shaved into delicate curls"},
            {"name": "Coffee", "quantity": 60.0, "unit": "ml", "notes": "Fresh hot espresso shot"},
            {"name": "Pure Vanilla Extract", "quantity": 0.5, "unit": "tsp", "notes": "Infused into hot espresso"}
        ],
        "required_tools": ["Vegetable Peeler (for chocolate shavings)", "Espresso Machine or Moka Pot", "Ice Cream Scoop"],
        "required_vessels": ["2 Chilled Glass Dessert Coupe Glasses"],
        "steps": [
            "Chill dessert coupe glasses in freezer for 15 minutes.",
            "Using vegetable peeler, draw firm strokes along edge of white chocolate bar to create delicate curls.",
            "Brew two hot shots of rich espresso; stir in a drop of pure vanilla extract.",
            "Place a generous scoop of chilled matcha gelato into each frozen coupe glass.",
            "Scatter white chocolate curls over the gelato.",
            "Pour hot vanilla-infused espresso over gelato tableside and serve immediately with a dessert spoon."
        ],
        "allergens": ["Dairy"],
        "substitutions": ["Hot brewed matcha tea can replace espresso for caffeine-free pairing.", "Vanilla gelato can substitute matcha."],
        "needed_ingredients": [],
        "generation_mode": "Master Chef Curated"
    },
    {
        "id": 115,
        "title": "Crispy Pesto Genovese & Ricotta Stuffed Shells",
        "summary": "Jumbo pasta shells stuffed with seasoned creamy ricotta, fresh basil pesto, and baked in sweet marinara sauce under a bubbling blanket of mozzarella.",
        "cuisine": "Italian",
        "meal_type": "Dinner",
        "prep_time_mins": 20,
        "cook_time_mins": 25,
        "servings": 4,
        "difficulty": "Easy",
        "ingredients_list": [
            {"name": "Penne Rigate", "quantity": 300.0, "unit": "g", "notes": "Or jumbo pasta shells (conchiglioni)"},
            {"name": "Ricotta Cheese", "quantity": 250.0, "unit": "g", "notes": "Whole milk fresh ricotta"},
            {"name": "Pesto Genovese", "quantity": 4.0, "unit": "tbsp", "notes": "Traditional basil pine nut pesto"},
            {"name": "Marinara Sauce", "quantity": 350.0, "unit": "ml", "notes": "Classic slow-simmered tomato passata"},
            {"name": "Mozzarella", "quantity": 150.0, "unit": "g", "notes": "Shredded low-moisture mozzarella"},
            {"name": "Parmesan", "quantity": 40.0, "unit": "g", "notes": "Grated aged Parmigiano"}
        ],
        "required_tools": ["Pastry Piping Bag or Tablespoon", "Cheese Grater", "Tongs"],
        "required_vessels": ["9x13-inch Ceramic Casserole / Baking Dish", "Large Stockpot for Pasta", "Medium Mixing Bowl"],
        "steps": [
            "Preheat oven to 190°C (375°F).",
            "Boil pasta shells in salted water until 2 minutes shy of al dente; drain and rinse with cold water to prevent sticking.",
            "In mixing bowl, stir ricotta, 2 tbsp Pesto Genovese, half the grated Parmesan, 1 egg, and black pepper until uniform.",
            "Spread marinara sauce across the bottom of the ceramic casserole dish.",
            "Spoon or pipe ricotta filling generously into each pasta shell and nestle shells tightly into marinara sauce.",
            "Drizzle remaining Pesto Genovese over the tops, then cover with shredded mozzarella and remaining Parmesan.",
            "Bake uncovered for 22 to 25 minutes until the cheese is bubbling, golden, and browned at the corners.",
            "Rest for 5 minutes before serving with extra fresh basil leaves."
        ],
        "allergens": ["Gluten", "Dairy", "Eggs"],
        "substitutions": ["Ground Italian sausage can be mixed into ricotta filling.", "Gluten-free pasta shells work well."],
        "needed_ingredients": [
            {"name": "Egg", "amount": "1 piece", "purpose": "Binding ricotta filling"},
            {"name": "Fresh Basil", "amount": "6 leaves", "purpose": "Garnish"}
        ],
        "generation_mode": "Master Chef Curated"
    }
]
