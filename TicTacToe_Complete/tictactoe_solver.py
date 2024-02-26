def check_rows(board):
    for i in range(0, 7, 3):
        if board[i] == board[i + 1] == board[i + 2] != " ":
            return board[i]
    return "False"

def check_columns(board):
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != " ":
            return board[i]
    return "False"

def check_diagonals(board):
    if board[0] == board[4] == board[8] != " ":
        return board[4]
    if board[2] == board[4] == board[6] != " ":
        return board[4]
    return "False"
