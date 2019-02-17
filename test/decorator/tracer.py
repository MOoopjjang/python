#!python
#-*- coding:utf-8 -*-



class Tracer:
	def __init__( self , aclass ):
		self.aclass = aclass

	def __call__(self , *args , **kargs ):
		print('__call__')
		self.wrapped = self.aclass( *args , **kargs )
		return self


	def __getattr__( self , attrname ):
		print('%s'%attrname)
		print('__getattr__')
		return getattr( self.wrapped , attrname)



@Tracer
class Spam:
	def display(self):
		print('spam : ')


@Tracer
class Person:
	def __init__( self , name ):
		self.name = name




if __name__ == '__main__':
	# s = Spam()
	# s.display()


	bob = Person('bob')
	jon = Person('jon')

	print('bob : %s , jon : %s'%(bob.name , jon.name))
