def init_board():
    board = []
    for i in range(3):
        board += [["-"]*3]
    #debugging code
    board = [["a","o","z"],["a","z","l"],["z","b","a"]]
    return board
    

def printboard(board):
    for line in board:
        for item in line:
            print item,
        print "\n"
        

def checkWin(board):
    for i in range(3):
        #check row
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return True
        #check colum
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            return True
    #check x
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return True
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return True
    return False

board = init_board()                
printboard(board)            
print checkWin(board)