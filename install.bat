@echo off
REM Child Management System - Windows Installation Script
REM This script automates the setup process

echo ================================
echo Child Management System Installer
echo ================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

echo [✓] Python found
echo.

REM Check if MongoDB is installed
mongod --version >nul 2>&1
if %errorlevel% neq 0 (
    echo WARNING: MongoDB might not be installed or not in PATH
    echo Please install MongoDB from https://www.mongodb.com/try/download/community
    echo.
)

echo [✓] Starting installation...
echo.

REM Create virtual environment
echo [1/4] Creating virtual environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)
echo [✓] Virtual environment created
echo.

REM Activate virtual environment
echo [2/4] Activating virtual environment...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)
echo [✓] Virtual environment activated
echo.

REM Upgrade pip
echo [3/4] Upgrading pip...
python -m pip install --upgrade pip >nul 2>&1
echo [✓] Pip upgraded
echo.

REM Install requirements
echo [4/4] Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo [✓] Dependencies installed
echo.

echo ================================
echo Installation Complete!
echo ================================
echo.
echo Next steps:
echo 1. Make sure MongoDB is running (mongod command or MongoDB service)
echo 2. Activate virtual environment: venv\Scripts\activate.bat
echo 3. Run the app: python app.py
echo 4. Open browser: http://localhost:5000
echo.
echo For detailed instructions, see README.md
echo.
pause
