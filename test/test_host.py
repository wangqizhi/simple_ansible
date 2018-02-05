#!/bin/python
# _*_ coding:utf-8 _*_

"""
    simple-ansible

    A simple Ansible-api example
    TODO: simple ui base flask

    :copyright: (c) 2018 by wqz
"""
from __future__ import (absolute_import, division, print_function)

import pytest
from ansible.parsing.dataloader import DataLoader

from spla.host import HostManager
from spla.contents import LC


def test_host():
    hm = HostManager(DataLoader(), LC['HOSTS_FILES'])
    print(dir(hm()))
    return hm()


if __name__ == '__main__':
    test_host()
