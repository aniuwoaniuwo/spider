# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-31 14:26:26
# @Author  : Weizhong Tu (mail@tuweizhong.com)

from django.conf import settings as original_settings

def settings(request):
    return {'settings': original_settings}

def ip_address(request):
    return {'ip_address': request.META['REMOTE_ADDR']}







