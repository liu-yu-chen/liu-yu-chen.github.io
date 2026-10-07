@echo off
cd /d "%~dp0"
hugo --cleanDestinationDir --minify
if errorlevel 1 exit /b 1
echo Built website in public\. See README.md for upload instructions.
