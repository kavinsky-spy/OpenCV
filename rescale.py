import cv2 as cv

img = cv.imread('Photos/June_odd-eyed-cat.jpg')
cv.imshow('Cat', img)

# Rescale image/video on show
def rescaleFrame(frame, scale=0.50):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_LINEAR)


resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

def changeRes(width, height):
    # Live video
    capture.set(3, width)
    capture.set(4, height)

# Reading Videos
# use int parameter for webcams connected.
capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.9)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
