#!/bin/bash

rm -rf ../.git
rm ../README.md

# po
sed -i 's/folder_i18n/nautilus-emblems/' ../po/POTFILES.in
sed -i 's/folder_path/nautilus-extension/' ../po/POTFILES.in
sed -i 's/folder_i18n/nautilus-emblems/' ../nautilus-extension/nautilus-emblems.py

cp ../nautilus-extension/nautilus-emblems.py /usr/share/share/nautilus-python/extensions/

# myself
rm -rf ../install-scripts

echo "Done"
