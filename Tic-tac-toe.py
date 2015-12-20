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

blocks = []
for i in range(3):
    for j in range(3):
        blocks.append([pygame.Rect((i*130) + 35 , (j*130) + 135, 120, 120), WHITE])


def buildText(board,i,j):
        
    if board[j][i] == "-":        
        text = myfont.render(" ", True, BLUE)
    else:
        text = myfont.render(board[j][i], True, BLUE)
    textRect = text.get_rect()
    textRect.centerx = i*130 + 95
    textRect.centery = j*130 + 195
    return text, textRect


def showText(board):    
    """Display numbers on screen"""
    
    for i in range(3):
        for j in range(3):
            window.blit(buildText(board,i,j)[0], buildText(board,i,j)[1])

while True:
    
    board = init_board()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    window.fill(WHITE)
    header = myfont.render("Tic-Tac-Toe", True, RED)
    player = smaller_font.render((checkPlayer(True)), True, BLUE)
    window.blit(player,(300, 100))
    window.blit(header, (30, 50))
    pygame.draw.rect(window, BLACK, pygame.Rect(25, 125, 400, 400))
    
    for block in blocks:
        pygame.draw.rect(window, block[1], block[0])



    

    showText(board)
        
    pygame.display.update()

    time.sleep(0.02)
