class Points_Gui:

    def __init__(self):
        self.x_positions = [66, 134, 202, 268, 338, 408, 531, 599, 667, 735, 803, 871]
        self.bench = 24
        self.far_bench = 456

    def get_position(self, index, height):
        if index >= 12:
            x_pos = self.x_positions[23-index]
            y_pos = self.far_bench - (42 * height)
        else:
            x_pos = self.x_positions[index]
            y_pos = self.bench + (42 * (height - 1))

        return x_pos, y_pos
