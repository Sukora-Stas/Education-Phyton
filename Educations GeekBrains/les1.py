# coding: utf-8

print("Hello world")
name = input("Ваше имя: ")
print(name, " добро пожаловать в мир Phyton")

answer = input("Давайте поработаем? (Y/N) ")

if answer == 'Y':
    print("Вам премия!")
elif answer == 'N':
    print("До свидания!")
else:
    print("Неизвестный ответ")