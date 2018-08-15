#!python3
#-*- coding:utf-8 -*-


# Make by MOoop

# Desc:
#	logger.

# Device :
#	- OS X
#	- Linux / Unix 


# version
#	v 0.9.0
#   v 1.0.0
#     - 시간별 Rotate기능 추가 ( MRotateDateFileHandler )



import time
from xml.etree import ElementTree as ET
import logging
import logging.handlers
from MRotateDateFileHandler import MRotateDateFileHandler


class mlogger:
	def __init__( self  , _config_path ):
		if self.__parsingConfigXml__( _config_path ) == False:raise Exception(_config_path+' invalide file!!!')
		self.__makeLogger__()


	def __del__( self ):
		self._loggerInfo.clear()


	def __getLevel__( self , _str_level ):
		"""
		_str_level에 해당되는 logging level을 반환한다.
		Arguments:
			_str_level {string} -- logger level string
		
		Returns:
			[type] -- logging level
		"""
		if _str_level == 'INFO':
			return logging.INFO
		elif _str_level == 'DEBUG':
			return logging.DEBUG
		elif _str_level == 'ERROR':
			return logging.ERROR
		elif _str_level == 'CRITICAL':
			return logging.CRITICAL
		else:
			return logging.WARNING



	def __parsingConfigXml__( self ,  _config_path ):
		"""
		xml format의 설정파일을 dict 데이타로 convert
		Arguments:
			_config_path {[string]} -- config파일 ( xml format )
		
		Returns:
			bool -- [description]
		"""
		tree = ET.parse( _config_path )
		self._root = tree.getroot()
		appenders = self._root.findall('appender')
		if appenders == None or len(appenders) == 0:return False

		## log 정보 셋팅..
		self._loggerInfo = {}
		for appender in appenders:
			tmp = {}
			tmp['level'] = appender.find('level').get('value')
			tmp['DatePattern'] = appender.find('DatePattern').get('value')
			tmp['dir'] = appender.find('dir').get('value')
			tmp['fname'] = appender.find('fname').get('value')
			self._loggerInfo[appender.get('name')] = tmp

		## Default 셋팅이 없을 경우는 에러..
		if 'default' not in self._loggerInfo.keys():
			return False

		#  config 설정...
		confs = self._root.findall('config')
		if confs != None:
			self._configInfo = {}
			for conf in confs:
				tmp = {}
				if conf.get('name') == 'rotate':
					tmp['type'] = conf.find('type').get('value')
					tmp['logcnt'] = conf.find('logcnt').get('value')
					tmp['logsize'] = conf.find('logsize').get('value')
					self._configInfo[conf.get('name')] = tmp


	def __makeLogger__( self ):
		"""
		appender name에 해당되는 logger들을 생성한다.
		"""
		self._loggermapper = {}
		for key in self._loggerInfo.keys():
			m = self._loggerInfo[key]
			logger = logging.getLogger(key)
			formatter = logging.Formatter('[%(levelname)s | %(filename)s.%(lineno)s]-%(asctime)s-%(message)s')

			fpath = m['dir']+'/'+m['fname']
			fileHandler = None
			if self._configInfo != None and 'rotate' in self._configInfo.keys():
				## log size는 mb 단위 이다.
				rot_m = self._configInfo['rotate']
				mbytes = int(rot_m['logsize']) *(1024 * 1024)
				mcount = int(rot_m['logcnt'])
				fileHandler = None
				if rot_m['type'] == 'date':
					mrotObj = MRotateDateFileHandler(m , mcount , mbytes)
					fileHandler = mrotObj.getHandler()
				elif rot_m['type'] == 'size':
					fileHandler = logging.handlers.RotatingFileHandler(fpath , maxBytes = mbytes , backupCount = mcount)
				else:
					fileHandler = logging.FileHandler( fpath )
			else:
				fileHandler = logging.FileHandler( fpath )

			fileHandler.setFormatter(formatter)
			logger.addHandler(fileHandler)
			logger.setLevel(self.__getLevel__(m['level']))

			## logger연결...
			self._loggermapper[key] = logger


	def getLogger( self , _tag ):
		"""
		tag에 해당되는 logger를 반환해주는 외부 API
		Arguments:
			_tag {[string]} -- config파일의 appender name에 해당되는 이름.
		
		"""
		return self._loggermapper[_tag]






if __name__ == '__main__':
	loggerModule = mlogger('sample.xml')

	defLogger = loggerModule.getLogger('default')
	errLogger = loggerModule.getLogger('error')
	# delLogger = loggerModule.getLogger('del')
	xLogger = loggerModule.getLogger('xferlog')

	while True:
		defLogger.info('default'*1000)
		errLogger.info('error'*1000)
		# delLogger.debug('del')
		xLogger.info('xaadfadfafx'*1000)

		time.sleep(10)
		# time.sleep(0.5)




