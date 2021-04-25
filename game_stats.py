class GameStats:
    """Monitor statistic values in the game"""

    def __init__(self, ai_game):
        """initialization of statistic values"""
        self.settings = ai_game.settings
        self.reset_status()

        #run the game in active status
        self.game_active = True

    def reset_status(self):
        """initialization of statistic value, can be managed later"""
        self.ships_left = self.settings.ship_limit