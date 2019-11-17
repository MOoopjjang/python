#!python3
#-*- coding:utf-8 -*-




import re
import sys



"""
단어가 나타나는 위치를 보여주는 index를 만든다
"""

WORD_RE = re.compile(r'\w+')



def defaultdict_exam():
	import collections

	index = collections.defaultdict(list)
	with open(sys.argv[1] , encoding = 'utf-8') as fp:
		for lineno , line in enumerate(fp , 1):
			for match in WORD_RE.finditer(line):
				word = match.group()
				col_no = match.start() + 1
				index[word].append((lineno , col_no))

		for word in sorted(index , key = str.upper):
			print('{}:{}'.format(word , index[word]))


def defaultdict_exam2():
	import collections

	# d = collections.defaultdict( list )
	d = {}

	d['name'] = 'cwkim'
	d['age'] = 20
	d['friends'].append('park')

	print('friends : {}'.format(d['friends']))




def setdefault_exam():
	index = {}

	with open(sys.argv[1] , encoding = 'utf-8') as fp:
		for lineno , line in enumerate(fp , 1):
			for match in WORD_RE.finditer(line):
				word = match.group()
				col_no = match.start() + 1
				index.setdefault(word , []).append((lineno , col_no))


		for word in sorted(index , key = str.upper):
			print('{}:{}'.format(word , index[word]))

	




def normal():
	index = {}
	with open(sys.argv[1] , encoding='utf-8') as fp:
		for lineno , line in enumerate(fp , 1):
			for match in WORD_RE.finditer(line):
				word = match.group()
				colno = match.start() + 1

				occ = index.get(word , [])
				occ.append((lineno , colno))
				index[word] = occ

				
		for word in sorted(index , key = str.upper):
			print('{}:{}'.format(word , index[word]))

if __name__ == '__main__':
	# normal()
	# setdefault_exam()

	# defaultdict_exam()

	defaultdict_exam2()







