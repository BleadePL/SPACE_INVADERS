import sys
import pygame

class AlienInvasion:
    """Main class intended for resources managment and the game functionality"""
    def __init__(self):
        """Game initiation and creating its resources"""
        programIcon = pygame.image.load('icon.png')
        pygame.display.set_icon(programIcon)
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("SPACE_INVADERS")

    def run_game(self):
            """Main loop start"""
            while True:
                #Awiting for pressing the button or pressing the mouse button
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

                #Displaying last modified screen
                pygame.display.flip()


if __name__ == '__main__':
    #Creating a piece of game and running it
    ai = AlienInvasion()
    ai.run_game()