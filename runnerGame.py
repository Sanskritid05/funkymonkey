from matplotlib.font_manager import get_font
import pygame
from sys import exit
from random import randint

def display_score():
    global current_time
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = test_font.render(f'Score : {current_time}', False , (64, 64, 64))
    score_rect = score_surf.get_rect(center = (350, 50))
    screen.blit(score_surf, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            screen.blit(snail_surf, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else :
        return []


pygame.init()

# balnk game window (h,w)
screen = pygame.display.set_mode((720, 490))
pygame.display.set_caption("Runner Game")
clock = pygame.time.Clock()
test_font = pygame.font.Font('game_font.ttf', 50)
game_active = False
start_time = 0 
score = 0 


#images : surface : creation
ground_surf = pygame.image.load('ground2.png') .convert() # convert() :: for efficient use w.r.t pygame  
# score_surf = test_font.render('My Game' , False , (64,64,64)).convert()
# score_rect = score_surf.get_rect(center = (350, 50))

snail_surf = pygame.image.load('snail(1).png').convert_alpha() # alpha removes unnecessary background
snail_rect = snail_surf.get_rect(topright = (randint(900, 1100),330))
fly_surf = pygame.image.load('bird.png')


obstacle_rect_list = []


player_surf = pygame.image.load('gameCharacter.png').convert_alpha()
player_rect = player_surf.get_rect(topleft = (80, 180))

player_gravity = 0

#intro screen
player_stand  = pygame.image.load('gameCharacter.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0 , 1)
player_stand_rect = player_stand.get_rect(center = (350, 230))

game_name = test_font.render('Run Lola Run' , False , (64, 64, 64)).convert()
game_name_rect = game_name.get_rect(center = (350 , 100))

game_message = test_font.render('Press <SPACE> to Run' , False , (64, 64, 64)).convert()
game_message_rect = game_message.get_rect(center = (350 , 400))


#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer , 1300)

#game condition

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
        else:

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE :
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

        if event.type == obstacle_timer and game_active:
            if randint(0, 2) : 
                obstacle_rect_list.append(snail_surf.get_rect(topright = (randint(900, 1100),330)))
            else :
                obstacle_rect_list.append(snail_surf.get_rect(topright = (randint(900, 1100),110)))

    
    if game_active : 
        screen.blit(ground_surf, (0, 0)) #sky + ground
        # pygame.draw.rect(screen , '#daf0ff' , score_rect)   #color
        # pygame.draw.rect(screen , '#daf0ff' , score_rect,1)
        # screen.blit(score_surf, score_rect)
        score = display_score()

        # # snail_rect.x -= 8 
        # snail_rect.x -= 6 + score // 5 #speed inc by 1 every 10 seconds
        # if snail_rect.right  <= 0 :
        #     snail_rect.left = 800

        screen.blit(snail_surf, snail_rect)
        screen.blit(player_surf, player_rect)

        #player
        player_gravity += 1 
        player_rect.y += player_gravity

        #obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #fall 
        if player_rect.bottom >= 450 :
            player_rect.bottom = 450
        
        #collision 
        if (snail_rect.colliderect(player_rect)) :
            game_active = False #game over

    else:
        screen.fill((94, 129, 164))  
        screen.blit(player_stand, player_stand_rect)

        score_message = test_font.render(f'Your Score :{score}' , False , (64, 64, 64))
        score_message_rect = score_message.get_rect(center = (350 , 400))
        screen.blit(game_name , game_name_rect)

        if score == 0 :
            screen.blit(game_message, game_message_rect)
        else :
            screen.blit(score_message, score_message_rect)

            
    pygame.display.update() 
    
    #speed of snail
    clock.tick(110)

