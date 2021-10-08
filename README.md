# CV_theory

![Python](https://img.shields.io/badge/python-v3.9.4+-blue.svg)
![Cv2](https://img.shields.io/badge/cv2-4.5.4+-yellow)

## Basic Overview

This repository summarized computer vision theories.

---

## PSNR

```python
mse = np.mean((img1 - img2) ** 2)
# MSE 구하는 식

PLXEL_MAX = 255.0
# 8bit MAX는 255의 값을 가짐

return 20 * math.log10(PLXEL_MAX/math.sqrt(mse))
#PSNR 구하는 식

[output]
openCV를 이용한 PSNR : 52.37698680492553
주어진 수식을 이용한 함수구현 : 52.37698680492553
```

---

## Color transform

```python
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
```

---

## Filterring Smoothing

After converting the original image to Ycrcb, only the Y value was filtered with 3\*3 kernels and smoothing was performed.

```python
kernel = np.ones((3, 3), np.float32) / 9
# 3*3 커널값 저장

for i in range(5):
    Y = cv2.filter2D(Y, -1, kernel)
# 5번 필터링
```

<img src="./img/Filterring Smoothing.png" width="800" height="400">

---

## Histogram equalization

```python
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
```

dst -> function in cv2 , dst2 -> Self-made function
<img src="./img/Histogram equalization.png" width="800" height="400">

---

## Hough Line Detection

<img src="./img/Hough Line Detection.png" width="800" height="400">

---

## Contributing

Let's connect 👨‍💻 and forge the future together.😁✌

**Check the Repositories and don't forget to give a star.** 👇

:star: From [S-jooyoung](https://github.com/S-jooyoung)
