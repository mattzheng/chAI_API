# -*- coding: utf-8 -*-
"""
码隆科技
    https://github.com/MalongTech/productai-python-sdk
"""

from productai import Client

access_key_id = 'xxx'
access_key_secret = 'xxx'
cli = Client(access_key_id, access_key_secret)

# 衣物目标检测
url = 'http://xx.com/1.jpg'
api = cli.get_api('detect', '_0000025')
resp = api.query(url)

# 智能时尚衣物检测
api = cli.get_api('dressing', '_0000043')
resp = api.query(url)
eval(resp.content)