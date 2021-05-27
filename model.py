import pygame
import sys
from matrix import Matrix


class Cellular_Automaton_Model:
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
