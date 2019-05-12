#!python3
#-*- coding:utf-8 -*-


import re
import reprlib



RE_WORD = re.compile('\w+')


class Setence:
	def __init__( self , text ):
		self.text = text
		self.words = RE_WORD.findall(text)

	def __repr__( self ):
		return '[%s] %s'%(self.__class__.__name__ , reprlib.repr(self.text))

	def __iter__( self ):
		for word in self.words:
			yield word
		# return



if __name__ == '__main__':
	s = Setence('aoifaiof adifaodf. adlfkala aaa')
	print(s)
	for w in s:
		print(w)