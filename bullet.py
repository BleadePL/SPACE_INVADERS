import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class prepared for bullet managment, shot by Space ship"""

    def __init__(self, ai_game):
        """Creating bullet object in actual Space ship position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #creating rectangle and setting its position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #bullet position
        self.y = float(self.rect.y)

    def update(self):
        """Poruszanie pociskiem po ekranie"""
        #Update bullets position
        self.y -= self.settings.bullet_speed
        #Update rectangle position
        self.rect.y = self.y

    def draw_bullet(self):
        """Displaying bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)