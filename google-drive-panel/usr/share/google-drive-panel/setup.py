#!/usr/bin/env python
import os, time, webbrowser
from subprocess import Popen, PIPE, STDOUT
print 'setting up, please wait'
os.system('/usr/share/google-drive-panel/setup_two.py')

cmd = "yad --title 'Select the Folder to Sync with Google Drive' --width 800 --height 500 --file --directory"
yadprocess = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
yadout = yadprocess.stdout
yadprocess.wait()
drive_dir = yadout.read().strip()
drive_dir = '"' + drive_dir + '/"'
open('/usr/share/google-drive-panel/drive_dir', 'w').write(drive_dir)
cmd = "cd " + drive_dir + " && grive -a --dry-run"
griveprocess = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
griveout = griveprocess.stdout
grivein = griveprocess.stdin
griveerr = griveprocess.stderr
x = ''
y = ''
z = False
while z == False:
	x = griveout.read(1)
	y = y + x
	if x == '\n':
		if y[:4] == 'http':
			z = True
		else:
			y = ''
webbrowser.open(y)
os.system('clear')
time.sleep(2)
cmd = 'yad --width 500 --height 100 --title "Input Authentication Code" --text "  Input Authentication Code from Google Drive" --form --field="Code"'
yadprocess = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
yadout = yadprocess.stdout
yadprocess.wait()
authcode = yadout.read().strip()[:-1]
print authcode
grivein.write(authcode + ' \n')
griveprocess.wait()
if griveprocess.returncode != 0:
	print 'Error, something went wrong'
	exit()

os.system('yad --title "done with setup" --text " Run google-drive-panel to start. Also feel free to add google-drive-panel to startup apps, it is just better that way.  "')
time.sleep(3)
os.system('clear')
