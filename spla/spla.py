#!/bin/python
# _*_ coding:utf-8 _*_

"""
    simple-ansible

    A simple Ansible-api example
    TODO: simple ui base flask

    :copyright: (c) 2018 by wqz
"""
from __future__ import (absolute_import, division, print_function)

from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase
from ansible import constants as C

from spla.config import Config


class OptionsAttr(dict):
    def __init__(self, *args, **kwargs):
        super(OptionsAttr, self).__init__(*args, **kwargs)

    def __getattr__(self, key):
        try:
            v = self[key]
        except Exception:
            v = False
        if isinstance(v, dict):
            v = OptionsAttr(v)
        return v


class Spla(object):
    def __init__(self):
        self.config = Config()
        _options = namedtuple('Options',
                              ['connection',  # connection types: smart,ssh,paramiko...
                               'module_path',  # remote python module path
                               'forks',  # forks numbers
                               'become',  # True or False
                               'become_method',  # sudo or other
                               'become_user',  # who sudo
                               'check',  # TODO: unknown
                               'diff',  # TODO: unknown
                               'remote_user',  # remote user name
                               'ssh_common_args',  # add ssh args
                               'private_key_file',  # where private key
                               'verbosity',  # more information show
                               'host_key_checking',  # next version support for close host checking
                               ])
        _defaults = dict(
            connection='smart',
            remote_user='root',
            module_path=None,
            forks=100,
            become=True,
            become_method='sudo',
            become_user='root',
            check=False,
            diff=False,
            ssh_common_args=None,
            private_key_file=None,
            verbosity=4,
            host_key_checking=False,
        )
        for i, j in self.config.items():
            _defaults[i] = j
        self.options = _options(
            connection=_defaults['connection'],
            remote_user=_defaults['remote_user'],
            module_path=_defaults['module_path'],
            forks=_defaults['forks'],
            become=_defaults['become'],
            become_method=_defaults['become_method'],
            become_user=_defaults['become_user'],
            check=_defaults['check'],
            diff=_defaults['diff'],
            ssh_common_args=_defaults['ssh_common_args'],
            private_key_file=_defaults['private_key_file'],
            verbosity=_defaults['verbosity'],
            host_key_checking=_defaults['host_key_checking'],
        )


    def get_options(self):
        return self.options
