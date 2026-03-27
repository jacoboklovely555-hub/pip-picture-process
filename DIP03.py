#จงประมวลผลภาพด้วยการดึงค่าสี RGB ของภาพออกมา จากนั้นให้ทำการคำนวณหา
#ความถี่ของค่าสี (0-255) ในแต่ละค่าสีแยกเป็น R G และ B ออกจากกัน จากนั้นให้ทำการคำนวณหาค่าที่ควรสกัดจากค่าสีเหล่านั้นพร้อมการแสดงผลด้วยกราฟ
#ค่าสีที่มีค่าสูงสุด ค่าสีที่มีค่าต่ำสุด ค่าเฉลี่ยของค่าสีแดง
#ค่าสีที่มีค่าสูงสุด ค่าสีที่มีค่าต่ำสุด ค่าเฉลี่ยของค่าสีเขียว
#ค่าสีที่มีค่าสูงสุด ค่าสีที่มีค่าต่ำสุด ค่าเฉลี่ยของค่าสีน้ำเงิน
 
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = Image.open("WatWaAram.jpg").convert("RGB")
r, g, b = img.split()

channels = [('Red', r, 'red'), ('Green', g, 'green'), ('Blue', b, 'blue')]

plt.figure(figsize=(15, 5))

for i, (name, ch, color_code) in enumerate(channels):
    data = np.array(ch)
    
    c_max = np.max(data)
    c_min = np.min(data)
    c_mean = np.mean(data)
    
    print(f"Channel {name}: Max={c_max}, Min={c_min}, Mean={c_mean:.2f}")
    
    plt.subplot(1, 3, i+1)
    plt.hist(data.flatten(), bins=256, range=(0, 255), color=color_code, alpha=0.7)
    plt.title(f"Histogram of {name}\nMax:{c_max} Min:{c_min} Mean:{c_mean:.1f}")
    plt.xlabel("Intensity (0-255)")
    plt.ylabel("Frequency")

plt.tight_layout()
plt.show() 
