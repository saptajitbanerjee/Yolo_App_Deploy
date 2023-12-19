import cv2
import torch
import numpy as np
from flask import Flask, render_template, Response

fire_detected = False

# Load the YOLOv5 model
model = torch.hub.load('D:\Yolov5-Fire-Detection\yolov5', 'custom', path='D:/Yolov5-Fire-Detection/models/best.pt', source='local')
#model.conf = 0.35

app = Flask(__name__)

# Route for the video stream
@app.route('/video_feed')
def video_feed():
    return Response(video_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')

def video_stream():
    global fire_detected

    # Initialize the camera using OpenCV (assuming it's connected to /dev/video0)
    camera = cv2.VideoCapture("http://192.168.94.45:8000/stream.mjpg")
    #camera = cv2.VideoCapture(0)

    while True:
        success, image = camera.read()

        if not success:
            print("Failed to read frame from the camera.")
            break

        results = model(image)
        detected_objects = results.pred[0]

        if len(detected_objects) > 0 and not fire_detected:
            # Fire detected and email not sent yet
            # send_mail()
            fire_detected = True
        elif len(detected_objects) == 0:
            fire_detected = False  # Reset the flag if no fire is detected

        # Convert the frame to JPEG format
        ret, buffer = cv2.imencode('.jpeg', image)
        jpeg_bytes = buffer.tobytes()

        # Yield the frame to the video stream
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg_bytes + b'\r\n')

    camera.release()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
