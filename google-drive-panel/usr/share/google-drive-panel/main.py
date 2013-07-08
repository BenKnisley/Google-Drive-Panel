#!/usr/bin/env python
import pygtk, getpass
pygtk.require('2.0')
import os, gtk, appindicator, time, string

drive_dir = open('/home/' + getpass.getuser() + '/.drive_dir').read().strip()

class AppIndicatorExample:
    def __init__(self):
		self.ind = appindicator.Indicator ("google-drive-panel", "indicator-messages", appindicator.CATEGORY_APPLICATION_STATUS)
		self.ind.set_status (appindicator.STATUS_ACTIVE)
		self.ind.set_icon("/usr/share/google-drive-panel/google_drive_icon.png")

		self.menu = gtk.Menu()
        
		item = gtk.MenuItem("Update Google Drive")
		item.connect("activate", self.update)
		item.show()
		self.menu.append(item)

		item = gtk.MenuItem("Upload Files")
		item.connect("activate", self.upload)
		item.show()
		self.menu.append(item)

		item = gtk.MenuItem("Open Google Drive Folder")
		item.connect("activate", self.openfol)
		item.show()
		self.menu.append(item)

		self.ind.set_menu(self.menu)
        
    def openfol(self, widget, data=None):
		os.system('xdg-open ' + drive_dir)

    def upload(self, widget, data=None):
		os.system("/usr/share/google-drive-panel/newfile.py")
		os.system('cd ' + drive_dir + ' && grive')
		os.system("notify-send 'Done Copying File(s)'")

    def update(self, widget, data=None):
		os.system('cd ' + drive_dir + ' && grive')
		os.system("notify-send 'Done Copying File(s)'")

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    indicator = AppIndicatorExample()
    main()
