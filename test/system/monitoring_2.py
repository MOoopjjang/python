#!python3
#-*- coding:utf-8 -*-


import psutil
import cotyledon
import os , sys
import time


"""
  cotyledon + psutil ( system monitoring ... )
"""


class Manager( cotyledon.ServiceManager ):
	def __init__( self ):
		super( Manager , self).__init__()
		self.add(Monitor)



class Monitor( cotyledon.Service ):
	def __init__( self , worker_id ):
		super(Monitor , self).__init__(worker_id)

	def run( self ):
		while True:
			cpu_time = psutil.cpu_times()
			print('cpu_time : {}'.format(cpu_time))
			time.sleep(1)



def main():
	m = Manager()
	m.run()
	




if __name__ == '__main__':
	main()