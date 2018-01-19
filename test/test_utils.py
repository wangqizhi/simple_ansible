#!/bin/python
# _*_ coding:utf-8 _*_

"""
    simple-ansible

    A simple Ansible-api example
    TODO: simple ui base flask

    :copyright: (c) 2018 by wqz
"""
from __future__ import (absolute_import, division, print_function)

import sys
sys.path.append("./")

from spla.utils import EasyPassword


def test_easy_password():
    key = '1234567890123456'
    ep = EasyPassword(key)
    value = '1234567890123456'
    secret = ep.create(value)
    assert value == ep.get_value(secret)

if __name__ == '__main__':
    test_easy_password()
