# import the pygame module, so you can use it
import pygame

# define a main function


def load_board():
    # load and set the image
    board = pygame.image.load("board.png")
    pygame.display.set_caption("Backgammon")

    # create a surface
    screen_width, screen_height = 980, 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.blit(board, (0, 0))
    pygame.display.flip()
    return board, screen


def get_point_coordx(index):
    POINT_X_POSITIONS = [63, 131, 199, 265, 335, 405]
    return POINT_X_POSITIONS[index]


def get_point_coordy(height):
    return 24 + (height * 48)


def main():
    # Point positions

    # initialize the pygame module
    pygame.init()
    board, screen = load_board()
    counter = pygame.image.load("counter48.png")
    # define a variable to control the main loop
    running = True

    # add the counter to point 0
    for i in range(5):
        screen.blit(counter, (get_point_coordx(i), get_point_coordy(0))
    screen.blit(counter, (528, get_point_coordy(0)))
    screen.blit(counter, (596, get_point_coordy(0)))
    screen.blit(counter, (664, get_point_coordy(0)))
    screen.blit(counter, (732, get_point_coordy(0)))
    screen.blit(counter, (800, get_point_coordy(0)))
    screen.blit(counter, (868, get_point_coordy(0)))

    pygame.display.flip()
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():

            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running=False


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
