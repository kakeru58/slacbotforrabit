import os
import time
import requests
from datetime import datetime
from slackbot.bot import respond_to
import numpy as np
import cv2
TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  # ここ入力


@respond_to('写真')
def takepicture_func(message):
    ImagePath = './Path/my_picture.jpg'

    camera = cv2.VideoCapture(2)
    if not camera.isOpened():
        return
    ret, frame = camera.read()
    cv2.imwrite(ImagePath, frame)
    time.sleep(1)
    CHANNEL = 'CRTKHQSJG'
    TIT 'ウサギさん'
    files = {'file': open(ImagePath, 'rb')}
    param = {
        'token': TOKEN,
        'channels': CHANNEL,
        'filename': "filename",
        'initial_comment': "写真を撮影しました。", 'title': TITLE
    }
    requests.post(url="https://slack.com/api/files.upload", params=param, files=files)
    camera.release()
    cv2.destroyAllWindows()
