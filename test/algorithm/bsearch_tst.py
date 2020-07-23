#!python3
# -*- coding:utf-8 -*-

'''
 - 이진 검색 테스트
 - 코드 refactoring 필요
'''
DIVIDE = 2


def search(_ar, max_index, length, s, e, searchV):
    print('>>>> {} :::: length : {} ::: s : {} ::::e : {}<<<<'.format(_ar[s:e], length, s, e))

    if int(length / DIVIDE) == 0:
        return e if _ar[e] == searchV else -1

    index = max_index if (int(length / DIVIDE) + s) > max_index else (int(length / DIVIDE) + s)

    #################
    # 검색 범위지정을 위한
    #################
    piece_len = int(length / DIVIDE)
    v = _ar[index]
    print('index : {}, piece_len : {} , v : {}'.format(index, piece_len, v))
    if v == searchV:
        print('!!!!search {}:{}'.format(index, v))
        return index

    if searchV > v:
        s = index + 1
        e = max_index if (index + piece_len) > max_index else index + piece_len
    else:
        e = index - 1
        s = index - piece_len

    # 배열은 0부터 시작하므로 0 인덱스도 길이로 포함
    length = e - s + 1

    print('s : {} , e: {} , length : {}'.format(s, e, length))
    # 재귀
    return search(_ar, max_index, length, s, e, searchV)


def tst1():
    import timeit

    # ar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # ar = [1, 2, 3 , 5, 6,  8, 9, 10, 11, 12]
    ar = [i for i in range(10)]
    print('******** {} *******'.format(len(ar)))
    while True:
        searchV = int(input('>>'))
        s = timeit.default_timer()
        index = search(ar, len(ar) - 1, len(ar), 0, len(ar), searchV)
        if index == -1:
            print('searach not found')
        else:
            print('{} 에 존재합니다.'.format(index))


def tst2():
    # def bsearch(_ar, low, high, searchV):
    #     if low > high:return -1
    #      mid = int((high + low) / 2)
    #      print('high : {} , low : {} , mid : {}'.format(high , low,mid))
    #
    #      print('searchV : {} , v : {}'.format(searchV, _ar[mid]))
    #      if searchV == _ar[mid]:
    #          print('-------- search : {} ---------'.format(mid))
    #          return mid
    #      elif searchV > _ar[mid]:
    #          return bsearch(_ar, mid + 1, high, searchV)
    #      else:
    #          return bsearch(_ar, low, mid - 1, searchV)

    def bsearch(_ar, low, high, searchV):
        print('>>>>> low : {} , high : {} <<<<<'.format(low, high))
        if low > high: return -1

        mid = int((high + low) / 2)

        print('mid : {} , v : {} , searchV : {}'.format(mid, _ar[mid], searchV))
        if _ar[mid] == searchV:
            return mid

        if _ar[mid] > searchV:
            return bsearch(_ar, low , mid - 1, searchV)
        else:
            return bsearch(_ar, mid+1, high , searchV)

    # ar = [i for i in range(1, 13)]
    ar = [1, 2, 4, 7, 8, 10, 11, 12, 15]
    while True:
        searchV = int(input('>>'))
        if bsearch(ar, 0, len(ar) - 1, searchV) == -1:
            print('exit')
            break


def tst3():
    def solution(n, times):
        left = 0
        right = max(times) * n
        temp = right
        answer = right

        print('>>>>> left : {} , right : {} , temp : {} , answer : {} <<<<<'.format(left, right, temp, answer))

        while right >= left:
            mid = (right + left) // 2
            people = 0
            print('LOOP :: right : {} , left : {} , mid : {} , people : {}'.format(right, left, mid, people))
            for i in times:
                people += mid // i
                print('[[[ i : {} , people : {} ]]]'.format(i, people))

            print('**** people : {} , n : {}'.format(people , n))
            if people == n:
                if answer >= mid:
                    answer = mid
                right = mid - 1
            elif people > n:
                right = mid - 1
            else:
                left = mid + 1

        print('result ==? answer : {} , temp : {}'.format(answer , temp))
        if answer == temp:
            return right + 1
        else:
            return answer

    v = solution(6, [7, 10])
    print('v : {}'.format(v))


if __name__ == '__main__':
    # tst1()
    # tst2()
    tst3()
