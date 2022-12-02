'''
Написать программу, которая генерирует двумерный массив на A x B элементов (A и B вводим с клавиатуры)
И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)
'''
from random import randint as rd

rows = int(input('Введите кол-во строк: '))
columns = int(input('Введите кол-во столбцов: '))
array = []

for i in range(rows):
    array.append([])
    for _ in range(columns):
        array[i].append(rd(1, 9))

for i in array:
    print(i)

resultList = []
for i in range(rows):
    resultList.append(0)
    for j in range(columns):
        resultList[i] += array[i][j]

for i in range(len(resultList)):
    print(f'Средне-арифметическое {i+1}-й строки: {resultList[i] // columns}')

result = 0
for i in range(rows):
    for j in range(columns):
        result = result + array[i][j]

print(f'Средне-арифметическое всех элементов: {result // (rows * columns)}')