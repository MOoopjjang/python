#!python
#-*- coding:utf-8 -*-


import threading
import time
import random

count = 1
lock = threading.Lock()

def worker_a():
	global count
	global lock

	lock.acquire()
	try:
		while count < 100:
			count +=1
			print(' worker_a :: count : {}'.format(count))
			time.sleep(random.randint(0,1))
	finally:
		lock.release()
		

def worker_b():
	global count
	global lock

	lock.acquire()
	try:
		while count > -100:
			count -=1
			print('worker_b:: count:{}'.format(count))
			time.sleep(random.randint(0,1))
	finally:
		lock.release()



def main():
	t1 = threading.Thread(target = worker_a , args = ())
	t2 = threading.Thread(target = worker_b , args = ())
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print('finish!!!')



if __name__ == '__main__':
	main()




