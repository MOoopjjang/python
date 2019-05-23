#!python3
#-*- coding:utf-8 -*-



import requests


class IfChecker:
	def __init__( self , configMgr ):
		self._configMgr = configMgr



	def run( self ):
		for info in self._configMgr:
			if info[0] == 'params':
				self._param = info[1]
			else:
				try:
					url = info[1].strip('\n')+self._param.strip('\n')
					print('get... {}'.format(url))
					res = requests.get(url)
					if res.status_code == 200:
						print('success ..{} '.format(info[1] ))
					else:
						print('failed ..{} response : {}'.format(info[1] , res.status_code))
				except:
					print('except : '+info[1])
				

