#!python3


import os , sys


def main():
	d1={'a':1 , 'b':2, 'c':3} 
	d2={'c':3,'f':2 , 'z':1}

	d3 = d1.items()-d2.items()
	print(d3)


if __name__ == '__main__':
	main()

