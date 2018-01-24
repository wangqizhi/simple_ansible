#!/bin/python
# _*_ coding:utf-8 _*_

"""
    simple-ansible

    A simple Ansible-api example
    TODO: simple ui base flask

    :copyright: (c) 2018 by wqz
"""
from __future__ import (absolute_import, division, print_function)

import os
from collections import namedtuple

from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase
from ansible import constants as C

from spla.config import Config
from spla.contents import LC
from spla.utils import EasyPassword


class ResultCallback(CallbackBase):
    def __init__(self, result):
        super(ResultCallback, self).__init__()
        self.result = result
    
    # callback when task execute
    def v2_runner_on_ok(self, result, **kwargs):
        self.result['tasks_run'].append(result._host)

    # callback when task failed
    def v2_runner_on_failed(self, result, ignore_errors=False):
        self.result['tasks_failed'].append(result._host)

    # callback when task unreachable
    def v2_runner_on_unreachable(self, result):
        self.result['tasks_unreachable'].append(result._host)


class Spla(object):
    """
    spla = Spla()
    spla.tqm_run()
    """
    def __init__(self):
        self.tasks = []
        self.results = dict(tasks_run=[], tasks_failed=[], tasks_unreachable=[])
        # counter
        self._JS = 0
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
        # defaults args
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
        self.loader = DataLoader()
        self.inventory = InventoryManager(loader=self.loader, sources=LC['HOSTS_FILES'])
        self.variable_manager = VariableManager(loader=self.loader, inventory=self.inventory)
        self.play_source = dict(
            name='',
            hosts='',
            gather_facts='no',
            tasks=self.tasks
        )
        self.results_callback = ResultCallback(self.results)  # TODO: build callback

    def get_options(self):
        """
        
        :return: options
        """
        return self.options

    def set_play_source(self, play_source):
        # TODO: check play_source
        for i in play_source:
            self.play_source[i] = play_source[i]

    def add_task(self, task=dict):
        # TODO: check task
        self.tasks.append(task)

    def _play(self):
        """
        
        :return: play
        """
        # TODO: if play_source is empty Raise
        return Play().load(self.play_source, variable_manager=self.variable_manager, loader=self.loader)

    def tqm_run(self):
        # close host_key check
        # next version need set host_key_checking=False in option
        C.HOST_KEY_CHECKING = False
        # TODO: now become_pass same as conn_pass ,need get from other become_pass
        _passwords = dict(conn_pass=self._get_password(), become_pass=self._get_password())
        try:
            _tqm = TaskQueueManager(
                inventory=self.inventory,
                variable_manager=self.variable_manager,
                loader=self.loader,
                options=self.options,
                passwords=_passwords,
                stdout_callback=self.results_callback,
            )
            _tqm.run(self._play())
        finally:
            if _tqm is not None:
                _tqm.cleanup()
        return self.results

    def _get_password(self):
        if os.path.exists('.secret_config'):
            try:
                with open('.secret_config', 'r') as sec_file:
                    # TODO: py3 support
                    key = sec_file.read()
            except IOError as e:
                print(e)
                print('Write key file failed!')
                raise
        else:
            try:
                with open('.secret_config', 'w') as sec_file:
                    # TODO: py3 support
                    key = str(raw_input('>> '))
                    if len(key) <= 16:
                        sec_file.write(key)
                    else:
                        # TODO: define Exception
                        raise KeyError
            except IOError as e:
                print(e)
                print('Write key file failed!')
                raise
        ep = EasyPassword(key)
        sec_pwd = self.config['password']
        return ep.get_value(sec_pwd)

    def get_result(self):
        return self.results
