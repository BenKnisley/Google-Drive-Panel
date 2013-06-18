#!/usr/bin/env python
import os
from subprocess import Popen, PIPE, STDOUT
drive_dir = open('/home/' + getpass.getuser() + '/.drive_dir').read().strip()
outstream = Popen('yad --dnd --width 200 --height 175 --title "Drag File Here"', shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
output = outstream.stdout
y = ''
while 1 == 1:
	x = output.read(1)
	if x == "\n":
		filetocopy = y[7:]
		filename = filetocopy[(1 - (len(filetocopy) - filetocopy.rindex('/'))):]
		y = ''
		drive_dir = drive_dir.strip("'")
		drive_dir = drive_dir.strip('"')
		newfile = "'" + drive_dir + filename + "'"
		filetocopy = "'" + filetocopy + "'"
		print filetocopy
		os.system("mv " + filetocopy + " " + newfile)
	else:
		y = y + x
		print Popen.poll(outstream)
		if Popen.poll(outstream) ==  0 or Popen.poll(outstream) == 1 or Popen.poll(outstream) == 252:
			print Popen.poll(outstream)
			exit()
