import pygame
import data.state as state
import data.player as player
import data.configuration as configuration


def check_input(doodle: player.Player, field_state: state.State):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            field_state.running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                doodle.x_change = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and field_state.game_is_over:
                doodle.x, doodle.y = configuration.player_start_position
                doodle.x_change, doodle.y_change = 0, 0
                field_state.score = 0
                field_state.game_is_over = False
            if event.key == pygame.K_LEFT:
                doodle.x_change = -doodle.speed
            if event.key == pygame.K_RIGHT:
                doodle.x_change = doodle.speed
