#!/bin/python
# _*_ coding:utf-8 _*_

"""
    simple-ansible

    A simple Ansible-api example
    TODO: simple ui base flask

    :copyright: (c) 2018 by wqz
"""
from __future__ import (absolute_import, division, print_function)


class ConfigAttribute(object):

    def __init__(self, name):
        print('in init')
        self.__name__ = name

    def __get__(self, obj, type=None):
        print(obj)
        if obj is None:
            return self
        rv = obj.config[self.__name__]
        return rv

    def __set__(self, obj, value):
        print(' in set')
        obj.config[self.__name__] = value


class Config(object):
    def __init__(self):
        print('init Config!')
