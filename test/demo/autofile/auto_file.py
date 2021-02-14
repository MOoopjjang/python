#!python3
# -*- coding:utf -*-

import os
from datetime import datetime


TARGET = os.path.join(os.getcwd() , 'target')
ORIGINAL = ''


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
