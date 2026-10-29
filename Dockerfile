# ===================================================
# Stage 1: Build React Vite Frontend
# ===================================================
FROM node:20-slim AS frontend-builder
WORKDIR /app/frontend

# Install dependencies cleanly for Linux
COPY frontend/package.json ./
RUN npm install

# Copy source configuration and code
COPY frontend/src ./src
COPY frontend/index.html ./
COPY frontend/vite.config.ts ./
COPY frontend/tsconfig.json ./
COPY frontend/tailwind.config.js ./
COPY frontend/postcss.config.js ./

# Compile production bundle
RUN npm run build

# ===================================================
# Stage 2: Python FastAPI Backend + Served Frontend
# ===================================================
FROM python:3.11-slim
WORKDIR /app

# Install system compilation packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
COPY backend/requirements.txt ./backend/
RUN pip install --no-cache-dir -r backend/requirements.txt

# Copy backend application source
COPY backend/ ./backend/

# Copy compiled frontend from Stage 1 into frontend/dist
COPY --from=frontend-builder /app/frontend/dist ./frontend/dist

# Expose default port
ENV PORT=8000
EXPOSE 8000

# Start Uvicorn ASGI server
CMD ["sh", "-c", "cd backend && uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
