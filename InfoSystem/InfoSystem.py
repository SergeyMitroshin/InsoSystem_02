﻿
# Точка входа программы
# Здесь будет вызываться головной метод из класса DataManager
# Что-то вроде init_system()

from Menutext import *
import os
import click
from IO_system import IO_system
from DataManager import DataManager
from TypeOfDepartments import TypeOfDepartments
import QueryManager

data_manager = DataManager()
def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')


def zaglushka():
    print('Здесь могла бы быть ваша реклама')


def menu(list_command: dict, invate: str):
    flag = True
    while flag:
        print(invate)
        command = input('Команда: > ')
        if command in list_command:
            list_command[command]()
            if command != '9':
                click.pause()
        elif command == "0" or command == '':
            flag = False
        else:
            print('Такой команды нет!!!')


def sub_menu_print_base():

    def print_per():
        IO_system.print_a_list_with_indexes(data_manager.persons)

    def print_pos():
        IO_system.print_a_list_with_indexes(data_manager.positions)

    def print_emp():
        IO_system.print_a_list_with_indexes(data_manager.employees)

    print_command = {'1': print_per,
                     '2': print_pos, '3': print_emp, '9': clear}
    menu(print_command, menu_print)


def sub_menu_append():
    append_command = {'1': data_manager.add_person,
                      '2': data_manager.add_employee, '3': data_manager.change_department, '4': data_manager.change_salary, '9': clear}
    menu(append_command, menu_append)


def sub_menu_delete():
    delete_command = {'1': data_manager.delete_employee, '2': zaglushka, '9': clear}
    menu(delete_command, menu_delete)


def sub_menu_query():
    def query_by_dep():
        print(' Выберите отдел:')
        selectedDepartment = IO_system.select_from_enum(TypeOfDepartments, ' Введите код отдела: ')
        IO_system.print_a_list_with_indexes(QueryManager.employees_from_department(  TypeOfDepartments(selectedDepartment), data_manager))
    query_command = {'1': query_by_dep, '2': zaglushka, '9': clear}
    menu(query_command, menu_query)


def main():

    try:
        isOk = IO_system.recover_data_base('statement',data_manager,'.txt')

        if not isOk:

            print('  Ошибка восстановления базы данных из файла')

            data_manager.init_system()

    except:
        data_manager.init_system()

    head_command = {'1': sub_menu_print_base, '2': sub_menu_append,
                    '3': sub_menu_delete, '4': sub_menu_query, '9': clear}
    menu(head_command, menu_head)
    IO_system.save_data_base('statement', data_manager, '.txt')

if __name__ == '__main__':
    main()
