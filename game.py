# Импортирование зависимостей/библиотек
import os
import random
import pygame
import main2


# Устанавливаем переменную окружения для центрирования окна Pygame на экране
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Инициализация Pygame и его модуля для работы со звуком
pygame.init()
pygame.mixer.init()

# Переменная для отслеживания состояния воспроизведения музыки
music_play = False

# Закомментированная строка для бесконечного воспроизведения музыки
# pygame.mixer.music.play(-1)

# Загрузка звука победы и установка его громкости
victory_sound = pygame.mixer.Sound('sounds/victory.wav')
victory_sound.set_volume(1.0)

# Загрузка изображения для экрана "Игра окончена"
game_over_image = pygame.image.load('assets/images/game_over.png')

# Загрузка звука для экрана "Игра окончена"
game_over_sound = pygame.mixer.Sound('sounds/g_o.wav')

# Загрузка изображения для экрана победы
win_image = pygame.image.load('assets/images/win.png')

# Загрузка изображения для главного меню
menu_image = pygame.image.load('assets/images/menu.png')

# Получение информации о текущем разрешении экрана
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h

# Установка размеров окна игры (меньше, чем разрешение экрана)
window_width, window_height = screen_width - 800, screen_height - 150

# Создание объекта для управления временем и FPS (кадры в секунду)
timer = pygame.time.Clock()
fps = 60

# Установка заголовка окна игры
pygame.display.set_caption('Donkey Kong')

# Загрузка и установка иконки для окна игры
icon = pygame.image.load('assets/images/gicon.png')
pygame.display.set_icon(icon)

# Загрузка шрифтов для текста в игре
font = pygame.font.Font('freesansbold.ttf', 50)  # Основной шрифт
font2 = pygame.font.Font('freesansbold.ttf', 30)  # Дополнительный шрифт

# Создание окна игры с заданными размерами
screen = pygame.display.set_mode([window_width, window_height])

# Вычисление размеров секций для игрового поля
section_width = window_width // 32
section_height = window_height // 32

# Вычисление наклона (slope) для игрового поля
slope = section_height // 8

# Время (в кадрах) между появлением новых бочек
barrel_spawn_time = 360

# Счетчик для управления появлением бочек (начальное значение — половина от barrel_spawn_time)
barrel_count = barrel_spawn_time / 2

# Время (в кадрах) для управления временем появления бочек
barrel_time = 360

# Загрузка и масштабирование изображения бочки
barrel_img = pygame.transform.scale(pygame.image.load('assets/images/barrels/barrel.png'),
                                    (section_width * 1.5, section_height * 2))

# Загрузка и масштабирование изображения огня (пламени)
flames_img = pygame.transform.scale(pygame.image.load('assets/images/fire.png'),
                                    (section_width * 2, section_height))

# Загрузка и масштабирование изображения бочки (вид сбоку)
barrel_side = pygame.transform.scale(pygame.image.load('assets/images/barrels/barrel2.png'),
                                     (section_width * 2, section_height * 2.5))

# Загрузка и масштабирование изображений Донки Конга (три разных кадра для анимации)
dk1 = pygame.transform.scale(pygame.image.load('assets/images/dk/dk1.png'),
                             (section_width * 5, section_height * 5))
dk2 = pygame.transform.scale(pygame.image.load('assets/images/dk/dk2.png'),
                             (section_width * 5, section_height * 5))
dk3 = pygame.transform.scale(pygame.image.load('assets/images/dk/dk3.png'),
                             (section_width * 5, section_height * 5))

# Загрузка и масштабирование изображений принцессы Пич (два разных кадра для анимации)
peach1 = pygame.transform.scale(pygame.image.load('assets/images/peach/peach1.png'),
                                (2 * section_width, 3 * section_height))
peach2 = pygame.transform.scale(pygame.image.load('assets/images/peach/peach2.png'),
                                (2 * section_width, 3 * section_height))

# Загрузка и масштабирование изображений огненного шара (два разных кадра для анимации)
fireball = pygame.transform.scale(pygame.image.load('assets/images/fireball.png'),
                                  (1.5 * section_width, 2 * section_height))
fireball2 = pygame.transform.scale(pygame.image.load('assets/images/fireball2.png'),
                                   (1.5 * section_width, 2 * section_height))

# Загрузка и масштабирование изображения молотка
hammer = pygame.transform.scale(pygame.image.load('assets/images/hammer.png'),
                                   (2 * section_width, 2 * section_height))

# Загрузка и масштабирование изображений Марио (разные состояния и анимации)
standing = pygame.transform.scale(pygame.image.load('assets/images/mario/standing.png'),
                                  (2 * section_width, 2.5 * section_height))
jumping = pygame.transform.scale(pygame.image.load('assets/images/mario/jumping.png'),
                                 (2 * section_width, 2.5 * section_height))
running = pygame.transform.scale(pygame.image.load('assets/images/mario/running.png'),
                                 (2 * section_width, 2.5 * section_height))
climbing1 = pygame.transform.scale(pygame.image.load('assets/images/mario/climbing1.png'),
                                   (2 * section_width, 2.5 * section_height))
climbing2 = pygame.transform.scale(pygame.image.load('assets/images/mario/climbing2.png'),
                                   (2 * section_width, 2.5 * section_height))

# Загрузка и масштабирование изображений Марио с молотком (разные состояния и анимации)
hammer_stand = pygame.transform.scale(pygame.image.load('assets/images/mario/hammer_stand.png'),
                                      (2.5 * section_width, 2.5 * section_height))
hammer_jump = pygame.transform.scale(pygame.image.load('assets/images/mario/hammer_jump.png'),
                                     (2.5 * section_width, 2.5 * section_height))
