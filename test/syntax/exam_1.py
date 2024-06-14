#!/bin/python

import sys, random


def line_astrik():
    import time

    ASTRIK = '*****'
    index = 5
    increment = False
    while True:
        output = ' '*index+ASTRIK
        print(f'{output}')
        time.sleep(1)
        if increment is False:
            if index != 0:
                index -= 1
            else:
                increment = True
                index += 1
        else:
            if index != 5:
                index += 1
            else:
                increment = False
                index -=1




win = 0
losses = 0
ties = 0
m = {
    'r': 'ROCK',
    'p': 'PAPER',
    's': 'SCISSORS'
}

# 가위 , 바위 , 보 프로그램...
def kbb():
    def ai_kbb():
        n = random.randint(1, 3)
        if n == 1:
            return 'r'
        elif n == 2:
            return 'p'
        else:
            return 's'

    def judgment(_p1, _p2):
        global win, losses, ties
        global m

        print(f'{m.get(_p1)} vs {m.get(_p2)}')
        if _p1 == _p2:
            ties += 1
        else:
            if _p1 is 'r':
                if _p2 is 'p':
                    losses += 1
                else:
                    win += 1
            elif _p1 is 'p':
                if _p2 is 's':
                    losses += 1
                else:
                    win += 1
            else:
                if _p2 is 'r':
                    losses += 1
                else:
                    win += 1

    while True:
        print(f'{win} Wins , {losses} Losses , {ties} Ties')
        input_ai = ai_kbb()
        input_c = input('Enter your move: (r)ock (p)aper (s)cissors or (q)uit:')
        if input_c is 'q':
            sys.exit(0)
        else:
            judgment(input_c, input_ai)


if __name__ == '__main__':
    # kbb()
    line_astrik()
