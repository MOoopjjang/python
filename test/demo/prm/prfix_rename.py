#!python

import os, sys
import shutil


def rmFileCopy(_org, _target , _skipFile):
    if (os.path.isdir(_org) is False) or (os.path.isdir(_target) is False):
        print('존재하지 않는 디렉토리 입니다.')
        sys.exit(1)

    for d, s, fs in os.walk(_org):
        for f in fs:
            try:
                fullPath = os.path.join(d, f)
                if fullPath == _skipFile:
                    continue
                targetPath = os.path.join(_target, '[RM]' + f)
                print(f'copy {fullPath} --> {targetPath}')
                shutil.copyfile(fullPath, targetPath)
            except:
                print('error')


if __name__ == "__main__":
    rmFileCopy('/Users/mooopjjang/Documents/work/code/github/python/test/tt',
               '/Users/mooopjjang/Documents/work/code/github/python/test/async',
               sys.argv[0])
