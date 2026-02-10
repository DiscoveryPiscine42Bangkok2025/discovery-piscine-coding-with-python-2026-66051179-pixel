#!/usr/bin/env python3
import sys

# 1. เช็คก่อนว่ามี Parameter ส่งมาไหม? (ต้องมากกว่า 1 เพราะ 1 คือชื่อไฟล์)
if len(sys.argv) > 1:
    # 2. วนลูปหยิบทีละคำ (เริ่มตั้งแต่ตัวที่ 1 จนจบ)
    for arg in sys.argv[1:]:
        
        # 3. เช็คว่าคำนี้ "ไม่ได้" ลงท้ายด้วย ism ใช่ไหม?
        if not arg.endswith("ism"):
            # ถ้าใช่ (ยังไม่มี ism) -> ให้เติม ism แล้วพิมพ์
            print(arg + "ism")
        
else:
    print("none")