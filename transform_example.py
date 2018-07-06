
from pyimagesearch.transform import four_point_transform
import numpy as np

import cv2


im = "images/livro-mesa.jpg"
left_top =(102,160)
right_top = (452, 131)
left_bottom = (0, 369)
right_bottom = (443, 343)



image = cv2.imread(im)

def transformado(image,left_top,right_top,left_bottom,right_bottom):
    pts = np.array([left_top, right_top, left_bottom, right_bottom])
    warped = four_point_transform(image, pts)
    cv2.line(image, left_top, right_top, (0,255,0),2)
    cv2.line(image, left_top, left_bottom, (0,255,0),2)
    cv2.line(image, left_bottom, right_bottom, (0,255,0),2)
    cv2.line(image, right_bottom, right_top, (0,255,0),2)

    cv2.imshow("Original", image)
    cv2.imshow("Corrigido", warped)
    cv2.waitKey(0)

transformado(image,left_top,right_top,left_bottom,right_bottom)
