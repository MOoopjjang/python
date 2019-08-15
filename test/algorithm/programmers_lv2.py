#!python3
#-*- coding:utf-8 -*-


def solution( nums ):
	"""
	 - nums/2 만큼을 골라야 한다.
	 - nums/2 고르는것중 최다 종류로 골라야 한다
	 - 그 값을 반환한다.


	 set을 이용
	"""

	my = int(len(nums)/2)
	print('my :{}'.format(my))

	filterS = set(nums)
	if len(filterS) >= (my*2):
		print('cc :{}'.format(my))


	s = set()
	for m in range(0,my):
		# print('m :{}'.format(m))
		for n in nums:
			if n != nums[len(nums)-1]:
				for nn in nums[n+1:]:
					s.add((n,nn))


	print('s : {}'.format(s))

	answer = 0
	return answer



def solution2(phone_book):
	"""
	문제 설명
		전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
		전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

		구조대 : 119
		박준영 : 97 674 223
		지영석 : 11 9552 4421
		전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

		제한 사항
		phone_book의 길이는 1 이상 1,000,000 이하입니다.
		각 전화번호의 길이는 1 이상 20 이하입니다.
	"""


	orgl = len(phone_book)
	fl = set(phone_book)
	cl = len(list(fl))

	if orgl != cl:return False

	for index,p in enumerate(phone_book):
		orglen = len(p)
		for pp in phone_book[index+1:]:
			spp = pp.replace(' ','')
			print('result : {} - {} :{}'.format(p , spp , spp.startswith(p)))
			if spp.startswith(p):
				return False

	return True




def solution4(progresses, speeds):

	"""

	  - progresses 별로 배포일 개산 및 매칭 ( dict )
	  - 순서별로 앞 > 뒤 개발 완료일이 클경우 { dict }
	  -  dict의 값들을 차레로 배열로 생성후 반환

	  result : PASS
	"""

	mdict = {}
	for index , progress in enumerate(progresses):
		v = 100 - progress
		day = int(v/speeds[index])
		mdict[index] = day

	print('mdict : {}'.format(mdict))	


	rdict = {}
	vv = 0
	ckey = None
	for k in mdict.keys():
		kv = mdict[k]
		if k not in rdict:rdict[k] = 0


		if (vv == 0) or (vv < kv):
			rdict[k]=1
			vv = kv
			ckey = k
		else:
			rdict[ckey]+=1

	answer = [v for k,v in rdict.items() if v != 0]
	return answer


def solution5(s):
	"""
	문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. 
	str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 (최소값) (최대값)형태의 문자열을 반환하는 함수, solution을 완성하세요.
	예를들어 s가 1 2 3 4라면 1 4를 리턴하고, -1 -2 -3 -4라면 -4 -1을 리턴하면 됩니다.

	result : PASS
	"""

	"""
	  - 분리
	  - sorted로 값 분리 
	"""
	splits = s.split(' ')
	intar = [ int(v) for v in splits]
	sortint = sorted(intar)
	answer = str(sortint[0])+' '+str(sortint[len(sortint)-1])
	return answer



if __name__ == '__main__':
	# solution([3,1,2,3])

	# print('result: {}'.format(solution2(['119', '97674223', '1195524421'])))
	# print('result: {}'.format(solution2(['123','456','789'])))
	# print('result: {}'.format(solution2(['12','123','1235','567','88'])))
	# print('result: {}'.format(solution2(['98','123','13235','567','88'])))
	# print('result: {}'.format(solution2([93,30,55])))

	# solution4([93,30,55] , [1,30,5])
	# solution4([93,30,55] , [1,30,5])


	# solution5("1 2 3 4")
	answer = solution5("-1 -2 -3 -4")
	print('answer : {}'.format(answer))

