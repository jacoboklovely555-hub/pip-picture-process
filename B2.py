#B2
from PIL import Image

img = Image.open("ButterBear.jpg")

target_width = 512
w_percent = target_width / float(img.size[0])
target_height = int(img.size[1] * w_percent)

resized = img.resize((target_width, target_height))
resized.save("resized.jpg")

print("ก่อน:", img.size)
print("หลัง:", resized.size)

