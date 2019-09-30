#!python3
#-*- coding:utf-8 -*-




def ex_4_4():
	oddv = [ v for v in range(1,11) if v%2 == 0 ]
	print('oddv : {}'.format(oddv))

def ex_4_5():
	d = {v:v**2 for v in range(1,11)}
	print('d : {}'.format(d))

def ex_4_7():
	gv = ('Got '+str(v) for v in range(1,11))
	print('gv : {}'.format(gv))

	for vv in gv:
		print('vv : {}'.format(vv))


def ex_4_9():
	geven = (v for v in range(1,11) if v%2 != 0)
	print('geven : {}'.format(geven))
	for index , v in enumerate(geven):
		if index == 2:print('v : {}'.format(v))
		# print('v : {}'.format(v))



if __name__ == '__main__':
	# ex_4_4()

	# ex_4_5()

	# ex_4_7()

	ex_4_9()
