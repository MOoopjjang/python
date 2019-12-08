#!python
#-*- coding:utf -*-



def test_5():
	s = '{name} has {n} message'
	ss = s.format(name = 'xferlog' , n = 'hi')
	print('ss : {}'.format(ss))

	class Info:
		def __init__( self , name , n ):
			self.name = name
			self.n = n


	info = Info('김철우' , 20)
	sv = s.format_map(vars(info))	
	print('sv : {}'.format(sv))	


def combines( _data , _maxsize ):

	apdata = []
	for _d in _data:
		if len(apdata) > _maxsize:
			yield ' '.join(apdata)
			apdata = []
		else:
			apdata.append(_d)

	yield ' '.join(apdata)



def tst_4():
	for c in combines(['ckalfdkas' , 'aldkfalfda' , 'ccccc' , 'idmkadkadfkla' , 'claiemafdm'] , 10):
		print('c : {}'.format(c))


def tst_3():
	texts = ['i','am','hero','kknda']

	jtext = ' '.join(texts)
	print('jtext : {}'.format(jtext))

	adfa = ['kcwda' , 20 , 2.14 , 'kknda']
	r_adfa = '-'.join(str(x) for x in adfa)
	print('r_adfa : {}'.format(r_adfa))



def tst_2():
	text = 'hello world'
	print('ljust : {}'.format(text.ljust(20)))
	print('rjust : {}'.format(text.rjust(20)))
	print('center : {}'.format(text.center(20)))

	print('ljust , = : {}'.format(text.ljust(20 , '=')))


def tst_1():
	import re

	text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
	print('text: {}'.format(text))
	ctext = re.sub(r'(\d+)/(\d+)/(\d+)' , r'\3-\1-\2' , text)
	print('ctext: {}'.format(ctext))



def namedtuple_tst():
	'''
		- 이름으로 접근가능
		- db로 부터 데이타륿 받아서 정재시 유용
	'''
	from collections import namedtuple

	subscriber = namedtuple('subscriber' , ['addr' , 'joined'])
	sub = subscriber('jonesy@example.com' , '2012-10-19')
	print('sub : {}'.format(sub))

	print('sub.addr : {}'.format(sub.addr))
	print('sub.joined : {}'.format(sub.joined))


if __name__ == '__main__':
	# namedtuple_tst()

	# tst_1()

	# tst_2()

	# tst_3()

	# tst_4()

	test_5()





