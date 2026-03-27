#3

import cv2
import numpy as np

# โหลดภาพจากไฟล์
img = cv2.imread("TestPicture.jpg")

b, g, r = cv2.split(img)

# 1 Grayscale จากค่าสูงสุดของ RGB
gray_max = np.maximum(np.maximum(r, g), b)
result1 = cv2.merge([gray_max, gray_max, gray_max])
cv2.imwrite("result1.jpg", result1)

# 2 Sepia tone
sepia = np.zeros_like(img, dtype=np.float32)

sepia[:, :, 2] = 0.393*r + 0.769*g + 0.189*b
sepia[:, :, 1] = 0.349*r + 0.686*g + 0.168*b
sepia[:, :, 0] = 0.272*r + 0.534*g + 0.131*b

sepia = np.clip(sepia, 0, 255).astype(np.uint8)
cv2.imwrite("result2.jpg", sepia)

# 3 Cyanotype

cyanotype = np.zeros_like(img, dtype=np.float32)
cyanotype[:, :, 0] = b * 1.3
cyanotype[:, :, 1] = g * 1.1
cyanotype[:, :, 2] = r * 0.6

cyanotype = np.clip(cyanotype, 0, 255).astype(np.uint8)
cv2.imwrite("result3.jpg", cyanotype)


cv2.imshow("Result 1: Gray Max RGB", result1)
cv2.imshow("Result 2: Sepia", sepia)
cv2.imshow("Result 3: Cyanotype", cyanotype)

cv2.waitKey(0)
cv2.destroyAllWindows()
