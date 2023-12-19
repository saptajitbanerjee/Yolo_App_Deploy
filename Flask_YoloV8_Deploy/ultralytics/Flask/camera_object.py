import cv2
import torch
import numpy as np

import smtplib
from datetime import datetime


#global person_detected
person_detected = False

##model = torch.hub.load('/Yolov5-Fire-Detection/yolov5', 'custom', path='/Yolov5-Fire-Detection/models/best.pt', source='local') # Load The Model
model = torch.hub.load('/Yolov5-Fire-Detection/yolov5', 'custom', path='/Yolov5-Fire-Detection/yolov5/yolov5s.pt', source='local') # Load The Model
#model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True, force_reload=True)
model.eval()
model.conf = 0.30  # confidence threshold (0-1)

model.iou = 0.5  # NMS IoU threshold (0-1)

model_1 = torch.hub.load('D:\Yolov5-Fire-Detection\yolov5', 'custom', path='D:/Yolov5-Fire-Detection/models/best.pt', source='local')
#model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True, force_reload=True)
model_1.eval()
model_1.conf = 0.30  # confidence threshold (0-1)

model_1.iou = 0.5  # NMS IoU threshold (0-1)

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        #self.video = cv2.VideoCapture("https://rpi-stream.s3.ap-south-1.amazonaws.com/latest_frame.jpeg")
        #self.video = cv2.VideoCapture("http://192.168.225.45:8000/stream.mjpg")
        #self.video = cv2.VideoCapture("https://raspberrypi-camera.at.remote.it:33000/stream.mjpg")
        ##self.video = cv2.VideoCapture("https://x5oiuzfs.connect.remote.it/stream.mjpg")
        self.video = cv2.VideoCapture(0)
        #self.video = cv2.resize(self.video,(840,640))
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        results = model(image)
        a = np.squeeze(results.render())
        results = model_1(image)
        a += np.squeeze(results.render())
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()