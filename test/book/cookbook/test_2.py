#!python3
#-*- coding:utf-8 -*-

# test/book/cookbook




#####################################################################################
'''
AS-IS
'''
class One:
	'''
	AS-IS
	'''
	def __init__(  self , _name ):
		self._name = _name

	def getName( self ):
		return self._name
'''
TO-BE
'''
def MOne(_name):
	name = _name
	def getName():
		return name
	return getName

def tst():
	'''
	단일 메소드를 제공하는 class를 method로 변경
	'''
	o = One('xferlog')
	print('{name}'.format(name=o.getName()))

	print('*'*20)
	o2 = MOne('cwkim')
	print('{name}'.format(name = o2()))

#####################################################################################


#####################################################################################
def apply_async( func , args , * , callback):
	result = func(*args)
	callback( result )


def add( x , y):
	return x+y

def str_prefix( _str ):
	return 'xferlog==>'+_str


class H2:
	def __init__( self ):
		self.seq = 0

	def handler( self , result):
		self.seq +=1
		print('[{}] result : {}'.format(self.seq , result))


def tst2():
	'''
	7.10 콜백함수에 추가적 상태 넣기
	'''
	h = H2()
	for i in range(10):
		if i%2 == 0:
			apply_async( add , (i,3) , callback = h.handler)
		else:
			apply_async( str_prefix , ('hi={}'.format(i),) , callback = h.handler)

	

#####################################################################################



if __name__ =='__main__':
	# tst()

	tst2()
	