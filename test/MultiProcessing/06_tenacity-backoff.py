#!python3
# -*- coding:utf-8 -*-


import tenacity
import random

"""
tenacity에서 지수 백오프를 이용한 대기.
"""

def do_someting():
	if random.randint(0,1) == 0:
		print('Failure')
		raise RuntimeException
	print('Success')


@tenacity.retry(wait=tenacity.wait_exponential(multiplier=0.5,max=30,exp_base=2),)
def do_retry_someting():
	do_someting()


def main():
	do_retry_someting()



if __name__ == '__main__':
	main()