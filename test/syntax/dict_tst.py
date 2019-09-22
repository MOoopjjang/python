#!python3
#-*- coding:utf-8 -*-



SAMPLE_DICT = {'name':'xferlog' , 'age' : 20 , 'addr':'incheon'}

def tst_1():
	tmpdict = {}
	k = 0
	tmpdict[k] = 10
	print('tmpdict : {}'.format(tmpdict))


def tst_2():
	# copy method테스트
	copy_sample = SAMPLE_DICT.copy()
	print('copy_sample : {}'.format(copy_sample))


def tst_3():
	drinks = {
		'martine':['vodka' , 'vermouth'],
		'black russian':['vodka' , 'kahlua'],
		'white russian':['cream' , 'kahlua' , 'vodka'],
		'manhattan':['rye' , 'vermouth' , 'bitters'],
		'screwdriver':['orange juice' , 'vodka']
	}


	for name , contents in drinks.items():
		if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
			print('name : {}'.format(name))


	for k , v in drinks.items():
		if 'cream' not in v and ('vodka' in v and 'kahlua' in v):
			print(k)


def main():
	print('main')

	d = {'name':'xferlog' , 'age':20}
	# dl = [ for key in d.keys() ]
	# print(dl)

	# print(type(d.values()))
	vl = []
	for v in d.values():
		vl.append(v)

	print(vl)

	addr = d.get('addr' , 'unknown')
	print(addr)


if __name__ == '__main__':
	# tst_1()

	# tst_2()

	tst_3()












