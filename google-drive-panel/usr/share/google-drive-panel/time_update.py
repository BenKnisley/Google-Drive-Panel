#!/usr/bin/env python
import os, time

drive_dir = open('/home/' + getpass.getuser() + '/.drive_dir').read().strip()

while 1 == 1:
	time.sleep(300)
	os.system('cd ' + drive_dir + ' && grive')
