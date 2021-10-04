import cv2
import numpy as np

"""
cv2.equalizeHist(src, dst=None) -> dst
• src: 입력 영상. 
• dst: 결과 영상.
"""

src = cv2.imread("window.jpg")
# 이미지 불러오기

if src is None:
    print("Image load is failed!!")
# 불러오기 실패시 출력

Ycrcb = cv2.cvtColor(src, cv2.COLOR_RGB2YCrCb)
# openCV 자체변환 함수

Y, cr, cb = cv2.split(Ycrcb)
# 채널별로 나눠주기


Y = cv2.equalizeHist(Y)
# Y정보만으로 Histogram Equalization

dst_Ycbcr = cv2.merge((Y, cr, cb))
dst = cv2.cvtColor(dst_Ycbcr, cv2.COLOR_YCrCb2RGB)
# REB영상으로 다시 만들기


###################################################
height, width, channel = src.shape


hist, bins = np.histogram(Y.flatten(), 256, [0, 256])
# 이미지 히스토그램 구해주기

cdf = hist.cumsum()
# 각 멤버값을 누적하여 더한 1차원 배열 생성

cdf_m = np.ma.masked_equal(cdf, 0)
# cdf에서 값이 0인 부분  mask 처리


cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
#  균일화 방정식 코드

cdf = np.ma.filled(cdf_m, 0). astype("uint8")
# mask처리된 부분을 o으로 다시 리턴

out = (np.dstack((Y, cr, cb)))
out_rgb = cv2.cvtColor(out, cv2.COLOR_YCrCb2RGB)

img2 = cdf[out_rgb]


#########################################################
resize_src = cv2.resize(src, (400, 400))
resize_dst = cv2.resize(dst, (400, 400))
resize_dst2 = cv2.resize(img2, (400, 400))

# 크기 조절


PSNR1 = cv2.PSNR(resize_src, resize_dst)
PSNR2 = cv2.PSNR(resize_src, resize_dst2)
# openCV 를 이용한 PSNR 값을 PSNR1,2에 저장

print(PSNR1, PSNR2)


cv2.imshow("src", resize_src)
cv2.imshow("dst", resize_dst)
cv2.imshow("dst2", resize_dst2)

cv2.waitKey()
# 출력

cv2.destroyAllWindows()
