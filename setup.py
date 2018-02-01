# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='tdt2',
      version='1.0',
      description='tdt2: A Python module to access Tucker Davis Technologies System II hardware',
      author='Christopher Brown',
      author_email='cbrown1@pitt.edu',
      maintainer='Christopher Brown',
      maintainer_email='cbrown1@pitt.edu',
      packages=['tdt2',],
      requires = ['pyserial',
                 ],
      platforms = ['any'],
      classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Multimedia :: Sound/Audio :: Speech',
        'Topic :: Multimedia :: Sound/Audio :: Analysis',
        'Topic :: Scientific/Engineering',
        ],
     )
