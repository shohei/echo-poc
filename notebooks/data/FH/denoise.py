import numpy as np
import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture('1.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 10.0, (480,480))

while True:
    try:
        _,frame = cap.read()
        edges = cv2.Canny(frame,100,200)
        frame = cv2.cvtColor(frame, code=cv2.COLOR_BGR2RGB)
        # cv2.imshow('canny',frame)
        dst = cv2.fastNlMeansDenoisingColored(frame, None, 10, 10, 7, 21)
        cv2.imshow('canny',dst)
        out.write(dst)
        key = cv2.waitKey(1) & 0xff
        if key == ord('q'):
            break
    except:
        out.release()

    # dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
    # # dst2=cv2.cvtColor(dst,code=cv2.COLOR_BGR2RGB)
    #
    # plt.subplot(121), plt.imshow(img)
    # # plt.subplot(122), plt.imshow(dst)
    # # plt.subplot(122), plt.imshow(dst2)
    # plt.show()
