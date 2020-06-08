#!python3
#-*- coding:utf-8 -*-



import random
import timeit

'''
 - 타자 게임
'''

ARRAY = ['코끼리','dog','cat','고양이','dock']


def getRow():
	x = random.choice(ARRAY)
	return (x,'-> {} <-'.format(x))



def main():
	count = 0

	start = timeit.default_timer()
	org , dptext = getRow()
	print(dptext)
	
	while count < 6:
		input_text = input('')
		if org != input_text:continue

		count +=1
		org , dptext = getRow()
		print(dptext)


	print('total time : {}'.format(round(timeit.default_timer()-start , 2)))



	

if __name__ == '__main__':
	main()
