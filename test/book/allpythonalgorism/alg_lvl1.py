#!python3
# -*- coding:utf-8 -*-
# https://www.onlybook.co.kr/entry/algorithm-interview-errata ( 정오표 )

def reorder_data_in_log_files():
    '''
    로그를 재정렬 하라
    기준 :
      1. 로그의 가장 앞 부분은 식별자이다.
      2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
      3. 식별자는 순서에 영향을 끼치지 않지만,문자가 동일할 경우 식별자 순으로 한다.
      4. 숫자 로그는 입력 순서대로 한다.
    ex :
      입력 : logs = ["dlg1 8 1 5 1" , "let1 art can","dlg2 3 6" , "let2 own kit dlg" , "let3 art zero"]
      출력 : logs = ["let1 art can" , "let3 art zero" , "let2 own kit dlg" , "dlg1 8 1 5 1" , "dlg2 3 6"]
    '''

    import re

    def setNumAr(_text):
        rgx = re.compile('[a-zA-Z]')
        ss = _text.split(' ')
        isAllDigit = False
        for s in ss[1:]:
            if len(rgx.findall(s)) == 0:
                isAllDigit = True
                break
        print(f'{_text} --> isAllDigit : {isAllDigit}')
        return isAllDigit


    def setTextAr(_text , _tar):
        _tar.append(_text)

    def sortTextAr(_tar):
       _tar.sort(key = lambda x:(x.split(' ')[1:] , x.split(' ')[0]))


    def merge(_tar, _nar):
        return _tar.extend(_nar)

    orgAr = ["dlg1 8 1 5 1", "let1 art can", "dlg2 3 6", "let2 own kit dlg", "let3 art zero"]
    nar , tar = [] , []
    for text in orgAr:
        print(f'============== text : {text} ===================')
        if setNumAr(text):
            nar.append(text)
        else:
            setTextAr(text , tar)

    sortTextAr(tar)
    merge(tar , nar)

    print(f'nar : {nar} , tar : {tar}')






def palindrome_tst():
    '''
    - 입력받은 문자열을 뒤집어도 같은 문자열일경우
    - 영문 , 숫자만 가능
    '''

    def isPalindrome(strs):
        import re

        rgx = re.compile('[a-zA-Z0-9]')
        reText = rgx.findall(strs)
        print(f'reText :{reText}')
        ar = [c.lower() for c in reText]
        rar = ar[::-1]
        return ar == rar

    inputText = input('input text :')
    if isPalindrome(inputText):
        print('pallindrome')
    else:
        print('not pallindrome')


if __name__ == '__main__':
    #palindrome_tst()
    reorder_data_in_log_files()
