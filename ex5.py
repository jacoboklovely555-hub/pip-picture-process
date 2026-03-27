#ex5 จงหา Library สำหรับลบภาพพื้นหลังออกจากรูป
from rembg import remove
from PIL import Image

# เปิดรูป
input_path = "input.png"
output_path = "output.png"

with open(input_path, "rb") as i:
    with open(output_path, "wb") as o:
        input_data = i.read()
        output_data = remove(input_data)
        o.write(output_data)

print("ลบพื้นหลังเรียบร้อยแล้ว!")
