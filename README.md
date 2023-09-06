# Nautilus Emblems

**A file marking extension for Nautilus (GTK 4)**  

-Forked from costales/folder-color in order to achieve two goals:
 1. Remove code unneeded for marking files with emblems in Nautilus simplifying the extension.
 2. Bypass a bug caused by the folder color changing code causing nautilus to crash on launch when folders are bookmarked.

# EMBLEMS 

![image](https://github.com/0ddfactory/nautilus-emblems/assets/25939455/4e59af49-d1da-4c27-a927-bb358ad84884)

Nautilus Emblems will use any of these standard emblems:

 * `emblem-important`
 * `emblem-urgent`
 * `emblem-favorite`
 * `emblem-default`
 * `emblem-new`

# INSTALL

In project directory:
```
chmod +x install.sh
./install.sh
nautilus -q
```
OR

Install via AUR with yay:
```
yay -S nautilus-emblems
```
![AUR](https://github.com/0ddfactory/nautilus-emblems/assets/25939455/525429ce-ce99-4f13-84b6-4ccb57c7b197)


# UNINSTALL

In project directory:
```
chmod +x uninstall.sh
./uninstall.sh
nautilus -q
```
