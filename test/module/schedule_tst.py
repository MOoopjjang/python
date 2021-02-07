#!python3
# -*- coding:utf-8 -*-

import schedule
import time
import datetime


def tst1():
    def efunc(**kwargs):
        l = [ f'{k}={str(v)}' for k,v in kwargs.items()]
        output = '<-->'.join(l)
        print(f'output : {datetime.datetime.now()}:{output}')

    schedule.every(3).seconds.do(efunc,name='xferlog' , age=20)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    tst1()
