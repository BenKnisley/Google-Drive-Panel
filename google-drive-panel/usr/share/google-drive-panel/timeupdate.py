#!/usr/bin/env python
import getpass, time, os
while True:
	drive_dir = open('/home/' + getpass.getuser() + '/.drive_dir').read().strip()
	os.system('cd ' + drive_dir + ' && grive')
	time.sleep(300)
