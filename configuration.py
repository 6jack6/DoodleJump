import pygame

pygame.init()
pygame.font.init()

# library of game const

# colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (128, 255, 128)

# screen parameters
WIDTH = 400
HEIGHT = 500
fps = 60

# player constants
player_size = (85, 70)
player_start_position = WIDTH / 2 - 40, HEIGHT / 2

# text fonts
font = pygame.font.Font(None, 24)
finish_game_font = pygame.font.Font(None, 28)

# game variables
timer = pygame.time.Clock()

# create screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Doodle Jump")
