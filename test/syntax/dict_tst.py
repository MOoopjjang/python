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

	tst_2()