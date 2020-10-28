#!python3
# -*- coding:utf-8 -*-

import threading
from threading import Thread
from queue import Queue
from demo.mthreadpool.mpool import MPool

'''
 - Custom Thread
'''


class MThread(Thread):
    def __init__(self, _queue, _condition):
        Thread.__init__(self)
        self._queue = _queue
        self._condition = _condition

    def getQueueCount(self):
        return len(self._queue)

    def pushQueue(self, _pool):
        self._queue.put(_pool)
        return self

    def run(self):
        while True:
            self._condition.acquire()
            while True:
                if self._queue.empty() == False:
                    # MPool 객체 반환 #
                    pool = self._queue.get()
                    pool.eFunc(pool.eData)
                    print('queue count : {}'.format(self._queue.qsize()))
                    break
                print('thread id: {} --> waiting'.format(threading.current_thread().ident))
                self._condition.wait()
            self._condition.release()


if __name__ == '__main__':
    import time


    def f1(_s):
        print(f'{_s}')


    def f2(_data):
        print('name : {} , age : {}'.format(_data['name'], _data['age']))


    q = Queue()
    c = threading.Condition()

    mt = MThread(q, c)
    mt.setDaemon(True)
    mt.start()

    count = 0
    while count < 10:
        time.sleep(2)
        if count % 2 == 0:
            p = MPool(f1, f"xferlog - {count}")
            mt.pushQueue(p)
            p = MPool(f2, {"name": f"xferlog{count}", "age": 30})
            mt.pushQueue(p)
        count += 1
        c.acquire()
        c.notify()
        c.release()

    print(">>>> END <<<")
