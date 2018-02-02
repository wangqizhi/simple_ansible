#!/bin/python
# _*_ coding:utf-8 _*_

"""
    simple-ansible

    A simple Ansible-api example
    TODO: simple ui base flask

    :copyright: (c) 2018 by wqz
"""
from __future__ import (absolute_import, division, print_function)


LC = dict(
    # spla config from local_config
    SELF_CONFIG=dict(),
    # spla secret key
    SECRET_KEY='/etc/spla/.secret_config',
    # spla config file
    CONFIG_FROM='/etc/spla/local_config',
    # ansible host file
    HOSTS_FILES=['/etc/spla/local_host'],
)
