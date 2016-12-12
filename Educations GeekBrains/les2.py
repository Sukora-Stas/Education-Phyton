# coding: utf-8
import os
import shutil
import sys
import psutil

print("Python, my first step")
print("Hello, my friend")
name = input("What your name: ")
print(name, ", nice to meet you, I glad to see you")

answer = ''  # пустая строка для сравнения с while

while answer != 'Q' or 'q':
    answer = input("Would you like to work? (Y/N/Q)")
    if answer == 'Y' or 'y':
        print("Good news!")
        print("I can:")
        print("[1] - show files list")
        print(
            "[2] - show information about sistem: name carrent directiry, platform (OS), coding of file system, user login, number CPU")
        print("[3] - show process list")
        print("[4] - catalog instaling python")
        print("[5] - duplication all files in current directory")
        print("[6] - duplication chosen files in current directory")
        print("[7] - delete chosen files in current directory")
        do = int(input("schoose nomber: "))

        if do == 1:
            print("Show files list:", os.listdir())
        elif do == 2:
            print("Information about sistem:")
            print("- name carrent directiry:", os.getcwd())
            print("- platform (OS):", sys.platform)
            print("- coding of file system:", sys.getdefaultencoding())
            print("- user login:", os.getlogin())
            print("- number CPU:", psutil.cpu_count())
        elif do == 3:
            print("Show process list:", psutil.pids())
        elif do == 4:
            print("Catalog instaling python:", sys.exec_prefix)
        elif do == 5:
            print("Duplication all files in current directory")
            file_list = os.listdir()
            i = 0  # присваиваем значению переменной i равной нулю
            while i < len(file_list):
                newfile = file_list[i] + '.dupl'
                shutil.copy(file_list[i], newfile)
                i += 1
        elif do == 6:
            print("Duplication chosen files in current directory")
            file_list = os.listdir()
            i = 0
            print("Which file would you like duplication?")
            while i < len(file_list):
                print('[', i, '] - ' + file_list[i])
                i = i + 1
            i = int(input("Schoose nomber: "))
            newfile = file_list[i] + '.dupl'
            shutil.copy(file_list[i], newfile)
            print("File is created in the current directory")
        elif do == 7:
            print("Delete chosen files in current directory")
            file_list = os.listdir()
            i = 0
            print("which file would you like delete?")
            while i < len(file_list):
                print('[', i, '] - ' + file_list[i])
                i += 1
            i = int(input("schoose nomber: "))
            os.remove(file_list[i])
            print("File is deleted from the current directory")
        else:
            pass
    elif answer == 'N' or 'n':
        print("До свидания!")
