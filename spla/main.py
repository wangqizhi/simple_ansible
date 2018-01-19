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
import getpass

from src import config

def guide():
    """获取用户名密码
    
    :return: 
    """
    try:
        ansible_user = os.environ['sa_ansible_user']
        ansible_pwd = os.environ['sa_ansible_pwd']
    except Exception as e:
        print(e)
        # TODO: support py3 need use input
        ansible_user = raw_input('Press User:')
        ansible_pwd = getpass.getpass('Press Password:')
        os.putenv('sa_ansible_user', ansible_user)
        os.putenv('sa_ansible_pwd', ansible_pwd)

    return ansible_user, ansible_pwd


def main():
    """main
    
    :return: 
    """
    (ansible_user, ansible_pwd) = guide()
    ansible_config = config.Config()
    print(ansible_user)
    print(ansible_pwd)
    print(ansible_config)

if __name__ == '__main__':
    print(__name__)
    main()

