# 2.2 WatWaAram22 jpg แปลงผลลัพธ์ 9 ส่วนในภาพเพียงภาพเดียว
#Gray Scale with Red    Gray Scale with Green    Gray Scale with Blue
#Gray Scale with Max   Gray Scale with Min       Gray Scale with Mean
#Black/White Color    Sepia Color     Cyanotype Color
# pip install Pillow numpy matplotlib
from PIL import Image, ImageOps
import numpy as np
img = Image.open("WatWaAram.jpg").convert("RGB")
w, h = img.size


canvas = Image.new("RGB", (w * 3, h * 3))

def get_processed_image(mode):
    
    new_img = Image.new("RGB", (w, h))
    pixels = img.load()
    out_pixels = new_img.load()
    
    for x in range(w):
        for y in range(h):
            r, g, b = pixels[x, y]
            
            if mode == "red": out_pixels[x,y] = (r, r, r)
            elif mode == "green": out_pixels[x,y] = (g, g, g)
            elif mode == "blue": out_pixels[x,y] = (b, b, b)
            elif mode == "max":
                v = max(r, g, b)
                out_pixels[x,y] = (v, v, v)
            elif mode == "min":
                v = min(r, g, b)
                out_pixels[x,y] = (v, v, v)
            elif mode == "mean":
                v = (r + g + b) // 3
                out_pixels[x,y] = (v, v, v)
            elif mode == "bw":
                v = 255 if (r + g + b) // 3 > 128 else 0
                out_pixels[x,y] = (v, v, v)
            elif mode == "sepia":
                tr = int(0.393 * r + 0.769 * g + 0.189 * b)
                tg = int(0.349 * r + 0.686 * g + 0.168 * b)
                tb = int(0.272 * r + 0.534 * g + 0.131 * b)
                out_pixels[x,y] = (min(tr, 255), min(tg, 255), min(tb, 255))
            elif mode == "cyanotype":
                v = (r + g + b) // 3
                out_pixels[x,y] = (int(v * 0.4), int(v * 0.7), v) 
                
    return new_img

modes = [
    "red", "green", "blue",
    "max", "min", "mean",
    "bw", "sepia", "cyanotype"
]

index = 0
for row in range(3):
    for col in range(3):
        print(f"Processing: {modes[index]}...")
        proc_img = get_processed_image(modes[index])
        # คำนวณตำแหน่ง (x, y) ที่จะแปะ
        canvas.paste(proc_img, (col * w, row * h))
        index += 1

canvas.save("WatWaAram22.jpg")
canvas.show()
print("Done! Saved as WatWaAram22.jpg")
