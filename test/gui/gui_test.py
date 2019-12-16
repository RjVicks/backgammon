import gui
import pygame

pygame.init()

ui = gui.Gui()
yellow_player = "Yellow"
ui.place(yellow_player, (1, 1))
pygame.time.delay(1000)
ui.move(yellow_player, (1, 1), (3, 1))
pygame.time.delay(1000)
ui.move(yellow_player, (3, 1), (24, 3))


running = True
while running:
    # event handling, gets all event from the event queue
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False
