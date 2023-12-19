FROM python:3.10-slim-bookworm
WORKDIR /Flask_YoloV8_Deploy
ADD . /Flask_YoloV8_Deploy

RUN pip install -r requirements.txt && pip install flask
RUN pip install ultralytics

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 unzip -y

RUN apt install awscli -y

CMD ["python3", "./Flask_YoloV8_Deploy/ultralytics/Flask/main.py"]

RUN chown -R 42420:42420 /Flask_YoloV8_Deploy
ENV HOME = /Flask_YoloV8_Deploy

