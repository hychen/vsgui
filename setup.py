#!/usr/bin/env python
# -*- encoding=utf8 -*-
#
# Copyright © 2010 Hsin Yi Chen
from distutils.core import setup

setup(
    name = 'vsgui',
    requires = ['ucltip(>=0.2)'],
    version = open('VERSION.txt').read().strip(),
    description = 'Very Simple Graphical library for Python shell script',
    long_description=open('README.txt').read(),
    author = 'Hsin-Yi Chen 陳信屹 (hychen)',
    author_email = 'ossug.hychen@gmail.com',
    license = 'GPLv2',
    packages=['vsgui'],
)
