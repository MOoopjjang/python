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
            # self.rlock = threading.RLock()

        def setCondition(self , cv):
            self.cv = cv

        def getCondition(self):
            return self.cv

        def run(self):
            while True:
                self.cv.acquire()
                while True:
                    if self.args[0]:
                        v = self.args[0].pop()
                        self.target(v)
                        break
                    print('wait>>>>')
                    self.cv.wait()
                self.cv.release()


            # self.rlock.release()
            # self.cv.release()



    condition = threading.Condition()
    ins = [10,2,3,4,5,6,7]
    mt = MThread(target=rfunc, args=(ins,))
    mt.setCondition(condition)
    mt.start()

    count = 0
    while count < 10:
        time.sleep(2)
        print('Notify >> ')
        condition.acquire()
        condition.notify()
        condition.release()
        count +=1

        if count%2 == 0:
            for i in range(1 , 10):ins.append(i)


    print('========= End ========')




if __name__ == '__main__':
    # tst_1()

    # tst_2()
    tst_3()
