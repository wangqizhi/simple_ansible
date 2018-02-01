#!/bin/python
# _*_ coding:utf-8 _*_

"""
    simple-ansible

    A simple Ansible-api example
    TODO: simple ui base flask

    :copyright: (c) 2018 by wqz
"""
from __future__ import (absolute_import, division, print_function)

from spla.modules import BaseModule


class PingModule(BaseModule):
    def __init__(self, tasks):
        super(PingModule, self).__init__(tasks)

    def ping(self):
        self.tasks.append(dict(action=dict(module='ping')))
