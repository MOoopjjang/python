#!python3
#-*- coding:utf-8 -*-


from datetime import datetime
from source.mod.authentication import Authentication


'''
 - 로그인한 정보를 보관하고 있다
 - 로그인이후에는 SecurityContextHolder 객체를 통해 사용자 정보를 확인할수 있따.
'''

class SecurityContextHolder:
	instance = False
	def __init__( self , _authentication = None ):

		if SecurityContextHolder.instance == False or _authentication == None:
			raise Exception('SecurityContextHolder 객체를 생성할수 없습니다.')
			
		self._logintime = datetime.now()
		self._authentication = _authentication
		SecurityContextHolder.instance = False


	def getUsername( self ):
		return self._authentication.getEmail()

	def getPassword( self ):
		return self._authentication.getPwd()

	def getAuthority( self ):
		return self._authentication.getAuthority()

	@staticmethod
	def getInstance( _auth ):
		SecurityContextHolder.instance = True
		return SecurityContextHolder( _auth )




if __name__ == '__main__':
	auth = Authentication('xferlog@naver.com' , '1111')
	sch = SecurityContextHolder.getInstance( auth )
	print('sch username : {}'.format(sch.getUsername()))

	# sch2 = SecurityContextHolder(auth)
