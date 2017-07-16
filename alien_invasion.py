# Define Run_Game function of Alien Invasion
# Created by Will Xu on July 16th, 2017

import sys
import pygame

from settings import Settings


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))     # Set window resolution;
    pygame.display.set_caption("Alien Invasion")                                                # Set window caption;

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(ai_settings.bg_color)
        pygame.display.flip()


run_game()
