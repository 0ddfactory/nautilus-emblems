#!/usr/bin/env python3

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import os, sys, glob, DistUtilsExtra.auto

# Create data files
data = [ ('/usr/share/nautilus-python/extensions',   ['nautilus-extension/folder-color.py']),]

# Setup stage
DistUtilsExtra.auto.setup(
    name         = "nautilus-emblems",
    version      = "1.0.0",
    description  = "A file marking extension for Nautilus",
    author       = "0ddfactory"
    url          = "https://github.com/0ddfactory/nautilus-emblems",
    license      = "GPL3",
    data_files   = data
)

