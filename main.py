import data.input
import data.platforms
import data.configuration as configuration
import data.state
import data.player
import data.setup as setup
import pygame


# creating a field and a player
pygame.display.set_caption("Doodle Jump")
state = data.state.State()
player = data.player.Player()
platforms = data.platforms.Platforms()


# starting playing
if __name__ == '__main__':
    while state.running:
        setup.timer.tick(configuration.fps)
        setup.screen.fill(configuration.white)
        setup.screen.blit(player.image, (player.x, player.y))

        # printing score and high score
        score_text = setup.font.render("Score " + str(state.score), True, configuration.black)
        setup.screen.blit(score_text, configuration.score_text_position)
        leader_score_text = setup.font.render("High score " + str(state.leader_score), True, configuration.black)
        setup.screen.blit(leader_score_text, configuration.high_score_position)

        platforms.draw()

        # checking input and updating the state
        data.input.check_input(player, state)
        if not state.game_is_over:
            player.check_collisions(platforms.blocks)
            player.update_x_coord()
            player.update_y_coord()
            state.score = platforms.update(player, state.score)

        # check if the game is over and updates the high score
        state.update(player)

        pygame.display.flip()

    pygame.quit()
