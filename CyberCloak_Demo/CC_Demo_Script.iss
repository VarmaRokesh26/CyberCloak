[Setup]
AppName=CyberCloak_demo
AppVersion=1.0
DefaultDirName={pf}\CyberCloak_demo
DefaultGroupName=CyberCloak_demo
OutputDir=.\installer_output
OutputBaseFilename=CyberCloakInstaller
Compression=lzma
SolidCompression=yes
PrivilegesRequired=admin

[Files]
; Make sure the EXE is sourced correctly
Source: "CyberCloak_demo.exe"; DestDir: "{app}"; Flags: ignoreversion

; Include config and logs folders
Source: "config\*"; DestDir: "{app}\config"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "logs\*"; DestDir: "{app}\logs"; Flags: ignoreversion recursesubdirs createallsubdirs

; Include readme file
Source: "README.txt"; DestDir: "{app}"; Flags: ignoreversion isreadme

[Icons]
Name: "{group}\CyberCloak_demo"; Filename: "{app}\CyberCloak__demo.exe"
Name: "{commondesktop}\CyberCloak_demo"; Filename: "{app}\CyberCloak__demo.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop icon"; GroupDescription: "Additional icons:"
