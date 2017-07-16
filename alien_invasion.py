# Define Run_Game function of Alien Invasion
# Created by Will Xu on July 16th, 2017

import sys
import pygame


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()


run_game()
