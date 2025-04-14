@echo off
set /p userVer=Enter version number (e.g., 2.0.8): 

:: Write to version.ini
echo [Version]> version.ini
echo AppVer=%userVer%>> version.ini

:: Pass it to .iss script as a DEFINE variable
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" /DAppVer="%userVer%" "CC_Demo_Script.iss"
pause