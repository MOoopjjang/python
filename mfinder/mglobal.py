#! python
#-*- coding:utf-8 -*-


import logging
import datetime



logger = None
now = None


def init():
	global logger
	logging.basicConfig(level = logging.DEBUG , format = '%(asctime)s - %(levelname)s - %(message)s')
	logger = logging.getLogger(__file__)
	now = datetime.datetime


def getLogger():
	global logger
	return logger

def setLogLevel(_level):
	global logger
	if _level == 'debug':
		logger.setLevel(logging.DEBUG)
	elif _level == 'info':
		logger.setLevel(logging.INFO)

def getCurrentTime(_format):
	global now
	return now.today().strftime(_format)

def getDefCurrentTime():
	global now
	return now.today().strftime('%Y-%m-%d %H:%M%S')