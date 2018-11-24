
import numpy as np
import cv2
import pandas as pd
import indicoio
import datetime
indicoio.config.api_key = '7bdeb1f76e744d1c8927f8766004f603' #this key needs to be hidden XD

from PIL import Image

# function to get username from frontend or sth idk
#def getname(name):
#    username = name

# filename example: Nana181124-134158Pitch.csv
username = "tester"
curtime = datetime.datetime.now().strftime("%y%m%d%H%M%S")
csvname = username + "-" + curtime + "-pitch.csv"


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


#Enter video name to be processed here
cap = cv2.VideoCapture("tester.avi")


#Global variables
iteration = 0 
emotionDict = {}
imgShot = "img.png"

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if frame is None:
        break

    gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.15, minNeighbors=8)

    for (x, y, w, h) in faces:
        
        #region of interest
        roi_gray = gray[y:y+h, x:x+w] 
        roi_color = frame[y:y+h, x:x+w]

        #write every image to a temp image
        cv2.imwrite(imgShot, roi_color)
        imgShotOpen = Image.open(imgShot)

        #get emotion with indicoio
        pixel_array = np.array(imgShotOpen)
        curEmoDict = indicoio.fer(pixel_array)

        #collect results in a new dict
        for key in curEmoDict:
            if key not in emotionDict:
                emotionDict[key] = []
            emotionDict[key].append(curEmoDict.get(key))

        #Face Detection Rectangle
        color = (130, 236, 77) #BGR 
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h

        #draw on the frame, start from x,y , end at x+w y+h, and detailsa~
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)


    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# Pass result dict to csv
df = pd.DataFrame(emotionDict)
df.to_csv(csvname)


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
