import pygame
import sys
import scipy.signal as sp
import numpy as np


class Cell:
    """
    Basic cell in the matrix which tracks True/False and color.
    """

    color_map = {True: "BLACK", False: "WHITE"}

    def __init__(self, color="WHITE", val=False) -> None:
        self.color = color
        self.val = val

    def __repr__(self):
        if self.val:
            return "  X  "
        else:
            return "  _  "


class Matrix:
    """
    Performs all the operations related to matrix manipulation.
    """

    def __init__(self, height=800, width=800, rows=40, columns=40) -> None:
        """
        Initialises dimensions, grid, filters and surface to draw.
        """
        """Editable"""
        self.height, self.width = height, width
        self.total_rows, self.total_columns = rows, columns
        self.gap_x, self.gap_y = (
            self.width // self.total_columns,
            self.height // self.total_rows,
        )
        """Non Editable"""
        self.even_matrix = [[False for j in range(columns)] for i in range(rows)]
        self.odd_matrix = [[False for j in range(columns)] for i in range(rows)]
        self.even = True
        self.moore_filter = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        self.von_neumann_filter = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]

        """Display"""
        self.WIN = pygame.display.set_mode((height, width))
        pygame.draw.rect(self.WIN, "WHITE", (0, 0, height, width))

        """Horizontal and vertical lines"""
        for i in range(columns):
            gap = i * self.gap_x
            pygame.draw.line(self.WIN, "BLACK", (gap, 0), (gap, height))
        for i in range(rows):
            gap = i * self.gap_y
            pygame.draw.line(self.WIN, "BLACK", (0, gap), (width, gap))
        pygame.display.update()
        # pygame.draw.line(WIN, "BLACK", (100, 0), (200, 200))

    def get_population(self, generation):
        """
        Returns the population of the world at the given generation.
        """
        return np.sum(self.even_matrix if generation % 2 == 0 else self.odd_matrix)

    def manual_update(self, pos):
        """
        Used when updated with a mouse. Changes Boolean in matrix and draws Rect.
        """
        color_map = {True: "BLACK", False: "WHITE"}
        x = pos[0] // self.gap_x
        y = pos[1] // self.gap_y

        matrix = self.even_matrix if self.even else self.odd_matrix

        matrix[y][x] = not matrix[y][x]
        tile = pygame.draw.rect(
            self.WIN,
            color_map[matrix[y][x]],
            (x * self.gap_x, y * self.gap_y, self.gap_x, self.gap_y),
        )
        pygame.display.update(tile)

    def increment_time_step(self, birth, survival):
        """
        Increments the generation and repopulates the matrix.
        Has 2 matrices which serve as the previous state for each other.
        """
        birth = [int(i) for i in birth]
        survival = [int(i) for i in survival]

        curr_matrix, next_matrix = (
            (self.even_matrix, self.odd_matrix)
            if self.even
            else (self.odd_matrix, self.even_matrix)
        )
        """Creating neighbour matrix directly using scipy for speed."""
        neighbour_matrix = sp.correlate2d(
            curr_matrix, self.moore_filter, mode="same", boundary="wrap"
        )

        """Update rule logic"""
        for i in range(self.total_rows):
            for j in range(self.total_columns):
                neighbours = neighbour_matrix[i][j]

                if neighbours in birth:
                    # print("Birth", neighbours)
                    next_matrix[i][j] = True
                    pygame.draw.rect(
                        self.WIN,
                        "BLACK",
                        (j * self.gap_x, i * self.gap_y, self.gap_x, self.gap_y),
                    )
                elif neighbours in survival:
                    # print("Survival", neighbours)
                    next_matrix[i][j] = curr_matrix[i][j]
                else:
                    next_matrix[i][j] = False
                    # print("Rest", neighbours)
                    pygame.draw.rect(
                        self.WIN,
                        "WHITE",
                        (j * self.gap_x, i * self.gap_y, self.gap_x, self.gap_y),
                    )
        self.even = not self.even

        """Draw lines after every update."""
        for i in range(self.total_columns):
            gap = i * self.gap_x
            pygame.draw.line(self.WIN, "BLACK", (gap, 0), (gap, self.height))
        for i in range(self.total_rows):
            gap = i * self.gap_y
            pygame.draw.line(self.WIN, "BLACK", (0, gap), (self.width, gap))
        pygame.display.update()

    def __repr__(self) -> str:
        result = ""
        for i in range(len(self.matrix)):
            result += "\n"
            for j in range(len(self.matrix[0])):
                result += str(self.matrix[i][j])
        return result


class Cellular_Automation_Model:
    """
    Moore Rules:
    3/23         Game of Life
    2/           Seed
    36/23        High Life
    3678/34678   Day and Night
    35678/5678   Diamoeba
    234/         Persian Rug
    345/5        Long Life

    """

    def __init__(self, birth="2", survival=""):
        # TODO Add von Neumann rules.
        """Editable"""
        self.birth = list(birth)
        self.survival = list(survival)
        self.delta_time = 500

        """Non Editable"""
        self.model_name = "B" + birth + "/S" + survival
        self.grid = Matrix()
        self.generation = 0

        pygame.display.set_caption("Cellular Automata Model " + self.model_name)

    def driver(self):
        """
        Driver Code for the program.
        """
        run = False

        while True:
            pygame.time.delay(self.delta_time)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_q
                ):
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    run = True
                    pygame.display.set_caption(
                        "Cellular Automata Model " + self.model_name
                    )

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # TODO Fix toggle in square color.(Lines aren't redrawn.)
                    pos = pygame.mouse.get_pos()
                    self.grid.manual_update(pos)

                while run:
                    pygame.time.wait(self.delta_time)
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                            run = False
                            pygame.display.set_caption(
                                f"Paused: Generation = {self.generation} | "
                                f"Population = {self.grid.get_population(self.generation)}"
                            )

                    self.grid.increment_time_step(self.birth, self.survival)
                    self.generation += 1


if __name__ == "__main__":
    """
    Click to Toggle Cells.
    Spacebar for start/stop.
    q for Quitting.
    """

    m = Cellular_Automation_Model()

    # m.grid.manual_update((180, 100))
    # m.grid.manual_update((180, 200))
    # m.grid.manual_update((180, 300))

    # m.grid.even_matrix
    # m.grid.odd_matrix

    # m.grid.increment_time_step("3", "23")

    m.driver()