import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((720, 490))
pygame.display.set_caption("Runner Game")
clock = pygame.time.Clock()
test_font = pygame.font.Font('game_font.ttf', 50)

# Images and Surfaces
ground_surf = pygame.image.load('ground2.png').convert()
score_surf = test_font.render('My Game', False, (64, 64, 64)).convert()
score_rect = score_surf.get_rect(center=(350, 50))
snail_surf = pygame.image.load('snail(1).png').convert_alpha()
snail_rect = snail_surf.get_rect(topright=(700, 280))
player_surf = pygame.image.load('gameCharacter.png').convert_alpha()
player_rect = player_surf.get_rect(topleft=(80, 180))

player_gravity = 0
ground_level = 300

# Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Keyboard input for jump
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= ground_level:
                player_gravity = -25

        # Optional: Mouse input
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if player_rect.collidepoint(event.pos):
        #         player_gravity = -25

    # Draw background and UI
    screen.blit(ground_surf, (0, ground_level))
    pygame.draw.rect(screen, '#daf0ff', score_rect)
    pygame.draw.rect(screen, '#daf0ff', score_rect, 1)
    screen.blit(score_surf, score_rect)

    # Snail movement
    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)

    # Player movement with gravity
    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= ground_level:
        player_rect.bottom = ground_level
        player_gravity = 0
    screen.blit(player_surf, player_rect)

    # Mouse Position (optional use)
    mouse_pos = pygame.mouse.get_pos()

    pygame.display.update()
    clock.tick(60)
