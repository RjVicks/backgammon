import pygame
import points_gui


class Gui:

    def __init__(self):
        pygame.display.set_caption("Backgammon")
        self.board_img = pygame.image.load("/home/robbie/computer-science/projects/backgammon/gui/imgs/board.png")

        screen_width, screen_height = 980, 480
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.screen.blit(self.board_img, (0, 0))
        pygame.display.flip()
        self.yellow_counter = pygame.image.load(
            "/home/robbie/computer-science/projects/backgammon/gui/imgs/yellow_counter.png")
        self.purple_counter = pygame.image.load(
            "/home/robbie/computer-science/projects/backgammon/gui/imgs/purple_counter.png")
        self.point_coords = points_gui.Points_Gui()

    def get_counter_img(self, player_colour):
        if player_colour == "Yellow":
            return self.yellow_counter
        if player_colour == "Purple":
            return self.purple_counter

    def place(self, player_colour, position):
        counter_img = self.get_counter_img(player_colour)
        counter_coordinates = self.point_coords.get_position(position)
        counter_rect = self.screen.blit(counter_img, counter_coordinates)
        pygame.display.update(counter_rect)

    def remove(self, position):
        counter_coordinates = self.point_coords.get_position(position)
        counter_rect = pygame.Rect(counter_coordinates, (42, 42))
        self.screen.blit(self.board_img, counter_rect, counter_rect)
        pygame.display.update(counter_rect)

    def move(self, player_colour, start_position, end_position):
        self.remove(start_position)
        self.place(player_colour, end_position)
