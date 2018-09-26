#!python3
#-*- coding:utf8 -*-



class mlist:
	def __init__( self ):
		self._index = 0
		self._l = []
		self._iter = iter(self._l)


	def __del__( self ):
		del self._l[:]

	def __iter__( self ):



	def __next__( self ):
		if self._index >= len(self._l):
			return StopIteration

		v = self._l[self._index]
		self._index += 1
		return v



	def push( self , _d ):
		for ll in self._l:
			print(ll)
		self._l.append( _d )
		return self

	def pop( self ):
		return self._l.pop()



