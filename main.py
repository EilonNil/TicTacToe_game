import pygame
import game_functions.summoning_pieces.summon_cross
import game_functions.summoning_pieces.summon_circle
import game_functions.check_win


def main():
    IMAGE = 'images\\board.png'
    BOARD_SIZE = 360

    # making of the board
    pygame.init()
    size = (BOARD_SIZE, BOARD_SIZE)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Tic Tac Toe")
    img = pygame.image.load(IMAGE)
    screen.fill((255, 255, 255))  # the behind of the board is transparent so i will need to set the background as 
    # white for the black lines to be visible 
    screen.blit(img, (0, 0))
    pygame.display.flip()
    game(screen)  # starting the game


def game(screen):  # function that runs the main game itself
    POSITIONS = {'11': (3, 3), '12': (128, 3), '13': (248, 3),
                 '21': (3, 128), '22': (128, 128), '23': (248, 128),
                 '31': (3, 248), '32': (128, 248), '33': (248, 248)}
    # dictionary that will show where to place each  marker
    REFRESH_RATE = 60
    placements = [[6, 7, 8], [9, 10, 11], [12, 13, 14]]
    # will be changed, keeps track of the placed crosses and circles. numbers are different so checkWin() does not
    # automatically trigger at the start of the game
    count = 0
    clock = pygame.time.Clock()
    finish = False
    cross_turn = True  # check to see who's turn is it
    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                if cross_turn:
                    good_placement = game_functions.summoning_pieces.summon_cross.summon_x(screen, x, y, POSITIONS, placements)
                    if good_placement == 1:
                        count += 1
                        if game_functions.check_win.check_if_win(placements):
                            finish = True
                            print("Crosses win!")
                        elif count == 9:
                            print("Tie match, no player won!")
                            finish = True
                        cross_turn = False
                else:
                    good_placement = game_functions.summoning_pieces.summon_circle.summon_c(screen, x, y, POSITIONS, placements)
                    if good_placement == 1:
                        count += 1
                        if game_functions.check_win.check_if_win(placements):
                            finish = True
                            print("Circles win!")
                        cross_turn = True
        pygame.display.flip()
        clock.tick(REFRESH_RATE)


if __name__ == '__main__':
    main()
