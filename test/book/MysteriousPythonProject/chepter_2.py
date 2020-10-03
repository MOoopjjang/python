#!python3
# coding:utf-8

"""
팔린그램 주문 찾기
 - 회문 : 단어를 거꾸로 읽어도 동일한 단어 ( ex ) radar ,kayak , sexes )
 - 팔린그램 : 문구 전체가 회문의 형태를 가지고 있다.
 - http://wordlist.aspell.net/12dicts/ 에서 sample dict다운로드
   /International/2of4brif.txt 파일로 작업
"""

import sys



def palin_word():
    """
    회문 찾기
    """

    def readDict(_file):
        try:
            with open(_file, 'r') as fr:
                for _ in fr: yield fr.readline().strip()
        except IOError as e:
            print("{}\nError opening {}. Terminating program.".format(e, _file), file=sys.stderr)
            sys.exit(1)

    for line in readDict('2of4brif.txt'):
        if line == line[::-1]:
            print('회문 : {}'.format(line))


def search_palintext():
    """
    1. 문장을 입력받는다. ( 3 ~ 7 단어로 구성 )
    2. 단어의 길이가 짝수 인지 체크
    3. 우측의 문장을 단어별로 회문으로 구성
    4. 좌측 문장과 비교
    """

    def analy_text(org_list , le , rs):
        rtext = mtext_ar[rs:]
        print('rrtex : {}'.format(rtext[::-1]))
        tle = le
        for rt in rtext:
            print('>> l : {} - r : {}'.format(org_list[tle] ,rt[::-1]))
            if rt[::-1] != org_list[tle]:return False
            tle -= 1


    while True:
        mtext = input('input text (min : 3 , max : 7):')
        print('==== {} ===='.format(mtext))

        if mtext == 'quit':
            sys.exit(1)

        mtext_ar = mtext.split(" ")
        size = len(mtext_ar)
        le = int(size / 2) - 1
        rs = int(size/2) if size%2 == 0 else int(size/2)+1
        isPalinText = False
        if size%2 != 0:
            m = mtext_ar[le+1]
            if m == m[::-1]:
                isPalinText = analy_text(mtext_ar , le , rs)
        else:
            isPalinText = analy_text(mtext_ar, le, rs)

        if isPalinText == False:
            print('not palin text')
        else:
            print("'{}' is palinText".format(mtext))









def main():
    # palin_word()
    search_palintext()



if __name__ == '__main__':
    main()