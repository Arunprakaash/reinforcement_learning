import imageio
import pygame


class Render:
    def __init__(self, state):
        self.CLOCK = None
        self.SCREEN = None
        self.font = None
        self.GRAY_SHADES = [
            (39, 43, 48),
            (34, 40, 49),
            (238, 238, 238),
        ]
        self.BLUE = [
            (0, 172, 181),
            (0, 165, 181),
            (0, 160, 181),
            (0, 155, 181),
            (0, 150, 181)
        ]
        h, w = state.shape
        self.blockSize = 30
        self.WINDOW_HEIGHT = h * self.blockSize
        self.WINDOW_WIDTH = w * self.blockSize
        self.state = state
        self.frames = []
        self.init()

    def init(self):
        pygame.init()
        self.font = pygame.font.SysFont('Courier', 18, bold=True)
        self.SCREEN = pygame.display.set_mode((self.WINDOW_HEIGHT, self.WINDOW_WIDTH))
        self.CLOCK = pygame.time.Clock()
        self.SCREEN.fill(self.GRAY_SHADES[1])

    def draw(self, save_gif=True, is_terminal=False, gif_filename="minesweeper.gif", duration=5, fps=10):
        self.draw_grid()
        pygame.display.update()
        if save_gif:
            self.frames.append(pygame.surfarray.array3d(self.SCREEN))  # Capture frame
            if is_terminal:
                imageio.mimsave(gif_filename, self.frames, duration=1 / fps)
                self.frames = []

    def add_text(self, no, x, y, color):
        self.SCREEN.blit(self.font.render(str(no), True, color), (x, y))
        pygame.display.update()

    def draw_grid(self):
        j = 0
        for column in range(0, self.WINDOW_WIDTH, self.blockSize):
            i = 0
            for row in range(0, self.WINDOW_HEIGHT, self.blockSize):
                if self.state[i][j] == -1:
                    pygame.draw.rect(self.SCREEN, self.GRAY_SHADES[0], [column, row, self.blockSize, self.blockSize])
                if self.state[i][j] == 0:
                    pygame.draw.rect(self.SCREEN, self.GRAY_SHADES[2], [column, row, self.blockSize, self.blockSize])
                elif self.state[i][j] > 0:
                    pygame.draw.rect(self.SCREEN, self.BLUE[0], [column, row, self.blockSize, self.blockSize])
                    self.add_text(self.state[i][j], column + 10, row + 7, self.GRAY_SHADES[2])
                i += 1
            j += 1

    @staticmethod
    def bug_fix():
        return pygame.event.get()
