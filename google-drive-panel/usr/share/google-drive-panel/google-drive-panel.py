#!/usr/bin/env python
import os, os.path, sys, getpass, webbrowser

drive_dir = open('/home/' + getpass.getuser() + '/.drive_dir').read().strip()

########################################
############## FUNCTIONS ###############
########################################

def start():#Start
	os.system('/usr/share/google-drive-panel/main.py > /dev/null &')
	os.system('/usr/share/google-drive-panel/timeupdate.py > /dev/null &')
	print 'Google Drive Panel Started! You can close this terminal now'
	exit()

def help():#Help
	print('usage:')
	print('google-drive-panel [--setup]  [--update]')
	print('--setup    enters setup')
	print('--update    updates to Google Drive... duh')
	exit()

def update():#update
	os.system('cd ' + drive_dir + ' && grive')
	exit()

def setup():#Setup
	if os.path.isfile('/home/' + getpass.getuser() + '/.drive_dir') == True:
		os.remove('/home/' + getpass.getuser() + '/.drive_dir')
	print 'Setting up, may take a while'
	os.system('/usr/share/google-drive-panel/setup.py > /dev/null')
	exit()

def open_folder():#opens google drive folder
	os.system('xdg-open ' + drive_dir)
	exit()

def open_online():#opens google drive online
	webbrowser.open('http://drive.google.com')
	exit()

########################################
############## MAIN ####################
########################################

try:	#Tests to see if there is any command args
    sys.argv[1]
except IndexError:	#if there isn't any comm args
	if os.path.isfile('/home/' + getpass.getuser() + '/.drive_dir') == False:	#Test if setup is run yet
		setup()		 #If it has hasn't run, run it
	else:
		start()		#If it has, run gdrive panel

command = sys.argv[1]
commands = ['--start','--update','--open-folder','--open-online', '--help', '--setup', ]

if command in commands:
	if command == '--update':
		update()
	if command == '--help':
		help()
	if command == '--setup':
		setup()
	if command == '--start':
		start()
	if command == '--open-folder':
		open_folder()
	if command == '--open-online':
		open_online()
else:
	help()
	exit()





