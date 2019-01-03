#!python
#-*- coding:utf-8 -*-



IS_LOOP_EXIST = False

def handler( signum , frame ):
	global IS_LOOP_EXIST
	print('Signal handler called with signal {}'.format(signum))
	IS_LOOP_EXIST = True




def getString( x , _pid ):
	return '-{}- : {}'.format(_pid , x)


def exec( _lock ):
	result = [ getString( x , os.getpid() ) for x in range(10000) ]
	_lock.acquire()
	mode = 'a' if os.path.exists(os.getcwd()+'/result.txt') else 'w'
	with open(os.getcwd()+'/result.txt' , mode) as fw:
		for line in result:
			fw.write(line+'\n')
	_lock.release()



def main():

	signal.signal(signal.SIGALRM , handler )

	if os.path.exists(os.getcwd()+'/result.txt'):os.unlink(os.getcwd()+'/result.txt')

	s = timeit.default_timer()
	lock = Lock()
	if sys.argv[1] == '1':
		procs = [ Process(target = exec , args = (lock,)) for _ in range(8) ]
	else:
		procs = [ Thread(target = exec , args = (lock,)) for _ in range(8) ]

	for proc in procs:
		proc.start()
	for proc in procs:
		proc.join()

	print(' time : {}'.format(timeit.default_timer() - s))

	signal.alarm(1)

	while IS_LOOP_EXIST == False:
		print('sleep....')
		time.sleep(1)

	signal.alarm(0)
	print(' Program end!!!')

if __name__=='__main__':
	main()




