import pygame, sys, time, random
from pygame.locals import *
from move import *

pygame.init()
window = pygame.display.set_mode((450, 550))
pygame.display.set_caption("Tic-Tac-Toe")

WHITE = (255,255,255)
GREEN = (77,204,0)
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
myfont = pygame.font.SysFont(None, 50)
smaller_font = pygame.font.SysFont(None, 30)


def buildText(board,i,j):
        
    if board[i][j] == "-":        
        text = myfont.render(" ", True, BLUE)
    elif board[i][j] == "O":
        text = myfont.render(board[i][j], True, BLUE)
    elif board[i][j] == "X":
        text = myfont.render(board[i][j], True, BLACK)        
    textRect = text.get_rect()
    textRect.centerx = i*130 + 95
    textRect.centery = j*130 + 195
    return text, textRect


def showText(board):    
    """Display numbers on screen"""
    
    for i in range(3):
        for j in range(3):
            window.blit(buildText(board,i,j)[0], buildText(board,i,j)[1])

def quitWindow(event):
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
    

def win(board, player):
    
    window.fill(WHITE)
    label = myfont.render(checkPlayer(player) + " wins" , True, RED)
    labelRect = label.get_rect()
    labelRect.centerx = window.get_rect().centerx
    labelRect.centery = window.get_rect().centery
    window.blit(label, labelRect) 
    event = pygame.event.wait()
    quitWindow(event)        
    

def gameLoop():

    blocks = []
    for i in range(3):
        for j in range(3):
            blocks.append([pygame.Rect((i*130) + 35 , (j*130) + 135, 120, 120), WHITE])

    board = init_board()
    player = True

    while True:
        
        for event in pygame.event.get():
            quitWindow(event)
            if event.type == KEYDOWN:
                if event.key == K_1:                
                    board, player = main(player, board, 0, 0)
                if event.key == K_2:                
                    board, player = main(player, board, 1, 0)
                if event.key == K_3:                
                    board, player = main(player, board, 2, 0)
                if event.key == K_4:                
                    board, player = main(player, board, 0, 1)
                if event.key == K_5:                
                    board, player = main(player, board, 1, 1)
                if event.key == K_6:                
                    board, player = main(player, board, 2, 1)
                if event.key == K_7:                
                    board, player = main(player, board, 0, 2)
                if event.key == K_8:                
                    board, player = main(player, board, 1, 2)
                if event.key == K_9:                
                    board, player = main(player, board, 2, 2)
                                
               
        window.fill(WHITE)
        header = myfont.render("Tic-Tac-Toe", True, RED)
        player_now = smaller_font.render((checkPlayer(player)), True, BLUE)
        window.blit(player_now,(300, 100))
        window.blit(header, (30, 50))
        pygame.draw.rect(window, BLACK, pygame.Rect(25, 125, 400, 400))
        
        for block in blocks:
            pygame.draw.rect(window, block[1], block[0])

        showText(board)

        if checkWin(board):
            """Even though a player wins, the player has already been toggled
            Thus printing out the player will result in a incorrect player
            winning. NEED FIXING"""
            win(board, not player)
            
        
        pygame.display.update()

        time.sleep(0.02)


gameLoop()
