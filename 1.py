#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import hmac
import hashlib
import base64
import urllib.parse
 
timestamp = str(round(time.time() * 1000))
secret = ''
secret_enc = secret.encode('utf-8')
string_to_sign = '{}n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote(base64.b64encode(hmac_code))
# print(timestamp)
# print(sign)
 
 
import requests,json #导入依赖库
headers={'Content-Type': 'application/json'} #定义数据类型
webhook = 'https://oapi.dingtalk.com/robot/send?access_token='
#定义要发送的数据
#"at": {"atMobiles": "['"+ mobile + "']"
data = {
     "msgtype": "text",
        "text": {
            "content": "告警测试"
        },
     "at": {
            "isAtAll":True   # at为非必须
         }
    }
res = requests.post(webhook, data=json.dumps(data), headers=headers) #发送post请求
print(res.text)
