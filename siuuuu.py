import pygame
import math

# Инициализация Pygame
pygame.init()

# Установка размеров окна
width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Движение по пользовательской функции")

# Начальные координаты квадрата
x = 50
y = 50

# Начальная скорость и ускорение по оси y
speed_y = 0
acceleration_y = 0.02  # Уменьшенное ускорение

# Функция для движения по пользовательской функции
def custom_function(x):
    return 50 + 50 * math.sin(math.radians(x))

# Ввод времени в течение которого квадрат может двигаться
movement_time = int(input("Введите время в миллисекундах (например, 5000 для 5 секунд): "))

# Основной игровой цикл
run = True
start_time = pygame.time.get_ticks()  # Время начала движения квадрата
while run:
    win.fill((255, 255, 255))  # Очистка экрана

    # Рисование квадрата
    pygame.draw.rect(win, (255, 0, 0), (x, y, 50, 50))

    # Проверка времени движения квадрата
    current_time = pygame.time.get_ticks()
    if current_time - start_time < movement_time:
        # Обновление координат квадрата по пользовательской функции
        x += 0.3  # Уменьшенный шаг
        y = custom_function(x)

        # Применение ускорения к скорости по оси y
        speed_y += acceleration_y
        y += speed_y

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()  # Обновление экрана

pygame.quit()  # Выход из Pygame
