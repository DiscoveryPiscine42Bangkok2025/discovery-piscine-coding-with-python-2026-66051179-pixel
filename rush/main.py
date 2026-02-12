#!/usr/bin/env python3
from checkmate import checkmate

def main():
    
    # โจทย์ข้อที่ 1 (Rook อยู่มุม, King อยู่หลบ) -> ควรตอบ Fail
    # หมายเหตุ: เขียนชิดซ้ายเพื่อให้ไม่มีช่องว่างเกินมา
    print("--- Test 1 (4x4) ---")
    board1 = """\
R...
....
....\
"""
    checkmate(board1)

    # โจทย์ข้อที่ 2 (ไม่มีศัตรูเลย มีแต่ King) -> ควรตอบ Fail (หรือ All pieces missing)
    print("\n--- Test 2 (4x4 No Enemy) ---")
    board2 = """\
....
.K..
....
....\
"""
    checkmate(board2)

    # --- โค้ดเก่าที่ Comment ไว้ (จัดระเบียบให้แล้ว) ---
    
    # ตัวอย่าง: กระดาน 2x2
    # board = """\
    # ..
    # .K\
    # """
    # checkmate(board)

    # ตัวอย่าง: กระดาน 8x8 (มาตรฐาน)
    # board = """\
    # ..PK....
    # ..P...K.
    # ..PPP...
    # Q.......
    # ........
    # ........
    # ........
    # ........\
    # """
    # checkmate(board)

if __name__ == "__main__":
    main()