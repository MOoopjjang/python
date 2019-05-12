#!python3
#-*- coding:utf-8 -*-


"""
Class별로 객체 생성시 예약속성을 정의하여 override를 방지하는 sample code...
"""


class PrivateExc(Exception):pass


class Privacy:
	def __setattr__( self , attrname , value ):
		print
		if attrname in self.privates:
			raise PrivateExc( attrname , self )
		else:
			self.__dict__[attrname] = value



class Test( Privacy ):
	privates = ['age']

class Test2( Privacy ):
	privates = ['name' , 'pay']
	def __init__( self ):
		self.__dict__['name'] = 'Tom'


if __name__ == '__main__':
	t1 = Test()
	t2 = Test2()

	t1.name='xferlog'
	# t1.age=20

	# t2.name='kknda'
	t2.age=40
	print('t1.name : %s'%t1.name)
	print('t1.name : %s'%t1.name)


