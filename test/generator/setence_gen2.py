#!python3
#-*- coding:utf-8 -*-


import re
import reprlib


RE_WORD = re.compile('\w+')


"""
 제네레이터 함수...
"""
class Setence:
	def __init__( self , text ):
		self.text = text

	def __repr__( self ):
		return '[%s] %s'%(self.__class__.__name__ , reprlib.repr(self.text))

	def __iter__( self ):
		for match in RE_WORD.finditer( self.text ):
			yield match.group()


"""
  제네레이터 표현식...
"""
class Setence_genexp:
	def __init__( self , text ):
		self.text = text

	def __repr__( self ):
		return '[%s] %s'%(self.__class__.__name__ , reprlib.repr(self.text)) 

	def __iter__( self ):
		return (match.group() for match in RE_WORD.finditer( self.text ))





if __name__ == '__main__':
	text = 'xferlog kknda imcid %^&$% zbc'
	# s = Setence(text)
	s = Setence_genexp( text )
	for m in s:
		print(m)









