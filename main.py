import pygame
import sys


# Move Later
height, width = 800, 800
tot_rows, tot_columns = 20, 20
gap_x, gap_y = width // tot_columns, height // tot_rows
WIN = pygame.display.set_mode((height, width))


class Game_Of_Life:
    def __init__(self):
        pass


class Cell:
    def __init__(self, row_no, col_no, colour="WHITE", val=False) -> None:
        self.pos_x = int(row_no * gap_x)
        self.pos_y = int(col_no * gap_y)
        self.colour = colour
        self.val = val

    def draw_cell(self, WIN):
        pygame.draw.rect(
            WIN, self.colour, (self.pos_x, self.pos_y, width / 8, height / 8)
        )


class Matrix:
    def __init__(self) -> None:
        self.matrix = self.create_matrix()

    def create_matrix(self):
        grid = []
        for i in range(tot_rows):
            grid.append([])
            for j in range(tot_columns):
                node = Cell(j, i)
                grid[i].append(node)
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
                    if self.matrix[row][col].colour == "BLACK":
                        count += 1

                if tile.colour == "BLACK":
                    if count == 2 or count == 3:
                        newgrid.append("BLACK")
                    else:
                        newgrid.append("WHITE")

                else:
                    if count == 3:
                        newgrid.append("BLACK")
                    else:
                        newgrid.append("WHITE")

        return newgrid


def driver():
    run = None
    grid = Matrix()

    while True:
        pygame.time.delay(125)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                run = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = pos[0] // gap_y, pos[1] // gap_x
                if grid.matrix[col][row].colour == "WHITE":
                    grid.matrix[col][row].colour = "BLACK"

                elif grid.matrix[col][row].colour == "BLACK":
                    grid.matrix[col][row].colour = "WHITE"

            while run:
                pygame.time.wait(250)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        run = False

                newcolours = grid.update_grid()
                count = 0
                for i in range(len(grid.matrix)):
                    for j in range(len(grid.matrix[0])):
                        grid.matrix[i][j].colour = newcolours[count]
                        count += 1
                grid.update_display(WIN)
                # run= False

            grid.update_display(WIN)


if __name__ == "__main__":
    driver()