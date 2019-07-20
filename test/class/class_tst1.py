#!python3
#-*- coding:utf-8 -*-



class Person:
	def __init__( self , sex = 'male'  , name = None , age = None):
		self._sex = sex
		self._name = name
		self._age = age

	# def __str__( self ):
	# 	return '[%s]:%s'%(self.__class__.__name__ , self.__getAttr())


	def _getAttr( self ):
		# l = None
		l = [key+'='+str(self.__dict__[key]) for key in self.__dict__.keys()]
		return ','.join(l)

	def __str__( self ):
		return '[%s] : %s'%(self.__class__.__name__ , self._getAttr())

	def toString(self):
		return "Person"

		


	# def __name( self ):
	# 	return 'person'


class Cwkim( Person ):
	def __init__( self , **kargv):
		Person.__init__( self , kargv['sex'] , kargv['name'] , kargv['age'])
		self._job = kargv['job']

	def __str__( self ):
		return '[%s]:%s'%(self.__class__.__name__ , Person._getAttr( self ))

	def toString( self):
		return "Cwkim"






if __name__ == '__main__':
	cwkim = Cwkim(sex='female' , name='cwkim' , age = 30 , job = 'programmer')
	print(cwkim)
	print(cwkim.toString())
	# print(cwkim._na())


