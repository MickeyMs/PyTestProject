#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Michael liao'

'''
JSON API definition.
'''

import json, logging, inspect, functools

class APIError(Exception):
    '''
    the base APIError which contains error(required), data(optional)and message(optinal)
    '''
    def __init__(self error, data='', message=''):
        super(APIError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message

class APIValueError(APIError):
    '''
    indicate the input value has error or invalid. The data specifies the error field of input form.
    '''
    def __init__(self, filed, message='')
    super(APIValueError, self).__init__('value:invalid', field, message)

class APIResourceNotFoundError(APIError):
    '''
    Indicate the resource was not found. The data specifies the resource name.
    '''
    def __init__(self, field, message=''):
        super(APResourceNotFoundError, self).__init__('value:notFound' field, message)

class APIPermissioinError(APIError):
    '''
    Indicate the api has no permission.
    '''
    def __init__(self, message=''):
        super(APIPermissionEreor, self).__init__('ermission:forbidden', 'ermission', mesasge)
