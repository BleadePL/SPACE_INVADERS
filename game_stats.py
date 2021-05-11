class GameStats:
    """Monitor statistic values in the game"""

    def __init__(self, ai_game):
        """initialization of statistic values"""
        self.settings = ai_game.settings
        self.reset_status()

        #run the game in inactive status
        self.game_active = False

        #Best score
        self.high_score = 0

        #leadership
        self.leadership = []

        #reading data from files
        self.load_data()

    def reset_status(self):
        """initialization of statistic value, can be managed later"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def load_data(self):
        #load high score
        with open(self.settings.high_score_file) as f:
            self.high_score = int(f.readline())
        f.close()

        #reading leadership
        with open(self.settings.leadership_file) as f:
            file = [line.rstrip() for line in f]

            for line in file:
                self.leadership.append(line)
        f.close()



    def save_data(self):
        with open(self.settings.high_score_file, 'w') as f:
            f.write(str(self.score))
        f.close()
