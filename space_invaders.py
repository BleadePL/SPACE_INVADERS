import sys
import pygame

from settings import Settings
from pygame import mixer
from ship import Ship
from bullet import Bullet

class SpaceInvaders:
    """Main class intended for resources managment and the game functionality"""
    def __init__(self):
        """Game initiation and creating its resources"""

        # Game init
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("SPACE_INVADERS")


        #Icon init
        icon = pygame.image.load(self.settings.programIcon)
        pygame.display.set_icon(icon)

        #Ship Init
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        #Soundtrack Init
        mixer.music.load(self.settings.soundtrack)
        mixer.music.play(-1)

    def run_game(self):
            """Main loop game start"""
            while True:
                #Awiting for pressing the button or pressing the mouse button
                while True:
                    self._check_events()
                    self.ship.update()
                    self._update_bullets()
                    self._update_screen()

                #Refreshing screen
                self.screen.fill(self.settings.bg_color)

                #Ship Init
                self.ship.blitme()

                #Displaying last modified screen
                pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_bullets(self):
        """Updating bullets location and dealocation garbage ones"""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _fire_bullet(self):
        """Creating bullet and adding it to the sprite group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
        #Dodanie metody dźwięku braku pocisków

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()

if __name__ == '__main__':
    #Creating game and running it
    ai = SpaceInvaders()
    ai.run_game()