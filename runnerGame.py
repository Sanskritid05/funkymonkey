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

ground_surf = pygame.image.load('ground2.png') .convert() # convert() :: for efficient use w.r.t pygame  


score_surf = test_font.render('My Game' , False , 'Black').convert()
score_rect = score_surf.get_rect(center = (350, 50))


snail_surf = pygame.image.load('snail(1).png').convert_alpha() # alpha removes unnecessary background
snail_rect = snail_surf.get_rect(topright = (700,280))


player_surf = pygame.image.load('gameCharacter.png').convert_alpha()
player_rect = player_surf.get_rect(topleft = (80, 180))

# CHECKPOINT 3 --> Basic animation

# snail character position : animation purpose


# game time condition
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     print(event.pos)        # prints mouse pos (x,y)
        # if event.type == pygame.MOUSEBUTTONDOWN :
        #     print("Button Down")      # prints when button pressed

        # if event.type == pygame.MOUSEBUTTONUP:
        #     print("Button up")        # prints when button release

        # if event.type == pygame.MOUSEMOTION :
        #     if player_rect.collidepoint(event.pos) :
        #         print("Collision")          # prints when above the player character


    screen.blit(ground_surf, (0, 0))
    #CHECKPOINT 5 --> Drawing with Rectangles

    #draw module
    pygame.draw.rect(screen , 'Pink' , score_rect)
    pygame.draw.rect(screen , 'Pink' , score_rect , 15)
    pygame.draw.ellipse(screen , 'Brown' , pygame.Rect( ))



    screen.blit(score_surf, score_rect)

    # snail animation condition 

    #CHECKPOINT 4 --> Rectangles       ::  for positioning and collisions

    snail_rect.x -= 2 
    if snail_rect.right  <= 0 :
        snail_rect.left = 800

    screen.blit(snail_surf, snail_rect)
    screen.blit(player_surf, player_rect)

    #CHECKPOINT 5 --> Collision with Rectangle 
    # if player_rect.colliderect(snail_rect) :
    #     print("collision")

    #CHECKPOINT 6 --> Collide Points
    mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos) :
    #     print(pygame.mouse.get_pressed())


    # print(player_rect.left)    # rectangle position 80 from left 
    snail_rect.left -= 4 
    

    pygame.display.update()

    #speed of snail
    clock.tick(60)

   
