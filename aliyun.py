# -*- coding: utf-8 -*-

'''
阿里云使用
https://help.aliyun.com/document_detail/32030.html?spm=5176.doc44687.6.683.no2bWx
'''
# 查看bucket
import oss2
import json
import os
from PIL import Image

import oss2
auth = oss2.Auth('您的AccessKeyId', '您的AccessKeySecret')
service = oss2.Service(auth, '您的Endpoint')
print([b.name for b in oss2.BucketIterator(service)])

# ------获得图片名称 ------
from itertools import islice
auth = oss2.Auth('您的AccessKeyId', '您的AccessKeySecret')
bucket = oss2.Bucket(auth, '您的Endpoint', 'bucket名称')
for b in islice(oss2.ObjectIterator(bucket), 110):
    print(b.key)
# 前110个图片名称



# ------获得URL ------
'''
参考格式：
https://help.aliyun.com/document_detail/47660.html?spm=5176.doc32033.6.694.QQXtKQ
https://help.aliyun.com/document_detail/44688.html?spm=5176.doc44687.6.945.bNEiBA

水印的时候，base64转码工具网站：
5pS55Zu+54mH54mI5p2D5b2S5bGeZ3VzaHVodWHnvZHnq5k=就是base64编码
http://base64.xpcha.com/
'''
# 质量变为0.2，水印，加中文，白色字，居中对齐，旋转45，填充
style = 'image/quality,q_70/watermark,text_xxx,color_FFFFFF,align_1,rotate_45,fill_1,size_100/format,jpg'
url = bucket.sign_url('GET', b.key, 60, params={'x-oss-process': style}) 
    #  10 * 60代表过期时间
    # b.key代表该图片，存放bucket中的名字
    # text_  后面接base64编码
print(url)



# ------图片通过URL进行下载  ------
import requests
html = requests.get(url)
with open('picture.jpg', 'wb') as file:
    file.write(html.content)



#  ------上传本地文件 ------ 
    # https://help.aliyun.com/document_detail/32030.html?spm=5176.doc32027.6.683.NBcw2c
import oss2
auth = oss2.Auth('您的AccessKeyId', '您的AccessKeySecret')
bucket = oss2.Bucket(auth, '您的Endpoint', 'bucket名称')
bucket.put_object_from_file('remote.txt', 'local.txt')  # 把本地的local.txt上传到云服务器上，且重命名为remote.txt


#  ------通过URL下载图片  ------

import oss2
import json
import os
from PIL import Image
import requests
from tqdm import tqdm

from itertools import islice
auth = oss2.Auth('您的AccessKeyId', '您的AccessKeySecret')
bucket = oss2.Bucket(auth, '您的Endpoint', 'bucket名称')
save_path = '../../..'
style = 'image/quality,q_70/watermark,text_xxx,color_FFFFFF,align_1,rotate_45,fill_1,size_100/format,jpg'  # 水印效果

cnt = 0
n = 16880  # 代表该bucket里面有多少图片

for b in tqdm(islice(oss2.ObjectIterator(bucket), n )):
    if not b.key== 'save1/':
        url = bucket.sign_url('GET', b.key, 60, params={'x-oss-process': style}) #  10 * 60代表过期时间
        html = requests.get(url)
        if not os.path.exists(save_path + '\\' +  b.key):
            with open(save_path + '\\' +  b.key, 'wb') as file:
                file.write(html.content)
        cnt += 1
        print(cnt)
