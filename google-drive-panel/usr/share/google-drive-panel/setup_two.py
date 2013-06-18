#!/usr/bin/env python
import os

#Check for root
if os.geteuid() != 0:
	print 'You do not have root privileges'
	os.system('gksudo python "' + os.path.abspath( __file__ ) + '"')
	exit()

os.system('cd /usr/share/google-drive && sudo chmod 777 drive_dir')
os.system('add-apt-repository -y ppa:nilarimogard/webupd8')
os.system('add-apt-repository -y ppa:webupd8team/y-ppa-manager')
os.system('apt-get update')
os.system('apt-get -y install grive')
os.system('apt-get -y install yad')
exit(0)
