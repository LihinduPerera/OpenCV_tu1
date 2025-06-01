import cv2 as cv 

img = cv.imread('Photos/cat.jpg')

cv.imshow('Cat' , img)

# Converting img to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur the image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)
# reduse the canny edges using blur
reduse_canny = cv.Canny(blur, 125,175) # Use blur image to reduse the canny edges
cv.imshow('Redused canny Edges', reduse_canny)

# Dilating the images
dilated = cv.dilate(canny, (7,7) , iterations=4) #use canny Edge images for the dilating
cv.imshow('Dilated', dilated)

# Eroding the image - to get same-like edge cascate again
eroded = cv.erode(dilated, (7,7) , iterations=4)
cv.imshow('Erode' , eroded)

# resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)