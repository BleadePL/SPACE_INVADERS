class Settings:
    def __init__(self):
        """Class designed to store all game settings"""

        #Screen settings
        self.screen_width = 1280
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #icon import
        self.programIcon = "icon.png"

        #soundtrack import
        self.soundtrack = "soundtrack.wav"
        #Ship settings
        self.ship_speed = 0.9

        #bullet settings
        self.bullet_speed = 0.6
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 214, 0)
        self.bullets_allowed = 4