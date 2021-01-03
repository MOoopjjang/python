#!python3
# -*- coding:utf-8 -*-


import sys, os
import threading
import logging
import timeit, time
import requests
import logging
from queue import Queue
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.INFO, format='%(asctime)-%(levelname)-%(message)s')
logger = logging.getLogger(__file__)

URI = {
    "local": "http://localhost:8080/lss",
    "dev": "http://106.241.17.214:8080/lss"
}


def lssRequest(*args):
    print('start => {}'.format(args[0]))
    # logger.info(f'start ==> {args[0]}')

    headers = {
        "Content-Type": "application/json",
        "X-TOKEN-VALUE": "zinna1234"
    }
    timeout = (2, 2)

    try:
        res = requests.get(args[1], headers=headers, timeout=timeout)
        if res.status_code == 200:
            # logger.info(f'{args[0]}==>{res.json()}')
            print(f'{args[0]}==>{res.json()}')
            args[2].put(res.json())
        else:
            print(f'{args[0]}==> status : {res.status_code}')
    except:
        print(f'erro : {args[0]}')
    print(f'end ==> {args[0]}')


def main(argv):
    print("{}".format(argv[1]))

    u = URI['local']
    fu = u + "/prop/"
    q = Queue()
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = [executor.submit(lssRequest,  index, fu, q) for index in range(100)]
        for future in concurrent.futures.as_completed(futures):
            r = future.result()

    print('end : queue size : {}'.format(q.qsize()))


if __name__ == '__main__':
    main(sys.argv)
