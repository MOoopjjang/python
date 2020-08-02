#!python3
#-*- coding:utf-8 -*-



import cotyledon



class SubService( cotyledon.Service ):
	def __init__( self , worker_id):
		self._shutdown = threading.Event()
		super( SubService , self).__init__(worker_id)


	def run( self ):
		while self._shutdown.is_set() != True:
			print(' polling... {}'.format(datetime.datetime.now()))
			subprocess.Popen(['open' , 'log.txt'])
			time.sleep(60*3)

	def terminate( self ):
		self._shutdown.set()



def tst_1():
	"""
	cotyledon + subprocess.Popen 테스트
	"""
	import subprocess
	import time , datetime
	import cotyledon
	import threading

	manager = cotyledon.ServiceManager()
	manager.add(SubService , 2)
	manager.run()




if __name__ == '__main__':
	tst_1()
