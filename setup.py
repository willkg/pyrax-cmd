#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from setuptools import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')


setup(
    name='pyrax-cmd',
    version='0.1.0',
    description='Eats bugs (WILLCAGE FURY EDITION)',
    long_description=readme + '\n\n' + history,
    author='Will Kahn-Greene',
    author_email='willkg@bluesock.org',
    url='https://github.com/willkg/pyrax-cmd',
    include_package_data=True,
    install_requires=[
        'pyrax',
    ],
    license="BSD",
    zip_safe=True,
    keywords='',
    scripts=['pyrax-cmd'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
    ],
)
