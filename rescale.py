import cv2 as cv

img = cv.imread('Photos/IMG_1536.JPG')
cv.imshow('Cat', img)


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_LINEAR)


# Reading Videos
# use int parameter for webcams connected.
capture = cv.VideoCapture('Videos/131733564_1490180371175304_5900651882737316230_nddd')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()