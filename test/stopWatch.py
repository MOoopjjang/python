#!python
#-*- coding:utf-8 -*-

import time


class StopWatch():
	def __init__(self):
		self.__fir_start__ = 0;
		self.__start__ = 0
		self.__stop__ = 0


	def start(self):
		t = time.time()
		if self.__fir_start__ == 0:self.__fir_start__ = t;
		self.__start__ = t


	def stop(self):
		self.__stop__ = time.time()
		return round(self.__stop__ - self.__start__)

	def totalTime(self):
		return round(self.__stop__ - self.__fir_start__)

	def clean(self):
		self.__start__ = 0
		self.__stop__ = 0 
		return self
