#5

import pyqrcode
import png
import os
# ฟังก์ชันสำหรับสร้าง QR Code ตามคณะและจำนวนนักศึกษา
def generate_student_qrcodes(faculty_name, faculty_code, n):
   #  สร้างโฟลเดอร์ตามชื่อคณะ 
   if not os.path.exists(faculty_name):
       os.makedirs(faculty_name)
       print(f"สร้างโฟลเดอร์: {faculty_name}")
   # 2. Loop สร้างรหัสนักศึกษาจำนวน n คน
   for i in range(1, n + 1):
       # สร้างเลขรันลำดับ 4 หลัก (เช่น 0001, 0002)
       number = str(i).zfill(4)
       # รหัสนักศึกษา = รหัสคณะ + เลขลำดับ
       std_code = faculty_code + number
       # สร้าง QR Code
       qr_code = pyqrcode.create(std_code)
       # กำหนดที่อยู่ไฟล์ (บันทึกในโฟลเดอร์คณะ)
       filepath = os.path.join(faculty_name, f"{std_code}.png")
       qr_code.png(filepath, scale=10)
# กำหนดจำนวนนักศึกษา (n คน)
n_students = 10  # คุณสามารถเปลี่ยนค่า n เป็นจำนวนที่ต้องการได้ที่นี่
# คณะอักษรศาสตร์ 
generate_student_qrcodes("Arts", "670510500", n_students)
#  คณะวิทยาศาสตร์ 
generate_student_qrcodes("Science", "670710700", n_students)
print(f"\nประมวลผลเสร็จสิ้น: สร้าง QR Code คณะละ {n_students} ไฟล์")
