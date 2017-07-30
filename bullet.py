# Define Bullet class in Alien Invasion
# Created by Will Xu on July 30th, 2017


import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """To create a class to control the firing of bullets from the ship"""

    def __init__(self, ai_settings, screen, ship):
        """To create bullet object at the ship's initial position"""
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a rect at (0, 0) to represent the bullet object, then set its initial position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """The bullet will move upwards upon firing"""
        # Update bullet position
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
