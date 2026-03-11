@echo off
echo ===============================
echo Cleaning old build files...
echo ===============================

rmdir /s /q build
rmdir /s /q dist
del main.spec

echo Clean complete!
echo ===============================
pause