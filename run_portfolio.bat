@echo off
REM ============================================================
REM  Vignesh Personal Portfolio — One-Click Launcher
REM  Requirements: Python 3.10+  (https://www.python.org)
REM ============================================================

title Vignesh Portfolio - AI Powered

echo.
echo  ========================================================
echo    VIGNESH PERSONAL PORTFOLIO
echo    Powered by IBM Granite (Agentic AI) + Streamlit
echo  ========================================================
echo.

REM ── Locate Python ────────────────────────────────────────────
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo  [ERROR] Python not found. Please install Python 3.10+
    echo          Download: https://www.python.org/downloads/
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('python --version 2^>^&1') do set PYVER=%%i
echo  [INFO]  Using %PYVER%

REM ── Change to script directory ────────────────────────────────
cd /d "%~dp0"
echo  [INFO]  Working directory: %CD%

REM ── Create virtual environment if needed ─────────────────────
if not exist ".venv\Scripts\activate.bat" (
    echo.
    echo  [SETUP] Creating virtual environment (.venv) ...
    python -m venv .venv
    if %errorlevel% neq 0 (
        echo  [ERROR] Failed to create virtual environment.
        pause
        exit /b 1
    )
    echo  [OK]    Virtual environment created.
)

REM ── Activate venv ─────────────────────────────────────────────
call .venv\Scripts\activate.bat
echo  [OK]    Virtual environment activated.

REM ── Install / upgrade dependencies ───────────────────────────
echo.
echo  [SETUP] Installing / verifying dependencies from requirements.txt ...
pip install -q -r requirements.txt
if %errorlevel% neq 0 (
    echo  [ERROR] Dependency installation failed. Check your internet connection.
    pause
    exit /b 1
)
echo  [OK]    All dependencies satisfied.

REM ── .env file reminder ───────────────────────────────────────
if not exist ".env" (
    echo.
    echo  [WARN]  No .env file found!
    echo          The AI Assistant will run in demo mode.
    echo          To enable IBM Granite AI:
    echo            1. Copy .env.example to .env
    echo            2. Add your WATSONX_API_KEY and WATSONX_PROJECT_ID
    echo          Get keys at: https://cloud.ibm.com/iam/apikeys
    echo.
)

REM ── Launch Streamlit ──────────────────────────────────────────
echo.
echo  [INFO]  Launching portfolio at http://localhost:8501
echo          Press Ctrl+C in this window to stop the server.
echo.
echo  ========================================================
echo.

streamlit run app.py --server.port 8501

REM ── On exit ───────────────────────────────────────────────────
echo.
echo  [INFO]  Portfolio server stopped.
pause
