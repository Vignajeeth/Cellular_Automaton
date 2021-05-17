import pygame
import sys


# Move Later
height, width = 800, 800
tot_rows, tot_columns = 20, 20
gap_x, gap_y = width // tot_columns, height // tot_rows
WIN = pygame.display.set_mode((height, width))
delta_time = 125


class Game_Of_Life:
    def __init__(self):
        pass


class Cell:

    color_map = {True: "BLACK", False: "WHITE"}

    def __init__(self, row_no, col_no, color="WHITE", val=False) -> None:
        self.pos_x = int(row_no * gap_x)
        self.pos_y = int(col_no * gap_y)
        self.color = color
        self.val = val

    def draw_cell(self, WIN):
        pygame.draw.rect(
            WIN, self.color, (self.pos_x, self.pos_y, width / 8, height / 8)
        )

    def __repr__(self):
        if self.val:
            return "  X  "
        else:
            return "  _  "


class Matrix:
    def __init__(self) -> None:
        self.matrix = self.create_matrix()

    def create_matrix(self):
        grid = [[Cell(j, i) for j in range(tot_columns)] for i in range(tot_rows)]
        return grid

    def draw_matrix(self, win):
        # gap = width // ROWS
        for i in range(tot_rows):
            pygame.draw.line(win, "BLACK", (0, i * gap_y), (width, i * gap_y))
            for j in range(tot_columns):
                pygame.draw.line(win, "BLACK", (j * gap_x, 0), (j * gap_x, width))

    def update_display(self, win):
        for row in self.matrix:
            for spot in row:
                spot.draw_cell(win)
        self.draw_matrix(win)
        pygame.display.update()

    def neighbour(self, tile):
        col, row = tile.pos_x // gap_x, tile.pos_y // gap_y
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
            if 0 <= row <= (tot_rows - 1) and 0 <= col <= (tot_columns - 1):
                actual.append(i)
        return actual

    def update_grid(self):
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
                    if count in [2, 3]:
                        newgrid.append("BLACK")
                    else:
                        newgrid.append("WHITE")

                else:
                    if count == 3:
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


def driver():
    run = False
    grid = Matrix()

    while True:
        pygame.time.delay(delta_time)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_q
            ):
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                run = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = pos[0] // gap_y, pos[1] // gap_x
                grid.matrix[col][row].val = not grid.matrix[col][row].val
                grid.matrix[col][row].color = grid.matrix[col][row].color_map[
                    grid.matrix[col][row].val
                ]

            while run:
                pygame.time.wait(delta_time)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        run = False
                        # print(grid)

                newcolors = grid.update_grid()
                count = 0
                for i in range(len(grid.matrix)):
                    for j in range(len(grid.matrix[0])):
                        grid.matrix[i][j].color = newcolors[count]
                        count += 1
                grid.update_display(WIN)
            grid.update_display(WIN)


if __name__ == "__main__":
    # Click to Toggle Cells.
    # Spacebar for start/stop.
    # q for Quitting.
    driver()