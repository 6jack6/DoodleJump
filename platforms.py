import random
from player import *


class Platfroms:
    def __init__(self):
        self.coords = [[175, 480, 70, 10], [250, 380, 70, 10], [100, 380, 70, 10], [175, 280, 70, 10],
                       [250, 180, 70, 10], [100, 180, 70, 10], [175, 80, 70, 10]]
        self.blocks = []

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, item):
        return self.coords[item]

    # update platforms position on the screen to make the player climb higher
    def update(self, player: Player, points):
        if player.y < HEIGHT / 2 and player.y_change < 0:
            for j in range(len(self.coords)):
                self.coords[j][1] -= player.y_change * 3
        else:
            pass
        for j in range(len(self.coords)):
            if self.coords[j][1] > HEIGHT:
                self.coords[j] = [random.randint(0, WIDTH - 70), random.randint(-50, -10), 70, 10]
                points += 1
        return points

    def draw(self):
        self.blocks = []
        for i in range(len(self.coords)):
            block = pygame.draw.rect(screen, green, self[i])
            self.blocks.append(block)
