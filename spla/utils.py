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
    """Easy password encode/decode
    
    """
    def __init__(self, key):
        self.key = key
        self.mode = 'easy'

    def _encrypt_fun(self, content):
        """encrypt
        
        :param content: content: encrypt content
        :return: string: 
        """
        mode = self.mode
        if mode == 'easy':
            obj = AES.new(self.key, AES.MODE_CBC, b'0'*16)
            if len(content) < 16 :
                print(content+b'0'*(16-len(content)))
                o = b2a_hex(obj.encrypt(content+b'0'*(16-len(content))))
                return o
            else:
                return ''
        else:
            # todo: other mode
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
                return o
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
