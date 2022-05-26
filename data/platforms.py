import random
import data.player as player
import pygame
import data.configuration as configuration
import data.setup as setup


class Platforms:
    def __init__(self):
        self.coords = [[175, 480, 70, 10], [250, 380, 70, 10], [100, 380, 70, 10], [175, 280, 70, 10],
                       [250, 180, 70, 10], [100, 180, 70, 10], [175, 80, 70, 10]]
        self.blocks = []

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, item):
        return self.coords[item]

    # update platforms position on the screen to make the player climb higher
    def update(self, doodle: player.Player, points):
        if doodle.y < configuration.HEIGHT / 2 and doodle.y_change < 0:
            for j in range(len(self.coords)):
                self.coords[j][1] -= doodle.y_change * 3
        else:
            pass
        for j in range(len(self.coords)):
            if self.coords[j][1] > configuration.HEIGHT:
                self.coords[j] = [random.randint(configuration.spawn_x1_range, configuration.spawn_x2_range),
                                  random.randint(configuration.spawn_y1_range, configuration.spawn_y2_range),
                                  configuration.platform_width, configuration.platform_height]
                points += 1
        return points

    def draw(self):
        self.blocks = []
        for i in range(len(self)):
            block = pygame.draw.rect(setup.screen, configuration.green, tuple(self.coords[i]))
            self.blocks.append(block)
