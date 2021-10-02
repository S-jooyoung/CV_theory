from PSNR import YCbCr2
import numpy as np
import cv2
import math
from matplotlib import pyplot as plt

src = cv2.imread("window.jpg")
# 이미지 불러오기

if src is None:
    print("Image load is failed!!")
# 오류시 출력

Ycbcr = cv2.cvtColor(src, cv2.COLOR_RGB2YCrCb)
# opencv 함수를 이용한 Ycbcr 변환

Ycbcr_plane = cv2.split(Ycbcr)
# 채널별로 나눠주기

edges = cv2.Canny(Ycbcr_plane[0], 50, 200, None, 3)
# Canny를 사용하여 edges 이미지 만들기

linesP = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, None, 20, 1)
# 확률 허프 변환

if linesP is not None:
    for i in range(0, len(linesP)):
        l = linesP[i][0]
        cv2.line(src, (l[0], l[1]), (l[2], l[3]), (0, 0, 255), 3, cv2.LINE_AA)

resize_src = cv2.resize(src, (600, 600))
# 사이즈 조절

cv2.imshow("src", resize_src)

cv2.waitKey()

cv2.destroyAllWindows()
