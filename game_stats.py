class GameStats():
    """Отслеживание статистики для игры"""

    def __init__(self, ai_settings):
        """Инициализирует стратистику"""
        self.ai_settings = ai_settings
        self.reset_stats()

        def reset_stats(self):
            """Инициализирует статистику, изменяющуюся в ходе игры"""
            self.ships_left = self.ai_settings.ship_limit
