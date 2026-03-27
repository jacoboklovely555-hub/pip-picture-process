#จงประมวลผลภาพถ่ายวัตวาอาราม ตั้งสื่อภาพ WaWcron,jpg จากนั้นให้ทำการ
#ประมวลผลภาพโดยการแปลงภาพสี RGB หรือ True Color Image ให้กลายเป็นภาพแบบ Gray Scale โดยการแทนค่าสีด้วยสี Red, Green, Blue, Max, Min, Mean ภาพแบบขาวดำ, Sepia Color, Cyanotype Color ได้ผลลัพธ์ออกมาเป็น 9 ภาพผลลัพธ์
#ให้ดำเนินการจนได้ผลลัพธ์ 2 ภาพ
#ภาพที่ 2.1 WatWaAram21 jpg ต่อภาพผลลัพธ์ให้กลายเป็นภาพเพียงภาพเดียวภาพที่ 2.2 WatWaAram22 jpg แปลงผลลัพธ์ 9 ส่วนในภาพเพียงภาพเดียว
#Gray Scale with Red    Gray Scale with Green    Gray Scale with Blue
#Gray Scale with Max   Gray Scale with Min       Gray Scale with Mean
#Black/White Color    Sepia Color     Cyanotype Color

from PIL import Image, ImageOps

img = Image.open("WatWaAram.jpg").convert("RGB")
w, h = img.size

def get_gray_mean(r, g, b):
    avg = (r + g + b) // 3
    return (avg, avg, avg)

output_img = Image.new("RGB", (w, h))
pixels = img.load()
out_pixels = output_img.load()

for x in range(w):
    for y in range(h):
        r, g, b = pixels[x, y]
        out_pixels[x, y] = get_gray_mean(r, g, b)

output_img.save("WatWaAram21.jpg")


