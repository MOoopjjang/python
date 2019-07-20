#!python3
#-*- coding:utf-8 -*-


class Person:
	def __init__( self , name , age  , job ):
		self._name = name
		self._age = age
		self._job = job

	def __str__( self  ):
		output = ''
		l = [ k+'='+str(v) for k,v in self.__dict__.items() ]
		return ','.join(l)





class Manager( Person ):
	def __init__( self , name , age ):
		Person.__init__( self , name , age , 'Manager')


	



class Saler( Person ):
	def __init__( self , name , age ):
		Person.__init__( self , name , age , 'Saler')



class Department:
	def __init__( self , *args ):
		self.members = list(args)

	def getJobs( self ):
		for n in self.members:
			yield n._name

	def addMember( self , member ):
		if member not in self.members:
			self.members.append(member)

	def removMember( self , member ):
		if member in self.members:
			self.members.remove(member)

	def showAllMember( self ):
		for person in self.members:
			print(person)



if __name__ == '__main__':

	bob = Manager('bob' , 10)
	sue = Saler('sue' , 20)

	print(sue)

	d = Department(bob , sue)
	for n in d.getJobs():
		print(n)

	d.addMember(Saler('kim',50))
	for n in d.getJobs():
		print(n)


	d.removMember(sue)
	print('*'*20)
	for n in d.getJobs():
		print(n)


	tmpl = ['cwkim' , 'bhkim' , 'ddd']
	tmpl.remove('bhkim')

	print(tmpl)
	print('*'*20)

	d.showAllMember()









