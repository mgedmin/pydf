# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pydf',
    version='14+mg1',
    description='colourised df(1)-clone',
    long_description="""
pydf is a python script that displays the amount of disk space available
on the mounted filesystems, using different colours for different
types of filesystems. Output format is completely customizable.
""",
    url='https://github.com/mgedmin/pydf',
    author='Radovan Garabík',
    author_email='garabik@kassiopeia.juls.savba.sk',
    maintainer='Marius Gedminas',
    maintainer_email='marius@gedmin.as',
    license='Public Domain',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: System Administrators',
        'License :: Public Domain',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: System',
        'Topic :: System :: Filesystems',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],
    keywords='df disk space colours filesystems',
    scripts=['pydf']
)
