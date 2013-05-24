#!/usr/bin/env python
import os, time
drive_dir = open('/usr/share/google-drive-panel/drive_dir').read().strip()
while 1 == 1:
	time.sleep(300)
	os.system('cd ' + drive_dir + ' && grive')
