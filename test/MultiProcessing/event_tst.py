#!python
#-*- coding:utf-8 -*-

import threading
import time



def myThreading( _event ):
	while not _event.is_set():
		print('Waiting for Event to be set')
		time.sleep(1)
	print('myThreading is set ')


if __name__ == '__main__':
	e = threading.Event()
	t = threading.Thread(target = myThreading , args = (e , ))
	t.start()
	time.sleep(10)
	e.set()