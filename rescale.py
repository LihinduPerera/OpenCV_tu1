import cv2 as cv

img = cv.imread('photos/cat_large.jpg')

# rescale frame is working perfectly with images, videos and also the live videos
def rescaleFrame(frame, scale=0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_img = rescaleFrame(img)
cv.imshow('cat',img)
cv.imshow('cat-resized',resized_img)

capture = cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('video', frame)
    cv.imshow('video resized' , frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
    
cv.waitKey(0)

# this is only work with live video
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)