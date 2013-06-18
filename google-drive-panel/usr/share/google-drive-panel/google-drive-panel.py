#!/usr/bin/env python
import os, sys

#Help Message, needs more added
def help():
	print('usage:')
	print('google-drive-panel [--setup]')
	print('--setup  enters setup')
	exit()

#Starts Setup
def setup():
	print 'Setting up, may take a while'
	os.system('/usr/share/google-drive-panel/setup.py > /dev/null')
	exit()

#Starts Gdrive panel
def start():
	os.system('/usr/share/google-drive-panel/main.py > /dev/null & /usr/share/google-drive-panel/time_update.py > /dev/null &')
	print 'Google Drive Panel Started! You can close this terminal now'
	exit()

try:	#Tests to see if there is any command args
    sys.argv[1]
except IndexError:	#if there isn't any comm args
	if len(open('/usr/share/google-drive-panel/drive_dir').read().strip()) < 3:		#Test if setup is run yet
		setup()		 #If it has hasn't run, run it
	else:
		start()		#If it has, run gdrive panel
else:	#if there is comm args
	if sys.argv[1] == '--setup':	#if the user wants setup
		setup()
	else:	#otherwise, display help
		help()

