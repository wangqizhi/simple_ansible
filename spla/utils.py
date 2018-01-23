#!/bin/python
# _*_ coding:utf-8 _*_

"""
    simple-ansible

    A simple Ansible-api example
    TODO: simple ui base flask

    :copyright: (c) 2018 by wqz
"""
from __future__ import (absolute_import, division, print_function)

import base64
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


class EasyPassword(object):
    """ Easy password encode/decode 
        
    """
    def __init__(self, key):
        if len(key) == 16:
            self.key = key
        elif 16 > len(key) > 0:
            self.key = key + b'0'*(16 - len(key))
        else:
            # TODO: define Exception
            print('key value Error!')
            raise
        self.mode = 'easy'

    def _encrypt_fun(self, content):
        """encrypt
        :param content: content: encrypt content
        :return: string: 
        """

        mode = self.mode
        if mode == 'easy':
            obj = AES.new(self.key, AES.MODE_CBC, b'0'*16)
            if len(content) == 16:
                o = b2a_hex(obj.encrypt(content))
                return o
            elif 16 > len(content) > 0:
                o = b2a_hex(obj.encrypt(content+b' '*(16-len(content))))
                return o
            else:
                return ''
        else:
            # TODO: other mode
            print()
            pass

    def _decode_fun(self, secret):
        """decode

        :param secret: string: decode content
        :return: string: 
        """
        mode = self.mode
        try:
            if mode == 'easy':
                obj = AES.new(self.key, AES.MODE_CBC, b'0'*16)
                o = obj.decrypt(a2b_hex(secret))
                return o.rstrip()
            else:
                # TODO: other mode
                pass
        except Exception as e:
            print(e)
            # TODO: more information
            # decode failed return
            return ''

    def create(self, content, mode='easy'):
        self.mode = mode
        value = self._encrypt_fun(content)
        return value

    def get_value(self, secret, mode='easy'):
        self.mode = mode
        return self._decode_fun(secret)
