@echo off
set /p userVer=Enter version number (e.g., 2.0.8): 

:: Write to version.ini
echo [Version]> version.ini
echo AppVer=%userVer%>> version.ini

"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" "CC_Premium_Lite_Script.iss"

pause
