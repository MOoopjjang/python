#!python3
#-*- coding:utf-8 -*-


import logging
import time



"""
 logging module 테스트
"""

def tst1():
	logging.basicConfig(filename='./test.log' , level = logging.DEBUG)
	logging.info('I told you so')
	logging.warning('Watch out!')


def fileHandler_tst():
	import logging.handlers

	mylogger = logging.getLogger('mylogger')
	formatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s]%(asctime)s > %(message)s')

	fileHandler = logging.FileHandler('./myLogger.log')
	streamHandler = logging.StreamHandler()
	fileHandler.setFormatter(formatter)
	streamHandler.setFormatter(formatter)


	mylogger.addHandler(fileHandler)
	mylogger.addHandler(streamHandler)

	mylogger.setLevel(logging.DEBUG)


	mylogger.info('hi')
	mylogger.debug('-'*20)

	for i in range(20):
		mylogger.info('test : {}'.format(i))
		time.sleep(1)



	mylogger.debug('-'*20)


def RotateFileHandler_tst():
	import logging.handlers


	# 1. 인스턴스 생성
	mylogger = logging.getLogger('mylogger')

	# 2. set LOG level
	mylogger.setLevel(logging.DEBUG)

	formatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s]%(asctime)s > %(message)s')


	fileMaxByte = 1024
	fileCount = 10
	# 3. Handler
	fileHandler = logging.handlers.RotatingFileHandler('./myLogger.log' , maxBytes = fileMaxByte , backupCount = fileCount)
	# fileHandler = logging.FileHandler('./myLogger.log')
	streamHandler = logging.StreamHandler()

	fileHandler.setFormatter(formatter)
	streamHandler.setFormatter(formatter)

	mylogger.addHandler(fileHandler)
	mylogger.addHandler(streamHandler)

	# mylogger.info('aaaa')

	while True:
		input_str = input('input ?')
		mylogger.info(input_str)

		if input_str == 'q':break





if __name__ == '__main__':
	# tst1()

	# fileHandler_tst()

	RotateFileHandler_tst()



