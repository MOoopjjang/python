#!python3
#-*- coding:utf-8 -*-

'''
	인증 객체
'''

import bcrypt
from src.python.defines.mpwattribute import MPWAttribute


class Authentication( MPWAttribute ):
	def __init__( self , email = None , pwd = None , _authority = None):
		MPWAttribute.__init__( self )
		self._email = email
		self._salt = bcrypt.gensalt()
		self._pwd = bcrypt.hashpw(pwd.encode() , self._salt )
		self._enable = 'Y'
		self._authority = 'USER' if _authority == None else _authority
		
		

	def __repr__( self ):	
		return self.getMpwAttribute('_pwd' , '_salt')


	def getEmail( self ):
		return self._email

	def getPwd( self ):
		return self._pwd

	def getAuthority( self ):
		return self._authority

	def getEnable( self ):
		return self._enable

	def setEnable( self , v ):
		self._enable = v

	def matched( self , rawPwd ):
		return bcrypt.checkpw( rawPwd.encode() , self._pwd)



if __name__ == '__main__':
	auth = Authentication('xferlog@naver.com' , '1111')
	print(auth)

	inputpw = input('p : ')
	if auth.matched(inputpw):
		print('matched')
	else:
		print('not matched')

