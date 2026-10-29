# FlavorFusion AI - PowerShell Launcher
$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host "========================================================" -ForegroundColor Green
Write-Host "         Starting FlavorFusion AI Platform...          " -ForegroundColor Green
Write-Host "========================================================" -ForegroundColor Green
Write-Host ""

# 1. Start Backend in separate window
Write-Host "[1/2] Starting Backend API Server (port 8000)..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$projectRoot\backend'; .\venv\Scripts\Activate.ps1; python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload"

Start-Sleep -Seconds 3

# 2. Start Frontend in separate window
Write-Host "[2/2] Starting Frontend App (port 5173)..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$projectRoot\frontend'; npm run dev"

Start-Sleep -Seconds 2

# 3. Open browser
Write-Host "Opening http://localhost:5173 in your browser..." -ForegroundColor Yellow
Start-Process "http://localhost:5173"

Write-Host ""
Write-Host "Servers launched successfully!" -ForegroundColor Green
Write-Host "Frontend:  http://localhost:5173" -ForegroundColor White
Write-Host "API Docs:  http://127.0.0.1:8000/docs" -ForegroundColor White
Write-Host "To shut down, simply close the opened PowerShell windows." -ForegroundColor Gray
