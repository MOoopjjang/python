#!python
#-*- coding:utf-8 -*-



import time

class MTail:
	def __init__( self , _file_name ):
		# print '__init__'
		self._file_ = open( _file_name )

	def follow( self ):
		# print 'run'
		self._file_.seek( 0 ,2)

		while True:
			rl = self._file_.readline()
			print ('rl : {}'.format(rl))
			if not rl:
				print ('-rl : {}'.format(rl))
				time.sleep(5)
				continue			
			yield rl



if __name__ == '__main__':
	mt = MTail('/Users/mooopjjang/Documents/work/gitrep/python/test/api/log.txt')
	for line in mt.follow():
		print(line, end=' ')

