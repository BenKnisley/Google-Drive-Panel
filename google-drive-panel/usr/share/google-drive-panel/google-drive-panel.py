#!/usr/bin/env python
import os, os.path, sys, getpass

#Help Message, needs more added
def help():
	print('usage:')
	print('google-drive-panel [--setup]  [--update]')
	print('--setup    enters setup')
	print('--update    updates to Google Drive... duh')
	exit()

#update
def update():
	os.system('cd ' + drive_dir + ' && grive')
	exit()

#Starts Setup
def setup():
	if os.path.isfile('/home/' + getpass.getuser() + '/.drive_dir') == True:
		os.remove('/home/' + getpass.getuser() + '/.drive_dir')
	print 'Setting up, may take a while'
	os.system('/usr/share/google-drive-panel/setup.py > /dev/null')
	exit()

#Starts Gdrive panel
def start():
	os.system('/usr/share/google-drive-panel/main.py > /dev/null')
	print 'Google Drive Panel Started! You can close this terminal now'
	exit()


try:	#Tests to see if there is any command args
    sys.argv[1]
except IndexError:	#if there isn't any comm args
	if os.path.isfile('/home/' + getpass.getuser() + '/.drive_dir') == False:	#Test if setup is run yet
		setup()		 #If it has hasn't run, run it
	else:
		start()		#If it has, run gdrive panel

command = sys.argv[1]
commands = ['--update', '--help', '--setup', '--start']

if command in commands:

	if command == '--update':
		update()
	if command == '--help':
		help()
	if command == '--setup':
		setup()
	if command == '--start':
		start()

else:
	help()
	exit()





