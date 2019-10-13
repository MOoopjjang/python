#!python3
#-*- coding:utf-8 -*-


import random


class BingoCage:
	def __init__( self , items ):
		self._items = items
		random.shuffle( self._items )


	def pick( self ):
		try:
			return self._items.pop()
		except:
			raise LookupError('pick from empty BingoCage')



	def __call__( self ):
		print('__call__')
		return self.pick()




if __name__ == '__main__':
	bingocage = BingoCage(['xferlog' , 'aaaa' , 'cwkim'])
	print(bingocage.pick())
	print(bingocage())


