#!python3
# -*- coding:utf-8 -*-
from demo.mthreadpool import mpool
from demo.mthreadpool.singleton_decorator import Singleton
# from demo.mthreadpool.mpool import *
import threading

"""
 - ThreadPool Manager
"""


@Singleton(dp=True)
class MThreadPoolManager:
    MAX_SIZE = 10

    def __init__(self):
        self._condition = threading.Condition()
        self._createPool_()

    def _createPool_(self):
        self.poolList = [mpool.MPool(self._condition) for _ in range(0, 10 + 1)]
        for p in self.poolList:
            p._thd.start()

    def _getPool_(self):
        '''
         - 구현중
         - 작업대기열 ( Queue )이 가장 작은 MPool 객체 반환
        '''
        from operator import itemgetter

        # sorted(self.poolList , key = itemgetter(''))


        min_pool = self.poolList[0]
        for p in self.poolList:
            if min_pool.getQueueCount() <= p.getQueueCount():
                continue
            min_pool = p
        return min_pool


    def exec(self , _eFunc , _eData ):
        from demo.mthreadpool.mqueue_obj  import MQueueObj
        jPool = self._getPool_()
        print('pool id : {}'.format(jPool.getThdId()))
        jPool.pushQueue(MQueueObj(_eFunc , _eData))
        self._condition.acquire()
        self._condition.notify()
        self._condition.release()



if __name__ == '__main__':


    def f1(_data):
        import time

        print('f1 calling')
        time.sleep(10)
        print('f1 end')


    def f2(*args):
        print('args{}'.format(args))
        r = 0
        for v in args[0]:
            r += v
        print('{}'.format(r))


    mtpm = MThreadPoolManager()

    print('*'*30)

    mtpm.exec(f1 , "aaaa")
    mtpm.exec(f2 , (1,5,21))
