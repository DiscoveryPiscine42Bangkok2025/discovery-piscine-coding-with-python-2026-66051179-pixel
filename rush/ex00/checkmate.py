#!/usr/bin/env python3

def is_safe(pos_x, pos_y, max_x, max_y):
    return 0 <= pos_x < max_x and 0 <= pos_y < max_y  #FIXED

def get_moves(piece, pos_x, pos_y, board, max_x, max_y):
    moves = []
    directions = []
    
    if piece == 'P':
        directions = [(-1, -1), (-1, 1)] 
        # แก้ไขชื่อตัวแปรให้ตรงกัน (dy, dx)
        for dy, dx in directions:
            new_y, new_x = pos_y + dy, pos_x + dx
            if is_safe(new_x, new_y, max_x, max_y):
                moves.append((new_y, new_x))
        return moves

    elif piece == 'B': 
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)] 
    elif piece == 'R': 
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    elif piece == 'Q': 
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]

    # แก้ไขชื่อตัวแปรในลูปให้ตรงกัน (dy, dx)
    for dy, dx in directions:
        new_y, new_x = pos_y + dy, pos_x + dx
        while is_safe(new_x, new_y, max_x, max_y):
            moves.append((new_y, new_x))
            
            if board[new_y][new_x] != '.':
                break
            
            new_y += dy
            new_x += dx
            
    return moves

def checkmate(board_str):
    try:
        clean_board_str = board_str.strip()
        if not clean_board_str:
            print("Empty Board")  #FIXED
            return

        raw_lines = clean_board_str.splitlines()

        rows = []
        for line in raw_lines:
            clean_line = line.strip()
            rows.append(clean_line)
        
        height = len(rows)
        width = len(rows[0])
        
        # 1. เช็คว่าทุกแถวยาวเท่ากันไหม
        for row in rows:
            if len(row) != width:
                print("Square Not Complete") #FIXED
                return

        # 2. เช็คว่าเป็นจัตุรัสไหม (กว้าง == สูง)
        if height != width:
            print("TABLE IS NOT SQUARE!!") #FIXED
            return

        # --- ส่วนที่แก้ไข: เปลี่ยนมาเก็บ List ของ King ---
        kings_found = [] 
        enemies = [] 

        for r in range(height):
            for c in range(width):
                piece = rows[r][c]
                if piece == 'K':
                    kings_found.append((r, c)) # เจอ K ให้เก็บพิกัดไว้
                elif piece in ['P', 'B', 'R', 'Q']:
                    enemies.append((piece, r, c))
                elif piece != '.':
                    print("Error, Found illegal piece") 
                    return

        # FIND King 
        king_count = len(kings_found)
        
        if king_count == 0:
            print("Don't have KING on chess board")
            return
            
        if king_count > 1:   
            excess = king_count - 1
            print(f"Error: Multiple Kings found. Excess: {excess}")
            return

        # ดึงตำแหน่ง King ตัวจริงออกมา (ตัวที่ 0)
        king_pos = kings_found[0]

        # --- คำนวณการรุกฆาต ---
        for piece, r, c in enemies:
            possible_moves = get_moves(piece, c, r, rows, width, height)
            if king_pos in possible_moves:
                print("Success")
                return

        # print("Failสส")

    except Exception:
        print("Fail11")