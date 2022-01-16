#!python3
# -*- coding:utf -*-

import os
import sys


def run(_rootDir, _target):
    for d, s, fs in os.walk(_rootDir):
        for f in fs:
            ext = os.path.splitext(f)[-1]
            fullpath = os.path.join(d, f)
            if ext[1:] in _target:
                print(f'delete --> path : {fullpath}')
                # os.unlink(fullpath)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('paramter error!!')
        sys.exit(1)

    run(sys.argv[1], sys.argv[2:])
