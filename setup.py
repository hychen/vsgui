#!/usr/bin/env python
# -*- encoding=utf8 -*-
#
# Copyright © 2010 Hsin Yi Chen
from distutils.core import setup

setup(
    name = 'vsgui',
    requires = ['ucltip(>=0.6)'],
    version = open('VERSION.txt').read().strip(),
    description = 'Very Simple Graphical library for Python shell script',
    long_description=open('README.txt').read(),
    author = 'Hsin-Yi Chen 陳信屹 (hychen)',
    author_email = 'ossug.hychen@gmail.com',
    license = 'BSD-2-clause License',
    packages=['vsgui'],
    classifiers = [
              "Development Status :: 3 - Alpha",
              "Intended Audience :: Developers",
              "License :: OSI Approved :: BSD License",
              "Operating System :: OS Independent",
              "Programming Language :: Python",
              "Programming Language :: Python :: 2.5",
              "Programming Language :: Python :: 2.6",
              "Programming Language :: Python :: 2.7",
              "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
