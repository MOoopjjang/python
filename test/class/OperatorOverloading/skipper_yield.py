#!python3
#-*- coding:utf-8 -*-



class SkiperObject:
	def __init__( self ,  wrapped ):
		self._wrapped = wrapped


	def __iter__( self ):
		offset = 0
		while offset < len(self._wrapped):
			item = self._wrapped[offset]
			offset +=2
			yield item



if __name__ == '__main__':
	so = SkiperObject('kakdalfkalfda')

	for x in so:
		for y in so:
			print(x+y , end = ' ')