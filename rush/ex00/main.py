#!/usr/bin/env python3
from checkmate import checkmate

def main():
    
    # --- Test 1 (4x4) ---
    print("--- Test 1 (4x4) ---")
    board1 = """\
R...
.K..
....
....\
"""
    checkmate(board1)

    # --- Test 2 (4x4 No Enemy) ---
    print("\n--- Test 2 (4x4 No Enemy) ---")
    board2 = """\
....
.K..
....
....\
"""
    checkmate(board2)

    # --- Test 3 (8x8) ---
    # เปิดใช้งานส่วนนี้เพื่อทดสอบ Board 8x8
    print("\n--- Test 3 (8x8) ---")
    board3 = """\
..PK....
..P...K.
..PPP...
Q.......
........
........
........
........\
"""
    checkmate(board3)

if __name__ == "__main__":
    main()