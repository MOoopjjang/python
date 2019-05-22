#!python3
#-*- coding:utf-8 -*-



def tst1():
	list_name = [ ' 홍길동' , '김병현' , '곽경진']
	list_age = [43 , 45 , 28 ]
	list_pos = ['사장' , '책임' , '연구원']

	for age , name , pos in zip( list_age , list_name , list_pos ):
		print('age : {} , name : {} , pos : {}'.format(age , name , pos))




if __name__ == '__main__':
	tst1()