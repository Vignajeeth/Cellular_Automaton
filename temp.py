import pygame
import sys
import numpy as np

# a=pygame.draw.rect(WIN, "RED", (10, 20, 30, 40))

# 10 distance from left
# 20 distance from top
# 30 width left
# 40 height top


height, width = 800, 800
WIN = pygame.display.set_mode((height, width))
tot_rows, tot_columns = 80, 40
gap_x, gap_y = (width // tot_columns, height // tot_rows)


class Cell:

    color_map = {True: "BLACK", False: "WHITE"}

    def __init__(self, row_no, col_no, color="WHITE", val=False) -> None:
        self.pos_x = int(row_no * gap_x)
        self.pos_y = int(col_no * gap_y)
        self.color = color
        self.val = val

    def draw_cell(self, WIN):
        pygame.draw.rect(WIN, self.color, (self.pos_x, self.pos_y, gap_x, gap_y))

    def __repr__(self):
        if self.val:
            return "  X  "
        else:
            return "  _  "


class Matrix:
    def __init__(self, height=800, width=800) -> None:
        self.matrix = self.create_matrix()
        self.height, self.width = height, width
        self.tot_rows, self.tot_columns = 80, 40

        self.gap_x, self.gap_y = (
            self.width // self.tot_columns,
            self.height // self.tot_rows,
        )

    def create_matrix(self):
        grid = [[Cell(j, i) for j in range(tot_columns)] for i in range(tot_rows)]
        return grid

    def draw_matrix(self, win):
        # gap = width // ROWS
        for i in range(self.tot_rows):
            pygame.draw.line(
                win, "BLACK", (0, i * self.gap_y), (self.width, i * self.gap_y)
            )
            for j in range(self.tot_columns):
                pygame.draw.line(
                    win, "BLACK", (j * self.gap_x, 0), (j * self.gap_x, self.width)
                )

    def update_display(self, win):
        for row in self.matrix:
            for spot in row:
                spot.draw_cell(win)
        self.draw_matrix(win)
        pygame.display.update()

    # Change here
    def neighbour(self, tile):
        col, row = tile.pos_x // self.gap_x, tile.pos_y // self.gap_y
        neighbours = [
            [row - 1, col - 1],
            [row - 1, col],
            [row - 1, col + 1],
            [row, col - 1],
            [row, col + 1],
            [row + 1, col - 1],
            [row + 1, col],
            [row + 1, col + 1],
        ]
        actual = []
        for i in neighbours:
            row, col = i
            if 0 <= row <= (self.tot_rows - 1) and 0 <= col <= (self.tot_columns - 1):
                actual.append(i)
        return actual

    # Change here
    def update_grid(self, birth, survival):
        birth = [int(i) for i in birth]
        survival = [int(i) for i in survival]
        newgrid = []
        for row in self.matrix:
            for tile in row:
                neighbours = self.neighbour(tile)
                count = 0
                for i in neighbours:
                    row, col = i
                    if self.matrix[row][col].color == "BLACK":
                        count += 1

                if tile.color == "BLACK":
                    if count in survival:
                        newgrid.append("BLACK")
                    else:
                        newgrid.append("WHITE")

                else:
                    if count in birth:
                        newgrid.append("BLACK")
                    else:
                        newgrid.append("WHITE")

        return newgrid

    def __repr__(self) -> str:
        result = ""
        for i in range(len(self.matrix)):
            result += "\n"
            for j in range(len(self.matrix[0])):
                result += str(self.matrix[i][j])
        return result


class Cellular_Automation_Model:
    def __init__(self, birth="2", survival=""):
        self.birth = list(birth)
        self.survival = list(survival)
        self.model_name = "B" + birth + "/S" + survival
        self.grid = Matrix()
        self.delta_time = 10

        pygame.display.set_caption("Cellular Automata Model " + self.model_name)

    def driver(self):
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
                    pos = pygame.mouse.get_pos()
                    col, row = pos[0] // gap_x, pos[1] // gap_y
                    self.grid.matrix[row][col].val = not self.grid.matrix[row][col].val
                    self.grid.matrix[row][col].color = self.grid.matrix[row][
                        col
                    ].color_map[self.grid.matrix[row][col].val]

                while run:
                    pygame.time.wait(self.delta_time)
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                            run = False
                            pygame.display.set_caption("Paused")
                            # print(grid)
                    # Change here
                    newcolors = self.grid.update_grid(self.birth, self.survival)
                    count = 0
                    for i in range(len(self.grid.matrix)):
                        for j in range(len(self.grid.matrix[0])):
                            self.grid.matrix[i][j].color = newcolors[count]
                            count += 1
                    self.grid.update_display(WIN)
                self.grid.update_display(WIN)


if __name__ == "__main__":
    # Click to Toggle Cells.
    # Spacebar for start/stop.
    # q for Quitting.
    m = Cellular_Automation_Model()
    m.driver()