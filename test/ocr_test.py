#!python3
#-*- coding:utf8 -*-


from PIL import Image
import pytesseract


def main():
	print(pytesseract.image_to_string(Image.open('058-062_003-0.jpg')))



if __name__ == '__main__':
	main()