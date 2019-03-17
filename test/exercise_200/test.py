#!python3
#-*- coding:utf-8 -*-



import json



# 에제 1
def trace( func ):
	print('trace func %s'%func.__name__)
	return func

@trace							
def sum(a,b,c):						# sum = trace(sum)					
	return a+b+c

def main():							
	ss = sum(1,2,3)					# ss = trace(sum)(1,2,3)
	print('%d'%ss)




if __name__ == '__main__':
	main()