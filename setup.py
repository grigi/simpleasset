"Simple Asset pipeline toolset"
from setuptools import setup

import simpleasset

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
    install_requires=[
    ],
    tests_require=[
        "jinja2",
    ],

    # Packages
    packages=['simpleasset'],
    include_package_data=True,
    package_data={'': ['README.rst']},

    # Scripts
    scripts=[
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

