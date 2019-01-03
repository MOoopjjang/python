#!python3
# -*- coding:utf-8 -*-


import tenacity
import random

"""
tenacity를 사용한 일정시간 대기
"""


def do_someting():
	if random.randint(0,1) == 0:
		print('Failure')
		raise RuntimeException
	print('Success')


@tenacity.retry(wait=tenacity.wait_fixed(1))
def do_retry_someting():
	do_someting()


def main():
	do_retry_someting()



if __name__ == '__main__':
	main()