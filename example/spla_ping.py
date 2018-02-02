#!/bin/python
# _*_ coding:utf-8 _*_

"""
    simple-ansible

    A simple Ansible-api example
    TODO: simple ui base flask

    :copyright: (c) 2018 by wqz
"""
from __future__ import (absolute_import, division, print_function)

from spla.spla import Spla


def run(host, name):
    """run a simple ping example

    """
    if not name:
        name = 'Spla gogo!'
    spla = Spla()
    play_source = dict(
        name=name,
        hosts=host,
    )
    spla.set_play_source(play_source)
    ping_module = spla.get_module()
    ping_module.ping()
    r = spla.tqm_run()
    print(r)


if __name__ == '__main__':
    run('test', 'spla!')
