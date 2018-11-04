#!python3
#-*- coding:utf-8 -*-



class Person:
	def __init__( self , name , job = None , pay = 0):
		self.name = name
		self.job = job
		self.pay = pay


	def __repr__( self ):
		return '[Person {} ,{}]'.format(self.name , self.pay)


	def lastName( self ):
		return self.name.split()[-1]


	def giveRaise(self , percent ):
		self.pay = int( self.pay * (1 + percent )) 


class Manager:
	def __init__(self , name , pay):
		self.person = Person(name , 'mgr' , pay)

	def giveRaise(self , percent , bonus=.10):
		self.person.giveRaise( percent + bonus )

	def __getattr__( self , attr ):
		return getattr(self.person , attr )

	def __repr__( self ):
		return str(self.person)



if __name__ == '__main__':
	bob = Person('Bob Smith')
	sue = Person('Sue Jones' , job = 'dev' , pay = 100000)
	print('{} , {}'.format(bob.name , bob.pay))
	print('{} , {}'.format(sue.name , sue.pay))
	print('{} , {}'.format(bob.lastName() , sue.lastName()))
	sue.giveRaise(.10)
	print('{}'.format(sue.pay))

	print('bob >> {}'.format(bob))
	print('sue >> {}'.format(sue))

	tom = Manager('Tom Jones' , 50000)
	tom.giveRaise(.10)
	print(tom.lastName())
	print(tom)


	print('-- All there --')
	for p in (bob , sue , tom):
		p.giveRaise(.10)
		print('{}'.format(p))
