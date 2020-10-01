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

    while True:
        mtext = input('input text (min : 3 , max : 7):')
        print('mtext : {}'.format(mtext))

        mtext_ar = mtext.split(" ")
        print('len : {}'.format(len(mtext_ar)))
        size = len(mtext_ar)
        le = int(size / 2) - 1
        rs = int(size/2) if size%2 == 0 else int(size/2)+1
        print('le : {} , rs : {}'.format(le , rs))
        isPalinText = False
        if size%2 != 0:
            m = mtext_ar[le+1]
            if m == m[::-1]:
                rtext = mtext_ar[rs:]
                print('rrtex : {}'.format(rtext[::-1]))
        else:
            pass

        if isPalinText == False:print('not palin text')









def main():
    # palin_word()
    search_palintext()



if __name__ == '__main__':
    main()