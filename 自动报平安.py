#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests

def sentMsg(msg):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    api_url = "https://qmsg.zendee.cn/send/49bdb9375842537a41ebc635a09229b2?msg= %s" % msg
    return requests.post(api_url, headers=headers).content

text = 'git推送测试'
print(sentMsg(text))

