#!/usr/bin/env python
import os, gtk, appindicator, getpass
import gdplib as lib

drive_dir = open('/home/' + getpass.getuser() + '/.drive_dir').read().strip()

ind = appindicator.Indicator("google-drive-panel", "indicator-messages", appindicator.CATEGORY_APPLICATION_STATUS)
ind.set_status(appindicator.STATUS_ACTIVE)
ind.set_icon("/usr/share/google-drive-panel/google_drive_icon.png")

menu = gtk.Menu()

item1 = gtk.MenuItem("Update Google Drive")
item1.connect("activate", lib.update)

item2 = gtk.MenuItem("Add Files")
item2.connect("activate", lib.add_file)

item3 = gtk.MenuItem("Open Folder")
item3.connect("activate", lib.open_folder)

item4 = gtk.MenuItem("Open Online")
item4.connect("activate", lib.open_online)

item5 = gtk.MenuItem("Settings")
item5.connect("activate", lib.setting)

item6 = gtk.MenuItem("Quit")
item6.connect("activate",  gtk.main_quit)


item1.show()
item2.show()
item3.show()
item4.show()
item5.show()
item6.show()

menu.append(item1)
menu.append(item2)
menu.append(item3)
menu.append(item4)
menu.append(item5)
menu.append(item6)


ind.set_menu(menu)

gtk.main()
