#!python3
#-*- coding:utf-8 -*-


import time
from futurist import periodics


"""
 주기적으로 scheduling 해주는 futurist.peridics.PeriodicWorker

 Code :
   - 두가지 작업을 처리
   - 하나는 1초마다 실행되어 작업 경과 시간을 출력
   - 다른 하나는 4초마다 실행되어 작업 진행에 대한 통계를 출력한다.

   퓨처리스트는 처리중인 작업통계를 제공하므로 application의 상태를 알고 싶을 때 유용하다.
"""

@periodics.periodic(1)
def every_one( started_at ):
	print(' 1: %s '%(time.time() - started_at))

w = periodics.PeriodicWorker([
	(every_one , (time.time(),) , {})
	])

@periodics.periodic(4)
def print_stats():
	print('stats : %s'%list(w.iter_watchers()))

w.add(print_stats)
w.start()
