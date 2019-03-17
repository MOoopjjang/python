#!python




class MList( list ):

	def __intersaction__( self , v):
		if v not in self:
			self.append(v)


	

	def madd(self , v ):
		self.__intersaction__(v)



if __name__ == '__main__':
	l = MList()

	l.madd('a')
	l.madd('b')
	l.madd('c')
	l.madd('a')


	print(l)

	del l[:]

	l.append('a')
	l.append('b')
	l.append('a')

	print(l)





