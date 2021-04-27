#!python3




def most_common_word():
    '''
    금지된 단어를 제와한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며 , 구두점( 마침표 , 쉼표 )또한 무시한다.

    입력 :
      paragraph = "Bob hit a ball , the hit BALL flew far after it was hit."
      banned = ["hit"]
    출력 :
      "ball"
    '''

    def in_most_common_word(paragraph , banned):
        d = {}
        paragraph = paragraph.lower().replace(",","").replace(".","")
        banned = [bannword.lower() for bannword in banned]
        print(f'paragraph : {paragraph} , banned : {banned}')
        for word in paragraph.split(' '):
            if word in banned:continue
            if word not in d:
                d[word] = 0
            d[word]+=1

        sd = sorted(d.items() , key = lambda x:x[1] , reverse=True)
        return sd[0]


    ret = in_most_common_word("Bob hit a ball , the hit BALL flew far after it was hit." , ["hit"])
    print(f'ret : {ret}')









if __name__ == '__main__':
    most_common_word()
