# FlavorFusion AI 🌿
### AI-Powered Multi-Ingredient Recognition, Taste Prediction & Personalized Food Discovery

FlavorFusion AI is an intelligent culinary chemistry and flavor discovery platform designed to explore how multiple ingredients interact, balance, and taste when combined. Built with a full-stack architecture combining FastAPI, React, TypeScript, Tailwind CSS, persistent database storage, real computer vision, explainable sensory flavor alchemy, and interactive AI assistance.

---

## 🌟 Key Features

### 1. 🌗 Dark, Light & System Default Themes
- Seamless 1-click theme switching from the navigation bar (or mobile menu) supporting **Light**, **Dark** (crafted with deep forest obsidian tones `#0c100e`), and **System Default** OS preference synchronization with local storage persistence.

### 2. ✨ Emergent Flavor Alchemy ("How It Tastes" Sensory Illusions)
- Evaluates non-linear taste perceptions and sensory illusions! For example:
  - **Vanilla Ice Cream + Soy Sauce** 🍨🥢: Fermented sodium suppresses bitterness while vanillin triggers the exact brain perception of **Rich Salted Caramel & Toasted Butterscotch**!
  - **Strawberries + Balsamic Vinegar** 🍓🍾: Acetic acid unlocks volatile fruit esters, tasting like **Macerated Plum & Blackberry Jam**!
  - **Watermelon + Feta + Mint** 🍉🧀: Citrulline sweetness and sheep brine create a **Crisp Mediterranean Summer Cloud**!
  - **Dark Chocolate + Chili + Olive Oil** 🍫🌶️: Capsaicin endorphins create an **Aztec Molten Fire & Ganache** experience!
- Highlights Gen-Z style vibe badges (*"Certified Banger 🔥"*, *"Unhinged Synergy 🤯"*).

### 3. 🍽️ Dishes You Can Make & Recipe Wishlisting
- Automatically computes **"Dishes You Can Make Using These Ingredients"** based on the active ingredients in your Flavor Lab.
- Provides 1-click **"❤️ Wishlist"** to save potential dishes to your personalized Culinary Dashboard and **"📖 Cook Recipe"** to immediately open step-by-step instructions.

### 4. 🧑‍🍳 Chef Fusion AI (Interactive Culinary Assistant)
- Floating assistant drawer accessible from anywhere on the platform (*"Ask Chef AI 🧑‍🍳"*).
- Ask food chemistry questions (*"Why does soy sauce on ice cream taste like caramel?"*, *"5-min midnight snack idea"*).
- Provides actionable formula chips with a 1-click **"Load into Flavor Lab 🧪"** button.

### 5. 🧪 Multi-Ingredient Flavor Lab (Up to 30+ Ingredients)
- Dynamic multi-ingredient workspace supporting from 1 to 30+ ingredients.
- Physical quantity scaling (grams, ml, pinches, tablespoons) and cooking technique modifiers (Raw, Roasted, Sautéed, Cooked, Boiled).
- 6-basic-taste radar chart (Sweet, Salty, Sour, Bitter, Umami, Spicy), aroma volatile breakdown, and pairwise chemical matrix.

### 6. 📷 Real Computer Vision Ingredient Recognition
- Real image feature extraction analyzing color histograms, brightness distributions, and spatial edge gradients.
- Webcam / photo capture integration directly into the Flavor Lab.

### 7. 🛡️ Hard Allergy Exclusions & Palate Personalization
- Hard allergy safety checks: ingredients violating user allergen constraints receive an immediate **0% match** and a critical warning banner.

---

## 🚀 How to Run the Application

### Option A: 1-Click Launchers (Recommended on Windows)

In the project root folder `C:\Users\shanm\.gemini\antigravity\scratch\flavorfusion-ai`:

- **Double-click `start.bat`** (or in Command Prompt run `start.bat`)
- Or in **PowerShell**:
  ```powershell
  .\start.ps1
  ```

This will automatically:
1. Start the FastAPI backend on `http://127.0.0.1:8000`
2. Start the Vite React frontend on `http://localhost:5173`
3. Launch your web browser directly to `http://localhost:5173`

---

### Option B: Manual Command Line Execution

#### Terminal 1 — Backend (FastAPI)
```powershell
cd backend
.\venv\Scripts\Activate.ps1
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```
Interactive API docs: **http://127.0.0.1:8000/docs**

#### Terminal 2 — Frontend (React + Vite)
```powershell
cd frontend
npm run dev
```
Web app: **http://localhost:5173**

---

## 🧪 Running Automated Tests

Run the full automated test suite (15 feature tests):
```powershell
cd backend
.\venv\Scripts\python.exe tests/test_all_features.py
```
*(All 15 integration tests pass cleanly).*

---

## 🔑 Demo Credentials

| Role | Email | Password |
|---|---|---|
| **Curator / Admin** | `admin@flavorfusion.ai` | `AdminPass123!` |
| **Gourmet Member** | `gourmet@flavorfusion.ai` | `Gourmet123!` |

*(Guest users can explore, scan photos, and analyze flavor combinations without logging in!)*
