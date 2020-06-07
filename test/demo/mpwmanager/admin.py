#!python3
#-*- coding:utf-8 -*-


'''
 관리자 기능 
  - 계정 목록 출력
  - 계정 삭제
  - 계정 block
  - 계정 추가
'''

from defines.singleton import Singleton
from mauthenticationmanager import MAuthenticationManager

@Singleton('[Admin]' , True )
class Admin:
	def __init__( self  , _authenticationManager  ):
		self._authenticationManager = _authenticationManager



	def getAllAuthenticationInfo( self ):
		'''
		 - 등록된 모든 계정의 정보를 출력한다. 
		'''
		return self._authenticationManager.getAllUsers()


if __name__ == '__main__':
	am = MAuthenticationManager()
	admin = Admin(am)
	infos = admin.getAllAuthenticationInfo()
	for user in infos:
		print(infos[user])