#!python3
#-*- coding:utf-8 -*-


'''
- user data class
'''


class PersonInformation:
	def __init__( self  , _id):
		self._id = _id
		self._infos = []


	def __iter__( self ):
		for info in self._infos:
			yield info


	def __getitem__( self  , x ):
		return self._infos[x]

	def __len__( self ):return len(self._infos)


	def __contains__( self , x ):
		for info in self._infos:
			if info.getInfo() == x.getInfo():
				return True
		return False

	def add( self , _info ):
		self._infos.append(_info)

	def remove( self , _info ):
		for idx , info in enumerate( self._infos ):
			if info.getInfo() == _info.getInfo():
				del self._infos[idx]
				break 
