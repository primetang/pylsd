#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-08 09:32:00
# @Author  : Gefu Tang (tanggefu@gmail.com)
# @Link    : https://github.com/primetang/pylsd
# @Version : 0.0.3

from setuptools import setup

setup(
    name='pylsd',
    version='0.0.3',
    description='pylsd is the python bindings for LSD - Line Segment Detector',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Gefu Tang',
    author_email='tanggefu@gmail.com',
    maintainer='kba',
    license='BSD',
    keywords=["LSD", 'line segmentation'],
    url='https://github.com/kba/pylsd',
    packages=['pylsd', 'pylsd.bindings', 'pylsd.lib'],
    package_dir={'pylsd.lib': 'pylsd/lib'},
    package_data={'pylsd.lib': ['darwin/*.dylib', 'win32/x86/*.dll', 'win32/x64/*.dll', 'linux/*.so']},
)
