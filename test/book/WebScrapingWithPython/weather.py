#!python3

import sys
from urllib.request import urlopen

URL = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109'



def getWeatherHtml():
    requstData = urlopen(URL)
    encoding = requstData.info().get_content_charset(failobj='utf-8')
    html = requstData.read().decode(encoding)
    print(f'{html}')
    return html


def save(_path , _data):
    with open(_path , 'wt', newline='') as fw:
        fw.write(_data)



if __name__ == '__main__':
    html = getWeatherHtml()
    # save('weather.jsp' , html)
