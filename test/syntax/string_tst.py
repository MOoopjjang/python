#!python3
# -*- coding:utf-8 -*-


"""
string 테스트
"""

SAMPLE_1 = 'xferlog kknda iablc iadifladkfalkflkak123 : '


def tst1():
    print(f'lower = {SAMPLE_1.lower()}')
    print(f'upper = {SAMPLE_1.upper()}')
    sample_l = SAMPLE_1.split(" ")
    print(f'sample_1 = {sample_l}')
    reverse_sample_1 = SAMPLE_1[::-1]
    print(f'reverse_sample_1= {reverse_sample_1}')
    print(f'start xferlog={SAMPLE_1.startswith("xferlog")}')
    print(f'xferlog end = {SAMPLE_1.endswith("xferlog")}')
    print("*"*100)
    print(f'kknda find = {SAMPLE_1.find("kknda")}')
    sindex = SAMPLE_1.find("kknda")
    print(f'sindex start = {SAMPLE_1[sindex:]}')
    join_sample_l = ':'.join(sample_l)
    print(f'join_sample_l = {join_sample_l}')
    print("*"*100)
    print(f'SAMPLE_1 len = {len(SAMPLE_1)}')
    str_a = '44'
    print(f'str_a = {int(44)}')
    print("*"*100)
    for v in SAMPLE_1:
        print(f'v = {v}')

    for i in range(len(SAMPLE_1)):
        print(f'i = {i}')


if __name__ == '__main__':
    tst1()
