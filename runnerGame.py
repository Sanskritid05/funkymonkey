from matplotlib.font_manager import get_font
import pygame
from sys import exit

pygame.init()

# balnk game window (h,w)
screen = pygame.display.set_mode((720, 490))
pygame.display.set_caption("Runner Game")
clock = pygame.time.Clock()
test_font = pygame.font.Font('game_font.ttf', 50)

#images : surface : creation
ground_surf = pygame.image.load('ground2.png') .convert() # convert() :: for efficient use w.r.t pygame  
score_surf = test_font.render('My Game' , False , (64,64,64)).convert()
score_rect = score_surf.get_rect(center = (350, 50))
snail_surf = pygame.image.load('snail(1).png').convert_alpha() # alpha removes unnecessary background
snail_rect = snail_surf.get_rect(topright = (700,330))
player_surf = pygame.image.load('gameCharacter.png').convert_alpha()
player_rect = player_surf.get_rect(topleft = (80, 180))
player_gravity = 0

#game condition
game_active = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active :

            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.collision(event.pos) :
                player_gravity = -25

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE and player_rect.bottom >= 450 :
                        player_gravity = -25     
        else :

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE :
                game_active = True
                snail_rect.left = 800
    
    if game_active : 
        screen.blit(ground_surf, (0, 0)) #sky + ground
        pygame.draw.rect(screen , '#daf0ff' , score_rect)   #color
        pygame.draw.rect(screen , '#daf0ff' , score_rect,1)
        screen.blit(score_surf, score_rect)

        snail_rect.x -= 8 
        if snail_rect.right  <= 0 :
            snail_rect.left = 800

        screen.blit(snail_surf, snail_rect)
        screen.blit(player_surf, player_rect)

        #gravity
        player_gravity += 1 
        player_rect.y += player_gravity

        #fall 
        if player_rect.bottom >= 450 :
            player_rect.bottom = 450
        
        #collision 
        if (snail_rect.colliderect(player_rect)) :
            game_active = False #game over

    else:
        screen.fill('Red')
            

   
    pygame.display.update() 
    
    #speed of snail
    clock.tick(60)

