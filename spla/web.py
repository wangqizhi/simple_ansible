#!/bin/python
# _*_ coding:utf-8 _*_

"""
    simple-ansible

    A simple Ansible-api example
    TODO: simple ui base flask

    :copyright: (c) 2018 by wqz
"""
from __future__ import (absolute_import, division, print_function)

from flask import Flask

from .spla import Spla

app = Flask(__name__)


# @app.route('/')
# def index():
#     spla = Spla()
#     play_source = dict(
#         name='web',
#         hosts='all',
#     )
#     spla.set_play_source(play_source)
#     print(spla.show_hosts())
#     return 'Hello, Spla!'
#
#
# def web_run(port=8080, debug=False):
#     if debug == 'stage':
#         app.run(port=port)
#     else:
#         app.run(port=port, debug=True)


class SplaUI(object):
    """
    A ansible api UI base on flask
    """
    def __init__(self):
        self.app = Flask(__name__)

    def index(self):
        return "Hello, Spla UI!"

    def run(self, port=8080, debug=False):
        # register route
        self.app.add_url_rule('/', 'index', self.index)
        # run web
        if debug == 'stage':
            self.app.run(port=port)
        else:
            self.app.run(port=port, debug=True)