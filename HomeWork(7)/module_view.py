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
def print_day(start, stop):
    with open('file.txt', 'r', encoding='utf-8') as data:
        text = data.read()
        source = text.find(start)
        finish = text.find(stop)
        print()
        print(text[source: finish:])
