@echo off
echo ===============================
echo Creating portable ZIP package...
echo ===============================

if not exist dist\cmainlock.exe (
    echo ERROR: main.exe not found. Build first!
    pause
    exit /b
)

cd dist
powershell Compress-Archive -Path main.exe, ..\config.cfg -DestinationPath main-portable.zip -Force
cd ..

echo Portable ZIP created: dist\main-portable.zip
echo ===============================
pause