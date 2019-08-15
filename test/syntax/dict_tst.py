#!python3
#-*- coding:utf-8 -*-



def tst_1():
	tmpdict = {}
	k = 0
	tmpdict[k] = 10
	print('tmpdict : {}'.format(tmpdict))

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
	tst_1()