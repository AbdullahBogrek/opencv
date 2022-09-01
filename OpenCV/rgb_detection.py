import cv2 as cv
import numpy as np

font = cv.FONT_HERSHEY_SIMPLEX

def mouseRGB(event,x,y,flags,param):
    global font
    if event == cv.EVENT_LBUTTONDOWN: #checks mouse left button down condition
        blue = frame[y, x, 0]
        green = frame[y, x, 1]
        red = frame[y, x, 2]
        colors = frame[y, x]
        string = "RGB: " + " " +str(red) +  "," + str(green) +  "," + str(blue) 
        print(string)
        print("Coordinates of pixel: X: ",x,"Y: ",y)

cv.namedWindow('mouseRGB')
cv.setMouseCallback('mouseRGB',mouseRGB)

cap = cv.VideoCapture(0)

while(True):

    ret, frame = cap.read()

    cv.imshow('mouseRGB', frame)

    if cv.waitKey(1) == 27:
        break

cap.release()
cv.destroyAllWindows()