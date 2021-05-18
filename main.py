import pygame
import sys
import scipy.signal as sp

# TODO Clean Code up


class Cell:
    """
    Useless as of now.
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
    def __init__(self, height=800, width=800, rows=40, columns=40) -> None:
        self.height, self.width = height, width
        self.total_rows, self.total_columns = rows, columns
        self.gap_x, self.gap_y = (
            self.width // self.total_columns,
            self.height // self.total_rows,
        )
        # Class Cell is not used. May require later.
        self.even_matrix = [[False for j in range(columns)] for i in range(rows)]
        self.odd_matrix = [[False for j in range(columns)] for i in range(rows)]
        self.even = True

        self.WIN = pygame.display.set_mode((height, width))
        pygame.draw.rect(self.WIN, "WHITE", (0, 0, height, width))
        for i in range(columns):
            gap = i * self.gap_x
            pygame.draw.line(self.WIN, "BLACK", (gap, 0), (gap, height))
        for i in range(rows):
            gap = i * self.gap_y
            pygame.draw.line(self.WIN, "BLACK", (0, gap), (width, gap))
        pygame.display.update()
        # pygame.draw.line(WIN, "BLACK", (100, 0), (200, 200))

    def manual_update(self, pos):
        """
        Used when updated with a mouse.
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
        Used for incrementing the time step and changing matrices.
        """
        birth = [int(i) for i in birth]
        survival = [int(i) for i in survival]
        filter = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        curr_matrix, next_matrix = (
            (self.even_matrix, self.odd_matrix)
            if self.even
            else (self.odd_matrix, self.even_matrix)
        )
        neighbour_matrix = sp.correlate2d(
            curr_matrix, filter, mode="same", boundary="wrap"
        )
        for i in range(self.total_rows):
            for j in range(self.total_columns):
                # neighbours = (
                #     np.sum(curr_matrix[i - 1 : i + 2][j - 1 : j + 2])
                #     - curr_matrix[i][j]
                # )

                # if i == self.total_rows - 1 and j == self.total_columns - 1:
                #     neighbours = (
                #         curr_matrix[i - 1][j - 1]
                #         + curr_matrix[i][j - 1]
                #         + curr_matrix[i - 1][j]
                #         + curr_matrix[i][0]
                #         + curr_matrix[i - 1][0]
                #         + curr_matrix[0][j]
                #         + curr_matrix[0][j - 1]
                #         + curr_matrix[0][0]
                #     )
                # elif i == self.total_rows - 1:
                #     neighbours = (
                #         curr_matrix[i - 1][j - 1]
                #         + curr_matrix[i][j - 1]
                #         + curr_matrix[0][j - 1]
                #         + curr_matrix[i - 1][j]
                #         + curr_matrix[0][j]
                #         + curr_matrix[i - 1][j + 1]
                #         + curr_matrix[i][j + 1]
                #         + curr_matrix[0][j + 1]
                #     )

                # elif j == self.total_columns - 1:
                #     neighbours = (
                #         curr_matrix[i - 1][j - 1]
                #         + curr_matrix[i][j - 1]
                #         + curr_matrix[i + 1][j - 1]
                #         + curr_matrix[i - 1][j]
                #         + curr_matrix[i + 1][j]
                #         + curr_matrix[i - 1][0]
                #         + curr_matrix[i][0]
                #         + curr_matrix[i + 1][0]
                #     )

                # else:
                #     neighbours = (
                #         curr_matrix[i - 1][j - 1]
                #         + curr_matrix[i][j - 1]
                #         + curr_matrix[i + 1][j - 1]
                #         + curr_matrix[i - 1][j]
                #         + curr_matrix[i + 1][j]
                #         + curr_matrix[i - 1][j + 1]
                #         + curr_matrix[i][j + 1]
                #         + curr_matrix[i + 1][j + 1]
                #     )
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
    B3/S23         Game of Life
    B2/S           Seed
    B36/S23        High Life
    B3678/S34678   Day and Night
    B35678/S5678   Diamoeba
    B234/S         Persian Rug
    B345/S5        Long Life

    """

    def __init__(self, birth="3", survival="23"):
        # TODO Add von Neumann rules.
        # TODO Add Generation Count
        # TODO Add Population Count
        self.birth = list(birth)
        self.survival = list(survival)
        self.model_name = "B" + birth + "/S" + survival
        self.grid = Matrix()
        self.delta_time = 10

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
                            pygame.display.set_caption("Paused")

                    self.grid.increment_time_step(self.birth, self.survival)


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