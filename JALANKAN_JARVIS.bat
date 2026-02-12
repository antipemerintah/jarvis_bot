@echo off
chcp 65001 >nul
cls
echo.
echo ================================================
echo    JARVIS ASSISTANT BOT - LAUNCHER
echo ================================================
echo.

set PYTHON_PATH=C:\Users\Admin\AppData\Local\Programs\Python\Python312\python.exe

if not exist "%PYTHON_PATH%" (
    echo [ERROR] Python 3.12 tidak ditemukan!
    echo Lokasi: %PYTHON_PATH%
    pause
    exit /b 1
)

echo [INFO] Mencoba versi Windows TTS (lebih stabil)...
echo.
"%PYTHON_PATH%" "%~dp0jarvis_windows.py"

if not %errorlevel% equ 0 (
    echo.
    echo [INFO] WindowsTTS tidak tersedia, mencoba pyttsx3...
    "%PYTHON_PATH%" "%~dp0jarvis_text.py"
)

pause

