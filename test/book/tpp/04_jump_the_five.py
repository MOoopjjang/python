#!python3
# -*- coding:utf-8 -*-


########################################
#
# 5를 중심으로 입력숫자 변환
#
########################################

m = {
    1: 9,
    2: 8,
    3: 7,
    4: 6,
    5: 0,
    6: 4,
    7: 3,
    8: 2,
    9: 1
}


def getNumber(_inputNum):
    global m
    return m[_inputNum]


def convert(_str):
    import re
    FILTER = '[0-9]'
    rgx = re.compile(FILTER)

    output = ''
    for v in _str:
        mo = rgx.search(v)
        if mo is not None:
            nv = int(v)
            output += str(getNumber(nv))
        else:
            output += v
    return output


if __name__ == '__main__':
    while True:
        inputValue = input('input str:')
        if inputValue == 'quit':
            break
        output = convert(inputValue)
        print(f'{output}')


