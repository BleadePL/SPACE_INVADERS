class Settings:
    def __init__(self):
        """Class designed to store all game settings"""

        #Screen settings
        self.screen_width = 1280
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #icon import
        self.programIcon = "Images/icon.png"

        #soundtrack import
        self.soundtrack = "Soundtrack/Vitaly.wav"


        #bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 214, 0)
        self.bullets_allowed = 4


        self.fleet_drop_speed = 10

        #Easy changing the speed of game
        self.speedup_scale = 1.1    #2 means double speed

        self.initialize_dynamic_settings()  #Change the value of speed atributes


    def initialize_dynamic_settings(self):
        """Initialization of settings during the game"""
        #Ship settings
        self.ship_speed = 5.0
        self.ship_limit = 3

        #alien settings
        self.alien_speed = 1.5

        #Moving right = 1/ left = -1
        self.fleet_direction = 1

    def increase_speed(self):                   #from _check_bullet_alien_collision
        """Changing settings about speed"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale