#!python3
#-*- coding:utf-8 -*-



import time



class StopWatcher:
	def __init__( self , _lap , _startTime ):
		self._time_lap = _lap
		self._start = _startTime
		self._end = None

	def __str__( self ):
		return '[%s]duration time : %d'%(self._time_lap , self._end-self._start)

	def getStart( self ):
		return 


	def end( self ):
		self._end = time.time()




if __name__ == '__main__':
	wl = []
	count = 0
	while True:
		try:
			count +=1
			cStopWatcher = StopWatcher(count , time.time())
			input('\"enter\" end')
		
			cStopWatcher.end()
			wl.append(cStopWatcher)
			print(cStopWatcher)
		except KeyboardInterrupt:
			break;


	print('*'*40)
	for w in wl:print(w)
		
		

		

		

