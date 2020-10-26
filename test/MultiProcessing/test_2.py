#!python
# -*- coding:utf-8 -*-


import time
import threading
from threading import Thread


def threadWorker():
    print('####### threadWorker Start #####')
    time.sleep(10)
    print('####### threadWorker End #######')

    print('enumerate () : {}'.format(threading.enumerate()))
    print('active_count () : {}'.format(threading.active_count()))


def daemonThread():
    # print('####### Daemon Thread Start #######')
    while True:
        print('####### Daemon Thread Start : {} #######'.format(threading.current_thread()))
        print('active_count : {}'.format(threading.active_count()))
        time.sleep(2)
    print('####### Daemon Thread End #######')


def tst_1():
    print('{}'.format(threading.main_thread()))

    nThread = Thread(target=threadWorker)
    dThread = Thread(target=daemonThread)

    dThread.setDaemon(True)

    dThread.start()
    nThread.start()

    print('####### main end #######')


def sample_func(_i):
    print('##### {} start #####'.format(threading.current_thread()))
    print('##### {} start #####'.format(threading.enumerate()))
    time.sleep(_i * 2)
    print('##### {} end #####'.format(threading.current_thread()))
    return _i * 2


def tst_2():
    import concurrent.futures
    from concurrent.futures import ThreadPoolExecutor

    with ThreadPoolExecutor(max_workers=2) as executor:
        tasks = [executor.submit(sample_func, i) for i in range(1, 3)]

        for task in tasks:
            print('result : {}'.format(task.result()))


def tst_3():
    def rfunc(_count):
        print(f'{_count}')

    class MThread(Thread):
        def __init__(self, target=None,
                     args=(), kwargs=None):
            Thread.__init__(self, target=target, args=args, kwargs=kwargs)
            self.target = target
            self.args = args
            self.kwargs = kwargs
            self.count = 0
            self.lock = None
            # self.rlock = threading.RLock()

        def setCondition(self , cv):
            self.cv = cv

        def getCondition(self):
            return self.cv

        def run(self):
            self.cv.acquire()
            while True:
                with self.cv:
                    self.count +=1
                    self.target(self.count)
                    print('wait>>>>')
                    self.cv.wait()


            # self.rlock.release()
            self.cv.release()

    mt = MThread(target=rfunc, args=(1,))
    mt.setCondition(threading.Condition())
    mt.start()

    # while True:
    #     time.sleep(2)
    #     print('Notify >> ')
    #     mt.getCondition().notify()






if __name__ == '__main__':
    # tst_1()

    # tst_2()
    tst_3()
