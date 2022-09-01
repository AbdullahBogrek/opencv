import cv2 as cv 
import numpy as np 

img = cv.imread("/home/abdullah/Desktop/OpenCV/OpenCV/images/hand.jpg")
height, width = img.shape[:2]
cv.resize(img,(0,0), fx = 0.1, fy = 0.1)

# resize the image
scale_percent = 50
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dsize = (width, height)
img = cv.resize(img, dsize)

# thresholding
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.blur(gray, (7,7))
ret, thresh = cv.threshold(blur, 68, 255, cv.THRESH_BINARY)

contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# we create a list for convex hull points
hull = []

# We're adding convex hull points to the list with for loop. But we add the indices with the false parameter. 
for i in range(len(contours)):
    hull.append(cv.convexHull(contours[i], False))

# canvas = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)
for i in range(len(contours)):
    cv.drawContours(img, hull, -1, (0, 255, 0))

cv.imshow("HULL", img)

cv.waitKey(0)
cv.destroyAllWindows()