# from game_manager import GameManager
import consts


class Snake:

    def __init__(self, keys, game, pos, color, direction):
        self.keys = keys
        self.game = game
        self.color = color
        self.direction = str(direction)
        self.cells = [pos]
        self.game.get_cell(pos).set_color(color)
        self.game.add_snake(self)

    def get_head(self):
        return self.cells[len(self.cells) - 1]

    def next_move(self):
        pos = self.cells[len(self.cells)-1]
        row = pos[0]
        col = pos[1]
        new_pos = (
            row - 1 if self.direction == 'UP' else row + 1 if self.direction == 'DOWN' else row,
            col - 1 if self.direction == 'LEFT' else col + 1 if self.direction == 'RIGHT' else col
        )
        if new_pos[0] == -1:
            new_pos = (consts.table_size - 1, new_pos[1])
        if new_pos[0] == consts.table_size:
            new_pos = (0, new_pos[1])

        if new_pos[1] == -1:
            new_pos = (new_pos[0], consts.table_size - 1)
        if new_pos[1] == consts.table_size:
            new_pos = (new_pos[0], 0)

        if self.game.get_cell(new_pos).color == consts.back_color:
            self.cells.append(new_pos)
            self.game.get_cell(new_pos).set_color(self.color)
            self.game.get_cell(self.cells.pop(0)).set_color(consts.back_color)
            return

        if self.game.get_cell(new_pos).color == consts.fruit_color:
            self.cells.append(new_pos)
            self.game.get_cell(new_pos).set_color(self.color)
            return

        self.game.kill(self)

    def handle(self, key):
        direction = self.direction
        new_direction = str(self.keys[key])
        if direction.__eq__('LEFT') and new_direction.__eq__('RIGHT') \
                or direction.__eq__('RIGHT') and new_direction.__eq__('LEFT') \
                or direction.__eq__('UP') and new_direction.__eq__('DOWN') \
                or direction.__eq__('DOWN') and new_direction.__eq__('UP'):
            return
        self.direction = new_direction

    def __eq__(self, other):
        return self.cells == other.cells
