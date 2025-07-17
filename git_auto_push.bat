@echo off
setlocal enabledelayedexpansion

:: Get current date and time
for /f %%i in ('powershell -command "Get-Date -Format yyyy-MM-dd_HH-mm-ss"') do set timestamp=%%i

:: Ask user for commit message
set /p usermsg=Enter commit message: 

:: Combine message with timestamp
set commitmsg=%usermsg% [%timestamp%]

:: Git commands
git add .
git commit -m "%commitmsg%"
git push origin main

pause
