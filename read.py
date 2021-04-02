import cv2 as cv

# img = cv.imread('Photos/June_odd-eyed-cat.jpg');
#
# cv.imshow('Cat', img)

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()

cv.waitKey(0)
