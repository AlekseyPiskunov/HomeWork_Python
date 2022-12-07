# Игра: Камень Ножницы Бумага

import random

list = ['Камень', 'Ножницы', 'Бумага']

while True:
    user = input('Введите один из вариантов - Камень, Ножницы или Бумага: ')
    computer = random.choice(list)
    print(f'Вы выбрали: {user}\nКомпьютер выбрал: {computer}')
    if user == computer:
        print(f'Ничья! Оба игрока выбрали: {computer}')
    elif user == 'Камень':
        if computer == 'Ножницы':
            print(f'Вы победили! Камень бьёт Ножницы.')
        else:
            print(f'Вы проиграли! Бумага оборачивает Камень.')
    elif user == 'Бумага':
        if computer == 'Камень':
            print(f'Вы выиграли! Бумага окутывает Камень.')
        else:
            print(f'Вы проиграли! Ножницы режут Бумагу.')
    elif user == 'Ножницы':
        if computer == 'Бумага':
            print(f'Вы выиграли! Ножницы режут Бумагу.')
        else:
            print(f'Вы проиграли! Камень бьёт Ножницы.')
    play_again = input('Будем играть ещё? ("Да"/"Нет"): ')
    if play_again.lower() != 'да':
        break