#!python3
#-*- coding:utf-8 -*-


class SkipObject:
	def __init__( self , data ):
		self._data = data

	def __iter__( self ):
		return SkipIterator(self._data)



class SkipIterator:
	def __init__( self , data):
		self._data = data
		self._offset = 0


	def __next__( self ):
		if self._offset >= len(self._data):
			raise StopIteration
		else:
			item = self._data[self._offset]
			self._offset +=1
			return item



if __name__ == '__main__':
	so = SkipObject('xferlogkknda')
	l = [ s for s in so ]
	print(l)
	l = [ s for s in so ]
	print(l)

	print(tuple(so) , tuple(so))





