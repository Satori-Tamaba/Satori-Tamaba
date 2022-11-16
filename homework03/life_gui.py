import pygame
from life import GameOfLife
from pygame.locals import *
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)
        self.speed = speed
        self.cell_size = cell_size
        self.width, self.height = self.life.rows * self.cell_size, self.life.cols * self.cell_size

        self.screen = pygame.display.set_mode((self.width, self.height))

    def draw_lines(self) -> None:
        # Copy from previous assignment
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def draw_grid(self) -> None:
        # Copy from previous assignment
        for row in range(self.life.rows):
            for col in range(self.life.cols):
                value = self.life.curr_generation[row][col]
                color = pygame.Color("green") if value else pygame.Color("white")
                pygame.draw.rect(
                    self.screen,
                    color,
                    pygame.Rect(
                        col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size
                    ),
                )
        return None

    def run(self) -> None:
        # Copy from previous assignment
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        fl_running = True
        is_pause = False
        while fl_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fl_running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        is_pause = not is_pause

                if event.type == pygame.MOUSEBUTTONUP:
                    click_x, click_y = pygame.mouse.get_pos()
                    y, x = click_x // self.cell_size, click_y // self.cell_size
                    self.life.curr_generation[x][y] = 0 if self.life.curr_generation[x][y] else 1

            self.draw_grid()
            self.draw_lines()

            if not is_pause:
                self.life.step()

            if self.life.is_max_generations_exceeded or not self.life.is_changing:
                fl_running = False

            pygame.display.flip()
            clock.tick(self.speed)

        pygame.quit()


game = GameOfLife((15, 15), max_generations=1000)
dui = GUI(game)
dui.run()
