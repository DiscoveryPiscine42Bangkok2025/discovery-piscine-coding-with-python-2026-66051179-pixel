#!/usr/bin/env python3
from checkmate import checkmate

def main():
    board = """\
R... 
.K.. 
..P. 
....\
"""
#     board_empty =""
#     board_not_sq="""\
# K...
# .K..
# ...\
# """
#     board_2k = """\
# K...
# .K..
# ....
# ....\
# """
#     board_3k = """\
# K...
# .K..
# ..K.
# ....\
# """
#     board_normal_2x2 = """\
# KQ
# BB\
# """
#     board_normal_3x3 = """\
# PPQ
# RKB
# RPB\
# """
#     board_normal_4x4 = """\
# .P.R
# BPPP
# PRQK
# BPPP\
# """
#     board_normal_5x5 = """\
# ..PP.
# ...RP
# .B.P.
# KRB.P
# .QPPP
# """
#     print("--- Test 1: Empty ---")
#     checkmate(board_empty)
#     print("\n--- Test 2: Not Square ---")
#     checkmate(board_not_sq)
#     print("\n--- Test 3: 2 King ---")
#     checkmate(board_2k)
#     print("\n--- Test 4: 3 King ---")
#     checkmate(board_3k)
#     print("\n--- Test 5: Normal 2x2 ---")
#     checkmate(board_normal_2x2)
#     print("\n--- Test 6: Normal 3x3 ---")
#     checkmate(board_normal_3x3)
#     print("\n--- Test 7: Normal 4x4 ---")
#     checkmate(board_normal_4x4)
#     print("\n--- Test 8: Normal 5x5 ---")
#     checkmate(board_normal_5x5)

    checkmate(board)

if __name__ == "__main__":
    main()