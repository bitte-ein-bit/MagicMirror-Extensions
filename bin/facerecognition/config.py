#!/usr/bin/python
# coding: utf8
# Raspberry Pi Face Recognition Treasure Box Configuration
# Copyright 2013 Tony DiCola 
import inspect
import os
import platform
import syslog

_platform = platform.system().lower()
path_to_file = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

personen = []

# Edit the values below to configure the training and usage of the
# face recognition box.
RECOGNITION_ALGORITHM = 1
# Threshold for the confidence of a recognized face before it's considered a
# positive match.  Confidence values below this threshold will be considered
# a positive match because the lower the confidence value, or distance, the
# more confident the algorithm is that the face was correctly detected.
# Start with a value of 3000, but you might need to tweak this value down if 
# you're getting too many false positives (incorrectly recognized faces), or up
# if too many false negatives (undetected faces).
if RECOGNITION_ALGORITHM == 1:
	POSITIVE_THRESHOLD = 50
elif RECOGNITION_ALGORITHM == 2:
	POSITIVE_THRESHOLD = 250
else:
	POSITIVE_THRESHOLD = 3000

# File to save and load face recognizer model.
TRAINING_FILE = path_to_file +'/training.xml'

# Size (in pixels) to resize images for training and prediction.
# Don't change this unless you also change the size of the training images.
FACE_WIDTH  = 92
FACE_HEIGHT = 112

# Face detection cascade classifier configuration.
# You don't need to modify this unless you know what you're doing.
# See: http://docs.opencv.org/modules/objdetect/doc/cascade_classification.html
HAAR_FACES         = path_to_file +'/haarcascade_frontalface.xml'
HAAR_SCALE_FACTOR  = 1.3
HAAR_MIN_NEIGHBORS = 4
HAAR_MIN_SIZE      = (30, 30)

def get_camera():
	syslog.syslog("-" * 20)
	syslog.syslog("Beutztes System: " + _platform)
	if _platform == "darwin":
		import webcam
		syslog.syslog("Webcam ausgewählt...")
	 	return webcam.OpenCVCapture(device_id=0)
	elif _platform == "linux" or _platform == "linux2":
		import picam
		syslog.syslog("PiCam ausgewählt...")
		return picam.OpenCVCapture()
	syslog.syslog("-" * 20)
