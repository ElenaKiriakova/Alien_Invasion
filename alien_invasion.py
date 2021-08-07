import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from  pygame.sprite import Group


def run_game():
    # Инициализирует игру и создает обьект экрана
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Создание корабля
    ship = Ship(ai_settings, screen)

    # Создание группы для хранения пуль
    bullets = Group()

    # Изменение цвета фона игры
    bg_color = (230,230,230)

    # Запуск основного цикла игры
    while True:
        # Отслеживание мобытий клавиатуры и мыши
        gf.check_events(ai_settings, screen, ship, bullets)
        #Движение корабля
        ship.update()

        bullets.update()

        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))
        # При каждом проходе цикла прорисовывется экран
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()