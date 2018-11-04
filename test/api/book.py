#!python3
#-*- coding:utf-8 -*-


#
# iterable , iterator 테스트
#

class BookInfo:
	def __init__( self , _title , _author , _price ):
		self.title = _title
		self.author = _author
		self.price = _price

	def __str__( self ):
		return '[title : {} , author : {} , price: {}]'.format(self.title , self.author , self.price)



class BookManager:
	def __init__( self ):
		self.book_list = []
		self.index = 0


	def __len__( self ):
		return len(self.book_list)


	def __iter__( self ):
		self.index = 0
		return self

	def __next__( self ):
		if self.index >= len(self.book_list):
			raise StopIteration

		rv = self.book_list[self.index]
		self.index +=1
		return rv


	def add( self , _d ):
		self.book_list.append(_d)



if __name__ == '__main__':
	bm = BookManager()

	bm.add(BookInfo('java','kcwda',1000))
	bm.add(BookInfo('c','bhkim',1000))
	bm.add(BookInfo('c++','hyun',1000))


	for b in bm:
		print('{}'.format(b))





















