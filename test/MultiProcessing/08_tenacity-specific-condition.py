#!python3
# -*- coding:utf-8 -*-


import tenacity
import random


"""
tenacity : backoff + 특정조건 (RuntimeError)
"""

def do_someting():
	if random.randint(0,1) == 0:
		print('Failure')
		raise RuntimeError
	print('Success')


@tenacity.retry(wait=tenacity.wait_exponential(multiplier=0.5,max=30,exp_base=2) , retry = tenacity.retry_if_exception_type(RuntimeError))
def do_retry_someting():
	do_someting()


def main():
	do_retry_someting()



if __name__ == '__main__':
	main()