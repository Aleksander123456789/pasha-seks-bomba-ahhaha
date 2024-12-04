from turtle import *
tracer(0)
left(90)
r = 10


for i in range(10):
    forward(22 * r)
    right(90)
    forward(16*r)
    right(90)
up()
forward(1*r)
right(90)
forward(1*r)
left(90)
down()
for i in range(10):
    forward(72*r)
    right(90)
    forward(79*r)
    right(90)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*r, y*r)
        dot(5, 'green')
update()        