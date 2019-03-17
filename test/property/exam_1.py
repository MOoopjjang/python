#!python
#-*- coding:utf -*-




class Person:
	def __init__( self , name ):
		self._name = name

	@property
	def name(self ):
		return self._name

	@name.setter
	def name( self , name ):
		self._name = name

	@name.deleter
	def name( self ):
		del self._name
	# name = property(getName , setName , delName , 'name property docs')



class PropSquare:
	def __init__(self , start):
		self._start = start

	def getX(self):
		return self._start**2

	def setX( self , value ):
		self._start = value


	X = property(getX , setX)



if __name__ == '__main__':
	p = Person('bob')
	print('n : %s'%p.name)
	p.name = 'xferlog'
	print('n : %s'%p._name)
	del p.name
	print('n : %s'%p.name)


	# pa = PropSquare(10)
	# pb = PropSquare(11)
	# print('pa : %d'%pa.X)
	# pa.X = 1000
	# print('pa : %d'%pa.X)






