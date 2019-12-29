#!python
#-*- coding:utf -*-


def tst_11():
	'''
	객체가 서로 다른 컨테이너에 들어있다.하지만 중첩된 반복문을 사용해 코드의 기독성을 해치고 싶지 않다.
	'''
	from itertools import chain

	l1 = ['1','2','3']
	l2 = ['a','b','c']

	for p in chain(l1,l2):
		print(p)



def tst_10():
	l1 = ['1','2','3']
	l2 = ['a','b','c']

	for p in list(zip(l1,l2)):
		print(p)

	d = dict(zip(l1,l2))
	for pp in d:
		print(d)

	print('-'*50)
	ll = list(zip(l1,l2))
	print(ll)



def tst_9():
	'''
	'''

	from collections import defaultdict

	word_summary = defaultdict(list)

	with open('/Users/mooopjjang/Documents/work/gitrep/python/test/algorithm/sample_2.txt' , 'r') as fr:
		for idx , line in enumerate(fr , 1):
			words = [ w.strip().lower() for w in line.split() ]
			for ss in words:
				word_summary[ss].append(idx)


	for k,v in word_summary.items():
		print('{} : {}'.format(k,v))




def tst_8():
	'''
	아이템 컬렉션에 대해 가능한 모든 순열과 조합을 순환
	'''
	from itertools import permutations

	items = ['a' , 'b' , 'c']
	for p in permutations(items):
		print(p)
	



def tst_7():
	from collections import deque

	class linehistory:
		def __init__( self , lines , hislength = 3 ):
			self._lines = lines
			self._queue = deque(maxlen = hislength )


		def __iter__( self ):
			for no , line in enumerate(self._lines , 1):
				self._queue.append((no , line))
				yield line



		def clear( self ):
			self._queue.clear()

		def getHistory( self ):
			return self._queue.copy()



	with open('tmp.txt' , 'r') as fr:
		lh = linehistory(fr , 10)
		for line in lh:
			print('{} , {}'.format(line , len(line.strip())) , end = ' ')
			if line.strip()=='python':
				for no , l in lh.getHistory():
					print('no :{},line:{}'.format(no , l),end = ' ')



def tst_6():
	l = [1,3,2,5,9]
	rl = reversed(l)
	# for v in rl:print('v : {}'.format(v))
	# print('rl : {}'.format(rl))


	class NameMananger:
		def __init__( self ):
			self._data = []

		def __iter__( self ):
			for v in self._data:
				yield v

		def __reversed__( self ):
			for v in self._data[::-1]:
				yield v

		def add(self , _v):
			self._data.append(_v)
			return self


	nm = NameMananger()
	nm.add('xferlog').add('kknda').add('ccc').add('cwkim')
	for n in nm:
		print('v : {}'.format(n))

	print('*'*30)
	for n in reversed( nm ):
		print('v : {}'.format(n))


	class Countdown:
		def __init__( self , start ):
			self._start = start

		def __iter__( self ):
			n = self._start
			while n >= 0:
				yield n
				n -= 1

		def __reversed__( self ):
			n = 0
			while n <= self._start:
				yield n
				n +=1



	print('*'*30)
	cd = Countdown(10)
	for n in cd:
		print('n : {}'.format(n))

	print('*'*30)
	for rn in reversed(cd):
		print('n : {}'.format(rn))




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
	# test_5()
	# tst_6()
	# tst_7()
	# tst_8()
	# tst_9()
	# tst_10()

	tst_11()





