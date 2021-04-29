class GameStats:
    """Monitor statistic values in the game"""

    def __init__(self, ai_game):
        """initialization of statistic values"""
        self.settings = ai_game.settings
        self.reset_status()

        #run the game in inactive status
        self.game_active = False

    def reset_status(self):
        """initialization of statistic value, can be managed later"""
        self.ships_left = self.settings.ship_limit