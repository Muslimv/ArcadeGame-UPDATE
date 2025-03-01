import pygame
import sys

# Инициализация звукового модуля Pygame
pygame.mixer.init()

# Загрузка фоновой музыки для меню
pygame.mixer.music.load('sounds/sounds1.mp3')

# Загрузка звука для меню
menu_sounds = pygame.mixer.Sound("sounds/menu_sounds.wav")


def show_menu(screen, menu_image):
    """
    Отображение главного меню игры.
    """
    menu_sounds.play()  # Воспроизведение звука меню
    pygame.mixer.music.play(-1)  # Бесконечное воспроизведение фоновой музыки
    return