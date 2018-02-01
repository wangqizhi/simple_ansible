#!/bin/python
# _*_ coding:utf-8 _*_

"""
    simple-ansible

    A simple Ansible-api example
    TODO: simple ui base flask

    :copyright: (c) 2018 by wqz
"""
from __future__ import (absolute_import, division, print_function)


class NginxModule(object):
    def __init__(self, tasks):
        self.tasks = tasks

    def get_task(self):
        return self.tasks

    def download_config(self, local_dir, nginx_conf_dir):
        _sub_tasks = [
            dict(action='fetch', args=dict(src=nginx_conf_dir + 'nginx.conf', dest=local_dir)),
            dict(action=dict(module='shell',
                             args=''.join(['ls ', nginx_conf_dir, 'vhosts/'])
                             ), register='nginx_conf_vhosts'
                 ),

            dict(action=dict(module='fetch',
                             args=dict(src=nginx_conf_dir + 'vhosts/{{ item }}',
                                       dest=local_dir),
                             ),
                 loop='items',
                 loop_args='{{ nginx_conf_vhosts.stdout.split() }}'
                 ),
        ]
        for i in _sub_tasks:
            self.tasks.append(i)
