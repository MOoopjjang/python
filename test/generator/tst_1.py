#!python3
#-*- coding:utf-8 -*-



class Manager:
	def __init__( self , _data):
		self._data = _data


	def __iter__( self):
		for d in self._data:
			yield d



if __name__ == '__main__':
	m = Manager(['xferlog' , 'kknda' , 'bbb' , 'ejkim'])
	for d in m:
		print(d)