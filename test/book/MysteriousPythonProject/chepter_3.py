#!python3
# coding:utf-8



import sys

"""
 - 아나그램
"""


def gen_dict(_file):
    try:
        with open(_file , 'r') as fr:
            for _ in fr:
                yield fr.readline().strip()
    except IOError as e:
        print('error : {}'.format(e))
        sys.exit(1)



def result_func(_result):
    for w in _result:
        print('result ==> {}'.format(w))


def process( iWord , wFunc , _file):
    anagram_list = []
    s_input_word = sorted(iWord)
    for word in wFunc(_file):
        # word = word.lower()
        if iWord != word and s_input_word == sorted(word):
            anagram_list.append(word)

    return anagram_list

def main( fProcess, rfunc):
    while True:
        input_word = input('input :')
        if input_word == 'q':break
        rfunc(fProcess(input_word.lower() , gen_dict , '2of4brif.txt'))


if __name__ == '__main__':
    main(process , result_func)



