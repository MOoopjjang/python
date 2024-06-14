#!python
#-*- coding:utf-8 -*-

#-------------------------------------------------------
#  MakeBy MOoop
#. Desc :
#		BeyounCompare crack
#
#-------------------------------------------------------

import getpass
import os


REG_FILE = 'registry.dat'

def main():
	bccDir = '/Users/%s/Library/Application Support/Beyond Compare'%getpass.getuser()
	fullPath = str(bccDir)+'/'+REG_FILE
	if os.path.exists(fullPath):
		os.unlink(fullPath)
		print('Delete ...%s'%REG_FILE)
	else:
		print('File Not Exists %s'%REG_FILE)



if __name__ == '__main__':
	main()