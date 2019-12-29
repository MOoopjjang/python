#!python3
#-*- coding:utf-8 -*-

'''
 파일내의 영어단어별 사용 count를 출력한다
'''

from collections import defaultdict
import re

class WordCount:
	def __init__( self , _filePath = None ):
		if _filePath is None:
			raise FileNotFoundError('parameter error')

		self._filePath = _filePath
		self._wc = defaultdict(int)
		self._rgx = re.compile(r'^[A-Za-z]+$')
		

	def run( self ):
		with open(self._filePath , 'r' ) as fr:
			for line in fr:
				s = line.split()
				for ss in s:
					mo = self._rgx.search(ss)
					if mo is not None:
						self._wc[mo.group()]+=1


		return self


	def result( self ):
		for k,v in self._wc.items():
			print('{} : {}'.format(k,v))



if __name__ == '__main__':
	wc = WordCount('sample_2.txt')
	wc.run().result()