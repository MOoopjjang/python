#!python3
#-*- coding:utf-8 -*-



def func( _x ):
	return _x*2



def filter_1_tst():
	num_list = [i for i in range(-5 , 5)]
	print('num_list : {}'.format(num_list))

	nn = list(filter(lambda x:x>0 , num_list))
	print('nn : {}'.format(nn))

    # combine
	combinear = list(map(lambda x:x+2 , list(filter(lambda x:x>0 , num_list))))
	print('combinear : {}'.format(combinear))


def map_1_tst():
	nar = [1,2,3,4,5,6]

	# dnar = list(map(func , nar))
	dnar = list(map(lambda x:x*2 , nar))
	print('dnar : {}'.format(dnar))


	ff = lambda x,_x:x+_x
	ffv = ff(1 , 10)
	print('ffv : {}'.format(ffv))



def main():
	# map_1_tst()
	filter_1_tst()



if __name__ == '__main__':
	main()