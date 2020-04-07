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


	def add( self , _info ):
		self._infos.append(_info)
