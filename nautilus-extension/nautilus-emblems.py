# Nautilus Emblems 1.0 - https://github.com/0ddfactory/nautilus-emblems
# Copyright (C) 2023-2024 0ddfactory
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# THIS IS A MODIFICATION OF FOLDER-COLOR REMOVING UNNECESSARY CODE
# FOR THE PURPOSE OF EMBLEM MARKING FILES.

import os, gettext, gi
from pathlib import Path
gi.require_version("Gtk", "4.0")
from gi.repository import Nautilus, Gtk, Gdk, GObject, Gio, GLib

# i18n
gettext.textdomain("nautilus-emblems")
_ = gettext.gettext
EMBLEMS_ALL = {
    "emblem-important": _("Important"),
    "emblem-urgent": _("In Progress"),
    "emblem-favorite": _("Favorite"),
    "emblem-default": _("Finished"),
    "emblem-new": _("New")
}
ICON_SIZE = 48

class NautilusEmblems:
    """Nautilus Emblems Class"""
    def __init__(self):
        self.is_modified = False
        self.emblems = []

    def _get_icon(self, icon_name):
        """Get icon, label and URI"""
        icon_theme = Gtk.IconTheme.get_for_display(Gdk.Display.get_default())
        icon = icon_theme.lookup_icon(icon_name, None, 48, 1, Gtk.TextDirection.LTR, Gtk.IconLookupFlags.FORCE_REGULAR)
        if icon_theme.has_icon(icon_name):
            return {"icon": Path(icon.get_icon_name()).stem, "uri": icon.get_file().get_uri()}
        else:
            return {"icon": "", "uri": ""}

    def set_emblems_theme(self):
        """Available emblems into system"""
        self.emblems.clear()
        for emblem in EMBLEMS_ALL.keys():
            icon_aux = self._get_icon(emblem)
            if icon_aux["icon"]:
                self.emblems.append({"icon": icon_aux["icon"], "label": EMBLEMS_ALL[emblem], "uri": icon_aux["uri"]})

    def get_emblems_theme(self):
        return self.emblems

    def set_emblem(self, item, emblem):
        emblem_aux = []
        emblem_aux.append(emblem["icon"])
        emblems = list(emblem_aux)
        emblems.append(None) # Needs
        item_aux = Gio.File.new_for_path(item)
        info = item_aux.query_info("metadata::emblems", 0, None)
        info.set_attribute_stringv("metadata::emblems", emblems)
        item_aux.set_attributes_from_info(info, 0, None)
        self._reload_icon(item)

    def set_restore(self, item):
        self._set_restore_emblem(item)
        self._reload_icon(item)

    def _set_restore_emblem(self, item):
        item_aux = Gio.File.new_for_path(item)
        info = item_aux.query_info("metadata::emblems", 0, None)
        info.set_attribute("metadata::emblems", Gio.FileAttributeType.INVALID, 0)
        item_aux.set_attributes_from_info(info, 0, None)

    def _reload_icon(self, item):
        os.utime(item, None)

    def get_is_modified(self, items):
        """Restore is enabled?"""
        # For each dir, search custom icon or emblem
        for item in items:
            # Get metadata file/folder
            item_path = item.get_location().get_path()
            item = Gio.File.new_for_path(item_path)
            info = item.query_info("metadata", 0, None)
            # If any metadata then restore menu
            if info.get_attribute_as_string("metadata::custom-icon-name") or \
               info.get_attribute_as_string("metadata::custom-icon") or \
               info.get_attribute_as_string("metadata::emblems"):
                self.is_modified = True
                return True
        self.is_modified = False
        return False

class NautilusEmblemsMenu(GObject.GObject, Nautilus.MenuProvider):
    """File Browser Menu"""
    def __init__(self):
        GObject.Object.__init__(self)
        self.all_dirs = True
        self.nautilusemblems = NautilusEmblems()
        self.theme = Gtk.Settings.get_default().get_property("gtk-icon-theme-name")
        self._load_theme()

    def get_file_items(self, items):
        """Click on directories or files"""
        if self._check_show_menu(items):
            if self.theme != Gtk.Settings.get_default().get_property("gtk-icon-theme-name"):
                self.theme = Gtk.Settings.get_default().get_property("gtk-icon-theme-name")
                self._load_theme()
            return self._show_menu(items)

    def _load_theme(self):
        self.nautilusemblems.set_emblems_theme()

    def _check_show_menu(self, items):
        if not items:
            return False
        
        self.all_dirs = True
        for item in items:
            # GNOME can only handle files
            if item.get_uri_scheme() != "file":
                return False
            if not item.is_directory():
                self.all_dirs = False
        return True

    def _show_menu(self, items):
        """Menu for [directories|files]: [Color,Restore,Emblems|Emblems,Restore]"""
        # Directories
        emblems = self.nautilusemblems.get_emblems_theme()
        is_modified = self.nautilusemblems.get_is_modified(items)

        # Main menu
        if emblems:
            top_menuitem = Nautilus.MenuItem(name="NautilusEmblemsMenu::colors", label=_("Emblem"))
        else:
            return
        submenu = Nautilus.Menu()
        top_menuitem.set_submenu(submenu)

        # Emblems
        if emblems:
            if self.all_dirs and colors:
                item = Nautilus.MenuItem(name="NautilusEmblemsMenu::emblems", label="―――", sensitive=False)
                submenu.append_item(item)
            for emblem in emblems:
                item = Nautilus.MenuItem(name="NautilusEmblemsMenu::emblem_" + emblem["icon"], label=emblem["label"], icon=emblem["icon"])
                item.connect("activate", self._menu_activate_emblem, items, emblem)
                submenu.append_item(item)
        # Restore
        if is_modified:
            item = Nautilus.MenuItem(name="ChangeFolderEmblemMenu::separator", label="―――", sensitive=False)
            submenu.append_item(item)
            item = Nautilus.MenuItem(name="NautilusEmblemsMenu::restore", label=_("Default"), icon="undo")
            item.connect("activate", self._menu_activate_restore, items)
            submenu.append_item(item)

        return top_menuitem,

    def _menu_activate_emblem(self, menu, items, emblem):
        """Menu: Clicked emblem"""
        for item in items:
            if not item.is_gone():
                self.nautilusemblems.set_emblem(item.get_location().get_path(), emblem)

    def _menu_activate_restore(self, menu, items):
        """Menu: Clicked restore"""
        for item in items:
            if not item.is_gone():
                self.nautilusemblems.set_restore(item.get_location().get_path())
