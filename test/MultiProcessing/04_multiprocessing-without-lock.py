#!python3
#-*- coding:utf-8 -*-


"""
 multiporcessing + lock
"""


import time
import multiprocessing

LOCK = multiprocessing.Lock()

def func():
	time.sleep(0.1)
	with LOCK:
		print('/\\_/\\')
		print('( O.O )')
		print(' > ^ <')



def main():
	procs = []

	with multiprocessing.Pool(processes = 3) as pool:
		for _ in range(5):
			procs.append(pool.apply_async(func))
		for j in procs:
			j.wait()



if __name__ == '__main__':
	main()