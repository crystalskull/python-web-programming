FTP:
====
  Use following commands to enable/disable local FTP server
  on MAC

  Enable:
  ======
  sudo -s launchctl load -w /System/Library/LaunchDaemons/ftp.plist

  Cross check if server is enabled by typing following command and check
  if login is prompted:
  cmd --> FTP localhost

  Disable:
  =======
  sudo -s launchctl unload -w /System/Library/LaunchDaemons/ftp.plist

EMAIL:
======
  To send and receive email using python programs make sure that in account
  settings 'Use less secure app' settings is enabled.


