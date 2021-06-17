import pygame
import sys
from matrix import Matrix


class Cellular_Automaton_Model:
    def __init__(self, rule, time=10):
        # TODO Add von Neumann rules.
        """Editable"""
        birth, survival = rule
        self.birth = list(birth)
        self.survival = list(survival)
        self.delta_time = time

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
            pygame.time.delay(10)
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

    def Gosper_Glider_Gun(self):
        """
        Works with height=1000, width=1000, rows=50, columns=50.
        """
        shift_down = 60
        shift_right = 140
        self.grid.manual_update((31 + shift_right, 412 + shift_down))
        self.grid.manual_update((55 + shift_right, 411 + shift_down))
        self.grid.manual_update((56 + shift_right, 431 + shift_down))
        self.grid.manual_update((33 + shift_right, 432 + shift_down))
        self.grid.manual_update((227 + shift_right, 410 + shift_down))
        self.grid.manual_update((253 + shift_right, 389 + shift_down))
        self.grid.manual_update((273 + shift_right, 371 + shift_down))
        self.grid.manual_update((292 + shift_right, 371 + shift_down))
        self.grid.manual_update((234 + shift_right, 430 + shift_down))
        self.grid.manual_update((231 + shift_right, 452 + shift_down))
        self.grid.manual_update((249 + shift_right, 471 + shift_down))
        self.grid.manual_update((270 + shift_right, 488 + shift_down))
        self.grid.manual_update((288 + shift_right, 489 + shift_down))
        self.grid.manual_update((331 + shift_right, 392 + shift_down))
        self.grid.manual_update((349 + shift_right, 409 + shift_down))
        self.grid.manual_update((351 + shift_right, 428 + shift_down))
        self.grid.manual_update((374 + shift_right, 429 + shift_down))
        self.grid.manual_update((354 + shift_right, 446 + shift_down))
        self.grid.manual_update((336 + shift_right, 475 + shift_down))
        self.grid.manual_update((314 + shift_right, 429 + shift_down))
        self.grid.manual_update((430 + shift_right, 412 + shift_down))
        self.grid.manual_update((451 + shift_right, 412 + shift_down))
        self.grid.manual_update((452 + shift_right, 391 + shift_down))
        self.grid.manual_update((431 + shift_right, 388 + shift_down))
        self.grid.manual_update((433 + shift_right, 366 + shift_down))
        self.grid.manual_update((451 + shift_right, 369 + shift_down))
        self.grid.manual_update((473 + shift_right, 348 + shift_down))
        self.grid.manual_update((469 + shift_right, 432 + shift_down))
        self.grid.manual_update((514 + shift_right, 331 + shift_down))
        self.grid.manual_update((511 + shift_right, 354 + shift_down))
        self.grid.manual_update((507 + shift_right, 428 + shift_down))
        self.grid.manual_update((508 + shift_right, 449 + shift_down))
        self.grid.manual_update((704 + shift_right, 372 + shift_down))
        self.grid.manual_update((732 + shift_right, 373 + shift_down))
        self.grid.manual_update((734 + shift_right, 385 + shift_down))
        self.grid.manual_update((716 + shift_right, 388 + shift_down))
