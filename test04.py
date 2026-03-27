#4

import cv2
import numpy as np
img = cv2.imread("TestPicture.jpg")

b, g, r = cv2.split(img)

# 1 Gray Max RGB

gray_max = np.maximum(np.maximum(r, g), b)
gray_img = cv2.merge([gray_max, gray_max, gray_max])

# 2 Sepia

sepia = np.zeros_like(img, dtype=np.float32)
sepia[:, :, 2] = 0.393*r + 0.769*g + 0.189*b
sepia[:, :, 1] = 0.349*r + 0.686*g + 0.168*b
sepia[:, :, 0] = 0.272*r + 0.534*g + 0.131*b
sepia = np.clip(sepia, 0, 255).astype(np.uint8)

# 3 Cyanotype

cyanotype = np.zeros_like(img, dtype=np.float32)
cyanotype[:, :, 0] = b * 1.3
cyanotype[:, :, 1] = g * 1.1
cyanotype[:, :, 2] = r * 0.6
cyanotype = np.clip(cyanotype, 0, 255).astype(np.uint8)

# รวมภาพเป็น 4 

top_row = np.hstack((img, gray_img))
bottom_row = np.hstack((sepia, cyanotype))
final_result = np.vstack((top_row, bottom_row))


cv2.imwrite("result4.jpg", final_result)


cv2.imshow("Final Result (4 Images)", final_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
