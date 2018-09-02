#!python
#-*- coding:utf-8 -*-


import datetime

def getDefCurrentDate():
	return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def getCurrentDate(_fmt):
	return datetime.datetime.now().strftime(_fmt)