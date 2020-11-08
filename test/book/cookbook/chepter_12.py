#!python3
# -*- coding:utf-8 -*-


"""
 - 병렬처리
"""

import threading
import time


def tst1():
    class PeriodicTimer:
        def __init__(self, _interval):
            self._cv = threading.Condition()
            self._interval = _interval
            self._flag = 0

        def start(self):
            t = threading.Thread(target=self.run)
            t.daemon = True
            t.start()

        def run(self):
            '''
            타이머를 실행하고 구간마다 기다리는 스레드에게 알림
            '''
            while True:
                time.sleep(self._interval)
                with self._cv:
                    self._flag ^= 1
                    print('## Notify All flag : {}'.format(self._flag))
                    self._cv.notify_all()

        def wait_for_tick(self):
            '''
            타이머의 다음 tick을 기다림
            '''
            with self._cv:
                last_flag = self._flag
                while last_flag == self._flag:
                    self._cv.wait()

    p = PeriodicTimer(5)
    p.start()

    def countdown(nticks):
        while nticks > 0:
            p.wait_for_tick()
            print('T-minus' , nticks)
            nticks -=1


    def countup( last ):
        n = 0
        while n < last:
            p.wait_for_tick()
            print('Counting' , n)
            n +=1
    threading.Thread(target = countdown , args = (10 , )).start()
    threading.Thread(target = countup , args = (5 , )).start()


if __name__ == '__main__':
    tst1()
