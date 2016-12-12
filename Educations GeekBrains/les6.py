# coding : utf-8
# PEP-8

import os
import sys
import shutil
import psutil  # сторонний


def makeList(array):  # функция построчного вывода списка
    i = 0
    while i < len(array):
        print(i, array[i])
        i += 1
    return


def makeList1(array):  # функция построчного вывода списка
    i = 0
    for f in array:
        print(i, f)
        i += 1
    return


def deleteDupl(filelist):
    i = 0
    d = 0
    while i < len(filelist):
        if filelist[i].endswith('.dupl'):
            os.remove(dir + filelist[i])  # функция удаления дубликатов
            i += 1
            d += 1
        else:
            i += 1
    print('\nДубликатов удалено: ' + str(d))
    return


print('I am Pythi (just like the Siri) xD')
print('by .gx')
name = input('\nВаше имя: ')
print('\nДоброго времени ' + name)
answer_yes = ['y', 'yes', 'н', 'нуы', 'ok', 'okey', 'щл', 'щлун']
answer_no = ['n', 'no', 'т', 'тщ']
answer = input('Поработаем? (Y/N) ').lower()  # с помощью .lower() переводим ответ в нижний регистр

while answer not in answer_yes + answer_no:
    print(name + ', извините, но вы ввели неизвестное мне значение.')
    answer = input('\nПоработаем? (Y/N) ')

while answer in answer_yes:
    print('\nОтлично!')
    print('Мы можем:')
    print(' [1] - производить вычисления с двумя числами;')
    print(' [2] - вывести список файлов необходимой директории;')
    print(' [3] - вывести информацию о системе;')
    print(' [4] - вывести список запущенных процессов;')
    print(' [5] - сделать дубликат файла из определённой директории;')
    print(' [6] - продублировать все файлы в определённой директории;')
    print(' [-6] - удалить все дубликаты файлов определённой директории созданные через меню 5 и 6;')

    do = int(input('Укажите номер действия: '))

    if do == 1:

        print(' [1] - cложение двух чисел')
        print(' [2] - вычитание двух чисел')
        print(' [3] - умножение двух чисел')
        print(' [4] - деление двух чисел')
        do = int(input('Укажите номер действия: '))

        if do == 1:
            a = int(input('\nВведите первое слогаемое: '))
            b = int(input('Введите второе слогаемое: '))
            sum = a + b
            print('Сумма чисел ', a, ' + ', b, ' = ', sum)
        elif do == 2:
            a = int(input('\nВведите уменьшаемое: '))
            b = int(input('Введите вычитаемое: '))
            sum = a - b
            print('Разность чисел ', a, ' - ', b, ' = ', sum)
        elif do == 3:
            a = int(input('\nВведите первый множитель: '))
            b = int(input('Введите второй множитель: '))
            sum = a * b
            print('Произведение чисел ', a, ' * ', b, ' = ', sum)
        elif do == 4:
            a = int(input('\nВведите делимое: '))
            b = int(input('Введите делитель: '))
            sum = a / b
            print('Частное значение чисел ', a, ' / ', b, ' = ', sum)
        else:
            print('\nНеизвестная операция')

    elif do == 2:
        print('\n' + r'Введите необходимую директорию (c:\\test\):')
        dir = input()
        file_list = os.listdir(dir)

        print('\nСписок файлов')
        makeList1(file_list)

    elif do == 3:
        print('\nЛогин пользователя:', os.getlogin())
        print('Платформа:', sys.platform)
        print('Версия:', sys.version)
        print('Колличество ядер процессора:', os.cpu_count())
        print('Кодировка файловой системы:', sys.getfilesystemencoding())
        print('Директория запущенного файла:', os.getcwd())
    elif do == 4:
        print('\n', psutil.pids())
    elif do == 5:
        print('\nДублирование файла')
        print(r'Введите необходимую директорию (c:\\test\):')
        dir = input()

        answer_sub = 'y'
        while answer_sub in answer_yes:
            file_list = os.listdir(dir)
            print('\nВыберите файл:')
            makeList(file_list)

            file_num = int(input('\nВведите номер файла: '))
            if os.path.isfile(dir + file_list[file_num]):
                file_dup = file_list[file_num] + '.dupl'
                shutil.copy(dir + file_list[file_num], dir + file_dup)  # копирование

                if os.path.exists(dir + file_dup):
                    print('\nДубликат сделан!')
                else:
                    print('\nЧто-то пошло не так.')
            else:
                print('Ошибка. Копировать можно только файлы.')

            answer_sub = input('\nПродожить работу в этой директории? (Y/N) ').lower()

    elif do == 6:
        print('\n' + r'Дублирование всех файлов директории (c:\\test\):')
        dir = input()
        file_list = os.listdir(dir)

        print('\nСписок файлов:')
        makeList(file_list)

        answer_sub = input('\nСоздаём дубликаты? (Y/N) ').lower()

        if answer_sub in answer_yes:
            i = 0
            while i < len(file_list):
                if os.path.isfile(dir + file_list[i]):
                    newfile = file_list[i] + '.dupl'
                    shutil.copy(dir + file_list[i], dir + newfile)  # копирование

                if os.path.exists(dir + newfile):
                    if i == len(file_list) - 1:
                        print('\nДубликаты готовы!')
                else:
                    print('\nЧто-то пошло не так.')
                i += 1
        else:
            pass

    elif do == -6:
        print('\nУдаление всех дубликатов созданных через меню 5 и 6')
        print(r'Введите необходимую директорию (c:\\test\):')
        dir = input()
        file_list = os.listdir(dir)

        print('\nСписок файлов:')
        makeList(file_list)

        answer_sub = input('\nУдаляем дубликаты? (Y/N) ').lower()

        if answer_sub in answer_yes:

            deleteDupl(file_list)

        else:
            pass
    else:
        print('\nНеизвестная операция')

    answer = input('\nПоработаем ещё ' + name + '? (Y/N)').lower()

    while answer not in answer_yes + answer_no:
        print(name + ', извините, но вы ввели неизвестное мне значение.')
        answer = input('\nПоработаем ещё? (Y/N)')

print('\nДо свидания =(')
input()
