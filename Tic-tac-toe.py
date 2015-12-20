import pygame, sys, time, random
from pygame.locals import *
#from moves import *

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

while True:
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    window.fill(WHITE)
    header = myfont.render("Tic-Tac-Toe", True, RED)
    player = smaller_font.render("Player:", True, BLUE)
    window.blit(player,(300, 100))
    window.blit(header, (30, 50))
    pygame.draw.rect(window, BLACK, pygame.Rect(25, 125, 400, 400))
    
    for block in blocks:
        pygame.draw.rect(window, block[1], block[0])
        
    pygame.display.update()

    time.sleep(0.02)
