[Setup]
AppName=CyberCloak_Premium_Lite
AppVersion=2.6.23
DefaultDirName={commonpf}\CyberCloak_Premium_Lite
DefaultGroupName=CyberCloak_Premium_Lite
OutputDir=.\installer_output
OutputBaseFilename=CyberCloakInstaller_2.6.23
Compression=lzma
SolidCompression=yes
PrivilegesRequired=admin
DisableDirPage=no

[Files]
Source: "CyberCloak_Premium_Lite.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "assets\cc_icon.ico"; DestDir: "{app}\assets"; Flags: ignoreversion

; Include config and logs folders
Source: "config\*"; DestDir: "{app}\config"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "logs\*"; DestDir: "{app}\logs"; Flags: ignoreversion recursesubdirs createallsubdirs

; Include readme file
Source: "README.txt"; DestDir: "{app}"; Flags: ignoreversion isreadme

[Icons]
Name: "{group}\CyberCloak Premium Lite"; Filename: "{app}\CyberCloak_Premium_Lite.exe"; IconFilename: "{app}\assets\cc_icon.ico"
Name: "{commondesktop}\CyberCloak Premium Lite"; Filename: "{app}\CyberCloak_Premium_Lite.exe"; IconFilename: "{app}\assets\cc_icon.ico"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop icon"; GroupDescription: "Additional icons:"
