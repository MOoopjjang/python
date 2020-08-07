#!python3
# -*- coding:utf-8 -*-

import webbrowser

def eaglesadmin_tst(_url , _limit):
    for _ in range(1,_limit):
        webbrowser.open_new_tab(_url)



if __name__ == '__main__':
    eaglesadmin_tst('http://192.168.0.44:8080/eaglesadmin/eelive/main' , 100)
    #eaglesadmin_tst('http://192.168.0.44:8080/eaglesadmin/admin/monitor/', 50)
