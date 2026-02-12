#!/usr/bin/env python3

def is_safe(x, y, max_x, max_y):
    # เช็คว่าพิกัดอยู่ในกระดานหรือไม่
    return 0 <= x < max_x and 0 <= y < max_y

def get_moves(piece, px, py, board, max_x, max_y):
    moves = []
    
    # กำหนดทิศทางการเดินของแต่ละตัว
    directions = []
    if piece == 'P':
        # Pawn กินทแยงขึ้นบน (ซ้าย/ขวา) เท่านั้นที่มีผลกับการรุก
        # หมายเหตุ: ใน Array [row][col] ถ้า row 0 อยู่บน
        # การกินขึ้นบนคือ row - 1
        directions = [(-1, -1), (-1, 1)] 
        for dy, dx in directions:
            ny, nx = py + dy, px + dx
            if is_safe(nx, ny, max_x, max_y):
                moves.append((ny, nx))
        return moves

    elif piece == 'B': # Bishop
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)] #upleft , upright
    elif piece == 'R': # Rook
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    elif piece == 'Q': # Queen
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]

    # Logic การเดินแบบพุ่ง (Raycasting) สำหรับ B, R, Q
    for dy, dx in directions:
        ny, nx = py + dy, px + dx
        while is_safe(nx, ny, max_x, max_y):
            moves.append((ny, nx))
            # ถ้าเจอตัวหมากขวางทาง (ที่ไม่ใช่ตัวเอง) ให้หยุด (Blocking)
            if board[ny][nx] != '.':
                break
            ny += dy
            nx += dx
            
    return moves

def checkmate(board_str):
    try:
        # 1. แปลงกระดาน ตัดช่องว่างหัวท้าย และแยกบรรทัด
        rows = [line.strip() for line in board_str.strip().splitlines()]
        
        # 2. เช็คความถูกต้องของกระดาน (สี่เหลี่ยมผืนผ้า)
        if not rows:
            print("Table Fail")
            return
        
        height = len(rows)
        width = len(rows[0])
        for row in rows:
            if len(row) != width:
                print("H&W Fail")
                return

        # 3. หาตำแหน่ง King และศัตรู
        king_pos = None
        enemies = [] # เก็บ tuple (ตัวอะไร, y, x)

        for r in range(height):
            for c in range(width):
                piece = rows[r][c]
                if piece == 'K':
                    king_pos = (r, c)
                elif piece in ['P', 'B', 'R', 'Q']:
                    enemies.append((piece, r, c))
                elif piece != '.':
                    print("Fail") # เจอตัวประหลาด
                    return

        # ถ้าไม่มี King
        if not king_pos:
            print("Fail")
            return

        # 4. จำลองการเดินของศัตรูทุกตัว
        # ถ้าตาเดินของศัตรูตัวไหน ทับตำแหน่ง King = โดนรุก (Success)
        for piece, r, c in enemies:
            possible_moves = get_moves(piece, c, r, rows, width, height)
            if king_pos in possible_moves:
                print("Success")
                return

        # รอด
        print("Fail")

    except Exception:
        print("Fail")