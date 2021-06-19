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

        pygame.display.set_caption(
            "Cellular Automata Model " + self.model_name
        )

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

                if (
                    event.type == pygame.KEYDOWN
                    and event.key == pygame.K_SPACE
                ):
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
                        if (
                            event.type == pygame.KEYDOWN
                            and event.key == pygame.K_SPACE
                        ):
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
        glider_gun_coordinates = [
            (31, 412),
            (55, 411),
            (56, 431),
            (33, 432),
            (227, 410),
            (253, 389),
            (273, 371),
            (292, 371),
            (234, 430),
            (231, 452),
            (249, 471),
            (270, 488),
            (288, 489),
            (331, 392),
            (349, 409),
            (351, 428),
            (374, 429),
            (354, 446),
            (336, 475),
            (314, 429),
            (430, 412),
            (451, 412),
            (452, 391),
            (431, 388),
            (433, 366),
            (451, 369),
            (473, 348),
            (469, 432),
            (514, 331),
            (511, 354),
            (507, 428),
            (508, 449),
            (704, 372),
            (732, 373),
            (734, 385),
            (716, 388),
        ]

        for a, b in glider_gun_coordinates:
            self.grid.manual_update((a + shift_right, b + shift_down))
