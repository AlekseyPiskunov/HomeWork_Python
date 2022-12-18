'''
2)Нужно написать программу.
В ней используем класс - имя студента (name), номер группы (group) и список полученных оценок (progress).
В самой программе выводим список всех студентов.
В программе нужно вывести список студентов, отсортированный по имени, А так же студентов, у которых низкие оценки.
'''

from random import choice
from random import randint as rd

class Students:
    def __init__(self, name, group, progress):
        self.name = name
        self.group = group
        self.progress = progress

    def get_name(self):
        return self.name

    def get_progress(self):
        return self.progress

    def get_avg(self):
        return sum(self.progress) / len(self.progress)

students = \
    [
        'Вася', 'Пётр', 'Наталия', 'Никита', 'Алексей', 'Анжела',
        'Андрей', 'Светлана', 'Ирина', 'Кирилл', 'Максим', 'Антон'
    ]
group = ['732', '612', '589', '432']

# Функция создаёт список из учеников , их групп и их оценок.
def add_list_students(arg_students, arg_groupe):
    list_students = []
    for _ in range(len(arg_students)):
        student = Students(choice(arg_students), choice(arg_groupe), [rd(1, 5), rd(1, 5), rd(1, 5), rd(1, 5), rd(1, 5)])
        list_students.append(student)
    return list_students

# Функция сортировки по имени.
def sort_by_name(list_students):
    for i in range(len(list_students) - 1):
        min_position = i
        for j in range(i + 1, len(list_students)):
            if list_students[j].name < list_students[min_position].name: min_position = j
        list_students[i], list_students[min_position] = list_students[min_position], list_students[i]
    return list_students

# Функция создаёт список отстающих студентов.
def add_list_lagging_behind_students(list_students):
    lagging_behind_students = []
    for i in list_students:
        if i.get_avg() < 3:
            lagging_behind_students.append(i)
    return lagging_behind_students

# Функция печати списка.
def print_list_students(list_students, text):
    print(text)
    for i in range(len(list_students)):
        print(f'Имя: {list_students[i].get_name()}, Группа: {list_students[i].group}, Оценки: {list_students[i].get_progress()}')
    print()

result = add_list_students(students, group)
result_list_students = sort_by_name(result)
print_list_students(result_list_students, 'Список всех студентов:')

result_lagging_behind_students = add_list_lagging_behind_students(result_list_students)
print_list_students(result_lagging_behind_students, 'Список отстающих студентов:')