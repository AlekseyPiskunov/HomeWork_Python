# Игра: Морской бой

from random import randint as rd
import time

# Инициализация поля.
def add_field():
    field = []
    for index in range(5):
        field.append([index])
        for _ in range(4):
            field[index].append(0)
    field[0][0] = 0
    field[0][1] = 1
    field[0][2] = 2
    field[0][3] = 3
    field[0][4] = 4
    return field

# Вывод поля на экран
def print_field(field):
    for item in field:
        print(item)

# Проверка на ввод.
def examination(inputText):
    button = True
    while button:
        try:
            value = int(input(f'{inputText}'))
            button = False
        except ValueError:
            print('Важно вводить числа!')
    return value

# Твоё игровое поле.
user_field = add_field()

# Игровое поле противника.
computer_field = add_field()

# Фэйковое поле для пользователя. Что бы не показывать поле с кораблём противника.
fake_field = add_field()

print('Твоё поле: ')
print_field(user_field)

print('Укажите координаты по которым будет расположен ваш Корабль.')
user_first_coordinate_ship = examination('Введите первую координату по вертикали (от 1 до 4): ')
user_second_coordinate_ship = examination('Введите вторую координату по вертикали (от 1 до 4): ')
user_field[user_first_coordinate_ship][user_second_coordinate_ship] = 1

# Компьютер выбирает расположения своего корабля на своём поле.
computer_first_coordinate_ship = rd(1, 4)
computer_second_coordinate_ship = rd(1, 4)
computer_field[computer_first_coordinate_ship][computer_second_coordinate_ship] = 1

print('\nТвоё поле с расположенным Кораблём:')
print_field(user_field)

while True:
    computer_first_coordinate_for_attack = rd(1, 4)
    computer_second_coordinate_for_the_attack = rd(1, 4)
    if user_field[computer_first_coordinate_for_attack][computer_second_coordinate_for_the_attack] == 2:
        continue
    else:
        user_field[computer_first_coordinate_for_attack][computer_second_coordinate_for_the_attack] = 2

    print('\nПодождите, идёт ход противника.')
    time.sleep(5)

    print('\nТвоё поле:')
    print_field(user_field)

    if computer_first_coordinate_for_attack == user_first_coordinate_ship and computer_second_coordinate_for_the_attack == user_second_coordinate_ship:
        print('Компьютер убил ваш Корабль!\nВы проиграли!')
        break
    else:
        print(f'Компьютер промазал. Он стрелял по координатам ({computer_first_coordinate_for_attack},{computer_second_coordinate_for_the_attack})')

    print('\nПоле противника:')
    print_field(fake_field)

    print('Ваш ход! Выберите координаты по которым будет выполнен выстрел.')
    user_first_coordinate_for_attack = examination('Введите первую координату по вертикали (от 1 до 4): ')
    user_second_coordinate_for_attack = examination('Введите вторую координату по горизонтали (от 1 до 4): ')
    computer_field[user_first_coordinate_for_attack][user_second_coordinate_for_attack] = 2
    fake_field[user_first_coordinate_for_attack][user_second_coordinate_for_attack] = 2

    if user_first_coordinate_for_attack == computer_first_coordinate_ship and user_second_coordinate_for_attack == computer_second_coordinate_ship:
        print('Поподание! Вы утопили Корабль противника! Победа!')
        break
    else:
        print('Ты промазал.')