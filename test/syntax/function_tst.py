#!python3
#-*- coding:utf-8 -*-




def func(arg , result = []):
	result.append(arg)
	print('arg : {} , result : {}'.format(arg , result))


def func2( **kwargs ):
	for k,v in kwargs.items():
		print('{}:{}'.format(k,v))



def func3(_data):
	for v in _data:
		yield v



if __name__ == '__main__':

	func('a')
	func('b')

	func2(name='xferlog' , age = 20)


	for vv in ['xferlog' , 'kknda' ' a' , 'cccc' , 'ddd']:
		print('vv : {}'.format(vv))


