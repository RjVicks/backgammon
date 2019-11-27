import pygame
import controller


def main():
    # Point positions

    # initialize the pygame module
    pygame.init()
    # define a variable to control the main loop
    control = controller.Controller()
    # main loop
    running = True
    while running:
        control.make_turn()
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
