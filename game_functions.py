# Define game functions in Alien Invasion
# Created by Will Xu on July 22nd, 2017

import sys
import pygame


def check_keydown_events(event, ship):
    """Respond to the keyboard events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_setting, screen, ship):
    """Update the image on the screen and switch to new screen"""
    screen.fill(ai_setting.bg_color)
    ship.blitme()

    pygame.display.flip()