hammer_overhead = pygame.transform.scale(pygame.image.load('assets/images/mario/hammer_overhead.png'),
                                         (2.5 * section_width, 3.5 * section_height))


# Начальная координата Y для нижней платформы (стартовая позиция)
start_y = window_height - 2 * section_height

# Координаты Y для других рядов платформ, вычисленные на основе начальной позиции и наклона
row2_y = start_y - 4 * section_height  # Второй ряд платформ
row3_y = row2_y - 7 * slope - 3 * section_height  # Третий ряд платформ
row4_y = row3_y - 4 * section_height  # Четвертый ряд платформ
row5_y = row4_y - 7 * slope - 3 * section_height  # Пятый ряд платформ
row6_y = row5_y - 4 * section_height  # Шестой ряд платформ

# Верхние границы для каждого ряда платформ (используются для коллизий и размещения объектов)
row6_top = row6_y - 4 * slope  # Верхняя граница шестого ряда
row5_top = row5_y - 8 * slope  # Верхняя граница пятого ряда
row4_top = row4_y - 8 * slope  # Верхняя граница четвертого ряда
row3_top = row3_y - 8 * slope  # Верхняя граница третьего ряда
row2_top = row2_y - 8 * slope  # Верхняя граница второго ряда
row1_top = start_y - 5 * slope  # Верхняя граница первого ряда

# Флаг для активации огненных шаров
fireball_trigger = False

# Текущий активный уровень
active_level = 0

# Счетчик для управления временем или событиями
counter = 0

# Текущий счет игрока
score = 0

# Рекордный счет
high_score = 0

# Количество жизней игрока
lives = 5

# Бонусные очки
bonus = 6000

# Флаг для первого запуска огненного шара
first_fireball_trigger = False

# Флаг для отслеживания победы
victory = False

# Флаг для сброса игры
reset_game = False

# Уровни игры, содержащие информацию о платформах, лестницах, молотках и цели
levels = [
    {
        # Платформы (мосты) на уровне. Каждый элемент — это кортеж (начальная позиция X, позиция Y, длина)
        'bridges': [
            (1, start_y, 15), (16, start_y - slope, 3),
            (19, start_y - 2 * slope, 3), (22, start_y - 3 * slope, 3),
            (25, start_y - 4 * slope, 3), (28, start_y - 5 * slope, 3),
            (25, row2_y, 3), (22, row2_y - slope, 3),
            (19, row2_y - 2 * slope, 3), (16, row2_y - 3 * slope, 3),
            (13, row2_y - 4 * slope, 3), (10, row2_y - 5 * slope, 3),
            (7, row2_y - 6 * slope, 3), (4, row2_y - 7 * slope, 3),
            (2, row2_y - 8 * slope, 2), (4, row3_y, 3),
            (7, row3_y - slope, 3), (10, row3_y - 2 * slope, 3),
            (13, row3_y - 3 * slope, 3), (16, row3_y - 4 * slope, 3),
            (19, row3_y - 5 * slope, 3), (22, row3_y - 6 * slope, 3),
            (25, row3_y - 7 * slope, 3), (28, row3_y - 8 * slope, 2),
            (25, row4_y, 3), (22, row4_y - slope, 3),
            (19, row4_y - 2 * slope, 3), (16, row4_y - 3 * slope, 3),
            (13, row4_y - 4 * slope, 3), (10, row4_y - 5 * slope, 3),
            (7, row4_y - 6 * slope, 3), (4, row4_y - 7 * slope, 3),
            (2, row4_y - 8 * slope, 2), (4, row5_y, 3),
            (7, row5_y - slope, 3), (10, row5_y - 2 * slope, 3),
            (13, row5_y - 3 * slope, 3), (16, row5_y - 4 * slope, 3),
            (19, row5_y - 5 * slope, 3), (22, row5_y - 6 * slope, 3),
            (25, row5_y - 7 * slope, 3), (28, row5_y - 8 * slope, 2),
            (25, row6_y, 3), (22, row6_y - slope, 3),
            (19, row6_y - 2 * slope, 3), (16, row6_y - 3 * slope, 3),
            (2, row6_y - 4 * slope, 14), (13, row6_y - 4 * section_height, 6),
            (10, row6_y - 3 * section_height, 3)
        ],
        # Лестницы на уровне. Каждый элемент — это кортеж (позиция X, позиция Y, длина)
        'ladders': [
            (12, row2_y + 6 * slope, 2), (12, row2_y + 26 * slope, 2),
            (25, row2_y + 11 * slope, 4), (6, row3_y + 11 * slope, 3),
            (14, row3_y + 8 * slope, 4), (10, row4_y + 6 * slope, 1),
            (10, row4_y + 24 * slope, 2), (16, row4_y + 6 * slope, 5),
            (25, row4_y + 9 * slope, 4), (6, row5_y + 11 * slope, 3),
            (11, row5_y + 8 * slope, 4), (23, row5_y + 4 * slope, 1),
            (23, row5_y + 24 * slope, 2), (25, row6_y + 9 * slope, 4),
            (13, row6_y + 5 * slope, 2), (13, row6_y + 25 * slope, 2),
            (18, row6_y - 27 * slope, 4), (12, row6_y - 17 * slope, 2),
            (10, row6_y - 17 * slope, 2), (12, -5, 13), (10, -5, 13)
        ],
        # Молотки на уровне. Каждый элемент — это кортеж (позиция X, позиция Y)
        'hammers': [
            (4, row6_top + section_height), (4, row4_top + section_height)
        ],
        # Цель уровня. Кортеж (позиция X, позиция Y, длина)
        'target': (13, row6_y - 4 * section_height, 3)
    }
]


