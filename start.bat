@echo off
REM Start the API in a new console window
start "" cmd /k "python -m uvicorn main:app --port 8000"
REM Wait a few seconds for the server to initialize
timeout /t 5 /nobreak >nul

REM Locate movie_tracker_ui.html relative to this script’s directory
set "UIFile="
for /r "%~dp0" %%f in (movie_tracker_ui.html) do (
  set "UIFile=%%f"
  goto :found
)
:found

REM If the file was found, open it; otherwise print an error
if defined UIFile (
  start "" "%UIFile%"
) else (
  echo Movie Tracker UI file not found. Ensure it exists in the project directory.
  pause
)
