#!python3
# -*- coding:utf-8 -*-


import subprocess
import time as t

if __name__ == '__main__':
    atime = 60
    count = 0

    while True:
        count = count + 1
        print(f'current time {count}')
        t.sleep(1.0)
        if count == 60:
            subprocess.Popen(['open', 'log.txt'])
            count = 0
