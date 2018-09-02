#!python3
# -*- coding:utf-8 -*-


import collections
from random import choice



card =  collections.namedtuple('Card' , ['rank' , 'suit'])

class FrenchDeck:
	ranks = [str(n) for n in range(2,11)] + list('JQKA')
	suits = 'spades diamonds clubs hearts'.split()

	def __init__(self):
		self._cards = [ card(rank , suit) for suit in self.suits for rank in self.ranks]


	def __len__(self):
		return len(self._cards)


	def __getitem__(self , position):
		return self._cards[position]
											






if __name__ == '__main__':
	f = FrenchDeck()
	print('len : {}'.format(len(f)))
	print(' i : {}'.format(f[0]))

	print('random :: {}'.format(choice(f)))
	print('>>{}'.format(f[:2]))
	print('>>>{}'.format(f[2:5]))

	for index , card in enumerate(f):
		print('{} -> {}'.format(index , card))