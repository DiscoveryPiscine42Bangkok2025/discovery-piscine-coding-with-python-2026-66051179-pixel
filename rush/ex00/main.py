#!/usr/bin/env python3
from checkmate import checkmate

def main():
    # Test 1: มี King 2 ตัว (เกินมา 1)
    print("--- Test 1: 2 Kings (Excess 1) ---")
    board_2k = """\
K...
.K..
...
....\
"""
    checkmate(board_2k)

    # Test 2: มี King 3 ตัว (เกินมา 2)
    print("\n--- Test 2: 3 Kings (Excess 2) ---")
    board_3k = """\




"""
    checkmate(board_3k)

    # Test 3: ปกติ (King 1 ตัว)
    print("\n--- Test 3: Normal (1 King) ---")
    board_normal = """\

.K..
R...
....\
"""
    checkmate(board_normal)

if __name__ == "__main__":
    main()