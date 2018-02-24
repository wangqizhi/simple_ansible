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
import sys
from collections import namedtuple

from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.plugins.callback import CallbackBase
from ansible import constants as C

from . import __version__
from .config import Config
from .contents import LC
from .utils import EasyPassword
from .module import TaskModule


class ResultCallback(CallbackBase):
    def __init__(self, result, info=False):
        super(ResultCallback, self).__init__()
        self.result = result
        self.info = info
    
    # callback when task execute
    def v2_runner_on_ok(self, result, **kwargs):
        self.result['tasks_run'].append(result._host)
        self.result['tasks_result'][result._host] = result._result

    # callback when task failed
    def v2_runner_on_failed(self, result, ignore_errors=False):
        self.result['tasks_failed'].append(result._host)
        self.result['tasks_result'][result._host] = result._result

    # callback when task unreachable
    def v2_runner_on_unreachable(self, result):
        self.result['tasks_unreachable'].append(result._host)
        self.result['tasks_result'][result._host] = result._result

    # callback anytime
    def v2_on_any(self, *args, **kwargs):
        # TODO: record in file
        if self.info:
            print(args)


class Spla(object):
    """
    spla = Spla()
    spla.tqm_run()
    """
    def __init__(self, module=None):
        self.module = module
        self.tasks = []
        self.results = dict(tasks_run=[], tasks_failed=[], tasks_unreachable=[], tasks_result=dict())
        # counter
        # self._JS = 0
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
                               'listhosts',  # support PlaybookExecutor
                               'listtasks',  # support PlaybookExecutor
                               'listtags',  # support PlaybookExecutor
                               'syntax',  # support PlaybookExecutor
                               ])
        # defaults args
        _defaults = dict(
            connection='smart',
            module_path=None,
            forks=100,
            become=True,
            become_method='sudo',
            become_user='root',
            check=False,
            diff=False,
            remote_user='root',
            ssh_common_args=None,
            private_key_file=None,
            verbosity=4,
            host_key_checking=False,
        )
        # load from config file
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
            listhosts=None,
            listtasks=None,
            listtags=None,
            syntax=None,
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
        self.results_callback = ResultCallback(self.results)

    @property
    def version(self):
        return __version__

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
        if isinstance(task, list):
            for i in task:
                self.tasks.append(i)
        else:
            self.tasks.append(task)

    def clear_task(self):
        """clear task list

        """
        self.tasks = []

    def get_module(self, module_name='ping'):
        """ get module by spla defined

        :return: instance
        """
        return TaskModule(module_name, self.tasks).load()

    def _play(self):
        """load play_source
        
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
            # play-book module
            if self.module == 'playbook':
                try:
                    filename = sys.argv[1]
                    path = os.getcwd()
                    if filename.startswith('/'):
                        f = filename
                    else:
                        f = '/'.join([path, filename])
                    if os.path.isfile(f):
                        _pe = PlaybookExecutor(
                            playbooks=[f],
                            inventory=self.inventory,
                            variable_manager=self.variable_manager,
                            loader=self.loader,
                            options=self.options,
                            passwords=_passwords,
                        )
                        _pe._tqm = _tqm
                        _pe.run()
                    else:
                        # TODO: use display from ansible
                        print("ERROR: file not exist!")
                        return False
                except IndexError:
                    # TODO: use display from ansible
                    print("ERROR: playbook module need file name!")
                    return False
            else:
                # tqm module
                _tqm.run(self._play())
        finally:
            if _tqm is not None:
                _tqm.cleanup()
        # return callback result:
        # self.results = dict(tasks_run=[], tasks_failed=[], tasks_unreachable=[], tasks_result=dict())
        return self.results

    def _get_password(self):
        _secret_config = LC['SECRET_KEY']
        if os.path.exists(_secret_config):
            try:
                with open(_secret_config, 'r') as sec_file:
                    # TODO: py3 support
                    key = sec_file.read()
            except IOError as e:
                print(e)
                print('ERROR: Write key file failed!')
                raise
        else:
            try:
                with open(_secret_config, 'w') as sec_file:
                    # TODO: py3 support
                    key = str(raw_input('Enter key>> '))
                    if len(key) <= 16:
                        sec_file.write(key)
                    else:
                        # TODO: define Exception
                        raise KeyError
            except IOError as e:
                print(e)
                print('ERROR: Write key file failed!')
                raise
        ep = EasyPassword(key)
        sec_pwd = self.config['password']
        return ep.get_value(sec_pwd)

    def get_result(self):
        return self.results
