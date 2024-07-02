[Setup]
AppName=CopyBurst
AppVersion=1.0
DefaultDirName={pf}\CopyBurst
DefaultGroupName=CopyBurst
OutputDir=./Output
OutputBaseFilename=CopyBurst_setup
PrivilegesRequired=admin
AllowCancelDuringInstall=yes
DisableProgramGroupPage=yes

[Files]
; Include the standalone executable
Source: "dist\main\main.exe"; DestDir: "{app}"; Flags: ignoreversion

; Include the Python DLLs and the entire Python runtime environment
Source: "dist\main\_internal\*"; DestDir: "{app}\_internal"; Flags: ignoreversion

[Icons]
Name: "{autoprograms}\CopyBurst"; Filename: "{app}\main.exe"; WorkingDir: "{app}"

[Run]
Filename: "{app}\main.exe"; Description: "Run CopyBurst"; Flags: nowait postinstall skipifsilent
