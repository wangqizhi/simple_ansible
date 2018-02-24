#!/bin/python
# _*_ coding:utf-8 _*_

"""
    simple-ansible

    A simple Ansible-api example
    TODO: simple ui base flask

    :copyright: (c) 2018 by wqz
"""
from __future__ import (absolute_import, division, print_function)

import argparse
from getpass import getpass

from spla.spla import Spla
from spla.utils import EasyPassword


def pre_work():
    """ready for start
    pass
    """
    pass


def modify_file_header():
    """modify file header
    
    """
    file_raw = []
    try:
        # TODO: get filename
        with open('run.py', 'r') as f:
            for i in f:
                file_raw.append(i)
    except IOError:
        pass
    try:
        n = 0
        # TODO: replace text as args
        replace_text = '''#!/bin/python
# _*_ coding:utf-8 _*_

"""
    simple-ansible

    A simple Ansible-api example
    TODO: simple ui base flask

    :copyright: (c) 2018 by wqz
"""
'''
        # TODO: get filename
        with open('run_copy.py', 'w') as f_copy:
            f_copy.write(replace_text)
            for i in file_raw:
                n += 1
                # TODO: start number as args
                # replace start before line:12
                if n > 11:
                    f_copy.write(i)
    except IOError:
        pass


def run(host, name):
    """run a simple ping example
    python run.py -a HOST
    """
    if not name:
        name = 'Spla gogo!'
    spla = Spla()
    play_source = dict(
        name=name,
        hosts=host,
    )
    spla.set_play_source(play_source)
    # task = dict(action=dict(module='ping'))
    # spla.add_task(task)
    ping_module = spla.get_module()
    ping_module.ping()
    r = spla.tqm_run()
    print(r)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Spla: easy to use')
    parser.add_argument('-a', '--host', dest='host', help='play source host')
    parser.add_argument('-n', '--name', dest='name', help='play source name')
    parser.add_argument('--modify', dest='modify', help='modify file header')
    parser.add_argument('--key', dest='key', help='secret key')
    args = parser.parse_args()
    if args.key:
        password = getpass("Enter password>> ")
        ep = EasyPassword(args.key)
        value = ep.create(password)
        print("OUT==> " + value)
    if args.modify:
        # TODO: add file mode
        modify_file_header()
    if args.host:
        run(args.host, args.name)
