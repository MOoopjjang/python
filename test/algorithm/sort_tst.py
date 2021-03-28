#!python3
# -*- coding:utf-8 -*-


count = 0

def qsort_tst():
    QSAMLPE1 = [1,4,5,3,12,4,6,7,5,3,3,6,34,3,5,4,2,4,2,2,4,6,6,7,7,8,8,5,4,3,2,7,8,9,9,8,6,5,4,6,7,76,565,44,336]

    def qsort(_ar):
        global count


        if len(_ar) < 2:
            return _ar

        count += 1
        print(f'count >> {count}')

        v = _ar[0]
        low =[ i for i in _ar[1:] if i <= v]
        high = [i for i in _ar[1:] if i > v]
        return qsort(low)+[v]+qsort(high)


    result = qsort(QSAMLPE1)
    print(f'result : {result}')



if __name__ == '__main__':
    qsort_tst()