import sys
import pygame

from settings import Settings
from pygame import mixer

class SpaceInvaders:
    """Main class intended for resources managment and the game functionality"""
    def __init__(self):
        """Game initiation and creating its resources"""

        # Game init
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("SPACE_INVADERS")


        #Icon init
        icon = pygame.image.load(self.settings.programIcon)
        pygame.display.set_icon(icon)

        #Soundtrack Init
        mixer.music.load(self.settings.soundtrack)
        mixer.music.play(-1)

    def run_game(self):
            """Main loop start"""
            while True:
                #Awiting for pressing the button or pressing the mouse button
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

                #Refreshing screen
                self.screen.fill(self.settings.bg_color)
                #Displaying last modified screen
                pygame.display.flip()


if __name__ == '__main__':
    #Creating game and running it
    ai = SpaceInvaders()
    ai.run_game()