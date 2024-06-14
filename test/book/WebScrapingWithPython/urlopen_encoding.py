#!python3

import sys
from urllib.request import urlopen

FILE_SAVE = False
SAVE_FILE='dp.html'

if __name__ == '__main__':
    f = urlopen('http://www.hanbit.co.kr/store/books/full_book_list.html')
    encoding = f.info().get_content_charset(failobj='utf-8')
    print('encoding' , encoding , file=sys.stderr)
    text = f.read().decode(encoding)
    print(f'{text}')

    if FILE_SAVE is True:
        with open(SAVE_FILE , 'wt' , newline='') as fw:
            fw.write(text)

