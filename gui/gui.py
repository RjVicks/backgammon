import pygame
import points_gui


class Gui:

    def __init__(self):
        pygame.display.set_caption("Backgammon")
        self.board_img = pygame.image.load("board.png")

        screen_width, screen_height = 980, 480
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.screen.blit(self.board_img, (0, 0))
        pygame.display.flip()
        self.yellow_counter = pygame.image.load("yellow_counter.png")
        self.purple_counter = pygame.image.load("purple_counter.png")
        self.point_coords = points_gui.Points_Gui()
        self.counter_rect = 0

    def place(self, counter, position):
        self.counter_rect = self.screen.blit(counter, self.point_coords.get_position(position))
        pygame.display.update(self.counter_rect)

    def remove(self, position_rect):
        self.screen.blit(self.board_img, position_rect, position_rect)
        pygame.display.update(position_rect)

    def move(self, counter, initial, to):
        self.remove(self.counter_rect)
        self.place(counter, to)


def main():
    # Point positions

    # initialize the pygame module
    pygame.init()
    gui = Gui()
    # define a variable to control the main loop

    # add the counter to point 0

    gui.place(gui.yellow_counter, (1, 1))
    pygame.time.delay(500)
    gui.move(gui.yellow_counter, (1, 1), (2, 1))

    # main loop
    running = True
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():

            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
