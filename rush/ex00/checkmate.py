# board structure example 4x4 :
# y\x ---------------------> +
#  | [0,0] [0,1] [0,2] [0,3]
#  | [1,0] [1,1] [1,2] [1,3]
#  V [2,0] [2,1] [2,2] [2,3]
#  + [3,0] [3,1] [3,2] [3,3]

# is_safe function used to check if the position is inside board.
def is_safe(pos_x, pos_y, max_x, max_y):
    return 0 <= pos_x < max_x and 0 <= pos_y < max_y

# get_moves function used to get all possible move for pieces.
def get_moves(piece, pos_x, pos_y, board, max_x, max_y):
    moves = []
    directions = []
    
    if piece == 'P':
        directions = [(-1, -1), (-1, 1)] 
        for dir_y, dir_x in directions:
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

    for dir_y, dir_x in directions:
        new_y, new_x = pos_y + dir_y, pos_x + dir_x
        while is_safe(new_x, new_y, max_x, max_y):
            moves.append((new_y, new_x))
            if board[new_y][new_x] != '.':
                break
            new_y += dir_y
            new_x += dir_x
    return moves

# checkmate function used to check if King can be captured by another pieces.
def checkmate(board_str):
    try:
        clean_board_str = board_str.strip()
        if not clean_board_str:
            print("Empty Board")
            return

        #Extract board_str into list.
        raw_lines = clean_board_str.splitlines()
        rows = []
        for line in raw_lines:
            clean_line = line.strip()
            rows.append(clean_line)
        
        height = len(rows)
        width = len(rows[0])
        
        # Check if board is valid
        for row in rows:
            if len(row) != width or height != width:
                print("Table is not square") #FIXED
                return

        kings_found = []
        enemies = []

        # Pieces Validation
        for r in range(height):
            for c in range(width):
                piece = rows[r][c]
                if piece == 'K':
                    kings_found.append((r, c))
                elif piece in ['P', 'B', 'R', 'Q']:
                    enemies.append((piece, r, c))
                elif piece != '.':
                    print("Error, Found illegal piece") 
                    return

        # Validate King Amount
        king_count = len(kings_found)
        if king_count == 0:
            print("Don't have any King on chess board")
            return
        if king_count > 1:   
            excess = king_count - 1
            print(f"Error: Multiple Kings found. Excess: {excess}")
            return

        # Check if King is in check
        king_pos = kings_found[0]
        for piece, r, c in enemies:
            possible_moves = get_moves(piece, c, r, rows, width, height)
            if king_pos in possible_moves:
                print("Success")
                return
        print("Fail")

    except Exception:
        print("Error Exception")