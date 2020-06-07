#!python3
#-*- coding:utf-8 -*-

'''
 - user 등록 / 인증 기능제공
 - 등록된 모든 user 인증정보 제공
 - 계정정보를 MDataAccessManager를 통해 저장/삭제/편집을 할수 있다.
'''


import defines.defines as df
from authentication import Authentication
from mdataaccessmanager import MDataAccessManager
from defines.singleton import Singleton

@Singleton('mAuthenticationManager' , True)
class MAuthenticationManager:
	def __init__( self ):
		self._repositoryManager = MDataAccessManager().load(df.AUTH_BIN)


	def _checkMember_( self , email ):
		return False if self._repositoryManager.findByOne( email ) else True

		
	def _checkEmailSyntax_( self , email ):
		import re

		rgx = re.compile(df.RGX_EMAIL)
		mo = rgx.search(email)
		return False if mo == None else True


	def createMember( self , email = None , pwd = None , authentication = None):
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
		self._repositoryManager.save(email , Authentication(email , pwd , authentication))


	def removeMember( self , _email ):
		'''
		member를 등록해지한다.
		'''
		auth = self._repositoryManager.findByOne(_email)
		if auth != None:
			try:
				self._repositoryManager.remove(_email)
			except:
				raise Exception('{} 계정삭제중 에러가 발생했습니다.'.format(_email))
			
			



	def certification( self , _email , _pwd ):
		'''
		인증 진행
		'''
		auth = self._repositoryManager.findByOne(_email)
		if auth == None:
			return False

		if auth.matched(_pwd):
			print('인증되었습니다.')
			return True;
		return False

					
	def getAllUsers( self ):
		'''
		등록된 모든 사용자의 정보를 반환한다.
		'''
		return self._repositoryManager.findByAll()
		

	
			




if __name__ == '__main__':
	import os

	os.unlink('auth.bin');

	mm = MAuthenticationManager()
	mm.createMember('xferlog@naver.com' , '11111')
	mm.createMember('cccc@naver.com' , '11111')
	mm.createMember('admin@naver.com' , '2222' , 'ADMIN')
	print('*'*20)
	mm.getAllUsers()



