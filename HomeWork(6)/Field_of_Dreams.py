# Игра: Поле чудес

import random

# Инициализация слов.
words = ['салат', 'космос', 'планета', 'география', 'физика',
         'крыло', 'самолёт', 'английский', 'рулетка', 'москва',
         'город', 'кино', 'фрукты', 'мультик', 'герой', 'катер',
         'значение', 'слово', 'гора', 'кролик', 'кошка', 'собака',
         'зонтик', 'велосипед', 'арматура', 'кресло', 'самокат']

# Компьютер выбирает слово.
hidden_word = random.choice(words)

# Инициализация пустого/собранного слова для демонстрации на экран.
def creating_a_demonstrative_word(length):
    data = [i for i in range(1, length + 1)]
    word = list(map(str, data))
    return word

demonstrative_word = creating_a_demonstrative_word(len(hidden_word))

print(f'Посмотрите на кол-во букв в слове: {"".join(demonstrative_word)}')

while True:
    main_question = input('Готовы назвать слово? ("Да"/"Нет"): ')

    if main_question.lower() == 'да':
        result_word = input('Назовите целиком слово: ')
        if result_word.lower() == hidden_word:
            print('Поздравляю! Вы угадали слово!')
            break
        else:
            print('Увы , вы не угадали!')
    else:
        result_letter = input('Тогда назовите букву: ')
        if result_letter.lower() in hidden_word:
            if hidden_word.count(result_letter.lower()) > 1:
                for i in range(len(hidden_word)):
                    if hidden_word[i] == result_letter.lower():
                        demonstrative_word[i] = result_letter.lower()
            index = hidden_word.index(result_letter.lower())
            demonstrative_word[index] = result_letter.lower()
            print(f'Отлично , такая буква есть!\nПосмотрите на ваш результат: {"".join(demonstrative_word)}')
        else:
            print('Увы , вы не угадали букву!')
            continue