import numpy as np
import cv2
import time
from threading import Thread
import vlc

cap = cv2.VideoCapture(1)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
is_open = False
curr_time = round(time.time()*1000)

media = vlc.MediaPlayer("ad.mp4")
while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print("kurwa", len(faces))
    if len(faces)==0:
        media.set_pause(1)
        continue
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        for (ex, ey, ew, eh) in eyes:
            curr_time = round(time.time()*1000)
            print (curr_time)
            is_open = True
        if is_open and (round(time.time()*1000) - curr_time)>1000:
            print(round(time.time()*1000)-curr_time)
            is_open= False
    if is_open:
        media.play()
        print("otwarte")
    else:
        media.set_pause(1)
        print("zamkniete")

cap.release()
cv2.destroyAllWindows()

