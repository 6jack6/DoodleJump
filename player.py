from configuration import *


class Player:
    def __init__(self):
        self.x, self.y = player_start_position
        self.speed = 10
        self.jump = False
        self.y_change = 0
        self.x_change = 0
        self.image = pygame.transform.scale(pygame.image.load("doodle.png"), player_size)

    def update_x_coord(self):
        self.x += self.x_change
        if self.x < -20:
            self.x = -20
        if self.x > WIDTH - 30:
            self.x = WIDTH - 30

    def update_y_coord(self):
        jump_height = 10
        gravity = .3
        if self.jump:
            self.y_change = -jump_height
            self.jump = False
        self.y += self.y_change
        self.y_change += gravity

    # makes player jump if he collides with blocks
    def check_collisions(self, block_list: list):
        for i in range(len(block_list)):
            if block_list[i].colliderect([self.x + 20, self.y + 60, 40, 5])\
                    and (self.jump is not True) and self.y_change > 0:
                self.jump = True
