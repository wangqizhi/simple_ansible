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
import sys
sys.path.append("./")

from spla.spla import Spla


def test_spla():
    spla = Spla()
    spla.tqm_run()
