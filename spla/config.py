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

from spla.contents import LC


class Config(dict):

    def __init__(self, defaults=None):
        self.defaults = defaults
        if not defaults:
            self.defaults = self.from_ini()
        # dict.__init__(self, defaults or {})

    def __repr__(self):
        return 'Config:{}'.format(str(self.defaults))

    def from_ini(self):
        try:
            cp = ConfigParser.ConfigParser()
            # TODO: vars local_config need in one file
            cp.read(LC['CONFIG_FROM'])
            for i, j in cp.items('base'):
                self[i] = cp.get('base', i)
        except IOError as e:
            # TODO: define Exception
            print(e)
            raise
        return cp
