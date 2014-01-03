"Simple Asset pipeline toolset"
import sys

from setuptools import setup

import simpleasset

INSTALL_DEPS = []
TEST_DEPS = []

PYVER = sys.version_info[0:2]
if PYVER == (2, 6):
    INSTALL_DEPS.append('argparse')
if PYVER == (3, 2):
    TEST_DEPS.append("Jinja2 == 2.6")
else:
    TEST_DEPS.append("Jinja2")


setup(
    name='simpleasset',
    version=simpleasset.VERSION,
    description=simpleasset.__doc__,
    long_description=open('README.rst').read(),
    author='Nickolas Grigoriadis',
    author_email='nagrigoriadis@gmail.com',
    url='https://github.com/grigi/simpleasset',
    license='MIT',
    zip_safe=False,
    test_suite='simpleasset.test_suite',

    # Dependencies
    install_requires=INSTALL_DEPS,
    tests_require=TEST_DEPS,

    # Packages
    packages=['simpleasset'],
    include_package_data=True,
    package_data={'': ['README.rst']},

    # Scripts
    scripts=[
        "scripts/assetgen.py",
    ],

    # Classifiers
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
