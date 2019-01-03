#!python3
#



import tenacity
import random


def do_something():
	if random.randint(0,1) == 0:
		print('Failure')
		raise RuntimeException
	print('Success')


def main():
	tenacity.Retrying()(do_something)




if __name__ == '__main__':
	main()



