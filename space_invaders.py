import sys
from time import sleep
import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from pygame import mixer
from ship import Ship
from bullet import Bullet
from alien import Alien

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

        self.leaderboard_on = False
        self.ending_message_on = False

        #creating instace of class gamestats gathering all statistic data
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        #Icon init
        icon = pygame.image.load(self.settings.programIcon)
        pygame.display.set_icon(icon)

        #Ship Init
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        #button play
        self.play_button = Button(self, "Play")
        self.high_score_button = Button(self, "High Scores")

        #Soundtrack Init
        mixer.music.load(self.settings.soundtrack)
        mixer.music.play(-1)
        mixer.music.set_volume(self.settings.volume)

    def run_game(self):
        """Main loop game start"""
        clock = pygame.time.Clock()                         #to maintain the constant frame rate
        while True:
            clock.tick(200)
            self._check_events()                            #awaiting for players action (new game etc)
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        """Reaction on mouse and keyboard actions"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:                      #any place where user clicked mouse
                mouse_pos = pygame.mouse.get_pos()                          #get pos returns tuple (X,Y)
                self._check_play_button(mouse_pos)                          #determine if the user clicked on the button
                self._check_high_score_button(mouse_pos)
                self._check_exit_score_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_play_button(self, mouse_pos):
        """Starting new game after pressing the play button"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)      #collidepoint checks wheter point of the mouse click is in the button (True or False - clicked button)
        if button_clicked and not self.stats.game_active:
            #clear all stats
            self.settings.initialize_dynamic_settings()                     #clear all the speedups and reseting all stats
            self.stats.reset_status()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()                                            #displaying all the ships

            #deleting aliens and bullet lists
            self.aliens.empty()
            self.bullets.empty()

            #creating new fleet and returning ship to its origin position
            self._create_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)


    def _check_high_score_button(self, mouse_pos):
        button_clicked = self.high_score_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.leaderboard_on = True
            self.sb.draw_leadership(mouse_pos)

    def _check_exit_score_button(self, mouse_pos):
        if self.leaderboard_on and self.sb.exit_button.collidepoint(mouse_pos):
            self.leaderboard_on = False


    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE and self.stats.game_active:
            self._fire_bullet()
        elif self.ending_message_on:
            if event.key != pygame.K_KP_ENTER:
                if event.key == pygame.K_BACKSPACE:
                    if len(self.sb.username) > 0:
                        self.sb.username = self.sb.username[: len(self.sb.username) - 1]    #Changing letter in scoreboard and in game stats(saving point)
                        self.stats.username = self.sb.username
                else:
                    self.stats.username += str(event.unicode)
                    print(event.unicode)
                    self.sb.draw_letter(event.unicode)                                      #Adding a new letter to display (whole nickname)
            else:
                self.ending_message_on = False
                self.sb.username = ""
                self.stats.save_score()


    def _check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_bullets(self):
        """Updating bullets location and dealocation garbage ones"""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:                                                 #bottom side of the bullet is out of the screen
                self.bullets.remove(bullet)

        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        """Collision reaction between bullets and aliens"""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)      #Every bullet is a key in dictionary, values is the list of the hit aliens

        if collisions:                                                                      #Checking if a dictionary exists
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)                #To make the game count points from hitting two enemies by one bullet
                for repeat in range(len(aliens)):
                    self.settings.bullet_hit_sound.play()                                   #Playing hit sound for every hit alien
            self.sb.prep_score()                                                            #Create new image for new score to be displayed on the screen
            self.sb.check_high_score()

        if not self.aliens:                                                                 #checking if aliens group is empty
            #getting rid of exisitng bullets and creating new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            #levelling up
            self.stats.level += 1
            self.sb.prep_level()

    def _ship_hit(self):
        """Reaction for collition with an alien's ship"""
        if self.stats.ships_left > 0:
            #reducing lives
            self.stats.ships_left -= 1

            #update the lifes count
            self.sb.prep_ships()

            #removing contents of alien and ship lists
            self.aliens.empty()
            self.bullets.empty()

            #creating new fleet
            self._create_fleet()
            self.ship.center_ship()

            #pause
            sleep(0.8)
        else:
            self.stats.game_active = False          #Game over
            pygame.mouse.set_visible(True)
            self.ending_message_on = True

    def _update_aliens(self):
        """Update aliens current location, check wheter the alien object hits the edge of the screen"""
        self._check_fleet_edges()
        self.aliens.update()

        #collition between alien and the space Ship
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.settings.ship_hit_sound.play()
            self._ship_hit()

        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """Checking wheter the alien reached the bottom screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                self.settings.ship_hit_sound.play()
                break


    def _fire_bullet(self):
        """Creating bullet and adding it to the sprite group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.settings.bullet_sound.play()                       #Bullet sound play
        else: self.settings.empty_magazine_sound.play()             #Empty magazine sound play


    def _create_fleet(self):
        """Creating the fleet"""
        #distance betweeen aliens is the alien's width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)                      #2 alien space between one side of the screen
        number_aliens_x = available_space_x // (2 * alien_width)                                #1 alien space between aliens

        #determine how many rows can be filled with enemies
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)    #3 aliens and one ship space between the player's ship and the fleet
        number_rows = available_space_y // (2 * alien_height)                                   #1 alien space between next rows

        #Creating full fleet
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)


    def _create_alien(self, alien_number, row_number):
        """Creating and placing an alien in the row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = (alien.rect.height + 30) + 2 * alien.rect.height * row_number        #Depending on images size
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Reaction on gettin an alien to the edge of screen"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Moving fleet towards down side of the screen and changing the direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        #self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.settings.image_background, (0, 0))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        #Displaying info about the scoreboard
        self.sb.show_score()

        if not self.stats.game_active:                                      # Displaying the button only when the game is inactive
            self.play_button.draw_button()
            self.high_score_button.draw_button()

            if self.leaderboard_on:
                self.sb.draw_leadership(pygame.mouse.get_pos())

            if self.ending_message_on:
                self.sb.draw_message_score()                                #Displaying ending message on the screen
                self.sb.draw_nickname()                                     #Displaying input username

        pygame.display.flip()

if __name__ == '__main__':
    #Creating game and running it
    ai = SpaceInvaders()
    ai.run_game()