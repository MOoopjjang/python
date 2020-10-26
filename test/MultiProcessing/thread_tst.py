#!python3
# -*- coding:utf-8 -*-

import threading
from threading import Thread

def tst1():
    def rfunc(index , _max):
        for n in range(1 , _max+1):
            print('tid :  [ {} ] - n : {}'.format(index , n))

    threads = [Thread(target = rfunc , args = (index , 1000)) for index in range(0 , 10)]
    for t in threads:t.start()
    for t in threads:t.join()


def lock_tst1():
    '''
    lock
    '''
    rlock = threading.RLock()
    def lfunc(index , _max):
        # with rlock:
        rlock.acquire()
        for n in range(1 , _max + 1):
            print(f'{index} - {n}')
        rlock.release()

    threads = [ Thread(target = lfunc , args = (index , 100,)) for index in range(0 , 10)]
    for t in threads:t.start()
    for t in threads:t.join()


if __name__ == '__main__':
    # tst1()
    lock_tst1()