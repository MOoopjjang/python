#!python


from setuptools import setup , find_packages

setup(
	name							= 'cwkimSample',
	version							= '1.0',
	description						= 'sample test',
	author							= 'MOoop',
	author_email					= 'MOoopjjang@gmail.com',
	install_requires				= ['Flask','requests'],
	packages 						= find_packages()
	)



