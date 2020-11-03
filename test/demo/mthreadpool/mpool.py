#!python3
# -*- coding:utf-8 -*-


'''
 - Manager에서 관리될 Thread Pool 객체
'''

from demo.mthreadpool.mthread import *
import threading
from queue import Queue
from demo.mthreadpool.mqueue_obj import MQueueObj


class MPool:
    def __init__(self, _condition):
        self._queue = Queue()
        self._thd = MThread(self._queue, _condition)

    def __str__( self ):
        return "thread id : {} - Queue Count : {}".format(self._thd.ident , self._queue.qsize())

    def __lt__( self , other):
        return self._queue.qsize() < other._queue.qsize()

    def getQueueCount(self):
        return self._queue.qsize()

    def pushQueue(self, _data):
        self._queue.put(_data)
        return self

    def getThdId(self):
        return self._thd.getId()


if __name__ == '__main__':
    import time


    def f1(_s):
        print(f'{_s}')


    def f2(_data):
        print('name : {} , age : {}'.format(_data['name'], _data['age']))


    c = threading.Condition()
    pool = MPool(c)
    pool._thd.setDaemon(True)
    pool._thd.start()

    count = 0
    while count < 10:
        time.sleep(2)
        if count % 2 == 0:
            p = MQueueObj(f1, f"xferlog - {count}")
            pool.pushQueue(p)
            p = MQueueObj(f2, {"name": f"xferlog{count}", "age": 30})
            pool.pushQueue(p)
        count += 1
        c.acquire()
        c.notify()
        c.release()

    print(">>>> END <<<")
