#!python
#-*- coding:utf-8 -*-



import logging

logger = None

def init():
	global logger
	logging.basicConfig(level = logging.DEBUG , format = '%(levelname)s-%(asctime)s-%(message)s')
	logger = logging.getLogger()


def getLogger():
	global logger
	return logger


def setLevel(_lvl):
	logger.setLevel(_lvl)