#!python3
#-*- coding:utf-8 -*-


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from bs4 import BeautifulSoup
import time
import urllib.request
from urllib.request import Request, urlopen
from urllib.request import URLError, HTTPError
from urllib.parse import quote

import json
import ast



# browser = webdriver.PhantomJS(os.getcwd()+'/phantomjs')
# options = webdriver.ChromeOptions()
# options.add_argument('--no-sandbox')
# options.add_argument("--headless")
# browser = webdriver.Chrome(os.getcwd()+'/chromedriver', chrome_options=options)
# browser = webdriver.PhantomJS(os.getcwd()+'/chromedriver')
# browser.set_window_size(1024, 768)

# url = 'https://www.google.com/search?q=' + quote(
#                 '박지효 글래머') + '&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch' + '&tbs=' + '&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'
# browser.get('http://www.google.com/search?q=jordan&newwindow=1&source=lnms&tbm=isch')

url = 'https://www.google.com/search?q=%EC%A7%80%ED%9A%A8%20%EA%B8%80%EB%9E%98%EB%A8%B8&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&tbs=&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'
# browser.get(url)
# time.sleep(1)
print("Getting you a lot of images. This may take a few moments...")

# element = browser.find_element_by_tag_name("body")
# # Scroll down
# for i in range(30):
#     element.send_keys(Keys.PAGE_DOWN)
#     time.sleep(0.3)

# try:
#     browser.find_element_by_id("smb").click()
#     for i in range(50):
#         element.send_keys(Keys.PAGE_DOWN)
#         time.sleep(0.3)  # bot id protection
# except:
#     for i in range(10):
#         element.send_keys(Keys.PAGE_DOWN)
#         time.sleep(0.3)  # bot id protection

# print("Reached end of Page.")
# time.sleep(0.5)

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
req = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(req)
respData = str(resp.read())

pageSource = respData
# browser.close()

# print(pageSource)
bsObj = BeautifulSoup(str(pageSource) , 'html.parser')
mainE = bsObj.findAll('div' , {'class':'rg_meta notranslate'})
print(len(mainE))
for e in mainE:
    stre = str(e)
    # print(stre)
    start = len('<div class="rg_meta notranslate">')
    end = len(stre) - len('</div>')
    # print(stre[start:end])
    loads = stre[start:end]
    # print(loads)
    # d= dict(loads)
    # loads = str('\"'+loads+'\"')

    start = loads.find('ou\":')
    ss = loads[start+5:]
    end = ss.find(',')
    sss = ss[:end-1]
    

    print(sss)

    # jsonStr = json.dumps(loads)

    # print(type(jsonStr))
    # a = ast.literal_eval(jsonStr)
    # print(type(a))

    # jsonStr = json.dumps(loads)
    # print('jsonStr : %s'%jsonStr)
    # jObj = json.loads(loads)

    # d = dict(jObj)
    # print(type(jObj))
 

# for index, e in enumerate(mainE):
#     try:
#         print(e.attrs['data-src'])
#     except:
#         pass
   

# for e in mainE:
#     src = e.attrs['data-src']
#     if src:
        # print(src)

# imgUrls = [ e.attrs['data-src'] for e in mainE if e.attrs['data-src'] != None and e.attrs['data-src'].startswith('http')]
# for img in imgUrls:
# 	print(img)


