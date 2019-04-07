#!python3
#-*- coding:utf-8 -*-


"""
  __iter__ 업그레이드 버전..
"""
class squares:
	def __init__( self , start , end ):
		self._start = start
		self._end = end

	def __iter__( self ):
		for value in range(self._start , self._end):
			yield value ** 2






if __name__=='__main__':
	for n in squares(1,5):
		print(n)
	