@echo off
python bump_version.py
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" "CyberCloakInstaller.iss"
pause