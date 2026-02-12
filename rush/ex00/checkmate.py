#!/usr/bin/env python3

def is_safe(x, y, max_x, max_y):
    return 0 <= x < max_x and 0 <= y < max_y

def get_moves(piece, pos_x, pps_y, board, max_x, max_y):
    moves = []
    directions = []
    
    if piece == 'P':
        directions = [(-1, -1), (-1, 1)] 
        for dy, dx in directions:
            new_y, new_x = pos_y + dir_y, pos_x + dir_x
            if is_safe(new_x, new_y, max_x, max_y):
                moves.append((new_y, new_x))
        return moves

    elif piece == 'B': 
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)] 
    elif piece == 'R': 
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    elif piece == 'Q': 
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]

    for dy, dx in directions:
        new_y, new_x = py + dy, px + dx
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
            print("Table Fail")
            return

        raw_lines = clean_board_str.splitlines()

        rows = []
        for line in raw_lines:
            clean_line = line.strip()
            rows.append(clean_line)
        
        if not rows:
            print("Table Fail")
            return
        
        height = len(rows)
        width = len(rows[0])
        for row in rows:
            if len(row) != width:
                print("H & W Fail")
                return

        king_pos = None
        enemies = [] 

        for r in range(height):
            for c in range(width):
                piece = rows[r][c]
                if piece == 'K':
                    king_pos = (r, c)
                elif piece in ['P', 'B', 'R', 'Q']:
                    enemies.append((piece, r, c))
                elif piece != '.':
                    print("Error, Found illegal piece") 
                    return

        if not king_pos:
            print("Don't have KING on chess board")
            return

        for piece, r, c in enemies:
            possible_moves = get_moves(piece, c, r, rows, width, height)
            if king_pos in possible_moves:
                print("Success")
                return

        print("Fail")

    except Exception:
        print("Fail")