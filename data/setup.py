import pygame
import data.configuration as configuration

pygame.init()
pygame.font.init()

# game variables
timer = pygame.time.Clock()

# create screen
screen = pygame.display.set_mode([configuration.WIDTH, configuration.HEIGHT])
a = 5

# text fonts
font = pygame.font.Font(None, 24)
finish_game_font = pygame.font.Font(None, 28)
