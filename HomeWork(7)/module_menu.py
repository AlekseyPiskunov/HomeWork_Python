# Проверка ввода числа.
def examination(input_value):
    button = True
    while button:
        try:
            result = int(input(f'{input_value}'))
            button = False
        except ValueError:
            print('Ошибка. Вы должны ввести число!')
    return result

# Инициализация меню.
def menu():
    print(
        'Меню\nЭлектронное расписание 8"б" класса!\n',
        'Вы можете:\n',
        '1) Посмотреть расписание всей недели.\n',
        '2) Посмотреть расписание определённого дня недели.\n',
        '3) Изменить уроки в выбранном дне недели.',
    )
    menu_result = examination('Введите один из вариантов (1, 2 или 3): ')
    while menu_result < 1 or menu_result > 3:
        menu_result = examination('Введите один из вариантов (1, 2 или 3): ')
    return menu_result
