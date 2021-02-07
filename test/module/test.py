#!python
#-*- coding:utf-8 -*-

def webbrowser_tst():
	import webbrowser
	input_count = input('count : ')
	for i in range(int(input_count)):
		webbrowser.open_new_tab('http://localhost:8080/eaglesadmin/mainPage')


def scheduler_tst():
	import schedule





if __name__ == '__main__':
    # webbrowser_tst()
	scheduler_tst()
