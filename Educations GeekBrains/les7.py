# coding : utf-8

import turtle
import random

turtle.circle(30)
turtle.speed(0)

answer = ''
while answer != 'n':
    answer = turtle.textinput("Нарисовать окружность", "Y/N")
    if answer == 'y':
        turtle.penup()
        turtle.goto(random.randrange(-300, 300), random.randrange(-200, 200))
        turtle.pendown()
        turtle.fillcolor(random.random(), random.random(), random.random())
        turtle.begin_fill()
        turtle.circle(random.randrange(1, 100))
        turtle.end_fill()
    else:
        pass
