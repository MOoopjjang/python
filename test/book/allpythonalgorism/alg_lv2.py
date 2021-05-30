#!python3
# -*- coding:utf-8 -*-



def product_of_array_except_self():
    '''
    배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라.

    입력 : [1,2,3,4]
    출력 : [24,12,8,6]
    주의 : 나눗셈을 하지 않고 O(n)에 풀이하라.
    '''
    pass



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

    def isContain(_output , _v):
        cIndex = -1
        if len(_output) == 0:
            return cIndex

        lv = list(_v)
        lv.sort()
        for  index , ar in enumerate(_output):
            text = ar[0]
            if len(text) != len(_v):continue

            tl = list(text)
            tl.sort()
            if tl != lv:continue

            cIndex = index
            break

        return cIndex

    def in_group_anagrams(_ar):
        output = []
        for i , v in enumerate(_ar):
            cIndex = isContain(output,v)
            if cIndex == -1:
                vv = []
                vv.append(v)
                output.append(vv)
            else:
                cAr = output[cIndex]
                cAr.append(v)
        return output


    result = in_group_anagrams(["eat" , "tea" , "tan" , "ate", "nat","bat"])
    print(f'>>>>>>>>>>> {result} <<<<<<<<<<<<<')






def longest_palindromic_substring():
    '''
    가장 긴 팰린드롬 부분 문자열을 출력하라.
    입력: "babad"
    출력: "bab"
    '''

    def isPalindrom(_s , _e , _ar):
        while _e > _s:
            print(f's : {_ar[_s]} , e : {_ar[_e]}')
            if _ar[_s] != _ar[_e]:
                return False
            _e -= 1
            _s += 1
        return True

    def left(_s , _e , _ar):
        while isPalindrom(_s,_e,_ar) == False:


    def right(_s , _e , _ar):pass


    ar = 'babad'
    result = isPalindrom(0 , len(ar)-1 , ar)
    print(f'result : {result}')

    if result == False:
        size = len(ar)
        e = int(size/2)
        s = 0
        result = isPalindrom(s , e , ar)
        print(f'result : {result}')






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

    def in_three_sum(nums):
        arr = []
        for i,iv in enumerate(nums[:len(nums)-2]):
            j = i+1
            if j > len(nums)-1:
                j = len(nums)-1
            for jv in nums[j:len(nums)-1]:
                k = j+1
                if k > len(nums)-1:
                    k = len(nums)-1
                for kv in nums[k:]:
                    # print(f'iv : {iv} , jv : {jv} , kv : {kv}')
                    if iv+jv+kv == 0:
                        rr = sorted([iv,jv,kv])
                        if rr not in arr:
                            arr.append(rr)
                j += 1

        return arr


    result = in_three_sum([-1,0,1,2,-1,-4])
    print(f'result : {result}')






if __name__ == '__main__':
    # group_anagrams()
    # three_sum()
    longest_palindromic_substring()