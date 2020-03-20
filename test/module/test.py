#!python
#-*- coding:utf-8 -*-






import webbrowser



if __name__ == '__main__':
	input_count = input('count : ')


	for i in range(int(input_count)):
		webbrowser.open_new_tab('http://localhost:8080/eaglesadmin/mainPage')