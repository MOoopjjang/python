#!python3
#-*- coding:utf-8 -*-



import json
import os , sys
from mcleaner import MCleaner

def main():
	if os.path.exists('config.json'):
		rootPath = os.getcwd() if (len(sys.argv) < 2 or sys.argv[1] == None) else sys.argv[1]
		print('rootPath : {}'.format(rootPath))
		with open('config.json' , 'r') as fr:
			jObj = json.load(fr)
			MCleaner(rootPath , jObj).run()
	else:
		raise Exception('config.json not found!!!')





if __name__ == '__main__':
	main()