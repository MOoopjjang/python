#!python
# -*- coding:utf-8 -*-

from xml.etree import ElementTree as ET


def main():
	tree = ET.parse('sample.xml')
	root = tree.getroot()
	appenders_tag = root.findall("appender")
	# print('{}'.format(type(appenders_tag)))
	confiDict = {}
	for a_tag in appenders_tag:
		d = {}
		d['level'] = a_tag.find('level').get('value')
		d['fmt'] = a_tag.find('fmt').get('value')
		d['dir'] = a_tag.find('dir').get('value')
		d['fname'] = a_tag.find('fname').get('value')
		confiDict[a_tag.get('name')] = d


	print('{}'.format(confiDict))




if __name__ == '__main__':
	main()