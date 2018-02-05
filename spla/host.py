#!/bin/python
# _*_ coding:utf-8 _*_

"""
    simple-ansible

    A simple Ansible-api example
    TODO: simple ui base flask

    :copyright: (c) 2018 by wqz
"""
from __future__ import (absolute_import, division, print_function)

from ansible.inventory.manager import InventoryManager


class HostManager(object):
    """host management

    """
    def __init__(self, loader, sources):
        self.im = InventoryManager(loader=loader, sources=sources)

    def __call__(self, *args, **kwargs):
        return self.im
