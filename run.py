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
from optparse import OptionParser

from spla.config import Config
from spla.utils import EasyPassword
from spla.spla import Spla


def pre_work():
    """ready for start

    :return: 
    """
    pass

def run():
    """Main

    """
    spla = Spla()
    spla.tqm_run()


if __name__ == '__main__':
    run()
