'''
Вводим с клавиатуры десятичное число.
Необходимо перевести его в шестнадцатиричную систему счисления.
'''

value = int(input('Введите число: '))

result: str = ''
a = '0123456789ABCDEF'

while value > 0:
    result = a[value % 16] + result
    value = value // 16

print(result)
