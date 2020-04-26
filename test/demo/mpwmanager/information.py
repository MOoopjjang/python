#!python3
#-*- coding:utf-8 -*-

'''
user의 정보를 저장하는 class
'''

class Information:
	def __init__( self , _info = None , _id = None , _pw = None ):
		if _info == None:raise Exception('parameter 누락.')

		self._info = _info
		self._id = _id
		self._pw = _pw


	def __repr__( self ):
		l = [ k+':'+str(v) for k,v in self.__dict__.items() ]
		return '@'.join(l)

	def getInfo( self ):return self._info

	def getId( self ):return self._id

	def getPassword( self ):return self._pw



if __name__ == '__main__':
	i1 = Information('www.naver.com' , 'xferlog' , '1111')
	i2 = Information('gmail' , 'mooopjjang' , '2222')

	l = []
	l.append(i1)
	l.append(i2)

	for info in l:
		print(info)
