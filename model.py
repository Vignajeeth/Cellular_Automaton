import pygame
import sys
from matrix import Matrix


class Cellular_Automaton_Model:
    def __init__(self, rule, time=100):
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
        self.grid.manual_update((31, 112))
        self.grid.manual_update((55, 111))
        self.grid.manual_update((56, 131))
        self.grid.manual_update((33, 132))
        self.grid.manual_update((227, 110))
        self.grid.manual_update((253, 89))
        self.grid.manual_update((273, 71))
        self.grid.manual_update((292, 71))
        self.grid.manual_update((234, 130))
        self.grid.manual_update((231, 152))
        self.grid.manual_update((249, 171))
        self.grid.manual_update((270, 188))
        self.grid.manual_update((288, 189))
        self.grid.manual_update((331, 92))
        self.grid.manual_update((349, 109))
        self.grid.manual_update((351, 128))
        self.grid.manual_update((374, 129))
        self.grid.manual_update((354, 146))
        self.grid.manual_update((336, 175))
        self.grid.manual_update((314, 129))
        self.grid.manual_update((430, 112))
        self.grid.manual_update((451, 112))
        self.grid.manual_update((452, 91))
        self.grid.manual_update((431, 88))
        self.grid.manual_update((433, 66))
        self.grid.manual_update((451, 69))
        self.grid.manual_update((473, 48))
        self.grid.manual_update((469, 132))
        self.grid.manual_update((514, 31))
        self.grid.manual_update((511, 54))
        self.grid.manual_update((507, 128))
        self.grid.manual_update((508, 149))
        self.grid.manual_update((704, 72))
        self.grid.manual_update((732, 73))
        self.grid.manual_update((734, 85))
        self.grid.manual_update((716, 88))
