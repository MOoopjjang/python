#!python3
#-*- coding:utf-8 -*-



import timeit

class StopWatch:
    def __init__(self):
        self._list = []
        self._index= 0
        self._start = 0

    def __repr__( self ):
        output = ''
        for item in self._list:
            output+='##'
            for k,v in item.items():
                output+='- {}:{}'.format(k,v)
        return output



    def start(self):
        self._start = timeit.default_timer()


    def pause(self):
        t = timeit.default_timer()
        data = {'i':self._index , 's':self._start , 'e':t - self._start}
        self._list.append(data)
        print('size : {}'.format(len(self._list)))

        # next 랩타임 갱신
        self._start = t
        self._index +=1

    def stop(self):
        self._list.clear()
        self._index = 0
        self._start = 0



if __name__ == '__main__':
    stopwatch = StopWatch()
    print('## Start ##')
    stopwatch.start()
    while True:
        v = str(input('enter>'))
        if v is 'q':
            break

        stopwatch.pause()


    print(stopwatch)



		
		

		

		

