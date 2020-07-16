#!python3
# -*- coding:utf-8 -*-

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

TEST_URL = 'http://www.naver.com'


def exam_1():
    try:
        html = urlopen(TEST_URL)
    except HTTPError as e:
        print('{}'.format(e))
    else:
        bobj = BeautifulSoup(html.read(), 'html.parser')

        #        tags = bobj.findAll({'p'})
        #        for t in tags:
        #            print('{}'.format(t))

        nameList = bobj.findAll(text='뉴스')
        for text in nameList: print('{}'.format(text))


u = set()


def exam_2():
    import os, sys

    def wiki_url_crawler(_url):
        global u

        html = urlopen('http://en.wikipedia.org{}'.format(_url))
        bObj = BeautifulSoup(html, 'html.parser')
        titleE = bObj.find('h1', {'class': 'firstHeading'})
        print('title : {}'.format(titleE.text))
        for link in bObj.findAll('a', href=re.compile('^(/wiki/)')):
            if 'href' in link.attrs and link.attrs['href'] not in u:
                print('new Page : {}'.format(link.attrs['href']))
                u.add(link.attrs['href'])
                wiki_url_crawler(link.attrs['href'])

    wiki_url_crawler('/wiki/Richard_II_of_England')

    if os.path.exists('wiki_crawling.txt'): os.unlink('wiki_crawling.txt')
    with open('wiki_crawling.txt', 'w') as fw:
        for line in u:
            fw.write(line + '\n')


if __name__ == '__main__':
    #    exam_1()
    exam_2()
