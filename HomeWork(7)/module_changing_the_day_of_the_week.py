# Функция изменения расписания на Понедельник.
def change_on_monday():
    with open('file.txt', 'r', encoding='utf-8') as data:
        res_text = data.read()
        start1 = res_text.find('Понедельник')
        stop1 = res_text.find('Вторник')
        start2 = res_text.find('Вторник')
        stop2 = res_text.find('Среда')
        start3 = res_text.find('Среда')
        stop3 = res_text.find('Четверг')
        start4 = res_text.find('Четверг')
        stop4 = res_text.find('Пятница')
        start5 = res_text.find('Пятница')
        week_days = \
            [
                res_text[start1: stop1:],
                res_text[start2: stop2:],
                res_text[start3: stop3:],
                res_text[start4: stop4:],
                res_text[start5::]
            ]

        monday = week_days[0]
        text = ''.join(monday)
        result_text = text.split('\n')
        index = 1
        for i in range(7):
            result_text.remove(result_text[index + 1])
            result_text.insert(index + 1, f'{index} урок: {input(f"Введите название {index} урока: ")}')
            index += 1
        result_text = '\n'.join(result_text)

        week_days.remove(week_days[0])
        week_days.insert(0, result_text)

    with open('file.txt', 'w', encoding='utf-8') as data:
        data.write(''.join(week_days))

# Функция изменения расписания на Вторник.
def change_on_tuesday():
    with open('file.txt', 'r', encoding='utf-8') as data:
        res_text = data.read()
        start1 = res_text.find('Понедельник')
        stop1 = res_text.find('Вторник')
        start2 = res_text.find('Вторник')
        stop2 = res_text.find('Среда')
        start3 = res_text.find('Среда')
        stop3 = res_text.find('Четверг')
        start4 = res_text.find('Четверг')
        stop4 = res_text.find('Пятница')
        start5 = res_text.find('Пятница')
        week_days = \
            [
                res_text[start1: stop1:],
                res_text[start2: stop2:],
                res_text[start3: stop3:],
                res_text[start4: stop4:],
                res_text[start5::]
            ]

        tuesday = week_days[1]
        text = ''.join(tuesday)
        result_text = text.split('\n')
        index = 1
        for i in range(5):
            result_text.remove(result_text[index + 1])
            result_text.insert(index + 1, f'{index} урок: {input(f"Введите название {index} урока: ")}')
            index += 1
        result_text = '\n'.join(result_text)

        week_days.remove(week_days[1])
        week_days.insert(1, result_text)

    with open('file.txt', 'w', encoding='utf-8') as data:
        data.write(''.join(week_days))

# Функция изменения расписания на Среду.
def change_on_wednesday():
    with open('file.txt', 'r', encoding='utf-8') as data:
        res_text = data.read()
        start1 = res_text.find('Понедельник')
        stop1 = res_text.find('Вторник')
        start2 = res_text.find('Вторник')
        stop2 = res_text.find('Среда')
        start3 = res_text.find('Среда')
        stop3 = res_text.find('Четверг')
        start4 = res_text.find('Четверг')
        stop4 = res_text.find('Пятница')
        start5 = res_text.find('Пятница')
        week_days = \
            [
                res_text[start1: stop1:],
                res_text[start2: stop2:],
                res_text[start3: stop3:],
                res_text[start4: stop4:],
                res_text[start5::]
            ]

        wednesday = week_days[2]
        text = ''.join(wednesday)
        result_text = text.split('\n')
        index = 1
        for i in range(6):
            result_text.remove(result_text[index + 1])
            result_text.insert(index + 1, f'{index} урок: {input(f"Введите название {index} урока: ")}')
            index += 1
        result_text = '\n'.join(result_text)

        week_days.remove(week_days[2])
        week_days.insert(2, result_text)

    with open('file.txt', 'w', encoding='utf-8') as data:
        data.write(''.join(week_days))


# Функция изменения расписания на Четверг.
def change_on_thursday():
    with open('file.txt', 'r', encoding='utf-8') as data:
        res_text = data.read()
        start1 = res_text.find('Понедельник')
        stop1 = res_text.find('Вторник')
        start2 = res_text.find('Вторник')
        stop2 = res_text.find('Среда')
        start3 = res_text.find('Среда')
        stop3 = res_text.find('Четверг')
        start4 = res_text.find('Четверг')
        stop4 = res_text.find('Пятница')
        start5 = res_text.find('Пятница')
        week_days = \
            [
                res_text[start1: stop1:],
                res_text[start2: stop2:],
                res_text[start3: stop3:],
                res_text[start4: stop4:],
                res_text[start5::]
            ]

        thursday = week_days[3]
        text = ''.join(thursday)
        result_text = text.split('\n')
        index = 1
        for i in range(4):
            result_text.remove(result_text[index + 1])
            result_text.insert(index + 1, f'{index} урок: {input(f"Введите название {index} урока: ")}')
            index += 1
        result_text = '\n'.join(result_text)

        week_days.remove(week_days[3])
        week_days.insert(3, result_text)

    with open('file.txt', 'w', encoding='utf-8') as data:
        data.write(''.join(week_days))


# Функция изменения расписания на Пятницу.
def change_on_friday():
    with open('file.txt', 'r', encoding='utf-8') as data:
        res_text = data.read()
        start1 = res_text.find('Понедельник')
        stop1 = res_text.find('Вторник')
        start2 = res_text.find('Вторник')
        stop2 = res_text.find('Среда')
        start3 = res_text.find('Среда')
        stop3 = res_text.find('Четверг')
        start4 = res_text.find('Четверг')
        stop4 = res_text.find('Пятница')
        start5 = res_text.find('Пятница')
        week_days = \
            [
                res_text[start1: stop1:],
                res_text[start2: stop2:],
                res_text[start3: stop3:],
                res_text[start4: stop4:],
                res_text[start5::]
            ]

        friday = week_days[4]
        text = ''.join(friday)
        result_text = text.split('\n')
        index = 1
        for i in range(6):
            result_text.remove(result_text[index + 1])
            result_text.insert(index + 1, f'{index} урок: {input(f"Введите название {index} урока: ")}')
            index += 1
        result_text = '\n'.join(result_text)

        week_days.remove(week_days[4])
        week_days.insert(4, result_text)

    with open('file.txt', 'w', encoding='utf-8') as data:
        data.write(''.join(week_days))
