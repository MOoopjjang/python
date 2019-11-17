#!python3
#-*- coding:utf-8 -*-


"""
지능형 (comprehension) dict 테스트
"""

import collections





class StrKeyDict ( collections.UserDict ):
	def __missing__( self , key ):
		if isinstance( key , str ):
			return 'unknown'
			# raise KeyError(key)
		return self[str(key)]

	def __contains__( self , key ):
		return str(key) in self.data

	def __setitem__( self , key , item ):
		self.data[str(key)] = item




def unmutable_tst():
	"""
	불변 dict 테스트
	"""
	from types import MappingProxyType

	d = {1:'a'}
	d_proxy = MappingProxyType(d)
	print('d_proxy : {}'.format(d_proxy))

	# d_proxy[2] = 'b'
	# print('d_proxy : {}'.format(d_proxy))

	d[2] = 'c'
	print('d_proxy : {}'.format(d_proxy))




def tst_1():

	d = StrKeyDict()
	d['name'] = 'xferlog'
	d['age'] = 20
	print('d : {}'.format(d))
	print('addr : {}'.format(d['addr']))


def tst_0():
	d = {}
	d['name'] = 'xferlog'
	d['age'] = 20

	print('addr : {}'.format(d.get('addr' , 'incheon')))



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
	# comprehension_dict_1()

	# tst_1()

	# tst_0()

	unmutable_tst()





