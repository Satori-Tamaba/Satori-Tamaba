import pathlib
import random
import typing as tp
from functools import reduce

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: float = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations if max_generations > 0 else float("inf")
        # Теeкущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        return [
            [random.randint(0, 1) if randomize else 0 for _ in range(self.cols)]
            for _ in range(self.rows)
        ]

    def get_cell(self, cell: Cell) -> int:
        return self.curr_generation[cell[0]][cell[1]]

    def get_neighbours(self, cell: Cell) -> Cells:
        neighbours_pos = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        return [
            self.curr_generation[cell[0] + i][cell[1] + j]
            for i, j in neighbours_pos
            if 0 <= cell[0] + i < self.rows and 0 <= cell[1] + j < self.cols
        ]

    def get_next_generation(self) -> Grid:
        new_grid = []
        for i in range(self.rows):
            list = []
            for j in range(self.cols):
                neighbours = self.get_neighbours((i, j))
                if self.curr_generation[i][j]:
                    if sum(neighbours) < 2 or sum(neighbours) > 3:
                        list.append(0)
                    else:
                        list.append(1)
                else:
                    if sum(neighbours) == 3:
                        list.append(1)
                    else:
                        list.append(0)
            new_grid.append(list)
        self.generations += 1
        return new_grid

    def invert_value(self, cell: Cell) -> None:
        self.curr_generation[cell[0]][cell[1]] = 1 - self.curr_generation[cell[0]][cell[1]]

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation, self.curr_generation = (
            self.curr_generation[:],
            self.get_next_generation(),
        )

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        return self.generations >= self.max_generations

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        return self.prev_generation != self.curr_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        with open(filename) as file:
            grid = []
            width = 0
            height = 0
            for i, line in enumerate(file):
                height += 1
                els = list(map(int, line.split()))
                if not width:
                    width = len(els)
                assert len(els) == width, "Неверный ввод! Различная длина строк"
                grid.append(els)
        game = GameOfLife((height, width))
        game.curr_generation = grid
        return game

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        with open(filename, "w") as file:
            file.write(
                "\n".join([" ".join(map(str, self.curr_generation[i])) for i in range(self.rows)])
            )
