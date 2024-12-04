#Повтори 2 [Вперёд 11 Направо 90 Вперёд 17 Направо 90]
#Поднять хвост
#Вперёд 7 Налево 90 Назад 1 Направо 90
#Опустить хвост
#Повтори 2 [Вперёд 15 Направо 90 Вперёд 7 Направо 90]





from turtle import *

tracer(0)
screensize(2000, 2000)
left(90)
down()
r = 30

# Рисование первого прямоугольника
for i in range(2):
    forward(11 * r)
    right(90)
    forward(17 * r)
    right(90)

up()
forward(7 * r)
left(90)
back(r * 1)
right(90)
down()

# Рисование второго прямоугольника
for i in range(2):
    forward(15 * r)
    right(90)
    forward(7 * r)
    right(90)

up()

# Рисование точек
for x in range(-30, 21):  # Изменено на -30 до 20
    for y in range(-30, 30):  # Изменено на -30 до 20
        goto(x * r, y * r)
        dot(3, 'red')

update()  # Обновление экрана после рисования
exitonclick()

