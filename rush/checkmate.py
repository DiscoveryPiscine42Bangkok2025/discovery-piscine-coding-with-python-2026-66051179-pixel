#!/usr/bin/env python3

#Postion start from 1,1 at the buttom left
#pos[0] -> X
#pos[1] -> Y

def mvable(to_mv,all_pos):
    if to_mv in all_pos:
        return False
    else:
        return True

def diag_mv(b_pos, chess_size, all_pos, x_dir, y_dir):
    moves = []
    i = 1
    while 0 < b_pos[0] + i * x_dir <= chess_size[0] and \
            0 < b_pos[1] + i * y_dir <= chess_size[1] and \
            mvable([b_pos[0] + i * x_dir, b_pos[1] + i * y_dir], all_pos):
        b_temp = [b_pos[0] + i * x_dir, b_pos[1] + i * y_dir]
        if not mvable(b_temp,all_pos):
            break
        moves.append(b_temp)
        i += 1
    return moves

def b_mv(b_pos, chess_size, all_pos):
    bmv = []
    # bottom left
    bmv.extend(diag_mv(b_pos, chess_size, all_pos, -1, -1))
    # bottom right
    bmv.extend(diag_mv(b_pos, chess_size, all_pos, 1, -1))
    # top left
    bmv.extend(diag_mv(b_pos, chess_size, all_pos, -1, 1))
    # top right
    bmv.extend(diag_mv(b_pos, chess_size, all_pos, 1, 1))
    return bmv

def p_mv(p_pos,chess_size,all_pos):
    pmv = []
    #R
    if p_pos[0] + 1 <= chess_size[0] and p_pos[1] + 1 <= chess_size[1]:
        p_temp = [p_pos[0] + 1,p_pos[1] + 1]
        if mvable(p_temp,all_pos):
            pmv.append(p_temp)
    #L
    if p_pos[0] - 1 > 0 and p_pos[1] + 1 <= chess_size[1]:
        p_temp = [p_pos[0] - 1,p_pos[1] + 1]
        if mvable(p_temp,all_pos):
            pmv.append(p_temp)
    return pmv

def st_mv(r_pos, chess_size, all_pos, x_dir, y_dir):
    moves = []
    i = 1
    while 0 < r_pos[0] + i * x_dir <= chess_size[0] and \
            0 < r_pos[1] + i * y_dir <= chess_size[1] and \
            mvable([r_pos[0] + i * x_dir, r_pos[1] + i * y_dir], all_pos):
        r_temp = [r_pos[0] + i * x_dir, r_pos[1] + i * y_dir]
        if not mvable(r_temp, all_pos):
            break
        moves.append(r_temp)
        i += 1
    return moves

def r_mv(r_pos, chess_size, all_pos):
    rmv = []
    # up
    rmv.extend(st_mv(r_pos, chess_size, all_pos, 0, 1))
    # down
    rmv.extend(st_mv(r_pos, chess_size, all_pos, 0, -1))
    # left
    rmv.extend(st_mv(r_pos, chess_size, all_pos, -1, 0))
    # right
    rmv.extend(st_mv(r_pos, chess_size, all_pos, 1, 0))
    return rmv

def q_mv(q_pos, chess_size, all_pos):
    qmv = []
    qmv.extend(r_mv(q_pos, chess_size, all_pos))
    qmv.extend(b_mv(q_pos,chess_size, all_pos))
    
    return qmv

def b_valid(b_l):
    if not b_l:
        return False
    r = len(b_l)
    for i in range(r):
        if len(b_l[i]) != r:
            return False
    for i in range(r):
        for j in range(r):
            if not b_l[i][j] in ['P','B','R','Q','K','.']:
                return False
    return True

def get_pos(b_l,chess_size):
    pos_dict = {'P': [], 'B': [], 'R': [], 'Q': [], 'K' :[]}
    
    for y in range(chess_size[1]):
        for x in range(chess_size[0]):
            piece = b_l[y][x]
            if piece in pos_dict:
                pos_dict[piece].append([x + 1, chess_size[1] - y])
    
    return pos_dict

def check_missing(pos_dict):
    if not pos_dict['K'] and \
            not pos_dict['P'] and \
            not pos_dict['B'] and \
            not pos_dict['R'] and \
            not pos_dict['Q']:
        return 42
    if not pos_dict['K']:
        return 1
    if not pos_dict['P'] and \
            not pos_dict['B'] and \
            not pos_dict['R'] and \
            not pos_dict['Q']:
        return 2
    if len(pos_dict['K']) > 1:
        return 3
    return 0

def get_all_possible_move(pos_dict, chess_size):
    all_possible_moves = {'P': [], 'B': [], 'R': [], 'Q': []}
    all_pos = [pos for piece_type, positions in pos_dict.items() if piece_type != 'K' for pos in positions]
    
    for p in pos_dict['P']:
        all_possible_moves['P'].extend(p_mv(p, chess_size, all_pos))
    for b in pos_dict['B']:
        all_possible_moves['B'].extend(b_mv(b, chess_size, all_pos))
    for r in pos_dict['R']:
        all_possible_moves['R'].extend(r_mv(r, chess_size, all_pos))
    for q in pos_dict['Q']:
        all_possible_moves['Q'].extend(q_mv(q, chess_size, all_pos))
    
    return all_possible_moves

def in_check(pos_dict, all_possible_moves):
    king_pos = pos_dict['K'][0]
    
    for piece_type in ['P', 'B', 'R', 'Q']:
        if king_pos in all_possible_moves[piece_type]:
            return True
    return False

def checkmate(board):
    # print('test')
    b_l = board.split()
    if b_valid(b_l):
        # print('This board is valid')
        chess_size = [len(b_l),len(b_l[0])]
        # print('chess size',chess_size)
        pos_dict = get_pos(b_l,chess_size)
        # print('all_position',pos_dict)
        c = check_missing(pos_dict)
        if c == 1:
            print('King is missing.')
        elif c == 2:
            print('All other pieces is missing.')
        elif c == 3:
            print('King should be only one.')
        elif c == 42:
            print('Empty Board')
        else:
            all_possible_moves = get_all_possible_move(pos_dict,chess_size)
            # print('all possible move',all_possible_moves)
            if in_check(pos_dict, all_possible_moves):
                print('Success')
            else:
                print('Fail')
    else:
        print('Error')