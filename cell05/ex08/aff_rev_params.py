#!/usr/bin/env python3
import sys

# โจทย์บอกว่าต้องมี parameter อย่างน้อย 2 ตัว
# (ถ้ารวมชื่อไฟล์ด้วย len ต้องเป็น 3 ขึ้นไป: ชื่อไฟล์ + พารามิเตอร์1 + พารามิเตอร์2)
if len(sys.argv) > 2:
    # 1. ตัดชื่อไฟล์ออกก่อน (เอาตั้งแต่ตัวที่ 1 ไปจนจบ)
    params = sys.argv[1:]
    
    # 2. กลับด้านลิสต์ (Reverse)
    params.reverse()
    
    # 3. วนลูปปริ้นท์ทีละตัว
    for param in params:
        print(param)
else:
    print("none")