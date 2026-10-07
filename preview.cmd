@echo off
cd /d "%~dp0"
where hugo >nul 2>nul
if errorlevel 1 (
  echo Hugo is required. See README.md.
  pause
  exit /b 1
)
echo Open http://localhost:1313/ or http://localhost:1313/zh/
hugo server --bind 127.0.0.1 --port 1313 --disableLiveReload
