#!/bin/python
# _*_ coding:utf-8 _*_

"""
    simple-ansible

    A simple Ansible-api example
    TODO: simple ui base flask

    :copyright: (c) 2018 by wqz
"""
from __future__ import (absolute_import, division, print_function)

import importlib


class TaskModule(object):
    """
    Create tasks by module
    """
    def __init__(self, module_name, tasks):
        self.module_name = module_name
        self.tasks = tasks
        module = importlib.import_module('spla.modules.'+module_name)
        # TODO: try except
        self.obj = getattr(module, module_name.capitalize()+'Module')

    def load(self):
        return self.obj(self.tasks)
