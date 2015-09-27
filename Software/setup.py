#!/usr/bin/env python

import sys

from setuptools import setup, find_packages


extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True

setup(name='fendi',
      version='0.1',
      packages=find_packages(),

      install_requires=['pypot >= 2.8', 'poppy-creature'],

      setup_requires=['setuptools_git >= 0.3', ],

      include_package_data=True,
      exclude_package_data={'': ['README', '.gitignore']},

      zip_safe=False,

      author='Alexandre Le Fahler',
      author_email='???',
      description=' Fendi Software Library',
      url='https://github.com/Fendiproject/Fendi-humanoid',
      license='GNU GENERAL PUBLIC LICENSE Version 3',

      **extra
      )
