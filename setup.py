# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import gchiam_cc
version = gchiam_cc.__version__

setup(
    name='gchiam_cc',
    version=version,
    author='',
    author_email='gordon.chiam@gmail.com',
    packages=[
        'gchiam_cc',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['gchiam_cc/manage.py'],
)