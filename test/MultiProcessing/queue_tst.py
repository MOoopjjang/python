#!python3
# -*- coding:utf-8 -*-


import threading
import time , random
import queue


# @profile
def myThread( _queue , _wQueue ,_index):
	while not _queue.empty():
		v = _queue.get()
		if v != None:
			print('v ::{}'.format(v))
			_wQueue.put('index : {} , value : {}'.format(_index , v))
			_queue.task_done()
			time.sleep(1)

	print('Thread End...')



if __name__ == '__main__':

	myQueue = queue.Queue()
	wQueue = queue.Queue()
	for i in range(0 , 10):
		myQueue.put(i)


	ts = []
	for i in range(4):
		t = threading.Thread(target = myThread , args = ( myQueue , wQueue , i,))
		ts.append(t)
		t.start()

	for th in ts:
		th.join()

	print('*'*100)
	while not wQueue.empty():
		print('{}'.format(wQueue.get()))
	print('*'*100)





