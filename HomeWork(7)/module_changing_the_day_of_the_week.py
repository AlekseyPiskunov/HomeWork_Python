# Функция изменения расписания на определённый день недели.
def change_day(day_week, count):
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

        friday = week_days[day_week]
        text = ''.join(friday)
        result_text = text.split('\n')
        index = 1
        for i in range(count):
            result_text.remove(result_text[index + 1])
            result_text.insert(index + 1, f'{index} урок: {input(f"Введите название {index} урока: ")}')
            index += 1
        result_text = '\n'.join(result_text)

        week_days.remove(week_days[day_week])
        week_days.insert(day_week, result_text)

    with open('file.txt', 'w', encoding='utf-8') as data:
        data.write(''.join(week_days))