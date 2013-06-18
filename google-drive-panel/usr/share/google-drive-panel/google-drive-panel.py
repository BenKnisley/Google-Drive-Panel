#!/usr/bin/env python
import os, sys

def help():
	print('usage:')
	print('google-drive-panel [--setup]')
	print('--setup  enters setup')
	exit()

def setup():
	print 'Setting up, may take a while'
	os.system('/usr/share/google-drive-panel/setup.py > /dev/null &')
	exit()

def start():
	os.system('/usr/share/google-drive-panel/main.py > /dev/null & /usr/share/google-drive-panel/time_update.py > /dev/null &')
	print 'Google Drive Panel Started! You can close this terminal now'
	exit()

try:
    sys.argv[1]
except IndexError:
	if len(open('/usr/share/google-drive-panel/drive_dir').read().strip()) < 3:
		setup()
	else:
		start()
else:
	if sys.argv[1] == '--setup':
		setup()
	else:
		help()
	

