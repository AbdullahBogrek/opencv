import cv2 as cv
import numpy as np 

font = cv.FONT_HERSHEY_SIMPLEX

img = cv.imread("/home/abdullah/Desktop/OpenCV/OpenCV/images/shapes.png",1)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_,threshold = cv.threshold(gray, 240, 255, cv.THRESH_BINARY)

contours,_ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

for contour in contours:
    
    approx = cv.approxPolyDP(contour, 0.01 * cv.arcLength(contour, True), True)

    cv.drawContours(img, [approx], 0, (0, 0, 0), 5)

    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if len(approx) == 3:
        cv.putText(img, "Triangle", (x,y), font, 1, (0, 0, 0), (0))
    
    elif len(approx) == 4:
        cv.putText(img, "Rectangle", (x,y), font, 1, (0,0,0), (0))

    elif len(approx) == 5:
        cv.putText(img, "Pentagon", (x,y), font, 1, (0,0,0), (0))

    elif len(approx) == 6:
        cv.putText(img, "Hexagon", (x,y), font, 1, (0,0,0), (0))

    elif len(approx) == 10:
        cv.putText(img, "Star", (x,y), font, 1, (0,0,0), (0))

    else:
        cv.putText(img, "Circle", (x,y), font, 1, (0,0,0), (0))

cv.imshow("IMG", img)
cv.waitKey(0)
cv.destroyAllWindows()