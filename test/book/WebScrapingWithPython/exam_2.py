#!python3
# -*- coding:utf-8 -*-


class Content:
    '''
    글/페이지 전체에 사용할 기반 클래스
    '''
    def __init__(self , topic , url , title , body):
        self.topic = topic
        self.url = url
        self.title = title
        self.body = body


    def print(self):
        '''
        출력 결과를 원하는 대로 바꿀 수 있는 함수
        '''
        print('New article found for topic : {}'.format(self.topic))
        print('URL : {}'.format(self.url))
        print('TITLE : {}'.format(self.title))
        print('BODY : {}'.format(self.body))


class Website:
    '''
    웹사이트 구조에 관한 정보를 저장할 클래스
    '''
    def __init__(self,name , url , searchUrl , resultListing , resultUrl , absoluteUrl , titleTag , bodyTag):
        self.name = name
        self.url = url
        self.searchUrl = searchUrl
        self.resultListing = resultListing
        self.resultUrl = resultUrl
        self.absoluteUrl = absoluteUrl
        self.titleTag = titleTag
        self.bodyTag = bodyTag




import requests
from bs4 import BeautifulSoup

class Crawler:
    def getPage(self , url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text , 'html.parser')

    def safeGet(self , pageObj , selector ):
        childObj = pageObj.select( selector )
        if childObj is not None and len(childObj) > 0:
            return childObj[0].get_text()
        return ''


    def search(self , topic , site ):
        '''
        주어진 검색어로 주어진 웹사이트를 검색해 결과 페이지를 모두 기록합니다.
        '''
        bs = self.getPage( site.searchUrl + topic )
        searchResults = bs.select(site.resultListing)
        for result in searchResults:
            url = result.select( site.resultUrl)[0].attrs['href']
            # 상대   URL인지 절대 URL인지 확인합니다.
            if(site.absoluteUrl):
                bs = self.getPage(url)
            else:
                bs = self.getPage( site.url + url )

            if bs is None:
                print('Something was wrong with that page or URL. Skipping')
                return

            title = self.safeGet(bs , site.titleTag)
            body = self.safeGet(bs , site.bodyTag)
            if title != '' and body != '':
                content = Content( topic , url , title , body )
                content.print()



def main():
    crawler = Crawler()
    siteData = [
        ['O\'Reilly Media',
         'http://oreilly.com',
         'https://ssearch.oreilly.com/?q=',
         'article.product-result',
         'p.title a',
         True,
         'h1',
         'section#product-description'
        ],
        ['Reuters' , 'http://reuters.com',
         'http://www.reuters.com/search/news?blob=',
         'div.search-result-content',
         'h3.search-result-title a',
         False,
         'h1',
         'div.StandardArticleBody_body_1gnLA'
        ],
        ['Brookings','http://www.brookings.edu',
         'https://www.brookings.edu/search/?s=',
         'div.list-content article',
         'h4.title a',
         True,
         'h1',
         'div.post-body'
        ]
    ]

    sites = []
    for row in siteData:
        sites.append(Website(name = row[0]
                             , url = row[1]
                             , searchUrl = row[2]
                             , resultListing  = row[3]
                             , resultUrl = row[4]
                             , absoluteUrl = row[5]
                             ,titleTag = row[6]
                             , bodyTag = row[7]))

    topics = ['python' , 'data science']
    for topic in topics:
        print('GETTING INFO ABOUT : {}'.format(topic))
        for targetSite in sites:
            crawler.search( topic , targetSite )


if __name__ == '__main__':
    main()
