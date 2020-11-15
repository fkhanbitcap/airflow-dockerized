# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup, find_packages

# Save version and author to __meta__.py
version = open('VERSION').read().strip()
dirname = os.path.dirname(__file__)
path = os.path.join(dirname, 'devchallenge', '__meta__.py')
meta = '''# Automatically created. Please do not edit.
__version__ = '%s'
__author__ = 'Muhamad Faizan Khan'
''' % version
with open(path, 'w') as F:
    F.write(meta)

setup(
    # Basic info
    name='devchallenge',
    version=version,
    author='Muhamad Faizan Khan',
    author_email='mfkhan1994@gmail.com',
    url='',
    description='Dev Challenge for IIB Institute',
    long_description=codecs.open('README.rst', 'rb', 'utf8').read(),

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries',
    ],

    # Packages and dependencies
    package_dir={'': '.'},
    packages=find_packages('.'),
    install_requires=[
    ],
    extras_require={
        'dev': [
            'python-boilerplate[dev]',
        ],
    },

    # Other configurations
    zip_safe=False,
    platforms='any',
)
