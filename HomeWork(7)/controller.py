from module_view import print_monday
from module_view import print_tuesday
from module_view import print_wednesday
from module_view import print_thursday
from module_view import print_friday
from module_view import print_file
from module_menu import menu
from module_changing_the_day_of_the_week import change_on_monday
from module_changing_the_day_of_the_week import change_on_tuesday
from module_changing_the_day_of_the_week import change_on_wednesday
from module_changing_the_day_of_the_week import change_on_thursday
from module_changing_the_day_of_the_week import change_on_friday

def di_it():
    while True:
        print()
        result_menu = menu()

        if result_menu == 1:
            print_file()
            print()
            input('Нажмите Enter для того , что бы попасть в меню и продолжить работу.')

        elif result_menu == 2:
            print()
            day = input('На какой день недели вы хотите посмотреть расписание? (Например: "Понедельник"): ')
            if day.lower() == 'понедельник':
                print_monday()
            elif day.lower() == 'вторник':
                print_tuesday()
            elif day.lower() == 'среда':
                print_wednesday()
            elif day.lower() == 'четверг':
                print_thursday()
            elif day.lower() == 'пятница':
                print_friday()

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

            input('Нажмите Enter для того , что бы попасть в меню и продолжить работу.')
