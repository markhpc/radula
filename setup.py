#!/usr/bin/python
from setuptools import setup, find_packages

setup(
    name='radula',
    version='0.0.1',
    packages=find_packages(),

    author='Mark Nelson',
    author_email='mark.enlson@dreamhost.com',
    description='Tools for distributed benchmarking of Ceph',
    license='LGPL',
    keywords='ceph distributed benchmarking',

    install_requires=[
        'Fabric >=1.4.0',
        'distribute >=0.6.10',
        'pycrypto >=2.5',
        'pysqlite >=2.6.3',
        'ssh >=1.7.13',
        ],
    )
