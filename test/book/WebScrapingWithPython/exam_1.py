#!python3
# -*- coding:utf-8 -*-

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

TEST_URL = 'http://www.naver.com'

def exam_0():
    T_URL = 'http://www.pythonscraping.com/pages/page3.html'
    html = urlopen(T_URL)
    bs = BeautifulSoup(html , 'html.parser')
    print(bs.find('img' , {'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())


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
    '''
     - wiki 페이지 내부 링크 crawler
    '''
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


count = 0
def exam_3():

    def getPageToBs(_url):
        html = urlopen(_url)
        return BeautifulSoup(html , 'html.parser')

    def getExternalLink(bs , _url):
        extLinks = []
        links = bs.findAll('a' , href = re.compile('^(http|www)((?!'+_url+').)*$'))
        if bool(links):
            for link in links:
                if link.attrs['href'] is not None and link.attrs['href']  not in extLinks:
                    extLinks.append(link.attrs['href'])

        return extLinks

    def getInternalLinks(bs , _url):
        intLinks = []
        links = bs.findAll('a',href=re.compile('^(/|.*'+_url+')'))
        if bool(links):
            for link in links:
                if link.attrs['href'] is not None and link.attrs['href']  not in intLinks:
                    fu = _url + link.attrs['href'] if link.attrs['href'].startswith('/') else link.attrs['href']
                    intLinks.append(fu)

        return intLinks


    def getRandomUrl(_urls):
        import random
        return _urls[random.randrange(0,len(_urls))]


    def url_crawler(_url):
        global count
        count +=1
        print('{} : {}'.format(count , _url))
        try:
            bs = getPageToBs(_url)
            elinks = getExternalLink(bs, _url)
            print('elinks : {} , bool : {}'.format(elinks , bool(elinks)))
            if bool(elinks):
                gourl = getRandomUrl(elinks)
                print('gourl : {}'.format(gourl))
                url_crawler(gourl)
            else:
                ilinks = getInternalLinks(bs, _url)
                print('ilinks : {} , bool : {}'.format(ilinks , bool(elinks)))
                if bool(ilinks):
                    gourl = getRandomUrl(ilinks)
                    print('in gourl>>{}'.format(gourl))
                    url_crawler(gourl)
        except HTTPError as e:
            print('{} ->e : {}'.format(_url,e.errno))


    url_crawler('http://oreilly.com')
    #url_crawler('https://locate.apple.com/')






if __name__ == '__main__':
    # exam_1()
    #exam_2()
    # exam_3()
    exam_0()
