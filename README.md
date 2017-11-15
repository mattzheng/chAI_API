# chAI_API

国内AI常见API调用情况，主要用python调用AI厂商的SDK



# 阿里云

可参考文档：https://help.aliyun.com/document_detail/32030.html?spm=5176.doc44687.6.683.no2bWx


主要指的是阿里云图片上传、下载、图片URL化、图片URL水印化+下载

```
pip install oss2
```

# face++
face++的python的SDK简直了，文档几乎为0，只有内容，没有pip 。这边测试的是人脸识别以及人体姿势识别两个接口。

#### SDK加载
下载链接：https://github.com/FacePlusPlus/python-sdk
直接调用里面的文件内容即可。
如果不想麻烦放在默认路径，可以自己加一下存放python-sdk的路径
```
import sys
sys.path.append(u'../face++/python-sdk-master/python-sdk')
```
然后载入：

```
from facepp import API, File
```

#### 人脸检测 + 人体姿势检测
api.detect(）是主要调用函数，其中的相关参数[参考链接](https://console.faceplusplus.com.cn/documents/4888373)


```
api.detect(image_file = File(r"C:/Desktop/1.jpg"),return_landmark = 1，return_attributes = ['skinstatus','age'])
```

 - return_landmark=2 。返回 106 个人脸关键点。
 - return_landmark=1	。返回 83 个人脸关键点。
 - return_landmark=0	不检测
 - return_attributes 的选项很多：
 - gender、age、smiling、headpose、facequality、blur、eyestatus、emotion、ethnicity、beauty、mouthstatus、eyegaze、skinstatus
 - calculate_all，0/1，仅正式 API Key
   可以使用，因为免费版顶多返回5个人脸，calculate_all可以设置为返回检测到的所有脸（人比较多的图片）
   
#### 注意
 - face++很大方，申请了的试用账号就可以有很多功能可以使用，每个用户使用免费服务只能创建 1000个 FaceSet，总计最多存储 100 万个人脸。
 - 最多返回5个数据点，5长脸

# 图普科技
接口很酷炫，但是这sdk文档，真是简陋...而且API输出内容比较复杂，麻烦。
接口是定向指定的，需要跟tupu事先沟通好才能试用，[官网接口介绍](https://www.tuputech.com/api/tasks)有一些是旧的，需要先问问。
github下载路径：https://github.com/tuputech/tupu-python-sdk

github下载之后，需要加一个__init__.py文件，如下内容，才能正常调用：
```
from .tupu_api import TUPU
```

主函数：

```
tupu_client = TUPU(secret_id, private_key_path, url)
```
private_key_path需要有了账号，生成了公钥、私钥才能拿到，这个步骤还是挺繁琐的，而且接口定向。


# 码隆科技

SDK-py文档写的比较完整，果然业界良心，[github地址](https://github.com/MalongTech/productai-python-sdk)。
这边估计最不人性化的就是，图像需要url化，不能本地图片直接检测，这个比较尴尬。。。
```
pip install productai
```
这边我尝试了衣物识别的相关内容。
```
from productai import Client

cli = Client(access_key_id, access_key_secret)
api = cli.get_api('detect', '_0000025')
```
关于'detect', '_0000025'，需要在官网查找对应接口的内容。


