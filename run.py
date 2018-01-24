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


def pre_work():
    """ready for start

    :return: 
    """
    pass


def modify_file_header():
    """modify file header
    
    :return: 
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


def run():
    """Main

    """
    spla = Spla()
    play_source = dict(
        name='test',
        hosts='10.21.67.90',
    )
    spla.set_play_source(play_source)
    task=dict(action=dict(module='ping'))
    spla.add_task(task)
    r = spla.tqm_run()
    print(r)


if __name__ == '__main__':
    run()
    # modify_file_header()
