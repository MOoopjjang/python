#!python3

import re

###########################
# 파일인지 url인지 판단하는
###########################

# FILTER = '[a-zA-Z0-9.]'
FILTER = '[^a-zA-Z0-9.]'
URLS = ('http://', 'https://')
FILES = ('.txt', '.log', '.doc')

if __name__ == '__main__':

    while True:
        inputv = input('input string->')
        # rgx = re.compile(FILTER)
        # mo = rgx.findall(inputv)
        # if mo is not None:
        #     print(f'특수문자는 입력할수 없습니다')
        #     continue

        if inputv.endswith(FILES) is True:
            print(f'Text file!!!')
        elif inputv.startswith(URLS):
            print(f'web url!!!')
        else:
            print(f'unknown ')
