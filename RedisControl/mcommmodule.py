#! python
#-*- coding: utf-8 -*-


import logging
import os
import datetime


logging.basicConfig(level = logging.INFO , format = '%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(os.path.abspath(__file__))


now = datetime.datetime



def getLogger():
	return logger

def getCurrentTime(_format):
	return now.today().strftime(_format)	

def getCurrentDefTime():
	return now.today().strftime('%y-%m-%d-%H:%M:%S')
























































