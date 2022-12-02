'''
Сгенерируйте список на 30 элементов.
Отсортируйте список по возрастанию, методом сортировки выбором.
'''
from random import randint as rd

list = []

for _ in range(30):
    list.append(rd(1, 9))

print(f'Изначальный список:\n{list}')

for i in range(len(list)-1):
    min_position = i
    for j in range(i + 1, len(list)):
        if list[j] < list[min_position]:
            min_position = j
    list[i], list[min_position] = list[min_position], list[i]

print(f'Отсортированный список:\n{list}')
