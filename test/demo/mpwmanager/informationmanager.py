#!python3
#-*- coding:utf -*-

'''
 - user data정보를 관리하는 클래스
 - 추가/편집/삭제 기능 제공
'''

import defines.defines as df
from authentication import Authentication
from mdataaccessmanager import MDataAccessManager
from defines.singleton import Singleton
from person_information import PersonInformation

@Singleton('InformationManager' , True)
class InformationManager:
	def __init__( self ):
		self._repository = MDataAccessManager().load('user.bin')
		self._cacheData = self._cache_()


	def __repr__( self ):pass


	def _cache_( self ):pass


	def add( self , _id , _data ):
		pi = PersonInformation( _id )
		pi.add( _data )