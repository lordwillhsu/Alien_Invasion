# Define Run_Game function of Alien Invasion
# Created by Will Xu on July 16th, 2017

import pygame

from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gfunc


def run_game():
    pygame.init()
    ai_settings = Settings()
    # Set window resolution;
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # Set window caption;
    pygame.display.set_caption("Alien Invasion")
    # Create Ship object;
    ship = Ship(ai_settings, screen)
    # Create group for bullets
    bullets = Group()

    while True:

        gfunc.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gfunc.update_bullets(bullets)
        gfunc.update_screen(ai_settings, screen, ship, bullets)

run_game()
