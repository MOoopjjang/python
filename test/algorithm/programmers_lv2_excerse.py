#!python3
#-*- coding:utf-8 -*-



def calculation(n):
	return int(n/3) , int((n-1)/3) , int(n%3)


def solution1(n):
	"""
	124 나라가 있습니다. 124 나라에서는 10진법이 아닌 다음과 같은 자신들만의 규칙으로 수를 표현합니다.

	124 나라에는 자연수만 존재합니다.
	124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용합니다.
	"""

	f , bf , s = calculation(n)
	resultStr = ''


	resultStr = str(bf)+'4' if s == 0 else str(f)+str(s)
	if resultStr.startswith('0'):	
		resultStr = resultStr.replace('0' , '')

	# firPlace = ''
	# if resultStr[0] not in [1,2,4]:
	# 	a,b,c = calculation(int(result[0]))
		


	# lastResult = firPlace.concat(resultStr[1:])
		
	return resultStr



def solution2(heights):
	"""
	수평 직선에 탑 N대를 세웠습니다. 모든 탑의 꼭대기에는 신호를 송/수신하는 장치를 설치했습니다.
	 발사한 신호는 신호를 보낸 탑보다 높은 탑에서만 수신합니다.
	  또한, 한 번 수신된 신호는 다른 탑으로 송신되지 않습니다.

	예를 들어 높이가 6, 9, 5, 7, 4인 다섯 탑이 왼쪽으로 동시에 레이저 신호를 발사합니다. 
	그러면, 탑은 다음과 같이 신호를 주고받습니다. 
	높이가 4인 다섯 번째 탑에서 발사한 신호는 높이가 7인 네 번째 탑이 수신하고, 
	높이가 7인 네 번째 탑의 신호는 높이가 9인 두 번째 탑이, 
	높이가 5인 세 번째 탑의 신호도 높이가 9인 두 번째 탑이 수신합니다.
	 높이가 9인 두 번째 탑과 높이가 6인 첫 번째 탑이 보낸 레이저 신호는 어떤 탑에서도 수신할 수 없습니다.
	"""
	answer = []
	for index , v in enumerate(heights):
		if index == 0:
			answer.append(0)
			continue

		curValue = heights[index]
		loop = index-1
		# tmpar = heights[:index]
		isFind = False
		while loop >= 0:
			if curValue < heights[loop]:
				isFind = True
				break
			loop -=1

		answer.append(loop+1 if isFind else 0)

	return answer




def solution(progresses, speeds):
	"""
	프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 
	각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

	또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 
	이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

	먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 
	적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.
	"""

	answer = []
	tdict = {}
	for index , v in enumerate(progresses):
		tdict[index] = int((100 - v)/speeds[index])

	print('tdict : {}'.format(tdict))
	deployCount = 1
	prevDeployDay = 0
	for k,v in tdict.items():
		if prevDeployDay == 0:
			prevDeployDay = v
		elif prevDeployDay >= v:
			deployCount +=1
			prevDeployDay = v
		else:
			answer.append(deployCount)
			deployCount = 1
			prevDeployDay = v

	answer.append(deployCount)
	return answer






def solution3(numbers):

	count = 0
	ar = list(numbers)
	for index , i in enumerate(ar):
		for index2,j in enumerate(ar):
			if index == index2:continue

			intI = int(i)
			insertV = int(i+j)
			if intI == 2 or intI == 3 or ( int(insertV%2) != 0 and int(insertV%3) != 0):
				count +=1


	answer = count
	return answer



def solution4(bridge_length, weight, truck_weights):
	"""
	트럭 여러 대가 강을 가로지르는 일 차선 다리를 정해진 순으로 건너려 합니다.
	 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다.
	  트럭은 1초에 1만큼 움직이며, 다리 길이는 bridge_length이고 다리는 무게 weight까지 견딥니다.
	※ 트럭이 다리에 완전히 오르지 않은 경우, 이 트럭의 무게는 고려하지 않습니다.

	예를 들어, 길이가 2이고 10kg 무게를 견디는 다리가 있습니다. 
	무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.
	"""

	total_sec = 0
	sector = 0
	queue = list()
	curidx = 0
	while True:
		total_sec +=1
		print('total_sec : {}'.format(total_sec))
		print('qsize : {} , sector : {}'.format(len(queue) , sector))
		if sector == bridge_length:
			print('get : {}'.format(queue[0]))
			del queue[0]
			sector = len(queue)
			if curidx >= len(truck_weights) and len(queue) == 0:
				break

		sector += 1

		if curidx < len(truck_weights):
			truck = truck_weights[curidx]
			print('bridge : {} - truck : {}'.format(queue , truck))
			if len(queue) == 0:
				queue.append(truck)
				curidx +=1
			else:
				if sum(queue)+truck <= weight:
					queue.append(truck)
					curidx +=1

		
	return total_sec



def func(numbers , i , ar):
	if i == len(numbers)-1:
		output = ''
		for v in numbers:
			output += str(v)

		ar.append(output)
	else:
		for j in range(i , len(numbers)):
			numbers[i] , numbers[j] = numbers[j] , numbers[i]
			func(numbers , i+1 , ar)
			numbers[i] , numbers[j] = numbers[j] , numbers[i]



def solution5(numbers):
	ar = []
	func(numbers , 0 , ar)

	ar.sort(reverse = True)
	return ar[0]
	


def perm( input , i):
	if i == len(input)-1:
		print(input)
	else:
		for j in range(i , len(input)):
			input[i] , input[j] = input[j] , input[i]
			print('i : {} , j : {} ,input : {}'.format(i,j,input))
			perm(input , i+1 , ar)
			print('*'*20)
			input[i] , input[j] = input[j] , input[i]
			print('n-i : {} , j : {} ,input : {}'.format(i,j,input))
		






if __name__ == '__main__':
	# for i in range(1,200):
	# 	answer = solution1(i)
	# 	print('answer :{} -> {} '.format(i,answer))

	# answer = solution2([1,5,3,6,7,6,5])



	# answer = solution([93,30,55] , [1,30,5])
	# answer = solution([50,70,55] , [50,10,1])

	


	# answer = solution4(2 , 10 , [7,4,5,6])
	# answer = solution4(100 , 100 , [10])
	# answer = solution4(100 , 100 , [10,10,10,10,10,10,10,10,10,10])

	

	answer = solution5([6, 10, 2])
	print('answer : {}'.format(answer))


