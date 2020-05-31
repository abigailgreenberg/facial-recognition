


import os
import face_recognition
import cv2 
import numpy as np
import sys, select
import time

images = os.listdir('picturesforcode')

known_images = []

print("beginning to analyze photos")
image_faces = [imagefile for imagefile in images if not imagefile.startswith('.') ]
for imagefile in image_faces:
    print("analyzing file ", imagefile)
    known_image = face_recognition.load_image_file('picturesforcode/'+imagefile)
    known_image_encoded = face_recognition.face_encodings(known_image)[0]
    known_images.append(known_image_encoded)

print("opening webcam")
time.sleep(2)
video_capture = cv2.VideoCapture(0)

counter = 0 
while True:
    frame_left, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]
    print("analyzing frame from webcam")
    rgb_frame_encoded = face_recognition.face_encodings(rgb_frame)
    if len(rgb_frame_encoded) != 0:
        print("found a face")
        results = face_recognition.compare_faces(known_images, rgb_frame_encoded[0], tolerance=0.5)
        try:
            results.index(True)
            index_of_true = results.index(True)
            name = image_faces[index_of_true]
            print("the person is ", os.path.splitext(name)[0])
            if counter < 1:
                time.sleep(10)
                counter = 1 
        except ValueError:
            print("no match")
    print("press enter to quit")
    input, _, _ = select.select( [sys.stdin], [], [], 3 )
    if (input): 
        print("closing webcam")
        break


video_capture.release()
cv2.destroyAllWindows()