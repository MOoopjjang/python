#!python3
# -*- encoding:utf-8 -*-


import os , sys


########################################
# ./picnic.py salad
#  => You are bringing salad
#
# ./picnic.py salad chips
# => You are bringing salad and chips
#
# ./picnic.py salad chips cupcakes
#=> You are bringing salad , chips, and cupcakes
#
########################################



def makeStr(_argv):
    PRE_STR = 'You are bringing '
    args = sys.argv[1:]
    size = len(args)
    bodyStr = ''
    if size is 0:
        print('parameter error')
        exit(1)

    # sorted
    if args[0] == '--sorted':
        del args[0]
        args.sort(reverse=False)
        size = len(args)

    if size is 1:
        bodyStr = args[0]
    elif size is 2:
        bodyStr = args[0]+' and '+args[1]
    else:
        lstr = ' and '+args[size-1]
        for param in args[:size-1]:
            bodyStr = bodyStr+param+','
        bodyStr = bodyStr+lstr
    return PRE_STR+bodyStr



if __name__ == '__main__':
    result = makeStr(sys.argv)
    print(f'result={result}')




