'''
4) Вводим с клавиатуры многозначное число.
Необходимо узнать и сказать последовательность цифр этого числа
при просмотре слева направо упорядочена по возрастанию или нет.
Например 1579 - да ( 1 меньше 5, 5 меньше 7, а 7 меньше 9), 1427 - нет
'''

value = input('Введите многозначное число: ')

count = 0
for i in range(len(value) - 1):
    if value[i] < value[i + 1]:
        count += 1

if count == len(value) - 1:
    for i in range(len(value) - 1):
        print(value[i], value[i + 1], sep=' меньше ', end=' ')
else:
    print(value, '- нет.')


# Вот такой вариантик с флажком)
# value = input('Введите многозначное число: ')
#
# is_ascending = True
# for i in range(len(value) - 1):
#     if value[i] >= value[i + 1]:
#         is_ascending = False
#         break
#
# if is_ascending:
#     for i in range(len(value) - 1):
#         print(value[i], value[i + 1], sep=' меньше ', end=' ')
# else:
#     print(value, '- нет.')



# Ещё такой вариантик.
# i = 0
# while i < len(value) - 1 and value[i] < value[i + 1]:
#     i += 1
# is_ascending = i == len(value) - 1
