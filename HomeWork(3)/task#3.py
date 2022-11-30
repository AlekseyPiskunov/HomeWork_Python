'''
Вводим с клавиатуры строку.
Необходимо развернуть подстроку между первой и последней буквой "о".
Если она только одна или её нет - то сообщить, что буква "о" - одна или не встречается.
'''

string = input('Введите строку: ')
string = string.lower()

if string.count('о') < 2:
    print('В строке не достаточно букв "о".')
else:
    start = string.find('о')
    stop = string.find('о', 2)
    a = string[:start+1]
    b = string[stop-1:start:-1]
    c = string[stop:]
    print(a + b + c)