class Player(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)  # Инициализация базового класса Sprite
        self.y_change = 0  # Изменение позиции по Y (для гравитации и прыжков)
        self.x_speed = 3  # Скорость перемещения по X
        self.x_change = 0  # Изменение позиции по X (для движения влево/вправо)
        self.landed = False  # Флаг, указывающий, находится ли игрок на платформе
        self.pos = 0  # Текущая позиция в анимации (0 или 1 для смены кадров)
        self.dir = 1  # Направление движения (1 — вправо, -1 — влево)
        self.count = 0  # Счетчик для управления анимацией
        self.climbing = False  # Флаг, указывающий, карабкается ли игрок по лестнице
        self.image = standing  # Текущее изображение игрока (по умолчанию — стоя)
        self.hammer = False  # Флаг, указывающий, держит ли игрок молоток
        self.max_hammer = 450  # Максимальное время использования молотка
        self.hammer_len = self.max_hammer  # Оставшееся время использования молотка
        self.hammer_pos = 1  # Позиция молотка в анимации (0 или 1)
        self.rect = self.image.get_rect()  # Прямоугольник для коллизий и отрисовки
        self.hitbox = self.rect  # Хитбокс игрока (для коллизий)
        self.hammer_box = self.rect  # Хитбокс молотка (для коллизий)
        self.rect.center = (x_pos, y_pos)  # Установка начальной позиции игрока
        self.over_barrel = False  # Флаг, указывающий, находится ли игрок над бочкой
        # Нижний прямоугольник для проверки коллизий с платформами
        self.bottom = pygame.rect.Rect(self.rect.left, self.rect.bottom - 20, self.rect.width, 20)

    def update(self):
        """Обновление состояния игрока (движение, гравитация, анимация, молоток)."""
        self.landed = False  # Сброс флага нахождения на платформе
        # Проверка коллизий с платформами
        for i in range(len(plats)):
            if self.bottom.colliderect(plats[i]):
                self.landed = True  # Игрок на платформе
                if not self.climbing:
                    # Корректировка позиции игрока, чтобы он стоял на платформе
                    self.rect.centery = plats[i].top - self.rect.height / 2 + 1
        # Гравитация, если игрок не на платформе и не карабкается
        if not self.landed and not self.climbing:
            self.y_change += 0.25  # Увеличение скорости падения
        # Обновление позиции игрока
        self.rect.move_ip(self.x_change * self.x_speed, self.y_change)
        # Обновление нижнего прямоугольника для коллизий
        self.bottom = pygame.rect.Rect(self.rect.left, self.rect.bottom - 20, self.rect.width, 20)
        # Управление анимацией
        if self.x_change != 0 or (self.climbing and self.y_change != 0):
            if self.count < 3:
                self.count += 1
            else:
                self.count = 0
                if self.pos == 0:
                    self.pos += 1  # Смена кадра анимации
                else:
                    self.pos = 0
        else:
            self.pos = 0  # Сброс анимации, если игрок не двигается
        # Управление молотком
        if self.hammer:
            self.hammer_pos = (self.hammer_len // 30) % 2  # Смена позиции молотка
            self.hammer_len -= 1  # Уменьшение времени использования молотка
            if self.hammer_len == 0:  # Если время вышло
                self.hammer = False  # Игрок больше не держит молоток
                self.hammer_len = self.max_hammer  # Сброс времени молотка

    def draw(self):
        """Отрисовка игрока с учетом его состояния (анимация, направление, молоток)."""
        if not self.hammer:
            # Анимация без молотка
            if not self.climbing and self.landed:
                if self.pos == 0:
                    self.image = standing  # Стоя
                else:
                    self.image = running  # Бег
            if not self.landed and not self.climbing:
                self.image = jumping  # Прыжок
            if self.climbing:
                if self.pos == 0:
                    self.image = climbing1  # Карабкание (кадр 1)
                else:
                    self.image = climbing2  # Карабкание (кадр 2)
        else:
            # Анимация с молотком
            if self.hammer_pos == 0:
                self.image = hammer_jump  # Прыжок с молотком
            else:
                self.image = hammer_overhead  # Молоток над головой
        # Отражение изображения, если игрок движется влево
        if self.dir == -1:
            self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.image = self.image
        # Обновление хитбокса
        self.calc_hitbox()
        # Отрисовка игрока на экране
        if self.hammer_pos == 1 and self.hammer:
            screen.blit(self.image, (self.rect.left, self.rect.top - section_height))
        else:
            screen.blit(self.image, self.rect.topleft)

    def calc_hitbox(self):
        """Вычисление хитбокса игрока и молотка."""
        if not self.hammer:
            # Хитбокс без молотка
            self.hitbox = pygame.rect.Rect((self.rect[0] + 15, self.rect[1] + 5),
                                           (self.rect[2] - 30, self.rect[3] - 10))
        elif self.hammer_pos == 0:
            # Хитбокс с молотком (горизонтальное положение)
            if self.dir == 1:
                self.hitbox = pygame.rect.Rect((self.rect[0], self.rect[1] + 5),
                                               (self.rect[2] - 30, self.rect[3] - 10))
                self.hammer_box = pygame.rect.Rect((self.hitbox[0] + self.hitbox[2], self.rect[1] + 5),
                                                   (self.hitbox[2], self.rect[3] - 10))
            else:
                self.hitbox = pygame.rect.Rect((self.rect[0] + 40, self.rect[1] + 5),
                                               (self.rect[2] - 30, self.rect[3] - 10))
                self.hammer_box = pygame.rect.Rect((self.hitbox[0] - self.hitbox[2], self.rect[1] + 5),
                                                   (self.hitbox[2], self.rect[3] - 10))
        else:
            # Хитбокс с молотком (вертикальное положение)
            self.hitbox = pygame.rect.Rect((self.rect[0] + 15, self.rect[1] + 5),
                                           (self.rect[2] - 30, self.rect[3] - 10))
            self.hammer_box = pygame.rect.Rect((self.hitbox[0], self.hitbox[1] - section_height),
                                               (self.hitbox[2], section_height))


class Hammer(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)  # Инициализация базового класса Sprite
        self.image = hammer  # Изображение молотка
        self.rect = self.image.get_rect()  # Прямоугольник для коллизий и отрисовки
        self.rect.top = y_pos  # Установка позиции Y
        self.rect.left = x_pos * section_width  # Установка позиции X (в пикселях)
        self.used = False  # Флаг, указывающий, был ли молоток подобран

    def draw(self):
        """Отрисовка молотка и проверка коллизии с игроком."""
        if not self.used:  # Если молоток еще не подобран
            screen.blit(self.image, (self.rect[0], self.rect[1]))  # Отрисовка молотка
            if self.rect.colliderect(player.hitbox):  # Проверка коллизии с игроком
                self.kill()  # Удаление молотка
                player.hammer = True  # Игрок теперь держит молоток
                player.hammer_len = player.max_hammer  # Установка времени использования молотка
                self.used = True  # Молоток подобран


class Barrel(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)  # Инициализация базового класса Sprite
        self.image = pygame.Surface((50, 50))  # Временная поверхность для бочки
        self.rect = self.image.get_rect()  # Прямоугольник для коллизий и отрисовки
        self.rect.center = (x_pos, y_pos)  # Установка начальной позиции бочки
        self.y_change = 0  # Изменение позиции по Y (для падения)
        self.x_change = 1  # Изменение позиции по X (для движения влево/вправо)
        self.pos = 0  # Текущая позиция в анимации (для вращения бочки)
        self.count = 0  # Счетчик для управления анимацией
        self.oil_collision = False  # Флаг, указывающий, столкнулась ли бочка с масляной бочкой
        self.falling = False  # Флаг, указывающий, падает ли бочка
        self.check_lad = False  # Флаг для проверки коллизии с лестницей
        self.bottom = self.rect  # Нижний прямоугольник для проверки коллизий

    def update(self, fire_trig):
        """Обновление состояния бочки (движение, падение, коллизии)."""
        if self.y_change < 8 and not self.falling:  # Увеличение скорости падения
            barrel.y_change += 2
        # Проверка коллизий с платформами
        for i in range(len(plats)):
            if self.bottom.colliderect(plats[i]):
                self.y_change = 0  # Остановка падения
                self.falling = False  # Бочка больше не падает
        # Проверка коллизии с масляной бочкой
        if self.rect.colliderect(oil_drum):
            if not self.oil_collision:
                self.oil_collision = True
                if random.randint(0, 4) == 4:  # Случайный шанс активации огня
                    fire_trig = True
        # Управление движением бочки
        if not self.falling:
            if row5_top >= self.rect.bottom or row3_top >= self.rect.bottom >= row4_top or row1_top > self.rect.bottom >= row2_top:
                self.x_change = 3  # Движение вправо
            else:
                self.x_change = -3  # Движение влево
        else:
            self.x_change = 0  # Остановка движения при падении
        # Обновление позиции бочки
        self.rect.move_ip(self.x_change, self.y_change)
        # Удаление бочки, если она вышла за пределы экрана
        if self.rect.top > screen_height:
            self.kill()
        # Управление анимацией вращения бочки
        if self.count < 15:
            self.count += 1
        else:
            self.count = 0
            if self.x_change > 0:  # Вращение вправо
                if self.pos < 3:
                    self.pos += 1
                else:
                    self.pos = 0
            else:  # Вращение влево
                if self.pos > 0:
                    self.pos -= 1
                else:
                    self.pos = 3
        # Обновление нижнего прямоугольника для коллизий
        self.bottom = pygame.rect.Rect((self.rect[0], self.rect.bottom), (self.rect[2], 3))
        return fire_trig  # Возвращение флага активации огня

    def check_fall(self):
        """Проверка, должна ли бочка начать падать (например, при столкновении с лестницей)."""
        already_collided = False
        below = pygame.rect.Rect((self.rect[0], self.rect[1] + section_height), (self.rect[2], section_height))
        for lad in lads:  # Проверка коллизии с лестницами
            if below.colliderect(lad) and not self.falling and not self.check_lad:
                self.check_lad = True
                already_collided = True
                if random.randint(0, 60) == 60:  # Случайный шанс начать падение
                    self.falling = True
                    self.y_change = 4
        if not already_collided:
            self.check_lad = False

    def draw(self):
        """Отрисовка бочки с учетом ее текущего состояния (вращение)."""
        screen.blit(pygame.transform.rotate(barrel_img, 90 * self.pos), self.rect.topleft)


class Flame(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)  # Инициализация базового класса Sprite
        self.image = fireball  # Изображение огненного шара
        self.rect = self.image.get_rect()  # Прямоугольник для коллизий и отрисовки
        self.rect.center = (x_pos, y_pos)  # Установка начальной позиции огненного шара
        self.pos = 1  # Текущая позиция в анимации (1 или -1 для смены кадров)
        self.count = 0  # Счетчик для управления анимацией
        self.x_count = 0  # Счетчик для управления изменением направления по X
        self.x_change = 2  # Изменение позиции по X (для движения влево/вправо)
        self.x_max = 4  # Максимальное количество шагов до смены направления по X
        self.y_change = 0  # Изменение позиции по Y (для падения или подъема)
        self.row = 1  # Текущий ряд, на котором находится огненный шар
        self.check_lad = False  # Флаг для проверки коллизии с лестницей
        self.climbing = False  # Флаг, указывающий, карабкается ли огненный шар по лестнице

    def update(self):
        """Обновление состояния огненного шара (движение, анимация, коллизии)."""
        if self.y_change < 3 and not self.climbing:  # Увеличение скорости падения
            flame.y_change += 0.25
        # Проверка коллизий с платформами
        for i in range(len(plats)):
            if self.rect.colliderect(plats[i]):
                flame.climbing = False  # Остановка карабкания
                flame.y_change = -4  # Отскок от платформы
        # Управление анимацией и изменением направления
        if self.count < 15:
            self.count += 1
        else:
            self.count = 0
            self.pos *= -1  # Смена кадра анимации
            if self.x_count < self.x_max:
                self.x_count += 1
            else:
                self.x_count = 0
                # Случайное изменение максимального количества шагов до смены направления
                if self.x_change > 0:
                    if self.row in [1, 3, 5]:  # Для нечетных рядов
                        self.x_max = random.randint(3, 6)
                    else:  # Для четных рядов
                        self.x_max = random.randint(6, 10)
                else:
                    if self.row in [1, 3, 5]:  # Для нечетных рядов
                        self.x_max = random.randint(6, 10)
                    else:  # Для четных рядов
                        self.x_max = random.randint(3, 6)
                self.x_change *= -1  # Смена направления движения по X
        # Управление анимацией огненного шара
        if self.pos == 1:
            if self.x_change > 0:
                self.image = fireball  # Огненный шар движется вправо
            else:
                self.image = pygame.transform.flip(fireball, True, False)  # Огненный шар движется влево
        else:
            if self.x_change > 0:
                self.image = fireball2  # Альтернативный кадр анимации (вправо)
            else:
                self.image = pygame.transform.flip(fireball2, True, False)  # Альтернативный кадр анимации (влево)
        # Обновление позиции огненного шара
        self.rect.move_ip(self.x_change, self.y_change)
        # Удаление огненного шара, если он выходит за пределы экрана
        if self.rect.top > screen_height or self.rect.top < 0:
            self.kill()

    def check_climb(self):
        """Проверка, должен ли огненный шар начать карабкаться по лестнице."""
        already_collided = False
        for lad in lads:  # Проверка коллизии с лестницами
            if self.rect.colliderect(lad) and not self.climbing and not self.check_lad:
                self.check_lad = True
                already_collided = True
                if random.randint(0, 120) == 120:  # Случайный шанс начать карабкание
                    self.climbing = True
                    self.y_change = -4  # Движение вверх по лестнице
        if not already_collided:
            self.check_lad = False
        # Определение текущего ряда, на котором находится огненный шар
        if self.rect.bottom < row6_y:
            self.row = 6
        elif self.rect.bottom < row5_y:
            self.row = 5
        elif self.rect.bottom < row4_y:
            self.row = 4
        elif self.rect.bottom < row3_y:
            self.row = 3
        elif self.rect.bottom < row2_y:
            self.row = 2
        else:
            self.row = 1

class Bridge:
    def __init__(self, x_pos, y_pos, length):
        """Инициализация платформы (моста)."""
        self.x_pos = x_pos * section_width  # Позиция X (в пикселях)
        self.y_pos = y_pos  # Позиция Y
        self.length = length  # Длина платформы (в секциях)
        self.top = self.draw()  # Верхняя линия платформы (для коллизий)

    def draw(self):
        """Отрисовка платформы."""
        line_width = 7  # Толщина линий
        platform_color = (225, 51, 129)  # Цвет платформы
        for i in range(self.length):
            # Координаты для отрисовки платформы
            bot_coord = self.y_pos + section_height
            left_coord = self.x_pos + (section_width * i)
            mid_coord = left_coord + (section_width * 0.5)
            right_coord = left_coord + section_width
            top_coord = self.y_pos
            # Отрисовка линий платформы
            pygame.draw.line(screen, platform_color, (left_coord, top_coord),
                             (right_coord, top_coord), line_width)
            pygame.draw.line(screen, platform_color, (left_coord, bot_coord),
                             (right_coord, bot_coord), line_width)
            pygame.draw.line(screen, platform_color, (left_coord, bot_coord),
                             (mid_coord, top_coord), line_width)
            pygame.draw.line(screen, platform_color, (mid_coord, top_coord),
                             (right_coord, bot_coord), line_width)
        # Верхняя линия платформы (для коллизий)
        top_line = pygame.rect.Rect((self.x_pos, self.y_pos), (self.length * section_width, 2))
        return top_line


class Ladder:
    def __init__(self, x_pos, y_pos, length):
        """Инициализация лестницы."""
        self.x_pos = x_pos * section_width  # Позиция X (в пикселях)
        self.y_pos = y_pos  # Позиция Y
        self.length = length  # Длина лестницы (в секциях)
        self.body = self.draw()  # Тело лестницы (для коллизий)

    def draw(self):
        """Отрисовка лестницы."""
        line_width = 3  # Толщина линий
        lad_color = 'light blue'  # Цвет лестницы
        lad_height = 0.6  # Высота одной секции лестницы
        for i in range(self.length):
            # Координаты для отрисовки лестницы
            top_coord = self.y_pos + lad_height * section_height * i
            bot_coord = top_coord + lad_height * section_height
            mid_coord = (lad_height / 2) * section_height + top_coord
            left_coord = self.x_pos
            right_coord = left_coord + section_width
            # Отрисовка линий лестницы
            pygame.draw.line(screen, lad_color, (left_coord, top_coord), (left_coord, bot_coord), line_width)
            pygame.draw.line(screen, lad_color, (right_coord, top_coord), (right_coord, bot_coord), line_width)
            pygame.draw.line(screen, lad_color, (left_coord, mid_coord), (right_coord, mid_coord), line_width)
        # Тело лестницы (для коллизий)
        body = pygame.rect.Rect((self.x_pos, self.y_pos - section_height),
                                (section_width, (lad_height * self.length * section_height + section_height)))
        return body


def draw_screen():
    """Отрисовка всех платформ и лестниц на экране."""
    platforms = []  # Список платформ
    climbers = []  # Список лестниц, по которым можно карабкаться
    ladder_objs = []  # Список объектов лестниц
    bridge_objs = []  # Список объектов платформ

    # Получение данных о лестницах и платформах из текущего уровня
    ladders = levels[active_level]['ladders']
    bridges = levels[active_level]['bridges']

    # Создание и отрисовка лестниц
    for ladder in ladders:
        ladder_objs.append(Ladder(*ladder))
        if ladder[2] >= 3:  # Если лестница достаточно длинная, добавляем в список для карабкания
            climbers.append(ladder_objs[-1].body)
    # Создание и отрисовка платформ
    for bridge in bridges:
        bridge_objs.append(Bridge(*bridge))
        platforms.append(bridge_objs[-1].top)

    return platforms, climbers


def draw_extras():
    """Отрисовка дополнительных элементов интерфейса (счет, бонусы, жизни и т.д.)."""
    screen.blit(font.render(f'I•{score}', True, 'white'), (3*section_width, 2*section_height))  # Текущий счет
    screen.blit(font.render(f'TOP•{high_score}', True, 'white'), (14 * section_width, 2 * section_height))  # Рекорд
    screen.blit(font.render(f'[  ][        ][  ]', True, 'white'), (20 * section_width, 4 * section_height))  # Панель
    screen.blit(font2.render(f'  M    BONUS     L ', True, 'white'), (20 * section_width + 5, 4 * section_height))  # Подписи
    screen.blit(font2.render(f'  {lives}       {bonus}        {active_level + 1}  ', True, 'white'),
                (20 * section_width + 5, 5 * section_height))  # Значения
    # Отрисовка принцессы Пич (анимация)
    if barrel_count < barrel_spawn_time / 2:
        screen.blit(peach1, (10 * section_width, row6_y - 6 * section_height))
    else:
        screen.blit(peach2, (10 * section_width, row6_y - 6 * section_height))
    # Отрисовка масляной бочки и возврат ее хитбокса
    oil = draw_oil()
    # Отрисовка бочек и Донки Конга
    draw_barrels()
    draw_kong()
    return oil


def draw_oil():
    """Отрисовка масляной бочки."""
    x_coord, y_coord = 4 * section_width, window_height - 4.5 * section_height  # Позиция бочки
    # Отрисовка основной части бочки
    oil = pygame.draw.rect(screen, 'blue', [x_coord, y_coord, 2 * section_width, 2.5 * section_height])
    # Отрисовка деталей бочки
    pygame.draw.rect(screen, 'blue', [x_coord - 0.1 * section_width, y_coord, 2.2 * section_width, .2 * section_height])
    pygame.draw.rect(screen, 'blue',
                     [x_coord - 0.1 * section_width, y_coord + 2.3 * section_height, 2.2 * section_width,
                      .2 * section_height])
    pygame.draw.rect(screen, 'light blue',
                     [x_coord + 0.1 * section_width, y_coord + .2 * section_height, .2 * section_width,
                      2 * section_height])
    pygame.draw.rect(screen, 'light blue',
                     [x_coord, y_coord + 0.5 * section_height, 2 * section_width, .2 * section_height])
    pygame.draw.rect(screen, 'light blue',
                     [x_coord, y_coord + 1.7 * section_height, 2 * section_width, .2 * section_height])
    # Надпись "OIL" на бочке
    screen.blit(font2.render('OIL', True, 'light blue'), (x_coord + .4 * section_width, y_coord + 0.7 * section_height))
    # Отрисовка красных кружков (индикаторов)
    for i in range(4):
        pygame.draw.circle(screen, 'red',
                           (x_coord + 0.5 * section_width + i * 0.4 * section_width, y_coord + 2.1 * section_height), 3)
    # Анимация огня над бочкой
    if counter < 15 or 30 < counter < 45:
        screen.blit(flames_img, (x_coord, y_coord - section_height))
    else:
        screen.blit(pygame.transform.flip(flames_img, True, False), (x_coord, y_coord - section_height))
    return oil


def draw_barrels():
    """Отрисовка бочек на экране."""
    screen.blit(pygame.transform.rotate(barrel_side, 90), (section_width * 1.2, 5.4 * section_height))
    screen.blit(pygame.transform.rotate(barrel_side, 90), (section_width * 2.5, 5.4 * section_height))
    screen.blit(pygame.transform.rotate(barrel_side, 90), (section_width * 2.5, 7.7 * section_height))
    screen.blit(pygame.transform.rotate(barrel_side, 90), (section_width * 1.2, 7.7 * section_height))


def draw_kong():
    """Отрисовка Донки Конга и его анимации."""
    phase_time = barrel_time // 4  # Время для каждой фазы анимации
    # Выбор изображения Донки Конга в зависимости от времени
    if barrel_spawn_time - barrel_count > 3 * phase_time:
        dk_img = dk2
    elif barrel_spawn_time - barrel_count > 2 * phase_time:
        dk_img = dk1
    elif barrel_spawn_time - barrel_count > phase_time:
        dk_img = dk3
    else:
        dk_img = pygame.transform.flip(dk1, True, False)  # Отражение изображения
        screen.blit(barrel_img, (250, 250))  # Отрисовка бочки
    screen.blit(dk_img, (3.5 * section_width, row6_y - 5.5 * section_height))  # Отрисовка Донки Конга


def check_climb():
    """Проверка, может ли игрок карабкаться по лестнице."""
    can_climb = False  # Может ли игрок карабкаться вверх
    climb_down = False  # Может ли игрок спускаться вниз
    # Прямоугольник для проверки коллизии под игроком
    under = pygame.rect.Rect((player.rect[0], player.rect[1] + 2 * section_height), (player.rect[2], player.rect[3]))
    for lad in lads:
        if player.hitbox.colliderect(lad) and not can_climb:
            can_climb = True  # Игрок может карабкаться вверх
        if under.colliderect(lad):
            climb_down = True  # Игрок может спускаться вниз
    # Управление состоянием карабкания
    if (not can_climb and (not climb_down or player.y_change < 0)) or \
            (player.landed and can_climb and player.y_change > 0 and not climb_down):
        player.climbing = False  # Игрок больше не карабкается
    return can_climb, climb_down


def barrel_collide(reset):
    """Проверка коллизии игрока с бочками."""
    global score
    # Прямоугольник для проверки коллизии под игроком
    under = pygame.rect.Rect((player.rect[0], player.rect[1] + 2 * section_height), (player.rect[2], player.rect[3]))
    for brl in barrels:
        if brl.rect.colliderect(player.hitbox):  # Если игрок столкнулся с бочкой
            reset = True  # Сброс игры
        elif not player.landed and not player.over_barrel and under.colliderect(brl):  # Если игрок перепрыгнул бочку
            player.over_barrel = True
            score += 100  # Начисление очков
    if player.landed:
        player.over_barrel = False  # Сброс флага перепрыгивания
    return reset


def reset():
    """Сброс игры при потере жизни или завершении уровня."""
    global player, barrels, flames, hammers, first_fireball_trigger, victory, lives, bonus
    global barrel_spawn_time, barrel_count
    pygame.time.delay(1000)  # Задержка перед сбросом
    # Удаление всех бочек, огненных шаров и молотков
    for bar in barrels:
        bar.kill()
    for flam in flames:
        flam.kill()
    for hams in hammers:
        hams.kill()
    # Восстановление молотков на уровне
    for hams in hammers_list:
        hammers.add(Hammer(*hams))
    lives -= 1  # Уменьшение количества жизней
    bonus = 6000  # Сброс бонусных очков
    player.kill()  # Удаление текущего игрока
    player = Player(250, window_height - 130)  # Создание нового игрока
    first_fireball_trigger = False  # Сброс флага первого огненного шара
    barrel_spawn_time = 360  # Сброс времени появления бочек
    barrel_count = barrel_spawn_time / 2  # Сброс счетчика бочек
    victory = False  # Сброс флага победы


def check_victory():
    """Проверка, достиг ли игрок цели уровня."""
    target = levels[active_level]['target']  # Получение данных о цели уровня
    # Создание прямоугольника для цели
    target_rect = pygame.rect.Rect((target[0]*section_width, target[1]), (section_width*target[2], 1))
    return player.bottom.colliderect(target_rect)  # Проверка коллизии игрока с целью


# Группы спрайтов для бочек, огненных шаров и молотков
barrels = pygame.sprite.Group()
flames = pygame.sprite.Group()
hammers = pygame.sprite.Group()

# Список молотков на уровне
hammers_list = levels[active_level]['hammers']
# Добавление молотков в группу
for ham in hammers_list:
    hammers.add(Hammer(*ham))

# Создание игрока
player = Player(250, window_height - 130)

# Получение прямоугольника для изображения "Игра окончена"
game_over_rect = game_over_image.get_rect()

# Основной игровой цикл
run = True

# Показ главного меню
main2.show_menu(screen, menu_image)

while run:
    screen.fill('black')  # Очистка экрана
    timer.tick(fps)  # Ограничение FPS

    # Проверка состояния игры
    if reset_game:  # Если требуется сброс игры
        if lives > 0:  # Если у игрока остались жизни
            reset()  # Сброс игры
            reset_game = False
        else:  # Если жизни закончились
            # Отображение изображения "Game Over"
            pygame.mixer.music.stop()  # Остановка музыки
            game_over_sound.play()  # Воспроизведение звука "Game Over"
            screen.fill('black')  # Очистка экрана
            # Отображение изображения "Game Over" по центру экрана
            screen.blit(game_over_image, (window_width // 2 - game_over_image.get_width() // 2, window_height // 2 - game_over_image.get_height() // 2))
            pygame.display.flip()  # Обновление экрана
            waiting = True
            while waiting:  # Ожидание действий игрока
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:  # Если игрок закрыл окно
                        run = False
                        waiting = False
                    if event.type == pygame.KEYDOWN:  # Если игрок нажал клавишу
                        if event.key == pygame.K_r:  # Если нажата клавиша "R" (рестарт)
                            pygame.mixer.music.play(-1)  # Воспроизведение музыки
                            lives = 6  # Сброс жизней
                            score = 0  # Сброс счета
                            reset_game = True  # Сброс игры
                            waiting = False
                        elif event.key == pygame.K_q:  # Если нажата клавиша "Q" (выход)
                            run = False
                            waiting = False
            continue  # Переход к следующей итерации цикла

    if victory:  # Если игрок победил
        # Отображение изображения выигрыша
        pygame.mixer.music.stop()  # Остановка музыки
        screen.fill('black')  # Очистка экрана
        # Отображение изображения победы по центру экрана
        screen.blit(win_image, (window_width // 2 - win_image.get_width() // 2, window_height // 2 - win_image.get_height() // 2))
        victory_sound.play()  # Воспроизведение звука победы
        pygame.display.flip()  # Обновление экрана
        
        waiting = True
        while waiting:  # Ожидание действий игрока
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Если игрок закрыл окно
                    run = False
                    waiting = False
                if event.type == pygame.KEYDOWN:  # Если игрок нажал клавишу
                    if event.key == pygame.K_r:  # Если нажата клавиша "R" (рестарт)
                        pygame.mixer.music.play(-1)  # Воспроизведение музыки
                        lives = 6  # Сброс жизней
                        score = 0  # Сброс счета
                        reset()  # Сброс игры
                        waiting = False
                    elif event.key == pygame.K_q:  # Если нажата клавиша "Q" (выход)
                        run = False
                        waiting = False
            continue

    # Уменьшение бонусных очков со временем
    if counter < 60:
        counter += 1
    else:
        counter = 0
        if bonus > 0:
            bonus -= 100

    # Отрисовка платформ, лестниц и дополнительных элементов
    plats, lads = draw_screen()
    oil_drum = draw_extras()
    climb, down = check_climb()  # Проверка, может ли игрок карабкаться
    victory = check_victory()  # Проверка победы

    # Логика появления бочек
    if barrel_count < barrel_spawn_time:
        barrel_count += 1
    else:
        barrel_count = random.randint(0, 120)  # Случайное время до следующей бочки
        barrel_time = barrel_spawn_time - barrel_count
        barrel = Barrel(270, 270)  # Создание новой бочки
        barrels.add(barrel)  # Добавление бочки в группу
        if not first_fireball_trigger:  # Если это первый огненный шар
            flame = Flame(5 * section_width, window_height - 4 * section_height)  # Создание огненного шара
            flames.add(flame)  # Добавление огненного шара в группу
            first_fireball_trigger = True  # Установка флага

    # Обработка бочек
    for barrel in barrels:
        barrel.draw()  # Отрисовка бочки
        barrel.check_fall()  # Проверка, должна ли бочка начать падать
        fireball_trigger = barrel.update(fireball_trigger)  # Обновление состояния бочки
        if barrel.rect.colliderect(player.hammer_box) and player.hammer:  # Если игрок ударил бочку молотком
            barrel.kill()  # Удаление бочки
            score += 500  # Начисление очков

    # Логика появления огненных шаров
    if fireball_trigger:
        flame = Flame(5 * section_width, window_height - 4 * section_height)  # Создание огненного шара
        flames.add(flame)  # Добавление огненного шара в группу
        fireball_trigger = False  # Сброс флага

    # Обработка огненных шаров
    for flame in flames:
        flame.check_climb()  # Проверка, должен ли огненный шар карабкаться
        if flame.rect.colliderect(player.hitbox):  # Если огненный шар столкнулся с игроком
            reset_game = True  # Сброс игры
    flames.draw(screen)  # Отрисовка огненных шаров
    flames.update()  # Обновление состояния огненных шаров

    # Обновление и отрисовка игрока
    player.update()
    player.draw()

    # Отрисовка молотков
    for ham in hammers:
        ham.draw()

    # Проверка коллизии игрока с бочками
    reset_game = barrel_collide(reset_game)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Если игрок закрыл окно
            run = False
        if event.type == pygame.KEYDOWN:  # Если игрок нажал клавишу
            if event.key == pygame.K_RIGHT and not player.climbing:  # Движение вправо
                player.x_change = 1
                player.dir = 1
            if event.key == pygame.K_LEFT and not player.climbing:  # Движение влево
                player.x_change = -1
                player.dir = -1
            if event.key == pygame.K_SPACE and player.landed:  # Прыжок
                current_volume = pygame.mixer.music.get_volume()  # Получение текущей громкости музыки
                pygame.mixer.music.set_volume(0.3)  # Уменьшение громкости музыки
                jump_sound = pygame.mixer.Sound('sounds/jump.wav')  # Загрузка звука прыжка
                pygame.mixer.music.set_volume(current_volume)  # Восстановление громкости музыки
                jump_sound.play()  # Воспроизведение звука прыжка
                jump_sound.set_volume(1.0)  # Установка громкости звука прыжка
                player.landed = False
                player.y_change = -6  # Придание игроку скорости для прыжка
            if event.key == pygame.K_UP:  # Карабкание вверх
                if climb:
                    player.y_change = -2
                    player.x_change = 0
                    player.climbing = True
            if event.key == pygame.K_DOWN:  # Карабкание вниз
                if down:
                    player.y_change = 2
                    player.x_change = 0
                    player.climbing = True
        if event.type == pygame.KEYUP:  # Если игрок отпустил клавишу
            if event.key == pygame.K_RIGHT:  # Остановка движения вправо
                player.x_change = 0
            if event.key == pygame.K_LEFT:  # Остановка движения влево
                player.x_change = 0
            if event.key == pygame.K_UP:  # Остановка карабкания вверх
                if climb:
                    player.y_change = 0
                if player.climbing and player.landed:
                    player.climbing = False
            if event.key == pygame.K_DOWN:  # Остановка карабкания вниз
                if climb:
                    player.y_change = 0
                if player.climbing and player.landed:
                    player.climbing = False

    pygame.display.flip()  # Обновление экрана

pygame.quit()  # Завершение работы Pygame