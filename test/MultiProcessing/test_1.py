#!python3.7.3
#-*- coding:utf-8 -*-

import concurrent.futures
import threading
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor


def func(_x):
    return _x * 2

def mt_test():
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(func , i) for i in range(1,100)]
        for future in concurrent.futures.as_completed(futures):
            print('{}'.format(future.result()))



def mt_test2():
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

    with ThreadPoolExecutor(max_workers = 10 ) as executor:
        futures = []
        futures.append(executor.submit(f1 , "aaaaa"))
        futures.append(executor.submit(f2 , (1,2,3)))
        for future in concurrent.futures.as_completed(futures):
            print('{}'.format(future.result()))







if __name__=='__main__':
    # mt_test()
    mt_test2()




