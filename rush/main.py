#!/usr/bin/env python3
from checkmate import checkmate

def main():
    # Test 1: โดน Rook รุก (Success)
    board1 = """\
R...
.K..
..P.
....\
"""
    print("Test 1 Expect Success:")
    checkmate(board1)
    print("-" * 10)

    # Test 2: ปลอดภัย (Fail)
    board2 = """\
..
.K\
"""
    print("Test 2 Expect Fail:")
    checkmate(board2)
    print("-" * 10)

    # Test 3: Pawn รุก (Success)
    # Pawn (P) อยู่บรรทัดล่างกว่า K และเยื้อง -> กินขึ้นบน
    board3 = """\
....
.K..
P...
....\
""" 
    print("Test 3 Expect Success:")
    checkmate(board3)

if __name__ == "__main__":
    main()