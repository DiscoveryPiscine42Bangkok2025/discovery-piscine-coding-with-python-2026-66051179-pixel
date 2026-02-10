#!/usr/bin/env python3
import sys

# 1. เช็คว่ามี Parameter มาครบ 2 ตัวไหม? (รวมชื่อไฟล์เป็น 3)
if len(sys.argv) == 3:
    # 2. แปลงข้อความให้เป็น "ตัวเลข" (int) ก่อน เพราะ sys.argv ส่งมาเป็น Text
    start_num = int(sys.argv[1])
    end_num = int(sys.argv[2])
    
    # 3. สร้างช่วงตัวเลขด้วย range()
    # สูตรคือ: range(เริ่ม, จบ + 1)
    # *ต้องบวก 1 เพราะ Python จะหยุด 'ก่อน' ถึงตัวสุดท้ายเสมอ
    numbers = list(range(start_num, end_num + 1))
    
    # 4. พิมพ์ออกมา
    print(numbers)
else:
    print("none")