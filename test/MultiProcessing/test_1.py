#!python3.7.3
#-*- coding:utf-8 -*-

import concurrent.futures
import threading
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor


def func(_x):
    return _x * 2


def main():

    def mt_test():
        with ThreadPoolExecutor(max_workers=100) as executor:
            futures = [executor.submit(func , i) for i in range(1,100)]
            for future in concurrent.futures.as_completed(futures):
                print('{}'.format(future.result()))

    def mp_test():pass


    # multi threading test
    mt_test()



if __name__=='__main__':
	main()




