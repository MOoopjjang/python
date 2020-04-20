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
		if len( self._cacheData ):
			self._cacheOne = PersonInformation( _id ) if self._cacheData[_id] is None else self._cacheData[_id]
		else:
			self._cacheOne = PersonInformation( _id )
		return self


	def load( self , _id ):
		self._cacheOne_( _id ) 
		return self

	def add( self , _id , _data ):
		if self._cacheOne is None:
			self._cacheOne_( _id )

		if len( self._cacheOne ) == 0:
			self._cacheOne.add( _data )
		else:
			if _data in self._cacheOne:
				self._cacheOne.remove( _data )
			self._cacheOne.add( _data )

		self._cacheData[_id] = self._cacheOne
		self._repository.save( _id , self._cacheOne )
		return self


	def remove( self , _id , _data ):pass



	def get( self , _id ):
		return self._cacheData[_id]



if __name__ == '__main__':
	# im = InformationManager.getInstance()
	im = InformationManager()
	# print('im : {}'.format(im))
	

	ifo = Information('www.naver.com' , 'xferlog' , '1111')
	ifo2 = Information('mypc' , 'cwkim' , 'cwkim123')
	im.load('xferlog').add('xferlog' , ifo).add('xferlog' , ifo2)
	print('*'*20)
	print(im)
	print('*'*20)
	pi = im.get( 'xferlog' )
	for infs in pi:
		print('{}'.format(infs))
	print('*'*20)
	ifo2 = Information('mypc' , 'ggg' , 'gggg')
	im.add('xferlog' , ifo2)
	for infs in pi:
		print('{}'.format(infs))

	print('*'*20)
	im2 = InformationManager()
	print(im2)






















