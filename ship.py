import pygame

class Ship:

    def __init__(self, ai_game):

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('spaceshipn.png')
        self.rect = self.image.get_rect()

        #Every new space ship appears on the bottom
        self.rect.midbottom = self.screen_rect.midbottom

        #Space ship position
        self.x = float(self.rect.x)

        #Ship movement
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #Aktualne położeni statku

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #Update object rect
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)