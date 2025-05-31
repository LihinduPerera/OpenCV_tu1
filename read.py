import cv2 as cv

#Read an image
# img = cv.imread('Photos/cat_large.jpg')

# cv.imshow('Cat', img)

#read a video
# capture = cv.VideoCapture(0) #use intergers for capture the camera - 0 for default camera and 1 , 2 ,3 .... those for other cameras
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read() # Read the current frame
    cv.imshow('video', frame) # Show the current frame

    if cv.waitKey(20) & 0xFF == ord('d'): # Wait for 20 milliseconds and check if 'd' is pressed
        break

capture.release() # Release the video capture object
cv.destroyAllWindows() # Close all OpenCV windows

cv.waitKey(0)