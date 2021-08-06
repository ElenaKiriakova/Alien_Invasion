import sys
import pygame

def run_game():
    # Инициализирует игру и создает обьект экрана
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    # Запуск основного цикла игры
    while True:
        # Отслеживание мобытий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Отображение последнего прорисованного экрана
        pygame.display.flip()

run_game()