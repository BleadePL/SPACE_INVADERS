import pygame.image
from pygame import mixer
class Settings:
    def __init__(self):
        """Class designed to store all game settings"""

        #Screen settings
        self.screen_width = 1280
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.leadership_bg = (181, 181, 181)

        #icon import
        self.programIcon = "Images/icon.png"                                #Game icon

        #file scores
        self.high_score_file = "Data/score_board.txt"                       #File containing the highest score

        #file leadership
        self.leadership_file = "Data/leadership.txt"                        #File containing leaderboard of players

        #file space background
        self.image_background = pygame.image.load("Images/universe.jpg")    #Background of the screen

        #soundtracks
        self.volume = 0.4
        self.soundtrack = "Soundtrack/Vitaly.wav"
        self.bullet_hit_sound = mixer.Sound("Soundtrack/bullet_hit_sound.wav")
        self.bullet_sound = mixer.Sound("Soundtrack/bullet_sound.wav")
        self.empty_magazine_sound = mixer.Sound("Soundtrack/empty_magazine.wav")
        self.ship_hit_sound = mixer.Sound("Soundtrack/ship_hit.wav")

        self.bullet_sound.set_volume(self.volume - 0.2)
        self.bullet_hit_sound.set_volume(self.volume + 0.1)
        self.ship_hit_sound.set_volume(self.volume + 0.2)

        #ship settings
        self.ship_limit = 3

        #bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 214, 0)
        self.bullets_allowed = 4


        self.fleet_drop_speed = 100

        #Easy changing the speed of game
        self.speedup_scale = 1.1    #2 means double speed

        #Easy changing the amount of points given to player (next stages - bonus points)
        self.score_scale = 1.5

        self.initialize_dynamic_settings()  #Change the value of speed atributes

        #the size of leadership pop up
        self.leadership_size_width = 350
        self.leadership_size_heigh = 450


    def initialize_dynamic_settings(self):
        """Initialization of settings during the game"""
        #Ship settings
        self.ship_speed = 5.0

        #bullet settings
        self.bullet_speed = 2.5

        #alien settings
        self.alien_speed = 1.5

        #Moving right = 1/ left = -1
        self.fleet_direction = 1

        #Scoring
        self.alien_points = 50      #destroying the alien (player gets the amount of points)

    def increase_speed(self):                   #from _check_bullet_alien_collision
        """Changing settings about speed"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)