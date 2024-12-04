#Повтори 9 [Вперёд 22 Направо 90 Вперед 6 Направо 90]
#Поднять хвост
#Вперед 1 Направо 90 Вперёд 5 Налево 90
#Опустить хвост
#Повтори 9 [Вперёд 53 Направо 90 Вперёд 75 Направо 90]


from turtle import *
tracer()
screensize(1000,1000)
left(90)
r = 20
down()
for i in range(9):
    forward(22 * r)
    right(90)
    forward(6 * r)
    right(90)
up()
forward(r * 1)
right(90)
forward(5 * r)
left(90)
down()
for i in range(9):
    forward(53 * r)
    right(90)
    forward(75 * r)
    right(90)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * r, y * r)
        dot(5, 'red')
update()
exitonclick()
