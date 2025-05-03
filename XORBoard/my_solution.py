def is_valid(board):

    rows, cols = len(board),len(board[0])
    if min(rows, cols) == 1:
        return True
    
    for r in range(1, rows):
        is_flipped = board[0][0] ^ board[r][0]
        for c in range(1, cols):
            if is_flipped ^ board[0][c] ^ board[r][c]:
                return False
    
    return True

