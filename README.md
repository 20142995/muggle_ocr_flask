# 验证码识别神器 muggle_ocr 简易flask API 版

    简述：可供多人使用，docker版可快速部署环境
    功能：提交图片内容的base64编码到对应接口，成功即返回识别结果，失败则返回为空

## 源码搭建(python3.6.9)

    git clone https://github.com/20142995/muggle_ocr_flask
    cd muggle_ocr_flask
    pip install -r requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
    python server.py

## docker搭建

### 自行编译

    git clone https://github.com/20142995/muggle_ocr_flask
    cd muggle_ocr_flask
    docker build . -t muggle_ocr_flask
    docker run -dit -p 5000:5000 muggle_ocr_flask

### 开箱即用

    docker run -dit -p 5000:5000 20142995/muggle_ocr_flask

## 使用样例

### python test.py

    #!/usr/bin/python3
    # -*- coding: UTF-8 -*-

    import requests
    import base64


    # 4-6位英数验证码识别
    url = "http://127.0.0.1:5000/muggle_ocr/captcha"

    for i in range(10):
        img = '1.png'
        r = requests.post(url,data=base64.b64encode(open(img,'rb').read()).decode())
        print(r.text)

    # 印刷字ocr识别 
    url = "http://127.0.0.1:5000/muggle_ocr/ocr"
    for i in range(10):
        img = '2.png'
        r = requests.post(url,data=base64.b64encode(open(img,'rb').read()).decode())
        print(r.text)

