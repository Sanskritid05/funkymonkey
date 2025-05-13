from matplotlib.font_manager import get_font
import pygame
from sys import exit

pygame.init()

# CHECKPOINT 1 --> Game screen  :: creating balnk window
screen = pygame.display.set_mode((700, 400))
pygame.display.set_caption("Runner Game")
clock = pygame.time.Clock()
test_font = pygame.font.Font('game_font.ttf', 50)

# CHECKPOINT 2 --> Load image :: with multiple surfaces
ground_surface = pygame.image.load('ground2.png') .convert() # convert() :: for efficient use w.r.t pygame  
text_surface = test_font.render('My Game' , False , 'Black').convert() 

snail_surface = pygame.image.load('snail(1).png').convert_alpha() # alpha removes unnecessary background
snail_rectangle = snail_surface.get_rect(topright = (700,280))


player_surface = pygame.image.load('gameCharacter.png').convert_alpha()
player_rectangle = player_surface.get_rect(topleft = (80, 180))

# CHECKPOINT 3 --> Basic animation

# snail character position : animation purpose


# game time condition
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(ground_surface, (0, 0))
    screen.blit(text_surface, (240 , 50))

    # snail animation condition 

    #CHECKPOINT 4 --> Rectangles
    snail_rectangle.x -= 2 
    if snail_rectangle.right  <= 0 :
        snail_rectangle.left = 800

    screen.blit(snail_surface, snail_rectangle)
    screen.blit(player_surface, player_rectangle)


    # print(player_rectangle.left)    # rectangle position 80 from left 
    snail_rectangle.left -= 4 
    

    pygame.display.update()

    #speed of snail
    clock.tick(60)

   
