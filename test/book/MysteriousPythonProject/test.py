#!python3
# coding:utf-8


from book.MysteriousPythonProject.load_dict import *
from collections import Counter


def tst1():
    SAM1 = 'i am lotte love'
    SAM2 = 'lovema'

    tsam = ''.join(SAM1.split())
    print('d_sam : {}'.format(tsam))
    csam = Counter(tsam)
    csam2 = Counter(SAM2)
    print('c_sam : {}'.format(csam))
    print('c_sam2 : {}'.format(csam2))

    text = ''
    for w in csam2:
        if csam2[w] <= csam[w]:
            text += w

    print('text : {}'.format(text))

    print('-' * 30)


def tst2():
    while True:
        name = input('name:')
        dict_infos = gen_load_dict('2of4brif.txt')
        l = find_anagram(name  , dict_infos)
        for word in l:
            print('word : {}'.format(word))


def find_anagram(_name, dict_info):
    tname = ''.join(_name.lower().split())
    d_name = Counter(tname)
    anagram_list = []
    for word in dict_info:
        d_word = Counter(word.lower())
        text = ''
        for w in d_word:
            if d_word[w] <= d_name[w]:
                text += w

        if len(text.lower()) == len(_name.lower()) and text.lower() not in anagram_list:
            anagram_list.append(text)
    return anagram_list


if __name__ == '__main__':
        # tst1()
    tst2()