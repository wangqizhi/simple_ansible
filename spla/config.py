#!/bin/python
# _*_ coding:utf-8 _*_

"""
    simple-ansible

    A simple Ansible-api example
    TODO: simple ui base flask

    :copyright: (c) 2018 by wqz
"""
from __future__ import (absolute_import, division, print_function)

import ConfigParser


class Config(dict):

    def __init__(self, defaults=None):
        self.defaults = defaults
        dict.__init__(self, defaults or {})

    def __repr__(self):
        return 'Config:{}'.format(str(self.defaults))

    def from_ini(self):
        try:
            cp = ConfigParser.ConfigParser()
            # TODO: vars local_config need in one file
            cp.read('local_config')
            self['username'] = cp.get('base', 'username')
            self['password'] = cp.get('base', 'password')
            self['become_user'] = cp.get('base', 'become_user')
        except IOError as e:
            pass
        return True

