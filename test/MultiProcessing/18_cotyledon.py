#!python3
#-*- coding:utf-8 -*-


import threading
import time

import cotyledon


"""
cotyledon :: 오랜시간동한 실행되는 process를 생성하기 위해 만들어진 module
 -- 내부적으로 여러개의 thread를 사용

 -- parent processor이 child processor를 관리
    ( 아래 예제는 2개의 child processor를 생성 및 관리됨)
 -- ps -ef|grep 18_cotyledon 으로 process확인 가능
 
 -- child process중 하나가 crash될경우 자동으로 다시 실행해준다.   
"""



class PrintWriter( cotyledon.Service ):
	def __init__( self , worker_id ):
		cotyledon.Service.__init__( self , worker_id)
		self._worker_id = worker_id
		self._shutdown = threading.Event()


	def run( self ):
		while not self._shutdown.is_set():
			print('run  ==>{}'.format(self._worker_id))
			time.sleep(1)


	def terminate( self ):
		self._shutdown.set()




if __name__ == '__main__':
	manager = cotyledon.ServiceManager()
	manager.add( PrintWriter , 1 )
	manager.run()


	
