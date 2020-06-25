#!python3.7.3
# -*- coding:utf-8 -*-


from setuptools import setup , find_packages

setup(
    name    = 'mpwmanager',
    version = '0.5',
    description = 'Password Manager',
    author  = 'MOoop',
    author_email = 'MOoopjjang@gmail.com',
    url = '',
    install_requires = [],
    packages = find_packages(exclude=['docs','test']),
    keywords    = ['python gui','PyQt','python class'],
    python_requires='==3.7'

)