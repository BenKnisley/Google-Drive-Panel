#!/usr/bin/env python
import os, getpass, 
import gdplib as lib

drive_dir = open('/home/' + getpass.getuser() + '/.drive_dir').read().strip()

try:
    sys.argv[1]
except IndexError:
	if os.path.isfile('/home/' + getpass.getuser() + '/.drive_dir') == False:
		lib.setup()	
	else:
		lib.start()	

command = sys.argv[1]
commands = ['--start','--update','--open-folder','--open-online', '--add-file', '--help', '--setup', ]

if command in commands:
	if command == '--update':
		lib.update()
	if command == '--help':
		lib.help()
	if command == '--setup':
		lib.setup()
	if command == '--start':
		lib.start()
	if command == '--open-folder':
		lib.open_folder()
	if command == '--open-online':
		lib.open_online()
	if command == '--add-file':
		lib.add_file()
else:
	help()
	exit()





