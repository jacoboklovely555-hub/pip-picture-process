#B4
import cv2

img = cv2.imread("Dragonball.jpg")

x1, y1, x2, y2 = 100, 100, 300, 300

roi = img[y1:y2, x1:x2]
blur = cv2.GaussianBlur(roi, (25, 25), 0)

img[y1:y2, x1:x2] = blur

cv2.imwrite("blurred_region.jpg", img)


