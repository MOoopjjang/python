#!python3
# -*- coding:utf-8 -*-


'''
앞뒤를 뒤집어도 똑같은 문자열을 팰린드롬(palindrome)이라고 합니다.
문자열 s가 주어질 때, s의 부분문자열(Substring)중 가장 긴 팰린드롬의 길이를 return 하는 solution 함수를 완성해 주세요.
예를들면, 문자열 s가 abcdcba이면 7을 return하고 abacde이면 3을 return합니다.
제한사항
    • 문자열 s의 길이 : 2,500 이하의 자연수
    • 문자열 s는 알파벳 소문자로만 구성

입출력 예
s	answer
abcdcba	7
abacde	3
입출력 예 설명
입출력 예 #1
4번째자리 'd'를 기준으로 문자열 s 전체가 팰린드롬이 되므로 7을 return합니다.
입출력 예 #2
2번째자리 'b'를 기준으로 aba가 팰린드롬이 되므로 3을 return합니다.

test case
    test('solution', () => {
      expect(solution("abcdcba")).toBe(7);
      expect(solution("abacde")).toBe(3);
      expect(solution("abcabcdcbae")).toBe(7);
      expect(solution("aaaa")).toBe(4);
      expect(solution("abcde")).toBe(1);
      expect(solution("a")).toBe(1);
      expect(solution("abcbaqwertrewqq")).toBe(9);
      expect(solution("abcbaqwqabcba")).toBe(13);
      expect(solution("abba")).toBe(4);
      expect(solution("abaabaaaaaaa")).toBe(7);
    });
'''


def solution(text):
    def getReverseText(_t):
        tmp = list(_t)
        tmp.reverse()
        return ''.join(tmp)

    limit = len(text) // 2
    total_len = len(text)
    ls = le = rs = re = count = 0

    while le < total_len:
        le += 1
        rs = le
        print('ls : {} , rs : {} , le : {} , limit : {}'.format(ls, rs, le, limit))
        ltext = getReverseText(text[ls:le + 1])
        rtext = text[rs:]
        print('ltext : {} | rtext : {}'.format(ltext, rtext))

        index = rtext.find(ltext)
        print('index : {}'.format(index))
        if index != -1:
            if index == 0:
                count = len(ltext) * 2 - 1
                # break
        else:
            ls += 1

    print('>>>> result : {} <<<<'.format(count))
    print('>>>> result text : {} <<<<'.format(text[ls:ls+count]))

    return count









    # while limit != le:pass




if __name__ == '__main__':
    # ar1 = 'xabcbaxfe'
    ar1 = 'abcdedcba'
    # ar1 = 'abacde'
    # ar1 = 'zcabade'
    # ar1 = 'zmdaimvaadafaabcdcbaf'
    # ar1 = 'zmdaimvaadafacuiacizf'
    # ar1 = 'abcde'
    # ar1 = 'abcabcdcbae'
    ar1 = 'aaaa'
    ar1 = 'abcde'
    ar1 = 'a'
    ar1 = 'abcbaqwertrewqq'
    solution(ar1)
