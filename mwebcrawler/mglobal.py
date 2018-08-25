#!python
#coding:utf-8

import logging
import datetime
import platform


# prt_func = {}
logger = logging.getLogger('mcrawler')
python_version = list(platform.python_version())

now = datetime.datetime


# def print_3(_str):
# 	print(_str)


# def print_2(_str):
# 	print _str	



def init():
	# global prt_func
	global logger
	logging.basicConfig(level = logging.DEBUG , format = '%(asctime)s - %(levelname)s - %(message)s')

	# for v in ['2','3']:
	# 	prt_func[v] = globals().get('print_'+v)

def getLogger():
	global logger
	return logger

def setLoggingLevel(_level):
	global logger
	if _level == 'debug':
		logger.setLevel(logging.DEBUG)
	elif _level == 'info':
		logger.setLevel(logging.INFO)

def mprint(_str):
	# global logger
	# global python_version
	# global prt_func
	
	# major_version = python_version[0]
	# logger.debug(major_version == '3')
	# logger.debug(type(major_version))

	# prt_func[major_version](_str)
	pass


def getCurrentTime(_format):
	global now
	return now.today().strftime(_format)


def getDefCurrentTime():
	global now
	return now.today().strftime('%Y-%m-%d %H:%M%S')






