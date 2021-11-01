import cv2
import numpy as np
import math
# 호출

img = cv2.imread("window.jpg")
# 이미지 불러오기

YCbCr2 = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)
Re_RGB = cv2.cvtColor(YCbCr2, cv2.COLOR_YCrCb2RGB)
# openCV 자체변환 함수 

def PSNR(img1, img2):

    mse = np.mean((img1 - img2) ** 2)
    # MSE 구하는 식
    
    PLXEL_MAX = 255.0
    # 8bit MAX는 255의 값을 가짐

    return 20 * math.log10(PLXEL_MAX/math.sqrt(mse))
    #PSNR 구하는 식

###############################################################

PSNR1 = cv2.PSNR(img,Re_RGB)
# openCV 를 이용한 PSNR 값을 PSNR1에 저장

PSNR2 = PSNR(img,Re_RGB)
# 수식을 이용한 함수구현 PSNR 값을 PSNR2에 저장


print("openCV를 이용한 PSNR :", PSNR1)
print("주어진 수식을 이용한 함수구현:", PSNR2)
# 출력

