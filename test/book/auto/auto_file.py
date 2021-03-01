#!python3
# -*- coding:utf-8 -*-

import os
from datetime import datetime
import shutil


ORIG = '/Users/gimcheol-u/Documents/Doc/my/book/examples/05/csv_files'


def createDir(_dateInfo):
    d = os.path.join(os.getcwd() , _dateInfo['year'] , _dateInfo['month'] , _dateInfo['day'] , _dateInfo['hour'])
    print(f'd : {d}')
    if os.path.exists(d) and os.path.isdir(d):
        print('exist')
    else:
        os.makedirs(d)
    return d



def cpfile(_org , _target):
    shutil.copyfile(_org , _target)
    print(f'{_org} --> {_target}')






def getDate():
    today = datetime.now()
    fmtdate = today.strftime("%Y:%m:%d_%H:%M:%S")
    # print(f'fmtdate : {fmtdate}')
    strdate , strtime = fmtdate.split('_')
    return {
        'year':strdate.split(':')[0],
        'month':strdate.split(':')[1],
        'day':strdate.split(':')[2],
        'hour': strtime.split(':')[0],
        'min': strtime.split(':')[1],
        'sec': strtime.split(':')[2]
    }



if __name__ == '__main__':
    dateInfo = getDate()
    print(dateInfo)
    targetDir = createDir(dateInfo)
    tf = os.path.join(targetDir , 'static.csv')

    if not os.path.exists(tf):
        with open(tf , 'w') as fw:
            fw.write('년월,매출\n')

    dirs = sorted(os.listdir(ORIG))
    for f in dirs:
        if f[-4:] != '.csv':continue
        value = 0
        ym=''
        with open(os.path.join(ORIG , f) , 'r') as fr:
            for index , line in enumerate(fr):
                if index == 0:continue

                row = line.strip().split(',')
                p , ym = row[1:3]
                value += int(p)

            with open(tf , 'at') as fw:
                fw.write('{},{}\n'.format(ym[:-3] , p))




