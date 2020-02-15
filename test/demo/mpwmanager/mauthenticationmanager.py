#!python3
#-*- coding:utf-8 -*-

'''
 - user 등록 / 인증 기능제공
 - 계정정보를 MDataAccessManager를 통해 저장/삭제/편집을 할수 있다.
'''


from authentication import Authentication

class MAuthenticationManager:
	def __init__( self ):
		self._members = []


	def createMember( self , email = None , pwd = None):
		'''
		새로운 사용자를 등록한다.
		'''
		if email == None or pwd == None:
			raise Exception('파라미터 오류입니다.')

		if self._existMember_( email ):
			raise Exception('{} 는 이미등록된 사용자입니다.'.format(email))

		#등록
		self._members.append(Authentication(email , pwd))




	def _existMember_( self , email ):
		if len(self._members) == 0:return True

		for m in self._members:
			if m.getEmail() == email:
				return True
		return False


