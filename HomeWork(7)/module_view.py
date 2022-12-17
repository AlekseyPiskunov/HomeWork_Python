# Вопрос с ответом (Да/Нет)
def examination_yes_no(result):
    while result.lower() != 'да' and result.lower() != 'нет':
        result = input('Вы должны ввести либо "Да" либо "Нет", попробуйте ещё раз: ')
    return result.lower()

# Функция чтения файла.
def print_file():
    with open('file.txt', 'r', encoding='utf-8') as data:
        print()
        print(data.read())

# Печать расписания на Понедельник.
def print_monday():
    with open('file.txt', 'r', encoding='utf-8') as data:
        text = data.read()
        start = text.find('Понедельник')
        finish = text.find('Вторник')
        print()
        print(text[start: finish:])

# Печать расписания на Вторник.
def print_tuesday():
    with open('file.txt', 'r', encoding='utf-8') as data:
        text = data.read()
        start = text.find('Вторник')
        finish = text.find('Среда')
        print()
        print(text[start: finish:])

# Печать расписания на Среду.
def print_wednesday():
    with open('file.txt', 'r', encoding='utf-8') as data:
        text = data.read()
        start = text.find('Среда')
        finish = text.find('Четверг')
        print()
        print(text[start: finish:])

# Печать расписания на Четверг.
def print_thursday():
    with open('file.txt', 'r', encoding='utf-8') as data:
        text = data.read()
        start = text.find('Четверг')
        finish = text.find('Пятница')
        print()
        print(text[start: finish:])

# Печать расписания на Пятницу.
def print_friday():
    with open('file.txt', 'r', encoding='utf-8') as data:
        text = data.read()
        start = text.find('Пятница')
        print()
        print(text[start::])