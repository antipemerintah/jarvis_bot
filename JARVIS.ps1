# JARVIS ASSISTANT - PowerShell Launcher
$pythonPath = "C:\Users\Admin\AppData\Local\Programs\Python\Python312\python.exe"
$scriptPath = Split-Path -Path $MyInvocation.MyCommand.Definition
$jarvisScript = Join-Path $scriptPath "jarvis_text.py"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "JARVIS ASSISTANT BOT" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

if (-not (Test-Path $pythonPath)) {
    Write-Host "[ERROR] Python 3.12 tidak ditemukan!" -ForegroundColor Red
    Write-Host "Path: $pythonPath" -ForegroundColor Red
    Read-Host "Press Enter untuk keluar"
    exit 1
}

if (-not (Test-Path $jarvisScript)) {
    Write-Host "[ERROR] Script jarvis_text.py tidak ditemukan!" -ForegroundColor Red
    Read-Host "Press Enter untuk keluar"
    exit 1
}

Write-Host "[OK] Python 3.12 ditemukan" -ForegroundColor Green
Write-Host "[OK] Script ditemukan" -ForegroundColor Green
Write-Host ""
Write-Host "Menjalankan JARVIS..." -ForegroundColor Yellow
Write-Host ""

& $pythonPath $jarvisScript
