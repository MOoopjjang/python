#!python3
#coding:utf-8

# Make By MOoop
# Desc:
#	Source  , Target의 Redis Server의 설정값을 load한다


import os
import logging
import json


class MRedisConfig():

	def __init__(self):
		logging.basicConfig(level = logging.INFO , format = '%(asctime)s - %(levelname)s - %(message)s')

		self.__support_modes = []
		self.__job_modes = []
		self.__config = {}

		self._funcs = [ self.__parse_types__ , self.__parse_jobmodes__ , self.__parse_srchosts__ 
		, self.__parse_tgthosts__ , self.__parse_srcpwd__ , self.__parse_tgtpwd__]

		self.__load_config__()



	def __parse_types__(self , _data):
		logging.debug('__parse_types__ :{} -- len:{}'.format(_data , len(str(_data))))
		logging.debug('type::{}'.format(type(_data)))
		# if len(_data) != None:
		self.__config['types'] = _data


	def __parse_hosts__(self , _hostKey , _data):
		# if len(_data) != 0:
		self.__config[_hostKey] = {}
		insertInfoDict = self.__config[_hostKey]
		count = 0
		hosts = _data.split(',')
		for h in hosts:
			ss = h.split(':')
			host = {}
			host['host'] = ss[0]
			host['port'] = ss[1]
			insertInfoDict['host'+str(count)] = host
			count +=1



	def __parse_srchosts__(self , _data):
		logging.debug('__parse_srchosts__ :{} -- len:{}'.format(_data , len(str(_data))))
		logging.debug('type::{}'.format(type(_data)))
		self.__parse_hosts__('srchosts' , _data)
		


	def __parse_tgthosts__(self , _data):
		logging.debug('__parse_tgthosts__ :{} -- len:{}'.format(_data , len(str(_data))))
		logging.debug('type::{}'.format(type(_data)))
		self.__parse_hosts__('tgthosts' , _data)
				


	def __parse_jobmodes__(self , _data):
		logging.debug('__parse_jobmodes__ :{} -- len:{}'.format(_data , len(str(_data))))
		logging.debug('type::{}'.format(type(_data)))
		# if len(_data) != None:
		self.__config['jobmodes'] = _data
			


	def __parse_srcpwd__(self , _data):
		logging.debug('__parse_srcpwd__ :{} -- len:{}'.format(_data , len(str(_data))))
		logging.debug('type::{}'.format(type(_data)))
		# if len(_data) != None:
		self.__config['srcpwd'] = _data


	def __parse_tgtpwd__(self , _data):
		logging.debug('__parse_tgtpwd__ :{} -- len:{}'.format(_data , len(str(_data))))
		logging.debug('type::{}'.format(type(_data)))
		# if len(_data) != None:
		self.__config['tgtpwd'] = _data


	def __load_config__( self ):
		"""
		json type의 config파일을 load한다.
		"""
		if os.path.exists(os.getcwd()+'/rc.config.json') == False:
			raise Exception('{}/rc.config.json not found!!!'.format(os.getcwd()))

		with open(os.getcwd()+'/rc.config.json' , 'r') as fr:
			jObj = json.load(fr)
			for func in self._funcs:
				func( jObj[func.__func__.__name__[len('__parse_'):-2]] )

		logging.info(self.__config)


	def getConfigInfo(self):
		return self.__config
	



if __name__ == '__main__':
	mc = MRedisConfig()
	# print(locals())








