#!python3
#-*- coding:utf-8 -*-

'''
	인증 객체
'''

import bcrypt


class Authentication:
	def __init__( self , email = None , pwd = None):
		self._email = email
		self._salt = bcrypt.gensalt()
		self._pwd = bcrypt.hashpw(pwd.encode() , self._salt )
		self._authority = 'USER'

	def __repr__( self ):
		return 'email : %s , pwd : %s'%(self._email , self._pwd)


	def getEmail( self ):
		return self._email

	def getPwd( self ):
		return self._pwd

	def getAuthority( self ):
		return self._authority

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

