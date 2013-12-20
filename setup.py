from setuptools import setup

import simpleasset

setup(
    name='simpleasset',
    version=simpleasset.VERSION,
    description=simpleasset.__doc__,
    long_description=open('README.rst').read(),
    author='Nickolas Grigoriadis',
    author_email='',
    url='https://github.com/grigi/simpleasset',
    license='MIT',
    zip_safe=False,

    # Dependencies
    install_requires=[],

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
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

