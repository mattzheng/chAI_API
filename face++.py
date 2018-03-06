# -*- coding: utf-8 -*-

"""
python2.7
"""

#  HTTP的调用方式
import urllib2
import urllib
import time
http_url='https://api-cn.faceplusplus.com/facepp/v3/detect'  # 人脸检测

#  -------------------Part 1 : 人脸识别 第一种方式：post方式 -------------------

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



# -------------------Part 1 : 人脸识别第二种方式：SDK调用方式 ----------------------------

import sys
sys.path.append(u'/.../python-sdk-master/python-sdk')
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


# -------------------Part 2: face++ 场景识别 + 人体语义分割 + OCR识别---------------------------
import sys
sys.path.append('/../face++/python-sdk')
from facepp import API, File
import urllib2,time

def faceplus_api(key,secret,filepath,http_url):

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
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_landmark')
    data.append('1')
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_attributes')
    data.append("gender,age,smiling,headpose,facequality,blur,eyestatus,emotion,ethnicity,beauty,mouthstatus,eyegaze,skinstatus")
    data.append('--%s--\r\n' % boundary)

    http_body='\r\n'.join(data)
    #buld http request
    req=urllib2.Request(http_url)
    #header
    req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
    req.add_data(http_body)
    qrcont = None
    try:
        #req.add_header('Referer','http://remotserver.com/')
        #post data to server
        resp = urllib2.urlopen(req, timeout=5)
        #get response
        qrcont=resp.read()
        #print qrcont

    except urllib2.HTTPError as e:
        print e.read()
        
    return qrcont

if __name__ == "__main__"
	# 场景识别
	http_url='https://api-cn.faceplusplus.com/imagepp/beta/detectsceneandobject'
	API_KEY = "xxx"
	API_SECRET = "xxx"
	face_one = 'http://bj-mc-prod-asset.oss-cn-beijing.aliyuncs.com/mc-official/images/face/demo-pic11.jpg'
	face_two = '/../Hydrangeas.jpg'
	result = faceplus_api( API_KEY,API_SECRET, face_two ,http_url)
	
	# 人体语义分割
	http_url='https://api-cn.faceplusplus.com/humanbodypp/v1/segment'
	API_KEY = "xxx"
	API_SECRET = "xxx"
	#face_one = 'http://bj-mc-prod-asset.oss-cn-beijing.aliyuncs.com/mc-official/images/face/demo-pic11.jpg'
	face_two = '/../out2.jpg'
	result = faceplus_api( API_KEY,API_SECRET, face_two ,http_url)

	# OCR识别
	http_url='https://api-cn.faceplusplus.com/imagepp/v1/recognizetext'
	API_KEY = "xxx"
	API_SECRET = "xxx"
	#face_one = 'http://bj-mc-prod-asset.oss-cn-beijing.aliyuncs.com/mc-official/images/face/demo-pic11.jpg'
	face_two = '/../out3.jpg'
	ocr_result = faceplus_api( API_KEY,API_SECRET, face_two ,http_url) 
	print ocr_result


