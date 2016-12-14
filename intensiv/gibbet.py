# coding: utf-8

# SublimeREPL

# Комментарий

import random
import sys
import turtle  # apt-get install python3-tk


# time.sleep(sec)

# PEP-8

def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def draw_line(from_x, from_y, to_x, to_y):
    ''' Функция рисования линии
    '''
    gotoxy(from_x, from_y)
    turtle.goto(to_x, to_y)


def draw_circle(x, y, r):
    gotoxy(x, y)
    turtle.circle(r)


def draw_gibbet(step):
    if step == 1:
        draw_line(-160, -100, -160, 80)
    elif step == 2:
        draw_line(-160, 80, -80, 80)
    elif step == 3:
        draw_line(-160, 40, -120, 80)
    elif step == 4:
        draw_line(-100, 80, -100, 40)
    elif step == 5:
        draw_circle(-100, 0, 20)
    elif step == 6:
        draw_line(-100, 0, -100, -50)
    elif step == 7:
        draw_line(-100, -10, -120, -20)
    elif step == 8:
        draw_line(-100, -10, -80, -20)
    elif step == 9:
        draw_line(-100, -50, -120, -60)
    elif step == 10:
        draw_line(-100, -50, -80, -60)


x = random.randint(1, 101)

print("Привет!")
print("Случайное число: ", x)

turtle.speed(-10)

turtle.color('green')

gotoxy(-200, 250)
turtle.write('Игра "Виселица". Загадано число от 1 до 100',
             font=('Arial', 20, 'normal'))

answer = turtle.textinput("Хотите играть", "y/n")

if answer == 'n':
    sys.exit(33)

answer = turtle.textinput("Давать подсказки", "y/n")

hints = answer == 'y'
# if answer == 'y':
#     hints = True

try_count = 0

while True:
    number = turtle.numinput("Попробуйте угадать", "Число", 0, 0, 100)

    if hints:
        gotoxy(200, 200 - 15 * try_count)
        turtle.color("blue")
        if number > x:
            turtle.write(str(number) + " Загаданное число меньше")
        else:
            turtle.write(str(number) + " Загаданное число больше")

    if number == x:
        gotoxy(-150, 200)
        turtle.color("blue")  # (123, 134, 57)
        turtle.write("Ура! Вы угадали!", font=('Arial', 20, 'normal'))
        break
    else:
        gotoxy(-150, 100)
        turtle.color("red")  # (123, 134, 57)
        turtle.write("Неверно!", font=('Arial', 16, 'normal'))
        try_count += 1
        draw_gibbet(try_count)

        if try_count == 10:
            gotoxy(-150, 150)
            turtle.color("brown")  # (123, 134, 57)
            turtle.write("Вы проиграли!", font=('Arial', 22, 'normal'))
            break


            # from tk import SimpleDialog
            # SimpleDialog.input()      Python 2

            # input("Нажмите ENTER")      # raw_input()
