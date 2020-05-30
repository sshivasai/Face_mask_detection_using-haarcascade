

import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
mask_cascade=cv2.CascadeClassifier('haarcascade_mask.xml')


video_src = '2.mp4'

cap = cv2.VideoCapture(video_src)




while True:
    ret, img = cap.read()
   
    if (type(img) == type(None)):
        break
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray,1.1,4 )
    masks= mask_cascade.detectMultiScale(gray,1.04,3)
    
    


    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    
    for (x,y,w,h) in masks:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        font=cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(img,'mask_found',(x,y),font,1,(255,255,255),3,cv2.LINE_8) 
    img=cv2.resize(img,(300,700))
    cv2.imshow('video', img)
    
   
    
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
