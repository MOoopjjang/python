#!python
#-*- coding:utf-8 -*-



class Person:
	def __init__( self , name ):
		self._name = name

	# def __getattr__( self , attr):
	# 	if attr == 'name':
	# 		return self._name
	# 	else:
	# 		raise AttributeError(attr)


	def __getattribute__( self , attr):
		if attr == 'name':
			attr = '_name'
		return object.__getattribute__( self , attr)



	def __setattr__( self , attr , value ):
		if attr == 'name':
			attr = '_name'
		self.__dict__[attr] = value


class Powers( object ):
	def __init__( self , square , cube ):
		self._square = square
		self._cube = cube


	def getSquare( self ):
		return self._square **2

	def setSquare( self , value ):
		self._square = value


	def getCube( self ):
		return self._cube **3

	def setCube( self , value ):
		self._cube = value

	square = property(getSquare , setSquare)
	cube = property(getCube , setCube)


class AttrPowers:
	def __init__( self , square , cube ):
		self._square = square
		self._cube = cube


	def __getattr__(self , attr ):
		if attr == 'square':return self._square*2
		elif attr == 'cube':return self._cube *3
		else:
			raise AttributeError(attr)

	def __setattr__( self , attr , value ):
		if attr == 'square':return self.__dict__['_square'] = value
		elif attr == 'cube':return self.__dict__['_cube'] = value
		else:
			self.__dict__[attr] = value


class AttributePowers:
	def __init__( self , square , cube ):
		self._square = square
		self._cube = cube

	def __getattribute__( self , attr ):
		if attr == 'square':
			return object.__getattribute__( self , '_square')
		elif attr == 'cube':
			return object.__getattribute__( self , '_cube')
		else:
			raise object.__getattribute__( self , attr)


		def __setattr__( self , attr , value ):
			if attr == 'square':self.__dict__['_square'] = value
			elif attr == 'cube':self.__dict__['_cube'] = value
			else:
				self.__dict__[attr] = value






if __name__ == '__main__':
	# p = Person('a')
	# p.name
	# p.name = 'xferlog'
	# print('name : %s'%p.name)

	p1 = Powers(1 , 3)
	print('square : %d'%p1.square)
	p1.square = 33
	print('square : %d'%p1.square)














