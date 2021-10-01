import cv2
import numpy as np
# 호출

img = cv2.imread("window.jpg")
# 이미지 불러오기

YCbCr2 = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)
Re_RGB = cv2.cvtColor(YCbCr2, cv2.COLOR_YCrCb2RGB)
# openCV 자체변환 함수 

y1, cr1, cb1 = cv2.split(YCbCr2)
#채널별로 나눠주기

resize_img1 = cv2.resize(img, (400,400))
resize_y1 = cv2.resize(y1, (400,400))
resize_rergb1 = cv2.resize(Re_RGB, (400,400))
#크기 조절

cv2. imshow("img", resize_img1)
cv2. imshow("y1", resize_y1)
cv2. imshow("re_RGB",resize_rergb1)
# 출력


################################## 
height, width, channel = img.shape
b = img[..., 0]
g = img[..., 1]
r = img[..., 2] 
# 크기를 구하고 rgb로 나누어주기 

y2 = np.zeros((height, width), dtype=np.float)
cr2 = np.zeros((height, width), dtype=np.float)
cb2 = np.zeros((height, width), dtype=np.float)

# y,cb,cr 에 빈영상 만들기

for i in range(height): 
    for j in range(width):
        y2[i][j] = 0.299 * r[i][j] + 0.587 * g[i][j] + 0.114 * b[i][j] 
        cb2[i][j] = (-0.172*r[i][j]) - (0.339*g[i][j]) + (0.511*b[i][j]) + 128
        cr2[i][j] = (0.511*r[i][j])- (0.428*g[i][j]) - (0.083*b[i][j]) + 128 
# RGB 영상을 YCbCr로 변환 수식

for i in range(height):
    for j in range(width):
        r[i][j] = y2[i][j] + 1.371*(cr2[i][j] - 128)
        g[i][j] = y2[i][j] - 0.698*(cr2[i][j] - 128) - 0.336*(cb2[i][j] - 128)
        b[i][j] = y2[i][j] + 1.732*(cb2[i][j] - 128)
# yCbCr을 RGB 변환 수식


out = (np.dstack((b, g, r)))
#  변환한 RGB 합치기

resize_y2 = cv2.resize(y2, (400,400))
resize_out = cv2.resize(out, (400,400))
# 크기조절

cv2.imshow('y2', resize_y2.astype(np.uint8)) 
cv2.imshow("re_RGB2", resize_out)
#출력

cv2.waitKey(0)
#화면유지

