import consts
from cell import Cell
# from snake import Snake

from math import inf, fabs


class GameManager:

    def __init__(self, size, screen, sx, sy, block_cells):
        self.table_size = size
        self.screen = screen
        self.sx = sx
        self.sy = sy
        self.block_cells = block_cells
        self.cells = list()
        self.snakes = list()
        self.turn = 1
        for i in range(size):
            self.cells.append(
                [Cell(screen, sx + i * consts.cell_size, sy + j * consts.cell_size) for j in range(size)])
        for block_cell in block_cells:
            self.get_cell(block_cell).set_color(consts.block_color)

    def add_snake(self, snake):
        self.snakes.append(snake)

    def get_cell(self, pos):
        x = pos[0]
        y = pos[1]
        return self.cells[y][x] if 0 <= x < self.table_size and 0 <= y < self.table_size else None

    def kill(self, killed_snake):
        for i in range(len(self.snakes)):
            if self.snakes[i].__eq__(killed_snake):
                self.snakes.pop(i)
                break

    def handle(self, keys):
        for snake in self.snakes:
            for key in keys:
                if snake.keys.__contains__(key):
                    snake.handle(key)
                    break

        for snake in self.snakes:
            snake.next_move()

        self.turn += 1
        if self.turn % 10 == 0:
            empty = []
            full = []
            for i in range(self.table_size):
                for j in range(self.table_size):
                    if self.cells[i][j].color == consts.back_color:
                        empty.append((i, j))
                    else:
                        full.append((i, j))
            manhhatan_dictance = []
            for em in empty:
                dic = inf
                for fu in full:
                    if fabs(em[0] - fu[0]) + fabs(em[1] - fu[1]) < dic:
                        dic = fabs(em[0] - fu[0]) + fabs(em[1] - fu[1])
                manhhatan_dictance.append((em[0], em[1], dic))

            mymax = manhhatan_dictance[0][2], 0
            for i in range(1, len(manhhatan_dictance)):
                if manhhatan_dictance[i][2] > mymax[0]:
                    mymax = manhhatan_dictance[i][2], i

            index = mymax[1]
            row, col = manhhatan_dictance[index][0], manhhatan_dictance[index][1]
            self.cells[row][col].set_color(consts.fruit_color)
