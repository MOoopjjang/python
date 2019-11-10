#!python3
#-*- coding:utf-8 -*-


"""
지능형 (comprehension) dict 테스트
"""

import collections

class StrKeyDict ( collections.UserDict ):
	def __missing__( self , key ):
		if isinstance( key , str ):
			raise KeyError(key)
		return self[str(key)]

	def __contains__( self , key ):
		return str(key) in self.data

	def __setitem__( self , key , item ):
		self.data[str(key)] = item


def comprehension_dict_1():
	DIAL_CODES = [
		(10 , 'korea'),
		(20 , 'japan'),
		(30 , 'china'),
		(40 , 'america')
	]
	ad = {country: code for code , country in DIAL_CODES}
	print('ad : {}'.format(ad))





if __name__ == '__main__':
	comprehension_dict_1()