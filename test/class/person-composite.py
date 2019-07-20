#!python3
#-*- coding:utf-8 -*-



class Person:
	def __init__( self , name , age , job , pay ):
		self.__name = name
		self.__age = age
		self.__job = job
		self.__pay = pay

	def getName(self):return self.__name
	def getAge(self):return self.__age
	def getJob(self):return self.__job
	def getPay(self):return self.__pay




class Manager:
	def __init__( self , name , age , pay):
		self.person = Person(name , age , 'Manager' , pay+20)


	def __getattr__( self , attrname ):
		def method( *args ):
			return getattr(self.person , attrname)(*args)
		return method

	def __str__( self ):
		return Person._Person__name



if __name__ == '__main__':
	manager = Manager('cwkim' , 20 , 100)
	print('name : {}'.format(manager.getName()))
	print('age : {}'.format(manager.getAge()))
	print(manager)



