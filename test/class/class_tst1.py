#!python3
#-*- coding:utf-8 -*-


from aa import A

class properties( object ):
	def getage( self ):return 40
	def setage( self , value ):
		print('value : %d'%value)
		self._age = value

	age = property( getage , setage , None , None )



# class A:
# 	def act( self ):print('A')


class B:
	def act( self ):print('B')



class C( B, A ):
	def act( self ):
		# super().act()
		B.act( self )
		A.act( self )


class Callee:
	# def __init__( self , *argvs  , **kargvs):
	# 	# print('__init__ : %s -- %s'%(argvs , kargvs))
	# 	self.argvs = argvs
	# 	self.kargvs = kargvs 

	def __call__( self  , *argvs , **kargvs):
		print('Callee : %s -- %s '%(argvs , kargvs ))





if __name__ == '__main__':

	# x = properties()
	# print('x.age : %d'%x.age)
	# x.age = 10
	# print('x.age : %d'%x.age)
	# print('x._age : %d'%x._age)
	# x.job = 'trainer'
	# print('x.job : %s'%x.job)


	# x = C()
	# x.act()


	# c = Callee()
	# c(1,2,3)

	print(__name__)
	a = A('xferlog')
	print(a)






