#!python3
#-*- coding:utf-8 -*-


class C:pass

class D( C ):
	__slots__ = ['a']



class E:
	__slots__ = ['a']

class F( E ):
	__slots__ = ['b']





if __name__ == '__main__':
	d = D()
	d.a = 1
	d.b = 2
	print('a : {} , b : {}'.format(d.a , d.b))
	print('dict : {}'.format(d.__dict__))


	f = F()
	f.a = 1
	f.b = 3
	print('{}'.format(f.__dict__))