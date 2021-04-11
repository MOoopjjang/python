#!python3
# -*- coding:utf-8 -*-


def p2_3():
    '''
    - 높이를 입력받아 다음과 같은 숫자 피라미드를 출력하는 다음 게임을 만들어보자.
      머저 숫자가 출력되는 규칙을 잘 찾아보라.
     =====================================================================
     피라미드의 높이를 입력하세요 : 7

                       1
                   1   3   1
                1  3   5   3  1
             1  3  5   7   5  3  1
          1  3  5  7   9   7  5  3  1
       1  3  5  7  9   11  9  7  5  3  1
     1 3  5  7  9  11  13  11 9  7  5  3  1
     =====================================================================


    '''


def p2_2():
    '''
    - 번호 맞히기 게임 ( up-and-dowwn)
    =====================================================================
    숨겨진 두 자리의 숫자를 추측하여 맞추는 게임
    게이머가 숫자를 예측하면 컴퓨터는 정답과 비교하여 "더 큰 숫자입니다" 나 " 더 작은 숫자입니다"
    그리고 맞힌 경우 "정답입니다"를 출력한다.
    중간에 맞히거나 10번 동안 맞히지 못하면 게임이 끝난다.
    =====================================================================
     * 정답을 answer 추측문자를 guess이라 하면,  answer와 guess를 비교하여 결과를
       출력하면 된다.
       정답 범위를 힌트로 제공하기 위해 min과 max변수를 사용한다.
     * 반복문으로는 for를 사용하고 최대 10번 반복하면서 , 중간에 정답을 맞히면 break문을 이용
       하여 루프를 빠져나와 게임을 종료한다.
    '''
    pass





def p2_1():
    '''
    - 소득을 입력하면 세금을 계산하고 세금과 세후 소득을 출력하는 프로그램작성
      ===================================================
    1200 >= 6%
    1200 ~ 4600 15%
    4600 ~ 8800 24%
    8800 ~ 15000 35%
    15000 <      38%
    '''

    traffic = {
        12000000 : 0.06,
        24000000 : 0.15,
        42000000 : 0.24,
        62000000 : 0.35,
        62010000 : 0.38
    }

    def calc(_mod , limit , per):
        print('-'*20)
        print(f'mod : {_mod} , {limit} , {per}')
        av = int(limit - (limit*per)) if _mod > limit else int(_mod - (_mod*per))
        print(f'av : {av}')
        print('-'*20)
        return {
            'cvalue' : av,
            'mod' : (0 if (_mod - limit) < 0 else (_mod - limit))
        }



    input_salary = int(input('salary : '))
    print(f'salary : {input_salary}')

    afterSalary =  0
    orgSalary = input_salary
    for v , p in traffic.items():
        retV = calc(orgSalary, v , p)
        afterSalary += retV['cvalue']
        print(f'afterSalary : {afterSalary}')
        print(f'cvalue : {retV["cvalue"]} , {retV["mod"]}')
        if retV['mod'] == 0:
            break
        orgSalary = retV['mod']

    print(f'>>>>> last salary : {afterSalary} <<<<<< ')




if __name__ == '__main__':
    p2_1()