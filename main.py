from input import *


state = State()
player = Player()
platforms = Platfroms()

# starting playing

while state.running:
    timer.tick(fps)
    screen.fill(white)
    screen.blit(player.image, (player.x, player.y))

    # printing score and high score
    score_text = font.render("Score " + str(state.score), True, black)
    screen.blit(score_text, (10, 10))
    leader_score_text = font.render("High score " + str(state.leader_score), True, black)
    screen.blit(leader_score_text, (WIDTH - 110, 10))

    platforms.draw()

    # checking input and updating the state
    check_input(player, state)
    if not state.game_is_over:
        player.check_collisions(platforms.blocks)
        player.update_x_coord()
        player.update_y_coord()
        state.score = platforms.update(player, state.score)

    # check if the game is over and updates the high score
    state.update(player)

    pygame.display.flip()

pygame.quit()
