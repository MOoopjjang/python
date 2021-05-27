#!python3
# -*- coding:utf-8 -*-

def group_anagrams():
    '''
    문자열 배열을 받아 애너그램 단위로 그룹핑하라.

    입력: ["eat" , "tea" , "tan" , "ate", "nat","bat"]
    출력 :
    [
        ["ate" , "eat" , "tea"],
        ["nat" , "tan"],
        ["bat"]
    ]
    '''

    def isContain(_output, _v):
        cIndex = -1
        if len(_output) == 0:
            return cIndex

        lv = list(_v)
        lv.sort()
        for index, ar in enumerate(_output):
            text = ar[0]
            if len(text) != len(_v): continue

            tl = list(text)
            tl.sort()
            if tl != lv: continue

            cIndex = index
            break

        return cIndex

    def in_group_anagrams(_ar):
        output = []
        for i, v in enumerate(_ar):
            cIndex = isContain(output, v)
            if cIndex == -1:
                vv = []
                vv.append(v)
                output.append(vv)
            else:
                cAr = output[cIndex]
                cAr.append(v)
        return output

    result = in_group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(f'>>>>>>>>>>> {result} <<<<<<<<<<<<<')


def longest_palindromic_substring():
    '''
    가장 긴 팰린드롬 부분 문자열을 출력하라.
    입력: "babad"
    출력: "bab"

<<<<<<< HEAD
    progress : ing
    '''
=======
    tmp_ar = []
    def in_left(_s , _e ,  org_ar, t_ar):
        while _e>_s:
            if org_ar[_s] != org_ar[_e]:
                in_left()
            else:
                _s+=1
                _e-=1




    def in_right(_s , _e , t_ar):pass




def three_sum():
    '''
    세수의 합

    배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.

    입력 : nums = [-1,0,1,2,-1,-4]
    출력 :
    [
      [-1,0,1]
      [-1,-1,2]
    ]
    '''

>>>>>>> 4aafe5b1e45d795e3a72a7f02fee79796138d034

    def isPalindrom(_ar, _s, _e):
        print(f'_ar : {_ar} , _s : {_s} , _e : {_e}')
        while _e > _s:
            if _ar[_s] != _ar[_e]:
                return False
            _s += 1
            _e -= 1
        return True


if __name__ == '__main__':
    group_anagrams()
