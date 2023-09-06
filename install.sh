#!/bin/bash

#Install Script
#Version = "1.0.0"

# po
sed -i 's/folder_i18n/nautilus-emblems/' ./po/POTFILES.in
sed -i 's/folder_path/nautilus-extension/' ./po/POTFILES.in
sed -i 's/folder_i18n/nautilus-emblems/' ./nautilus-extension/nautilus-emblems.py

cp ./nautilus-extension/nautilus-emblems.py /usr/share/nautilus-python/extensions/

echo "Done"
