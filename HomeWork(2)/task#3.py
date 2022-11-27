'''
3) Вводим с клавиатуры целое число - это зарплата.
Нужно вывести в консоль -  Минимальное кол-во  купюр, которыми можно выдать ЗП.
И сколько, и каких бухгалтер выдаст 25 рублевых купюр,  10 рублевых, 3 рублевых и 1 рублевых.
'''

value = int(input('Введите зарплату: '))

twentyFive = 25
ten = 10
three = 3
one = 1

resultTwentyFive = 0
resultTen = 0
resultThree = 0
resultOne = 0

while value != 0:
    if value >= twentyFive:
        value = value - twentyFive
        resultTwentyFive += 1
    elif value >= ten:
        value = value - ten
        resultTen += 1
    elif value >= three:
        value = value - three
        resultThree += 1
    elif value < three:
        value = value - one
        resultOne += 1

print(f'Общее минимальное кол-во купюр получается - {resultTwentyFive + resultTen + resultThree + resultOne}')
print(f'{resultTwentyFive} купюр по {twentyFive} рублей.')
print(f'{resultTen} купюр по {ten} рублей.')
print(f'{resultThree} купюр по {three} рублей.')
print(f'{resultOne} купюр по {one} рублей.')