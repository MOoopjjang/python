#!python3
#-*- coding:utf-8 -*-



class Base:
	def _getAttribute_( self ):
		return ",".join([k+":"+str(v) for k,v in self.__dict__.items()])


class Person( Base ):
	def __init__( self , name , age , pay ):
		self._name = name
		self._age = age
		self._pay = pay


	def __str__( self ):
		return '[person] {}'.format(self._getAttribute_())


	def givenRaise( self  , percent ):
		return self._pay * 10


class Manager( Person ):
	def givenRaise( self  , percent ):
		return self._pay * 10+10




if __name__ == '__main__':
	p = Person('xferlog' , 23 , 23)
	m = Manager('cwkim' , 23 , 23)

	print(p.givenRaise(10));
	print(m.givenRaise(10))
