#!/bin/bash


[ "$UID" -eq 0 ] || exec sudo "$0" "$@"
rm /usr/share/nautilus-python/extensions/nautilus-emblems.py

echo "Done"
