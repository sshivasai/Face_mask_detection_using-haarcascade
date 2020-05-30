import numpy
import cv2
import os
img=cv2.imread('Maskkk.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
mask_cascade=cv2.CascadeClassifier('haarcascade_mask.xml')
faces=face_cascade.detectMultiScale(gray,1.1,4)
masks=mask_cascade.detectMultiScale(gray,1.04,3)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w, y+h),(0,0,255),2)

for (mx,my,mw,mh) in masks:
    	font=cv2.FONT_HERSHEY_DUPLEX
    	cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    	cv2.putText(img,'mask_found',(x,y),font,1,(0,255,0),2,cv2.LINE_8)
img=cv2.resize(img,(700,400))
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()

