#!python3
#-*- coding:utf-8 -*-


"""
지능형 (comprehension) dict 테스트
"""

import collections





class CustomDict( collections.UserDict ):
	'''
	dict에 key값이 존재하지 않을경우 Customdict를 사용하여 default value를 반환한다.
	'''
	def __missing__( self , key ):
		if isinstance( key , str ):
			return 'unknown'
		return self.data[ str(key) ]

	def __contains__( self , key ):
		return str(key) in self.data

	def __setitem__( self , key , value ):
		self.data[ str(key) ] = value




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

	cd = CustomDict()
	cd['name'] = 'cwkim'
	cd['age'] = 20
	print('{cd}'.format(cd = cd))
	print('{addr}'.format(addr = cd['addr']))


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





