import pygame
import sys
import subprocess

# Инициализация Pygame
pygame.init()

# Загрузка изображения для фона меню
image = pygame.image.load("oboi.png")
# Масштабирование изображения под размер экрана
img1 = pygame.transform.scale(image, (750, 750))

# Создание окна с разрешением 750x750
scr1 = pygame.display.set_mode((750, 750))
# Установка заголовка окна
pygame.display.set_caption('ArcadeGame')

# Отображение фонового изображения на экране
scr1.blit(img1, (0, 0))
pygame.display.flip()  # Обновление экрана
show_image = True  # Флаг для отображения изображения

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():  # Обработка событий
        if event.type == pygame.QUIT:  # Если игрок закрыл окно
            running = False  # Завершение цикла
        elif event.type == pygame.KEYDOWN:  # Если игрок нажал клавишу
            if event.key == pygame.K_d:  # Если нажата клавиша "D"
                pygame.quit()  # Завершение работы Pygame
                subprocess.run(['python', 'game.py'])  # Запуск игры "game.py"
            elif event.key == pygame.K_s:  # Если нажата клавиша "S"
                pygame.quit()  # Завершение работы Pygame
                subprocess.run(['python', 'main1.py'])  # Запуск игры "main1.py"
            elif event.key == pygame.K_c:  # Если нажата клавиша "C"
                pygame.quit()  # Завершение работы Pygame
                subprocess.run(['python', 'game1.py'])  # Запуск игры "game1.py"
            elif event.key == pygame.K_v:  # Если нажата клавиша "V"
                pygame.quit()  # Завершение работы Pygame
                subprocess.run(['python', 'game2.py'])  # Запуск игры "game2.py"

# Завершение работы Pygame и выход из программы
pygame.quit()
sys.exit()