#!python
#-*- coding:utf-8 -*-



def tst():
	proc = subprocess.Popen(['echo' , 'Hello from the child!'] , stdout = subprocess.PIPE)
	out , err = proc.communicate()
	print(out.decode('utf-8'))


if __name__ == '__main__':
	tst()