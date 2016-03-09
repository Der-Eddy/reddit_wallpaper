; Script generated by the Inno Script Studio Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Reddit_Wallpaper"
#define MyAppVersion "1.0"
#define MyAppPublisher "Der-Eddy"
#define MyAppURL "https://github.com/Der-Eddy/reddit_wallpaper"
#define MyAppExeName "wallpaper.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{BD9453D5-4933-442C-909E-E63C9DB4A949}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={pf}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
LicenseFile=C:\Users\Eduard\Dev\Python\reddit_wallpaper\LICENSE
OutputDir=C:\Users\Eduard\Dev\Python\reddit_wallpaper\setup
OutputBaseFilename=reddit_wallpaper_setup
SetupIconFile=C:\Users\Eduard\Dev\Python\reddit_wallpaper\icon.ico
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: startup; Description: "Automatically start on login"; GroupDescription: "{cm:AdditionalIcons}"

[Files]
Source: "C:\Users\Eduard\Dev\Python\reddit_wallpaper\dist\wallpaper\wallpaper.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Eduard\Dev\Python\reddit_wallpaper\dist\wallpaper\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon
Name: "{userstartup}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: startup

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent