# 🚀 FlavorFusion AI — Vercel Deployment Guide

FlavorFusion AI is fully configured for deployment on **Vercel** with a React (Vite + TypeScript) frontend and a Python FastAPI backend.

---

## ⚡ Option 1: Deploy Directly via GitHub & Vercel Dashboard (Recommended)

This is the easiest and most automated deployment method.

### Step 1: Push your project to GitHub
If you haven't pushed the project to GitHub yet, run these commands in the terminal:

```bash
git add .
git commit -m "feat: complete FlavorFusion AI with Vercel deployment configuration"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo-name>.git
git push -u origin main
```

---

### Step 2: Import into Vercel
1. Log in to [vercel.com](https://vercel.com).
2. Click **Add New...** → **Project**.
3. Select your GitHub repository (`flavorfusion-ai`).
4. **Project Settings**:
   - **Framework Preset**: *Vite* (or leave on *Other* — `vercel.json` handles this automatically).
   - **Root Directory**: `./` (leave at repository root).
   - **Build Command**: `cd frontend && npm install && npm run build` (pre-configured in `vercel.json`).
   - **Output Directory**: `frontend/dist` (pre-configured in `vercel.json`).

---

### Step 3: Configure Environment Variables (Optional)
Under the **Environment Variables** section in Vercel:

| Variable | Recommended Value | Purpose |
| :--- | :--- | :--- |
| `DATABASE_URL` | *(Optional)* PostgreSQL connection string (e.g. from **Neon**, **Supabase**, or **Vercel Postgres**) | For persistent production database storage across serverless function lifecycles. |
| `SECRET_KEY` | *(Optional)* Random 32+ character string | Used for JWT authentication signing. |
| `GEMINI_API_KEY` | *(Optional)* Google Gemini API key | Enables generative AI recipe enhancements. |

> **Note on Database**:
> - If `DATABASE_URL` is omitted, the application uses an in-memory/temporary SQLite database initialized and seeded with all 179 ingredients in Vercel's `/tmp` directory.
> - For persistent users, favorites, and custom saved recipes in production, creating a free serverless database on **Neon** (`neon.tech`) or **Supabase** (`supabase.com`) and adding `DATABASE_URL` is recommended.

---

### Step 4: Click Deploy!
Vercel will:
1. Build the React frontend into `frontend/dist`.
2. Bundle the Python FastAPI application via `@vercel/python` into `/api/index.py`.
3. Provide you with a live URL (e.g. `https://flavorfusion-ai.vercel.app`).

---

## 💻 Option 2: Deploy Using the Vercel CLI

If you prefer deploying directly from your local terminal:

```bash
# 1. Install Vercel CLI globally
npm install -g vercel

# 2. Log in to your Vercel account
vercel login

# 3. Deploy preview
vercel

# 4. Deploy to production
vercel --prod
```

---

## 🌐 Option 3: Split Deployment (Frontend on Vercel + Backend on Render / Railway)

If you prefer running the Python FastAPI backend as a persistent container service:

1. **Deploy Backend**:
   - Push repository to GitHub.
   - On **Render.com** or **Railway.app**, create a new Web Service using the `backend/` folder or Dockerfile.
   - Note your backend URL (e.g., `https://flavorfusion-backend.onrender.com`).

2. **Deploy Frontend on Vercel**:
   - In Vercel, set **Root Directory** to `frontend`.
   - Add environment variable:
     ```
     VITE_API_BASE=https://flavorfusion-backend.onrender.com/api
     ```
   - Click **Deploy**.

---

## 📁 Architecture Files Configured

- `vercel.json`: Directs `/api/*` requests to the Python serverless entrypoint and all other routes to React Router's `index.html`.
- `api/index.py`: Serverless ASGI entrypoint exposing FastAPI's `app`.
- `api/requirements.txt` & `requirements.txt`: Python package dependencies.
- `package.json`: Root build orchestration script for Vercel.
- `frontend/src/services/api.ts`: Supports both relative `/api` and external `VITE_API_BASE`.
