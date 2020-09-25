board = [ 
    [ ' ', ' ', 'x' ] , 
    [ ' ', ' ', ' ' ] , 
    [ 'x', ' ', 'x' ] 
]


def display_board(board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            print(f"{board[r][c]}", end='')
            if c < len(board[r])-1:
                print("|", end='')
        print("")
        if r < len(board)-1:
            print("-+-+-")

def check_by_row(board):
    winner = False
    r=0
    while r<len(board):
        c=0
        count=0
        while c<len(board[r]):
            if board[r][c] == 'x':
                count += 1
            if count >= 3:
                winner = True
            c+=1
        r+=1
    return winner

def check_by_col(board):
    winner = False
    c=0
    while c<len(board[0]):
        r=0
        count=0
        while r<len(board):
            if board[r][c] == 'x':
                count += 1
            if count >= 3:
                winner = True
            r+=1
        c+=1
    return winner

def check_by_ullr(board):
    winner = False
    r=0
    c=0
    count=0
    while r<len(board):
        if board[r][c] == 'x':
            count += 1
        if count >= 3:
            winner = True
        c+=1
        r+=1
    return winner

def check_by_urll(board):
    winner = False
    r=0
    c=len(board[r])-1
    count=0
    while r<len(board):
        if board[r][c] == 'x':
            count += 1
        if count >= 3:
            winner = True
        c-=1
        r+=1
    return winner

display_board(board)
print(check_by_row(board))
print(check_by_col(board))
print(check_by_ullr(board))
print(check_by_urll(board))
