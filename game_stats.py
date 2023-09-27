class GameStats():
    """Отслеживание статистики для игры Alien Invasion."""

    def __init__(self, ai_game):
        """Инициализирует статистику."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Игра Alien Invasion запускается в активном состоянии.
        self.game_active = False

        # Рекорд не должен сбрасываться.
        with open('rezul.txt') as file_object:
            contents = file_object.read()
        self.high_score = int(contents)

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.settings.ship_limit
        self.ships_hit = self.settings.ship_hits
        self.score = 0
        self.level = 1
        self.kill = 0    