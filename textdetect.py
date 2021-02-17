# We will use open cv and tesseract, tesseract is a ocr tool for python
#PIL is is python imaging library and provides editing capabilities. 
#image grab is used to copy contents on screen and provide it to pil image memory

import cv2
import pytesseract
import time
from PIL import ImageGrab
import numpy as np

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('image.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#print(pytesseract.image_to_string(img)) #will print the image in string format in terminal

#detect character
hImg, wImg,_ = img.shape  #height and width of image
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    print(b)
    b = b.split(' ')
    print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x,hImg- y), (w,hImg- h), (0, 0, 255), 1)
    #cv2.putText(img,b[0],(x,hImg- y+10),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)





cv2.imshow('show',img)
cv2.waitKey(0)








