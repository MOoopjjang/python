#!python3
#-*- coding:utf-8 -*-

'''
	- 통계정보제공 ( .statistics)
'''

import random
import futurist
from futurist import waiters


def compute():
	return sum( [random.randint(1,1000) for _ in range(100000)])


with futurist.ThreadPoolExecutor(max_workers = 8 ) as worker:
	futures = [ worker.submit(compute) for _ in range(8) ]
	print(worker.statistics)

results = waiters.wait_for_all(futures)
print(worker.statistics)

print('result : {}'.format([r.result() for r in results.done]))

