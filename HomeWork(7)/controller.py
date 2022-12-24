from module_view import *
from module_menu import menu
from module_changing_the_day_of_the_week import *

def do_it():
    while True:
        days_week = \
            [
                ['понедельник', 'вторник', 0, 7],
                ['вторник', 'среда', 1, 5],
                ['среда', 'четверг', 2, 6],
                ['четверг', 'пятница', 3, 4],
                ['пятница', 'конец', 4, 6]
            ]

        print()
        result_menu = menu()

        if result_menu == 1:
            print_file()
            print()
            input('Нажмите Enter для того , что бы попасть в меню и продолжить работу.')


        elif result_menu == 2:
            print()
            day = input('На какой день недели вы хотите посмотреть расписание? (Например: "Понедельник"): ')
            if day.lower() == days_week[0][0]:
                print_day(days_week[0][0].capitalize(), days_week[0][1].capitalize())
            elif day.lower() == days_week[1][0]:
                print_day(days_week[1][0].capitalize(), days_week[1][1].capitalize())
            elif day.lower() == days_week[2][0]:
                print_day(days_week[2][0].capitalize(), days_week[2][1].capitalize())
            elif day.lower() == days_week[3][0]:
                print_day(days_week[3][0].capitalize(), days_week[3][1].capitalize())
            elif day.lower() == days_week[4][0]:
                print_day(days_week[4][0].capitalize(), days_week[4][1])
            else:
                print('Ошибка. Вы ввели что то не то...')
                continue

            input('Нажмите Enter для того , что бы попасть в меню и продолжить работу.')


        elif result_menu == 3:
            day = input('В каком дне недели хотите поменять расписание? (Например: "Понедельник"): ')
            if day.lower() == days_week[0][0]:
                print('Понедельник.')
                change_day(days_week[0][2], days_week[0][3])
            elif day.lower() == days_week[1][0]:
                print('Вторник.')
                change_day(days_week[1][2], days_week[1][3])
            elif day.lower() == days_week[2][0]:
                print('Среда.')
                change_day(days_week[2][2], days_week[2][3])
            elif day.lower() == days_week[3][0]:
                print('Четверг.')
                change_day(days_week[3][2], days_week[3][3])
            elif day.lower() == days_week[4][0]:
                print('Пятница.')
                change_day(days_week[4][2], days_week[4][3])
            else:
                print('Ошибка. Вы ввели что то не то...')
                continue

            input('Нажмите Enter для того , что бы попасть в меню и продолжить работу.')
