from module_view import *
from module_menu import menu
from module_changing_the_day_of_the_week import *

def di_it():
    while True:
        days_week = \
            [
                ['понедельник', 'вторник'],
                ['вторник', 'среда'],
                ['среда', 'четверг'],
                ['четверг', 'пятница'],
                ['пятница']
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
                print_day(days_week[4][0].capitalize(), 'конец')
            else:
                print('Ошибка. Вы ввели что то не то...')

            input('Нажмите Enter для того , что бы попасть в меню и продолжить работу.')

        elif result_menu == 3:
            day = input('В каком дне недели хотите поменять расписание? (Например: "Понедельник"): ')
            if day.lower() == 'понедельник':
                print('Понедельник.')
                change_on_monday()
            elif day.lower() == 'вторник':
                print('Вторник.')
                change_on_tuesday()
            elif day.lower() == 'среда':
                print('Среда.')
                change_on_wednesday()
            elif day.lower() == 'четверг':
                print('Четверг.')
                change_on_thursday()
            elif day.lower() == 'пятница':
                print('Пятница.')
                change_on_friday()
            else:
                print('Ошибка. Вы ввели что то не то...')

            input('Нажмите Enter для того , что бы попасть в меню и продолжить работу.')
