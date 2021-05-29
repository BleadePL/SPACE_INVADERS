import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class representing single alien in the fleet"""

    def __init__(self, ai_game):
        """Alien creating and setting its location"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #loading aliens image and defining rect atribute
        self.image = pygame.image.load('Images/alien.png')
        self.rect = self.image.get_rect()

        #adding the foo in the left top corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #current alien location
        self.x = float(self.rect.x)

    def check_edges(self):
        """Returns true if an alien is in the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

        return False


    def update(self):
        """Alien movement to the right or left"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
