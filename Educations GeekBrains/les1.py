# coding: utf-8

import os

print("Hello world")
name = input("Ваше имя: ")
print(name, " добро пожаловать в мир Phyton")

# PEP-8
while answer != 'q':
    answer = input("Давайте поработаем? (Y/N) ")
    if answer == 'Y':
        print("Продолжаем!")
        print("Я умею:")
        print(" [1] - выведу список файлов")
        print(" [2] - выведу информацию о системе")
        do = int(input("Укажите номер действия: "))
        if do == 1:
            print(os.listdir())
        elif do == 2:
            pass
        else:
            pass
    elif answer == 'N':
        print("До свидания!")
    else:
        print("Неизвестный ответ")
