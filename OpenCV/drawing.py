import cv2
import numpy as np

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN :
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (0, 131, 255), 5, cv2.LINE_AA)
        cv2.imshow('Image', img)
    elif event == cv2.EVENT_RBUTTONDOWN:
        points.clear()

img = np.zeros((512, 512, 3), np.uint8)
cv2.imshow('Image', img)
points = []

while True:
    key = cv2.waitKey(1)
    if key == 27:
        break
    if key == ord("d"):
        cv2.setMouseCallback('Image', click_event)
    elif key == ord("c"):
        points = []
        img *= 0

cv2.destroyAllWindows()