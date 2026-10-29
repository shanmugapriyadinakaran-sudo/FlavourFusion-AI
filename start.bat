@echo off
title FlavorFusion AI Launcher
echo ========================================================
echo          Starting FlavorFusion AI Platform...
echo ========================================================
echo.

:: 1. Start Backend in a separate window
echo [1/2] Starting Backend API Server (FastAPI on port 8000)...
start "FlavorFusion AI - Backend" cmd /k "cd /d %~dp0backend && .\venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload"

:: 2. Wait 3 seconds for backend to initialize
timeout /t 3 /nobreak >nul

:: 3. Start Frontend in a separate window
echo [2/2] Starting Frontend App (Vite on port 5173)...
start "FlavorFusion AI - Frontend" cmd /k "cd /d %~dp0frontend && npm run dev"

:: 4. Wait 2 seconds and open browser
timeout /t 2 /nobreak >nul
echo.
echo Opening browser at http://localhost:5173...
start http://localhost:5173

echo.
echo ========================================================
echo FlavorFusion AI is running!
echo   Frontend: http://localhost:5173
echo   Backend API / Docs: http://127.0.0.1:8000/docs
echo.
echo Leave this window or close it at any time.
echo To stop the servers, close the Backend and Frontend windows.
echo ========================================================
pause
