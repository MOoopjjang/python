#!python
#-*- coding:utf-8 -*-



def Tracer( aClass ):
	class Wrapped:
		def __init__( self , *args , **kargv ):
			self.fetches = 0
			self.aClass = aClass( *args , **kargv )

		def __getattr__( self , attrname ):
			print('{} fetches : {}'.format(attrname , self.fetches))
			if attrname not in self.aClass.ATTRIBUTES:
				raise TypeError(attrname)
			else:
				self.fetches += 1
				return getattr(self.aClass  , attrname)

	return Wrapped


@Tracer
class Person:
	ATTRIBUTES = ['_name' , '_age']
	def __init__( self , _name , _age , _addr ):
		self._name = _name
		self._age = _age
		self._addr = _addr



if __name__ == '__main__':
	p = Person('xferlog' , 10 , 'incheon')

	print(p._name +':'+str(p._age))

	print(p._addr)

