#!/usr/bin/env python
import os, os.path, sys, getpass, webbrowser
drive_dir = open('/home/' + getpass.getuser() + '/.drive_dir').read().strip()

########################################
############## FUNCTIONS ###############
########################################


def start(*args):#Start
	os.system('/usr/share/google-drive-panel/main.py > /dev/null &')
	os.system('/usr/share/google-drive-panel/timeupdate.py > /dev/null &')
	print 'Google Drive Panel Started! You can close this terminal now'
	return

def add_file(*args):#Start
	os.system("/usr/share/google-drive-panel/newfile.py")
	return

def help(*args):#Help
	print('usage:')
	print('google-drive-panel [--setup]  [--update]')
	print('--setup    enters setup')
	print('--update    updates to Google Drive... duh')
	return

def update(*args):#update
	os.system('cd ' + drive_dir + ' && grive')
	os.system("notify-send 'Done Copying File(s)'")
	return

def setup(*args):#Setup
	if os.path.isfile('/home/' + getpass.getuser() + '/.drive_dir') == True:
		os.remove('/home/' + getpass.getuser() + '/.drive_dir')
	print 'Setting up, may take a while'
	os.system('/usr/share/google-drive-panel/setup.py > /dev/null')
	return

def open_folder(*args):#opens google drive folder
	os.system('xdg-open ' + drive_dir)
	return

def open_online(*args):#opens google drive online
	webbrowser.open('http://drive.google.com')
	return

def setting(*args):
	print 'Feature coming soon'
	return
