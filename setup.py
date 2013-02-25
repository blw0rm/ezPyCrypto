# Installation script for ezPyCrypto

# to install this module, type:
#
#   python setup.py install

import sys,os
from distutils.core import setup, Extension

setup(name='ezPyCrypto',
	  version = '0.1',
	  description = 'ezPyCrypto - easy Python API for strong encryption',
	  py_modules = ['ezPyCrypto']
	  )
