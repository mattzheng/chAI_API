# -*- coding: utf-8 -*-

"""
python2.7
"""

#  HTTP的调用方式
import urllib2
import urllib
import time
http_url='https://api-cn.faceplusplus.com/facepp/v3/detect'  # 人脸检测

#  -------------------第一种方式：post方式 -------------------

key = "xxx"
secret = "xxx"
filepath = "../../001.jpg"
boundary = '----------%s' % hex(int(time.time() * 1000))
data = []
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
data.append(key)
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
data.append(secret)
data.append('--%s' % boundary)
fr=open(filepath,'rb')
data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'image_file')
data.append('Content-Type: %s\r\n' % 'application/octet-stream')
data.append(fr.read())
fr.close()
data.append('--%s--\r\n' % boundary)

http_body='\r\n'.join(data)
#buld http request
req=urllib2.Request(http_url)
#header
req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
req.add_data(http_body)
try:
	#req.add_header('Referer','http://remotserver.com/')
	#post data to server
	resp = urllib2.urlopen(req, timeout=5)
	#get response
	qrcont=resp.read()
	print qrcont

except urllib2.HTTPError as e:
    print e.read()



# -------------------第二种方式：SDK调用方式 ----------------------------

import sys
sys.path.append(u'C:\\Users\\mzheng50\\Desktop\\百度API\\face++\\python-sdk-master\\python-sdk')
from facepp import API, File


# 使用人脸检测，关键点检测
key = "xxx"
secret = "xxx"
api = API(key, secret )
    # 默认:srv = 'https://api-cn.faceplusplus.com/facepp/v3/'
api.detect(image_file = File(r"C:/Desktop/1.jpg"),return_attributes = ['skinstatus','age'])
    # 最多返回5个数据点

# 人体姿势识别
api = API(key, secret , srv = 'https://api-cn.faceplusplus.com/humanbodypp/v1/detect')
api.detect(image_file = File(r"C:/Desktop/1.jpg"))









