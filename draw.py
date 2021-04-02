import cv2 as cv
import numpy as np



blank = np.zeros((600, 600, 3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint the image a certain color
# blank[200:300, 300:400] = 0, 0, 225
# cv.imshow('Green', blank)

# 2. Draw a Rectangle
# cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=2)
# cv.imshow('Rectangle', blank)
#
#
# # 3. Draw A Circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=3)
# cv.imshow('Circle', blank)
#
# # 4. Draw a line
# cv.line(blank, (100, 250), (300, 400), (255, 255, 255), thickness=2)
# cv.imshow('Line', blank)

# 5. Write text
# cv.putText(blank, 'Hello, I can\' handle anymore :-) ', (0, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 1)
# cv.imshow('Text', blank);
#
# img = cv.imread('Photos/June_odd-eyed-cat.jpg')
# cv.imshow('Cat', img)

cv.waitKey(0)
