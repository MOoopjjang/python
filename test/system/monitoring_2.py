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

			print('-'*20+'cpu'+'-'*20)
			print('cpu_count : {}'.format(psutil.cpu_count(logical = False)))
			# print('cpu_affinity : {}'.format(len(psutil.Process().cpu_affinity())))
			print('cpu_time : {}'.format(cpu_time))
			print('cpu_percent -1 : {}'.format(psutil.cpu_percent()))
			print('cpu_percent -2 : {}'.format(psutil.cpu_percent( percpu = True)))

			print('-'*20+'mem'+'-'*20)
			print('virtual_memory : {}'.format(psutil.virtual_memory()))

			time.sleep(1)



def main():
	m = Manager()
	m.run()
	




if __name__ == '__main__':
	main()