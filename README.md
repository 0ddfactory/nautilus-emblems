# Nautilus Emblems

A file marking extension for Nautilus (GTK 4)
Forked from costales/folder-color in order to achieve two goals:
1. Remove unneeded code for changing folder colors
2. Bypass a bug caused by part of the original code meant to change the folder colors causing nautilus to crash on launch when folders are bookmarked.

# INSTALL

In project directory:
```
chmod +x install.sh
sudo ./install.sh
nautilus -q
```

# UNINSTALL

In project directory:
```
chmod +x uninstall.sh
sudo ./uninstall.sh
nautilus -q
```

# EMBLEMS 

Nautilus Emblems will use any of these standard emblems:

 * `emblem-important`
 * `emblem-urgent`
 * `emblem-favorite`
 * `emblem-default`
 * `emblem-new`
