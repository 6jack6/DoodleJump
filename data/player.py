import data.configuration as configuration
import pygame


class Player:
    def __init__(self):
        self.x, self.y = configuration.player_start_position
        self.speed = 10
        self.jump = False
        self.y_change = 0
        self.x_change = 0
        self.image = pygame.transform.scale(pygame.image.load("resources/images/doodle.png"), configuration.player_size)

    def update_x_coord(self):
        self.x += self.x_change
        if self.x < configuration.LEFT_BORDER:
            self.x = configuration.LEFT_BORDER
        if self.x > configuration.RIGHT_BORDER:
            self.x = configuration.RIGHT_BORDER

    def update_y_coord(self):
        if self.jump:
            self.y_change = -configuration.jump_height
            self.jump = False
        self.y += self.y_change
        self.y_change += configuration.gravity

    # makes player jump if he collides with blocks
    def check_collisions(self, block_list: list):
        player = list(configuration.player_borders)
        player[0] += self.x
        player[1] += self.y
        for i in range(len(block_list)):
            if block_list[i].colliderect(player)\
                    and (self.jump is not True) and self.y_change > 0:
                self.jump = True
