#!/bin/python
# _*_ coding:utf-8 _*_

"""
    simple-ansible

    A simple Ansible-api example
    TODO: simple ui base flask

    :copyright: (c) 2018 by wqz
"""
from __future__ import (absolute_import, division, print_function)

# TODO: py3 support: replace ConfigParser
import ConfigParser
import os

from .contents import LC


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
            _config = LC['CONFIG_FROM']
            if os.path.exists(_config):
                cp.read(_config)
                # read ansible base config from local_config
                for i, _ in cp.items('base'):
                    self[i] = cp.get('base', i)
                # refresh LC from local_config 'self'
                if 'self' in cp.sections():
                    for i, _ in cp.items('self'):
                        LC['SELF_CONFIG'][i] = cp.get('self', i)
            else:
                print("Error: Please create file: " + _config)
        except IOError as e:
            # TODO: define Exception
            print(e)
            raise
        return cp
