#!python
#-*- coding:utf-8 -*-


import os

def mprintLog( log_file , search_world , pre_index , post_index ):
	fr = open(log_file , 'r')
	logBuffer = fr.read().split('\n')
	fr.close()
	# print(logBuffer)

	print(type(logBuffer))
	for index,line in enumerate( logBuffer ):
		if search_world in line:
			start = index-pre_index if index-pre_index > 0 else 0
			end = index + post_index if index + post_index < len(logBuffer) else len(logBuffer)
			output = '\n'.join(logBuffer[start:end+1])
			print('{}'.format(output))
		
	
def get_log_data(logData , index , pre_i , post_i ):
	start = max(0 , logData.rfind('\n' , 0 , index))

	for i in range(0 , pre_i):
		start = max(0 , logData.rfind('\n' , 0 , start))

	end = logData.find('\n' , index , len(logData))
	for i in range(0 , post_i):
		nxt = logData.find('\n' , end+1 , len(logData))
		if nxt == -1:
			nxt = end
			break
		else:
			end = nxt

	return logData[start:end]






def printLog(log_file , search_world  , _which , pre_index , post_index):
	fr = open( log_file , 'r')
	logBuffer = fr.read()
	fr.close()

	index = logBuffer.find(search_world,_which)
	if index > 0:
		while True:
			print('-'*70)
			print(' search :{}'.format(search_world))
			print(' search index : {}'.format(index ))
			print('-'*70)
			result = get_log_data(logBuffer , index , pre_index , post_index )
			print('result :{}'.format(result))

			nxt = logBuffer.find(search_world , index+1 , len(logBuffer))
			if nxt == -1:
				break
			index = nxt






if __name__ == '__main__':
	# mprintLog('/svc/license-nxt/was/tomcat-7.0.68/logs/catalina.out' , 'REPROCESSING SKIP!!!' , 2 , 2)

	size = os.path.getsize('/svc/license-nxt/was/tomcat-7.0.68/logs/catalina.out')
	printLog('/svc/license-nxt/was/tomcat-7.0.68/logs/catalina.out' , 'REPROCESSING SKIP!!!' , int(size/2) , 2 , 2)






