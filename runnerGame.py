from matplotlib.font_manager import get_font
import pygame
from sys import exit

pygame.init()

# Game screen  
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner Game")
clock = pygame.time.Clock()
test_font = pygame.font.Font()

# Load image 
ground_surface = pygame.image.load('ground.png')  
# text_surface = pygame.image.load('My Game' , False , 'Black') 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(ground_surface, (0, 0))
    # screen.blit(text_surface, (300 , 50))
    pygame.display.update()
    clock.tick(60)
