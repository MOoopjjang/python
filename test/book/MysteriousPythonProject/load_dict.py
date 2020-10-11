#!python3
# -*- coding:utf-8 -*-

def gen_load_dict(_file):
    with open(_file, 'r') as fr:
        for _ in fr:
            yield fr.readline().lower().strip()


def load_dict(_file):
    word_list = []
    with open(_file , 'r') as fr:
        for _ in fr:
            word_list.append(fr.readline().lower().strip())
    return word_list
