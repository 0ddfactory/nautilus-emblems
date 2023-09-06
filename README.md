# Nautilus Emblems

**A file marking extension for Nautilus (GTK 4)**  

-Forked from costales/folder-color in order to achieve two goals:
 1. Remove unneeded code for changing folder colors for people who only need to mark files.
 2. Bypass a bug caused by part of the original code meant to change the folder colors causing nautilus to crash on launch when folders are bookmarked.

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
sudo ./install.sh
nautilus -q
```
OR

Install via AUR:

[![b68973092ba1e00cde8083c5b3050af3a538b2e1b8b49d317477b7b53494baa11bdd3af9fe3cb6a58982ac9dfd9808610ac36c39288009eea6db0f591b816a25](https://github.com/0ddfactory/nautilus-emblems/assets/25939455/525429ce-ce99-4f13-84b6-4ccb57c7b197)](https://aur.archlinux.org/packages/nautilus-emblems)


# UNINSTALL

In project directory:
```
chmod +x uninstall.sh
sudo ./uninstall.sh
nautilus -q
```
