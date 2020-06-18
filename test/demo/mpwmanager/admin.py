#!python3
#-*- coding:utf-8 -*-


'''
 관리자 기능 
  - 계정 목록 출력
  - 계정 삭제
  - 계정 block
  - 계정 추가

  ===>  createAuthenticationInfo , blockAuthentication 테스트 X
'''

from defines.singleton import Singleton
from mauthenticationmanager import MAuthenticationManager
from informationmanager import InformationManager

@Singleton('[Admin]' , True )
class Admin:
	def __init__( self  , _authenticationManager , _informationManager  ):
		self._authenticationManager = _authenticationManager
		self._informationManager = _informationManager



	def getAllAuthenticationInfo( self ):
		'''
		 - 등록된 모든 계정의 정보를 출력한다. 
		'''
		return self._authenticationManager.getAllMembers()



	def removeAuthenticationInfo( self , _id = None ):
		'''
		 - 계정 정보 삭제
		 - data 정보 삭제

		'''
		if _id is None:raise Exception('파라미터 오류')

		# 계정정보 삭제
		self._authenticationManager.removeMember( _id )

		# data정보제삭제제
		if self._informationManager.get(_id) != None:
			self._informationManager.load(_id).remove(_id)

	def createAuthenticationInfo(self , email = None , pwd = None , authentication = None ):
		'''
		계정정보를 추가한다.
		'''
		if email == None or pwd == None or authentication == None:raise Exception("파리미터 오류")

		self._authenticationManager.createMember(email , pwd , authentication)
		return self



	def blockAuthentication( self , _id = None , v = None ):
		'''
		사용자 계정 block 유/무
		'''
		if _id is None:raise Exception('파라미터 오류')

		ai = self._authenticationManager.getMember( _id )
		ai.setEnable(v)





if __name__ == '__main__':
	admin = Admin(MAuthenticationManager() , InformationManager())
	infos = admin.getAllAuthenticationInfo()
	print('-'*20)
	for user in infos:
		print(infos[user])

	print('-'*20)
	admin.removeAuthenticationInfo('cccc@naver.com')
	infos = admin.getAllAuthenticationInfo()
	for user in infos:
			print(infos[user])
