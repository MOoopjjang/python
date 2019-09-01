#!python3
#-*- coding:utf-8 -*-

import os , sys
import time

"""
tail 명령어 대충 구현...
"""


def grep(_fileName , _searchStr):
	with open(_fileName  , 'r') as fr:
		fr.seek(0 , 2)
		while True:
			line = fr.readline()
			if line == None or len(line) == 0 or ( line.find(_searchStr) == -1):
				continue

			yield line
			time.sleep(0.1)




def tail( _fileName ):
	with open(_fileName , 'r') as fr:
		fr.seek(0,2)

		while True:
			line = fr.readline()
			if line == None or len(line) == 0:
				continue

			yield line
			time.sleep(0.1)





if __name__ == '__main__':
	for l in grep(sys.argv[1] , sys.argv[2]):
		print(l)
	