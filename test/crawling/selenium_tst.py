#!python3
#-*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup


def naver_login():
    # import webbrowser
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import time

    browser = webdriver.Chrome(executable_path='./chromedriver')
    browser.get('http://naver.com')

    # login 버튼클릭
    print('로그인 버튼 클릭')
    elem = browser.find_element_by_class_name("link_login")
    elem.click()
    time.sleep(10)


    # browser 이동
    print('이전화면 이동')
    browser.back()
    time.sleep(10)
    print('앞에 화면이동')
    browser.forward()
    time.sleep(10)


    browser.back()
    time.sleep(10)
    # 검색창 입력
    print('검색어 입력')
    elem = browser.find_element_by_id("query")
    elem.send_keys('하이')
    time.sleep(5)
    print('검색버튼 엔터')
    elem.send_keys(Keys.ENTER)

    command = 'c'
    while command != 'q':
        command = input()












def daum_movie():
    for year in range(2015 , 2020):
        url = 'https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'.format(year)
        print('url : {}'.format(url))
        html = requests.get(url)
        html.raise_for_status()

        soup = BeautifulSoup(html.text,'html.parser')
        images = soup.find_all('img' , attrs={'class':'thumb_img'})
        print('{}'.format(len(images)))
        for index , image in enumerate( images[:5] ):
            image_url = image['src']
            if image_url.startswith('//'):
                image_url = 'https:'+image_url

            image_res = requests.get(image_url)
            image_res.raise_for_status()
            with open('movie_{}_{}.jpg'.format(year , index) , 'wb') as f:
                f.write(image_res.content)


if __name__ == '__main__':
    # daum_movie()
    naver_login()