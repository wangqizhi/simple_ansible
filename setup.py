#!/bin/python
# _*_ coding:utf-8 _*_

"""
    simple-ansible

    A simple Ansible-api example
    TODO: simple ui base flask

    :copyright: (c) 2018 by wqz
"""
from setuptools import setup

setup(
    name='spla',
    version='0.1a',
    packages=['spla', 'spla.modules'],
    url='https://github.com/wangqizhi/spla',
    license='',
    author='wqz',
    author_email='wangqizhi1987@gmail.com',
    description='Ansible api example or maybe ui',
    install_requires=['ansible'],
)
