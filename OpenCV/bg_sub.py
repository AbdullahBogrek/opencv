import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt

img = cv.imread("/home/abdullah/Desktop/OpenCV/OpenCV/images/hand.jpeg")
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

rect = (600, 550, 1150, 2000)

mask = np.zeros(rgb.shape[:2], np.uint8)

bg = np.zeros((1, 65), np.float64)
fg = np.zeros((1, 65), np.float64)

cv.grabCut(rgb, mask, rect, bg, fg, 5, cv.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8")

new = rgb * mask2[:, :, np.newaxis]