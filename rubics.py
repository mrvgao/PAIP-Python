facade = [[], [], []]


class Rubic:


    def __init__(self, facade, facade_north, facade_south, facade_west, facade_east, facade_down):
        self.facade = facade
        self.north = facade_north
        self.south = facade_south
        self.west = facade_west
        self.east = facade_east
        self.width = 3
        self.height = 3
        self.length = 3
        self.one_round = 4
    def rotate_south_north(self):
        for i in range(self.length):
            pass

    def rotate_south_north_one_step(self):
        'for _ in range(self.one_round):'
        pass

    def next_state(self):
        directions = {'south-north', 'west-east', 'plate'}


facade = [[], [], []]
facades = [facade] * 6
