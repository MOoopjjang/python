#!python3
#coding:utf-8


# usage
# python3 mcw.pyw save [key]
#				  list
#				  [key]


import pyperclip
import sys
import shelve


mcbShelf = shelve.open('mcb')
print(len(sys.argv))
if len(sys.argv) == 3:
	if sys.argv[1].lower() == 'save':
		mcbShelf[sys.argv[2]] = pyperclip.paste()	
	elif sys.argv[1].lower() == 'delete':
		del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
	if sys.argv[1] == 'list':	
		pyperclip.copy(str(list(mcbShelf.keys())))
	else:
		pyperclip.copy(mcbShelf[sys.argv[1]])	

mcbShelf.close()