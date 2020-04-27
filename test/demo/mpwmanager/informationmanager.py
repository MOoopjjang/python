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
from information import Information

@Singleton('InformationManager' , True)
class InformationManager:
	def __init__( self ):
		self._repository = MDataAccessManager().load('user.bin')
		self._cache_()


	def __repr__( self ):
		l = [key for key in self._cacheData]
		return '@'.join(l)



	def _cache_( self ):
		self._cacheData = self._repository.findByAll()
		return self

	def _cacheOne_( self , _id ):
		self._cacheOne = self._cacheData.get(_id , PersonInformation( _id )) if len( self._cacheData ) else PersonInformation( _id )
		return self

	def _remove_( self , _id ):
		if len( self._cacheData ):
			self._repository.remove( _id )
			# cacheData reload
			self._cache_()


	def load( self , _id ):
		'''
		계정에 맞는 정보를 load한다
		'''
		self._cacheOne_( _id ) 
		return self

	def add( self , _id , _data ):
		'''
		새로운 사용자 정보를 저장한다.
		'''
		if self._cacheOne is None:
			self._cacheOne_( _id )

		if len( self._cacheOne ) == 0:
			self._cacheOne.add( _data )
		else:
			if _data.getInfo() in self._cacheOne:
				self._cacheOne.remove( _data.getInfo() )
			self._cacheOne.add( _data )

		self._cacheData[_id] = self._cacheOne
		self._repository.save( _id , self._cacheOne )
		return self


	def edit( self , _id ,  _data):
		'''
		저장된 사용자 정보를 수정된 정보로 변경한다.
		'''
		if self._cacheOne is None:
			self._cacheOne_( _id )

		self._cacheOne.remove( _data.getInfo() )
		self._cacheOne.add( _data )
		self._cacheData[_id] = self._cacheOne
		self._repository.save( _id , self._cacheOne )
		return self


	def remove( self , _id , _getInfo = None ):
		'''
		사용정보를 삭제한다
		'''
		if self._cacheOne is None:
			self._cacheOne_( _id )

		if _getInfo is None:
			self._remove_( _id )
		else:
			if len( self._cacheOne ) > 0 and _getInfo in self._cacheOne:
				self._cacheOne.remove( _getInfo )
				self._repository.save( _id , self._cacheOne )
		return self

	
	def get( self , _id ):
		'''
		사용자 정보를 가져온다
		'''
		return self._cacheData[_id]



if __name__ == '__main__':
	im = InformationManager()
	

	ifo = Information('www.naver.com' , 'xferlog' , '1111')
	ifo2 = Information('mypc' , 'cwkim' , 'cwkim123')
	info_a = Information('shinhan' , 'kcwda1' , 'aaaaa')

	im.load('xferlog').add('xferlog' , ifo).add('xferlog' , ifo2)
	im.load('khlee').add('khlee' , info_a)
	print('*'*20)
	print(im)
	print('*'*20)
	pi = im.get( 'xferlog' )
	for infs in pi:print('{}'.format(infs))
	pi2 = im.get('khlee')
	for infs in pi2:print('{}'.format(infs))
	print('*'*20)
	ifo2 = Information('mypc' , 'ggg' , 'gggg')
	im.load('xferlog').add('xferlog' , ifo2)
	for infs in pi:
		print('{}'.format(infs))

	print('*'*20)
	im2 = InformationManager()
	print(im2)

	print('*'*20)
	print('remove test')
	print('*'*20)
	im2.load('khlee').remove('khlee')
	print(im2)




















