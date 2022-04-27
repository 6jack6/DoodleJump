from platforms import *
from state import *


def check_input(player: Player, state: State):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state.running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.x_change = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and state.game_is_over:
                player.x, player.y = player_start_position
                player.x_change, player.y_change = 0, 0
                state.score = 0
                state.game_is_over = False
            if event.key == pygame.K_LEFT:
                player.x_change = -player.speed
            if event.key == pygame.K_RIGHT:
                player.x_change = player.speed
