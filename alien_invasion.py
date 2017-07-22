# Define Run_Game function of Alien Invasion
# Created by Will Xu on July 16th, 2017

import pygame

from settings import Settings
from ship import Ship
import game_functions as gfunc


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))     # Set window resolution;
    pygame.display.set_caption("Alien Invasion")                                                # Set window caption;
    ship = Ship(ai_settings, screen)                                                            # Create object Ship;

    while True:

        gfunc.check_events(ship)
        ship.update()
        gfunc.update_screen(ai_settings, screen, ship)

run_game()
