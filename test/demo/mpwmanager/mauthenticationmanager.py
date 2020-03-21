#!python3
#-*- coding:utf-8 -*-

'''
 - user 등록 / 인증 기능제공
 - 계정정보를 MDataAccessManager를 통해 저장/삭제/편집을 할수 있다.
'''


import defines.defines as df
from authentication import Authentication
from mdataaccessmanager import MDataAccessManager


# RGX_EMAIL = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

class MAuthenticationManager:
	def __init__( self ):
		self._members = []
		self._repositoryManager = MDataAccessManager()


	def __repr__( self ):
		l = [str(m.getEmail())+':'+str(m.getPwd()) for m in self._members]
		return '==='.join(l)


	def createMember( self , email = None , pwd = None):
		'''
		새로운 사용자를 등록한다.
		'''
		if email == None or pwd == None:
			raise Exception('파라미터 오류입니다.')

		if self._checkMember_( email ) == False:
			errmsg = '{} 는 이미등록된 사용자입니다.'.format(email)
			raise Exception(errmsg)

		if self._checkEmailSyntax_( email ) == False:
			errmsg = '{} 는 email이 아닙니다.'.format(email)
			raise Exception(errmsg)

		#등록
		self._members.append(Authentication(email , pwd))


	def certification( self , _email , _pwd ):
		'''
		인증 진행
		'''
		for m in self._members:
			if _email == m.getEmail() and m.matched(_pwd):
				print('인증 되었습니다.')
				return True


		return False

					

	def _checkMember_( self , email ):
		if len(self._members) == 0:return True

		for m in self._members:
			if m.getEmail() == email:
				return False
		return True


	def _checkEmailSyntax_( self , email ):
		import re

		rgx = re.compile(df.RGX_EMAIL)
		mo = rgx.search(email)
		if mo == None:return False
		return True
			




if __name__ == '__main__':
	mm = MAuthenticationManager()
	mm.createMember('xferlog@naver.com' , '11111')
	mm.createMember('cccc@naver.com' , '11111')
	print(mm)



