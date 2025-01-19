import cv2
#import face_recognition
#import dlib
import os, sys
import numpy as np
import threading

from deepface import DeepFace

#cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #picks the first camera
cap = cv2.VideoCapture(0) #picks the first camera
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0

face_match = False

referenceImage = cv2.imread("captured_frame.jpg") # just for testing, could be any image
print("hi")
print(cv2.__version__)

if not cap.isOpened():
    print("Error: Could not open the camera.")
    sys.exit()


def check_face(frame):
    #cv2.imwrite("captured_frame.jpg", frame)

    global face_match
    try:
        if DeepFace.verify(frame, referenceImage.copy())['verified']:
            face_match = True
            print("positive face match")
    except ValueError:
        face_match = False

while True:
    ret, frame = cap.read()
    if ret:
        if counter % 30 == 0:
            try: 
                #check_face(frame.copy())
                threading.Thread(target = check_face, args = (frame.copy(),)).start() #passed as a tuple
            except ValueError:
                print("face not a match " + counter)
                #pass #does not recognize a face
                
        counter += 1

        if face_match:
            cv2.putText(frame, "MATCH!!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 3)
        else:
            cv2.putText(frame, "NO MATCH", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 3)

        cv2.imshow("video",frame)
    else:
        print("not receiving frame, maybe camera is not connected or working...")
    key = cv2.waitKey(1)
    if key == ord("q"): # press q to stop the loop
        break
cv2.destroyAllWindows()

print(cv2.__version__)


# run using /Users/Samuel/.pyenv/versions/3.10.9/bin/python3 facerecognition.py 
# becuase of library needs and virtual environment
# usually takes 10 sec to load