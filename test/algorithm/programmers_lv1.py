#!python3

"""
 초급
"""

def solution2( participant, completion ):
	"""
	result ( 호율 : X )
	"""
	for p in participant:
		if p in completion:
			completion.remove(p)
		else:
			return p




def solution(n = None):
	"""
	result ( PASS )
	"""
	if n == None or n > 10000000000:
		raise Exception("error")

	strN = str(n)
	answer = []
	index = len(strN)-1
	while index >= 0:
		answer.append(int(strN[index]))
		index-=1

	print(answer)

def solution3(strings, n):
	"""
	result ( 기능 : X )
	"""
    from operator import itemgetter


    ss = sorted(strings , key = lambda s: (s[n] , s[ n+1 if (len(s)-1)>n else n ]))
    print(ss)


def solution6(n):
	"""
	result ( PASS )
	"""
    cstr = str(n)
    l = sorted(cstr , reverse = True)
    d_str = ''.join(l)
    answer = int(d_str)
    print(answer)
    return answer

def solution7(arr):
	"""
	result ( PASS )
	"""
	print('before ::{}'.format(arr))

	before = -1
	answer = []
	for i in arr:
		if before != i:
			answer.append(i)
		before = i

	
	print('after ::{}'.format(answer))
	return answer


if __name__ == '__main__':
	# print(solution2(['leo', 'kiki', 'eden'] , ['eden', 'kiki']))
	# print(solution2(['mislav', 'stanko', 'mislav', 'ana'] , ['stanko', 'ana', 'mislav']))

	# solution3(['sun', 'bed', 'car'] , 1)
	# solution3(['abce', 'abcd', 'cdx'] , 2)

	# solution6(118372)

	# solution7([1,1,3,3,0,1,1])
	solution7([4,4,4,3,3])





