import time

from numpy import int32 as intnp
from numpy import multiply, zeros, add, random, count_nonzero


class MineSweeper:
    def __init__(self, width, height, bomb_no):
        self.bomb_locs = None
        self.state = None
        self.fog = None
        self.grid = None
        self.grid_width = width
        self.grid_height = height
        self.bomb_no = bomb_no
        self.box_count = self.grid_width * self.grid_height
        self.uncovered_count = 0
        self.reset()

    def reset(self):
        self.grid = zeros((self.grid_width, self.grid_height), dtype=intnp)
        self.fog = zeros((self.grid_width, self.grid_height), dtype=intnp)
        self.state = zeros((self.grid_width, self.grid_height), dtype=intnp)
        self.bomb_locs = random.choice(range(self.box_count), self.bomb_no, replace=False)
        self.plant_bombs()
        self.hint_maker()
        self.update_state()
        self.uncovered_count = 0

    def update_state(self):
        self.state = multiply(self.grid, self.fog)
        self.state = add(self.state, (self.fog - 1))

    def plant_bombs(self):
        reordered_bomb_locs = []
        grid_width = self.grid_width
        for bomb_loc in self.bomb_locs:
            row = int(bomb_loc / grid_width)
            col = int(bomb_loc % grid_width)
            self.grid[row][col] = -1
            reordered_bomb_locs.append((row, col))
        self.bomb_locs = reordered_bomb_locs

    def hint_maker(self):
        grid_height = self.grid_height
        grid_width = self.grid_width
        for r, c in self.bomb_locs:
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if i > -1 and j > -1 and i < grid_height and j < grid_width and self.grid[i][j] != -1:
                        self.grid[i][j] += 1

    def choose(self, i, j):

        if self.grid[i][j] == 0:
            unfog_zeros(self.grid, self.fog, i, j)
            self.uncovered_count = count_nonzero(self.fog)
            self.update_state()
            if self.uncovered_count == self.box_count - self.bomb_no:
                return self.state, True, 1
            return self.state, False, 0.5

        elif self.grid[i][j] > 0:
            self.fog[i][j] = 1
            self.uncovered_count = count_nonzero(self.fog)
            self.update_state()
            if self.uncovered_count == self.box_count - self.bomb_no:
                return self.state, True, 1
            return self.state, False, 0.5

        else:
            return self.state, True, -1


def unfog_zeros(grid, fog, i, j):
    h, w = grid.shape
    queue = [(i, j)]
    while len(queue) > 0:
        i, j = queue.pop()
        for r in range(i - 1, i + 2):
            for c in range(j - 1, j + 2):
                if 0 <= r < h and 0 <= c < w:
                    if grid[r][c] == 0 and fog[r][c] == 0:
                        queue.append((r, c))
                    fog[r][c] = 1


def speed_test(iterations):
    start = time.perf_counter()
    for i in range(iterations):
        game = MineSweeper(10, 10, 10)
        game.choose(0, 0)
    end = time.perf_counter() - start
    return end
