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
from spla.contents import LC


def run(host, name):
    """Example: play-book

    :param host: string
    :param name: string
    :return: None
    """
    if not name:
        name = 'Spla gogo!'
    spla = Spla(module='playbook')
    play_source = dict(
        name=name,
        hosts=host,
    )
    spla.set_play_source(play_source)
    r = spla.tqm_run()
    print(r)


if __name__ == '__main__':
    run('all', 'spla play-book!')
