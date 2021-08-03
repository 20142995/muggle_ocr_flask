#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import base64
import muggle_ocr

from flask import Flask, request

sdk_Captcha = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.Captcha)
sdk_OCR = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.OCR)

app = Flask(__name__)

@app.route("/muggle_ocr/<mode>",methods=["POST"])
def index1(mode="captcha"):
    if request.get_data():
        text = ''
        try:
            if mode == "captcha":
                text = sdk_Captcha.predict(image_bytes=base64.b64decode(request.get_data().decode()))
            if mode == "ocr":
                text = sdk_OCR.predict(image_bytes=base64.b64decode(request.get_data().decode()))
        except Exception as e:
            print('[-] error:{}'.format(e))
        return text

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
