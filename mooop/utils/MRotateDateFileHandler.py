#!python3
#-*- coding:utf-8 -*-


# Makey by MOoop
# Desc
#	시간단위( day , hour , min , sec ) 로 FileRotate를 진행한다.


# Version 1.0.0



import logging
import datetime
import time
import threading
import os
import shutil


class MRotateDateFileHandler:
	def __init__( self , _configInfo , _maxCount = 30 , _maxSize = 1):
		self._config_info_ = _configInfo
		self._maxCount_ = _maxCount
		self._maxSize_ = _maxSize
		# File Handler 생성
		self._FileHandler_ = logging.FileHandler(self._config_info_['dir']+'/'+self._config_info_['fname'])

		# bg 실행
		self.__bgrun__()

	def __del__( self ):
		print('__del__ called :')


	def __getSleepTime__( self ):
		lowerFmt = self._config_info_['DatePattern'].lower()
		if lowerFmt.find(r':%s'):return 1
		elif lowerFmt.find(r':%m'):return 60
		elif lowerFmt.find(r':%h'):return 60*60
		else:
			return 24*(60*60)



	# def __changeDateRotateFile__( self ):
	# 	"""
	# 	현재 시간이 rotate조건인지 체크후 파일 rotate진행
	# 	"""
	# 	curLog = self._config_info_['dir']+'/'+self._config_info_['fname']
	# 	curDate = (lambda x:datetime.datetime.now().strftime(x))(self._config_info_['DatePattern'])
	# 	cfiletime = datetime.datetime.fromtimestamp(os.path.getctime(self._config_info_['dir']+'/'+self._config_info_['fname']))
	# 	fileStrDate = cfiletime.strftime(self._config_info_['DatePattern'])

	# 	if 'catalina.log' in self._config_info_['fname']:
	# 		print('curDate : {} , fileStrDate : {}'.format(curDate , fileStrDate))

	# 	if curDate != fileStrDate:
	# 		shutil.copy(curLog , curLog+'_'+curDate)
	# 		fw = open(curLog , 'w')
	# 		fw.truncate()
	# 		fw.close()


	def __changeDateRotateFile__( self ):
		curLog = self._config_info_['dir']+'/'+self._config_info_['fname']
		curDate = (lambda x:datetime.datetime.now().strftime(x))(self._config_info_['DatePattern'])
		shutil.copy(curLog , curLog+'_'+curDate)
		fw = open(curLog , 'w')
		fw.truncate()
		fw.close()

        



	def __remove_old_log__( self ):
		"""
		log file의 count가 maxCount를 초과할시 가장 오래된 파일부터 삭제한다.
		"""
		prefix_name = self._config_info_['fname']
		all_f = os.listdir(self._config_info_['dir'])
		fns = [fn for fn in all_f if fn.strip().startswith(prefix_name)]
		# 역순으로 정렬 ( 가장 오래된 파일이 가장뒤로..)
		fns.sort(key = lambda x:os.path.getmtime(self._config_info_['dir']+'/'+x) , reverse = True)

		if len(fns) > int(self._maxCount_):
			while len(fns) >  int(self._maxCount_):
				os.unlink(self._config_info_['dir']+'/'+fns[-1])
				del fns[-1]




	def __chkrotate__(self):
		"""
		BG Rotate 기능 수행.
		"""
		sleeptime = self.__getSleepTime__()
		while True:
			self.__remove_old_log__()
			self.__changeDateRotateFile__()
			time.sleep(sleeptime)
		


	def __bgrun__( self ):
		self._bgthread_ = threading.Thread(target = self.__chkrotate__ , args = ())
		self._bgthread_.daemon = True
		self._bgthread_.start()


	def getHandler( self ):
		return self._FileHandler_



if __name__ == '__main__':
	obj = MRotateDateFileHandler(None , 10)
	obj.__remove_old_log__()









