def init_board():
    board = []
    for i in range(3):
        board += [["-"]*3]
    #debugging code
    #board = [["-","-","X"],["-","-","X"],["-","-","X"]]
    return board
    
def printBoard(board):
    for line in board:
        for item in line:
            print item,
        print "\n"
        
def checkWin(board):
    for i in range(3):
        #check row
        if board[i][0] != "-" and board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return True
        #check colum
        if board[0][i] != "-" and board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            return True
    #check x
    if board[0][0] != "-" and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return True
    if board[0][2] != "-" and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return True
    return False

def checkPlayer(player):
    if player:
        return "Player 1"
    else:
        return "Player 2"

    
def main(player,board,i,j):                        

    if not checkWin(board):

        if board[i][j] == "-":
            if player:
                board[i][j] = "O"
            else:
                board[i][j] = "X"               

           
            if checkWin(board):
                print checkPlayer(player), "wins"
            player = not player

    return board, player
            

