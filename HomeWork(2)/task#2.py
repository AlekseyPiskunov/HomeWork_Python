'''
2) Вводим с клавиатуры целое число X.
Далее вводим Х целых чисел.
Необходимо вывести на экран максимальное и второе максимальное число из введенных чисел.
'''

# Вариант 1
# x = int(input('Введите целое число Х: '))
# list = []
# for i in range(x):
#     list.append(input(f'Введите {i + 1} число: '))
#
# firstMaxValue = list[0]
# for i in list:
#     if i > firstMaxValue: firstMaxValue = i
#
# secondMaxValue = list[0]
# for i in list:
#     if i > secondMaxValue and i != firstMaxValue:
#         secondMaxValue = i
#
# print(f'Первое максимальное число: {firstMaxValue}')
# print(f'Второе максимальное число: {secondMaxValue}')

# Вариант 2
x = int(input('Введите целое число Х: '))

firstMaxValue, secondMaxValue = None, None
for i in range(x):
    k = int(input(f'Введите {i + 1} число: '))
    if firstMaxValue is None: firstMaxValue = k
    elif secondMaxValue is None: secondMaxValue = k
    elif k > firstMaxValue:
        secondMaxValue = firstMaxValue
        firstMaxValue = k
    elif k > secondMaxValue:
            secondMaxValue = k

print(f'Первое максимальное число: {firstMaxValue}')
print(f'Второе максимальное число: {secondMaxValue}')