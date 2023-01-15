'''
Создать 2 массива NumPy.
Один из случайных чисел, второй - используя arange или linspace.
После этого выполнить математические операции - сложить, перемножить, делить.
Найти максимальный элемент в каждой строчке и столбце первого массива (из случайных чисел).
Найти максимальный элемент из 2 массивов.
Изменить форму массива
'''

import numpy as np

# Создаём первый массив.
arrayFirst = np.random.randint(9, size=6, dtype=int)
print(f'Первый массив: {arrayFirst}')
# Создаём второй массив.
arraySecond = np.arange(1, 7)
print(f'Второй массив: {arraySecond}')

print()
# Сложение, деление, умножение.
resultSum = arrayFirst + arraySecond
resultDiv = arrayFirst / arraySecond
resultMult = arrayFirst * arraySecond
print(f'Результат сложения: {resultSum}')
print(f'Результат деления: {resultDiv}')
print(f'Результат перемножения: {resultMult}')

print()
# Изменяем наши массивы.
newFirstArray = arrayFirst.reshape(2, 3)
newSecondArray = arraySecond.reshape(2, 3)
print(f'Изменённый первый массив:\n {newFirstArray}')
print(f'Изменённый второй массив:\n {newSecondArray}')

print()
# Ищем максимальный элемент в каждой строчке и столбце первого массива.
maxElementColumns = newFirstArray.max(axis=0)
maxElementRows = newFirstArray.max(axis=1)
print(f'Максимальные элементы по столбцам из первого массива:\n {maxElementColumns}')
print(f'Максимальные элементы по строкам из первого массива:\n {maxElementRows}')


print()
# Ищем максимальный элемент из двух наших массивов.
temp = np.array([arrayFirst.max(), arraySecond.max()])
print(f'Максимальный элемент из двух массивов: {temp.max()}')