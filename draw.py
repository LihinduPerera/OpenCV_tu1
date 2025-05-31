import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# 1.Paint image in certain color
# blank[:] = 0,255,0
# cv.imshow('Green', blank)

# 2.paint for certain range
# blank[200:300, 300:400] = 0,0,255
# cv.imshow('Red Squre', blank)

#3. draw rectangle
cv.rectangle(blank, (0,0), (250,250) , (255,0,0), thickness=5)
# cv.rectangle(blank, (0,0), (250,250) , (255,0,0), thickness=cv.FILLED) #For filling the rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=1)
cv.imshow('blue Rectangle shape', blank)

# 4.Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40 , (0,0,255), thickness=3)
cv.imshow('Circle', blank)


#5.draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2) , (255,255,0) , thickness=7)
cv.line(blank, (100,250), (300,400) , (255,255,0) , thickness=7)
cv.imshow('lines' , blank)

#6. Write a text on the image
cv.putText(blank, "Hello, my name is Lihindu!", (0,255) , cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)
cv.imshow('text' , blank)


cv.waitKey(0)