#!python3
#-*- coding:utf-8 -*-


ar = ['name' , 'age' , 'addr']

class Person:
	def __init__( self):pass


	def __getattr__( self , attr ):
		if attr not in ar:
			raise Exception(' error')
		else:
			return getattr(self.__dict__ , attr)


	def __setattr__( self , attr , v ):
		if attr not in ar:
			raise Exception('aaa')
		else:
			self.__dict__[attr] = v



if __name__ == '__main__':
	p = Person()
	# p.name = 'xferlog'
	print(p.name)
			
