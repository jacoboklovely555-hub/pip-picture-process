#B1

from PIL import Image
import numpy as np

img = Image.open("cute.jpg").convert("L")
img.save("grayscale.jpg")

arr = np.array(img)

print("Mean:", arr.mean())
print("Std:", arr.std())


