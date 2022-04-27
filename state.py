from configuration import *


class State:
    def __init__(self):
        self.score = 0
        self.leader_score = 0
        self.game_is_over = False
        self.running = True

    def update(self, player):
        if self.score > self.leader_score:
            self.leader_score = self.score
        if player.y >= HEIGHT - 55:
            player.y = HEIGHT - 55
            finish_game_text = finish_game_font.render("Game over. Press Space to continue", True, black)
            screen.blit(finish_game_text, (WIDTH / 2 - 150, HEIGHT / 2))
            self.game_is_over = True
