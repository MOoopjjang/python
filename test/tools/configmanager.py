#!python3
#-*- coding:utf-8 -*-


import json
import sys , os

class ConfigMgr:
	def __init__( self , config_path = None ):
		if config_path == None:
			raise Exception('_config_path is None!!!')
		self._config_path = config_path

	def __iter__( self ):
		with open(self._config_path , 'r') as fr:
			for line in fr:
				yield line.split('=')

		
	def setConfigPath( self , new_config_path ):
		self._config_path = new_config_path



if __name__ == '__main__':
	c = ConfigMgr(os.getcwd()+'/sample.txt')
	for i in range(10):
		genObj = c.getConfig()
		print('-'*10+str(i)+'-'*10)
		for b in genObj:
			if b[0] == 'params':print('param : {}'.format(b[1]))
			else:
				print('ip : {}'.format(b[1]))
