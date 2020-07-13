#!python3
# -*- coding:utf-8 -*-


def exam_1():
    from urllib.request import urlopen
    from urllib.error import HTTPError
    from bs4 import BeautifulSoup

    try:
        html = urlopen('http://www.pythonscraping.com/pages/error.html')
    except HTTPError as e:
        print('{}'.format(e))
    else:
        bobj = BeautifulSoup(html.read() , 'html.parser')
        print('{}'.format(bobj.text))



if __name__ == '__main__':
    exam_1()
