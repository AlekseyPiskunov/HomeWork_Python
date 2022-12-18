'''
1)Написать программу, где создадим класс Soup (для определения типа супа),
принимающий 1 аргумент - который отвечает за основной продукт к выбираемому супу.
В этом классе создать метод show_my_soup(), выводящий на печать «Суп - {Основной продукт}» в случае наличия добавки.
Это как доп к этой задаче - иначе отобразится следующая фраза: «Обычный кипяток»
'''

class Soup:
    def __init__(self, name, ingredient=''):
        self.name = name
        self.ingredient = ingredient

    def show_my_soup(self):
        if self.ingredient == '':
            print('Обычный кипяток')
        else:
            print(f'{self.name} - {self.ingredient}')

bouillon = Soup('Бульён')
pea_soup = Soup('Гороховый суп', 'горох')

bouillon.show_my_soup()
pea_soup.show_my_soup()