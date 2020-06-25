#!python3
#-*- coding:utf -*-

'''
 - user data정보를 관리하는 클래스
 - 추가/편집/삭제 기능 제공
'''

import source.defines.defines as df
from source.manager.mdataaccessmanager import MDataAccessManager
from source.defines.singleton import Singleton
from source.mod.person_information import PersonInformation
from source.mod.information import Information


def getInstance():
	@Singleton('InformationManager' , True)
	class InformationManager:
		def __init__( self ):
			self._repository = MDataAccessManager().load(df.USER_BIN)
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


		def get( self , _id , _info = None , _sec = 'N' ):
			'''
			사용자 정보를 가져온다
			'''
			import pyperclip

			pi = self._cacheData.get(_id , None)
			if pi is None or len(pi) == 0:return None

			if _info is None:
				return pi
			else:
				for idx , info in enumerate( pi ):
					if _info == info.getInfo():
						if _sec == 'Y':
							# clip board에 복사
							pyperclip.copy( pi[idx].getPassword() )
						else:
							return pi[idx].getPassword()
			return None


		def printInfo( self , _id ):
			'''
			사용자의 등록한 정보를 출력한다.
			'''
			self._cacheOne_( _id )

			if self._cacheOne is None:
				print('존재하지 않는 사용자 입니다.')
			else:
				for index , p in enumerate( self._cacheOne ):
					print('[{}]{}'.format(index , p))

	return InformationManager()


if __name__ == '__main__':
	df.initRepositoryPath(__file__)
	im = getInstance()

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
	im2 = getInstance()
	print(im2)

	print('*'*20)
	print('remove test')
	print('*'*20)
	im2.load('khlee').remove('khlee')
	print(im2)

	print('*'*20)
	im.edit('xferlog' , Information('mypc' , 'edit' , 'edit'))
	im.printInfo('xferlog')

	im.get('xferlog' , _info = 'mypc' , _sec='Y')

	print('*'*20)
	print('im : {} - im2 : {}'.format(id(im) , id(im2)))




