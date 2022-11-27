'''
1) Вводим с клавиатуры целое число X и У.
Выводим на экран количество чисел между Х и У, которые делятся на 2 и 3
'''

x = int(input('Введите целое число "X": '))
y = int(input('Введите целое число "Y": '))

if x > y:
    minValue = y
    maxValue = x
else:
    minValue = x
    maxValue = y

result = 0
for i in range(minValue + 1, maxValue):
    if i % 2 == 0 and i % 3 == 0:
        result += 1

print(f'Количество чисел между Х и У, которые делятся на 2 и 3 = {result}')