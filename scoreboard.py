import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    """Class dedicated to the scoring system"""
    def __init__(self, ai_game):
        self.ai_game = ai_game

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.username = ""          #Responsible for saving a nickname

        #Font for the score point
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 30)

        #Preparing the images of score
        self.prep_score()           #Prepare the
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Convert text to an image"""
        rounded_score = round(self.stats.score, -1) # -1 parameter will round number into multiple of 10
        score_str = "{:,}".format(rounded_score)    #Formating the text from 100000000 to 1,000,000
        label_score = "Score: "
        label_score += score_str

        self.score_image = self.font.render(label_score, True, self.text_color, self.settings.bg_color)   #creating the image on the screen

        #Displaying score
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20     #displaying the score to the right
        self.score_rect.top = 20

    def prep_high_score(self):
        """Convert a best score into image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        label_high_score = "High Score: "
        label_high_score += high_score_str
        self.high_score_image = self.font.render(label_high_score, True, self.text_color, self.settings.bg_color)

        #dispay the best score in the middle up screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx     #set in the horizontal middle
        self.high_score_rect.top = self.score_rect.top              # to make all the scores rectangle be on the same height


    def check_high_score(self):                                             #Checked in bullet_alien_collisions
        """Checking wheter the player beat the actual high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
            self.stats.save_data()

    def show_score(self):
        """Displaying the actual scores"""
        self.screen.blit(self.score_image, self.score_rect)     #blit displays an image showing the actual score in the score rect position
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)                            #method draw for all group of the ships on the screen

    def prep_level(self):
        """Converting level information into image"""
        level_str = str(self.stats.level)
        label_lvl = "Lvl: "
        label_lvl += level_str
        self.level_image = self.font.render(label_lvl, True, self.text_color, self.settings.bg_color)

        #Level number is displayed under the actual score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right           #right atribute returns x position
        self.level_rect.top = self.score_rect.bottom + 10       #botom returns y postion, placing the level image 10pxls under the actual score

    def prep_ships(self):                                       #Initialisation from method check_play_button
        """Displays remaining ship lifes"""
        self.ships = Group()                                    #creating new group for the changing of conditions (player got hit)
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width    #placing all ships on the screen
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_leadership(self):
        """Creating pop up with leadership"""
        self.leadership_rect = pygame.Rect(0, 0, self.settings.leadership_size_width, self.settings.leadership_size_heigh)
        self.leadership_rect.center = self.screen.get_rect().center
        self.screen.fill(self.settings.leadership_bg, self.leadership_rect)

        leadership = sorted(self.stats.leadership, key=lambda x: int(x.split(',')[1]), reverse=True)
        start_pos_x, startingpos_y = self.leadership_rect.topleft

        for word in leadership:
            word_surface = self.font.render(word, True, pygame.Color('black'))
            word_width, word_height = word_surface.get_size()
            self.screen.blit(word_surface, (start_pos_x, startingpos_y))
            startingpos_y += word_height


        self.exit_button = pygame.Rect(0, 0, 20, 20)
        self.exit_button.topright = self.leadership_rect.topright

        msg_image = self.font.render("X", True, pygame.Color('white'), pygame.Color('green'))
        self.msg_image_rect = msg_image.get_rect()
        self.msg_image_rect.center = self.exit_button.center

        self.screen.fill(pygame.Color("green"), self.exit_button)
        self.screen.blit(msg_image, self.msg_image_rect)

    def draw_leadership(self, mouse_pos):
        """Displays table with high scores"""
        self.prep_leadership()
        return self.exit_button.collidepoint(mouse_pos)

    def prep_message_score(self):
        """Creating method for saving a placement's score"""

        self.end_message_rect = pygame.Rect(0, 0, self.settings.screen_width, self.settings.screen_height)
        self.end_message_rect.center = self.screen.get_rect().center
        self.screen.fill(pygame.Color('black'), self.end_message_rect)

        self.msg_image_end = pygame.font.SysFont(None, 80).render("Game over, Enter your username and hit enter", True, pygame.Color('white'), pygame.Color('green'))
        self.screen.blit(self.msg_image_end, self.msg_image_end.get_rect())



    def draw_message_score(self):
        """Display game over message"""
        self.prep_message_score()


    def draw_letter(self, character):
        """Add a leter to the username"""
        self.username += character

    def draw_nickname(self):
        """Draw current nickname"""
        msg_image = pygame.font.SysFont(None, 80).render(self.username, True, pygame.Color('white'))
        self.screen.blit(msg_image, (0, self.msg_image_end.get_rect().bottom + 10))
