@echo off
echo ===============================
echo Building main.exe...
echo ===============================

python -m PyInstaller --noconsole --onefile --add-data "config.json;." main.py

echo.
echo Build complete!
echo Your EXE is in the /dist folder.
echo ===============================
pause