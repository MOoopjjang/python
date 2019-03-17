#!python3
#-*- coding:utf-8 -*-



class MyList ( list ):
	def __getitem__( self , offset ):
		print('(indexing %s at %s)'%(self,  offset))
		return list.__getitem__( self , offset -1)



if __name__ == '__main__':
	m = MyList('abc')
	print('m : {}'.format(m))
	for x in m:print(x)

	print(m[0])