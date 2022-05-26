import data.configuration as configuration
import data.setup as setup


class State:
    def __init__(self):
        self.score = 0
        self.leader_score = 0
        self.game_is_over = False
        self.running = True

    def update(self, player):
        if self.score > self.leader_score:
            self.leader_score = self.score
        if player.y >= configuration.HEIGHT - 55:
            player.y = configuration.HEIGHT - 55
            finish_game_text = setup.finish_game_font.render("Game over. Press Space to continue",
                                                             True, configuration.black)
            setup.screen.blit(finish_game_text, (configuration.WIDTH / 2 - 150, configuration.HEIGHT / 2))
            self.game_is_over = True
