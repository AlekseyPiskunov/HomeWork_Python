'''
Вводим с клавиатуры строку.
Необходимо сказать, является ли эта строка дробным числом.
'''

# Пытался сделать таким образом , но не уверен что это полноценное решение.
# Ну у меня по сути просто ответ зависит от наличия точки.

string = input('Введите строку: ')

if string.find('.') != -1 and string.count('.') == 1:
    print('Строка является дробным числом.')
else:
    print('Строка не является дробным числом.')



# Нашел какое-то решение с интернета, но если честно я не понимаю его...
# import re

# def isfloat(s):
#     find = re.findall(r"\d*\.\d+", s)
#     if find:
#         return True
#     else:
#         return False
#
# print(isfloat('1'))
# print(isfloat('1.'))
# print(isfloat('1.1'))
# print(isfloat('.'))
# print(isfloat('.1'))