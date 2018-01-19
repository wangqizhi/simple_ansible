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
# import getpass

from spla.config import Config
from spla.utils import EasyPassword

def pre_work():
    """准备工作

    :return: 
    """
    # 秘钥检查
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
                if len(key) == 16:
                    sec_file.write(key)
                elif len(key) < 16:
                    add = 16 - len(key)
                    sec_file.write(key+'\0'*add)
                else:
                    raise

        except IOError as e:
            print(e)
            print('Write key file failed!')
            raise
    config = Config()
    config.from_ini()
    username = config['username']
    become_user = config['become_user']
    ep = EasyPassword(key)
    sec_pwd = config['password']
    password = ep.get_value(sec_pwd)
    return username, become_user, password


def run():
    """Main

    """
    print(pre_work())
    # (username, become_user, password) = pre_work()


if __name__ == '__main__':
    run()
