[Setup]
AppName=CyberCloak_Demo
AppVersion=1.5.23
DefaultDirName={commonpf}\CyberCloak_Demo
DefaultGroupName=CyberCloak_Demo
OutputDir=.\installer_output
OutputBaseFilename=CyberCloakInstaller_1.5.23
Compression=lzma
SolidCompression=yes
PrivilegesRequired=admin
DisableDirPage=no

[Files]
Source: "CyberCloak_Demo.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "assets\cc_icon.ico"; DestDir: "{app}\assets"; Flags: ignoreversion

; Include config and logs folders
Source: "config\*"; DestDir: "{app}\config"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "logs\*"; DestDir: "{app}\logs"; Flags: ignoreversion recursesubdirs createallsubdirs

; Include readme file
Source: "README.txt"; DestDir: "{app}"; Flags: ignoreversion isreadme

[Icons]
Name: "{group}\CyberCloak Demo"; Filename: "{app}\CyberCloak_Demo.exe"; IconFilename: "{app}\assets\cc_icon.ico"
Name: "{commondesktop}\CyberCloak Demo"; Filename: "{app}\CyberCloak_Demo.exe"; IconFilename: "{app}\assets\cc_icon.ico"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop icon"; GroupDescription: "Additional icons:"
