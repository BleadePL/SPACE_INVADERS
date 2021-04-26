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
        #Ship settings
        self.ship_speed = 5.0
        self.ship_limit = 3

        #bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 214, 0)
        self.bullets_allowed = 4

        #alien settings
        self.alien_speed = 1.5
        self.fleet_drop_speed = 10
        #Moving right = 1/ left = -1
        self.fleet_direction = 1
