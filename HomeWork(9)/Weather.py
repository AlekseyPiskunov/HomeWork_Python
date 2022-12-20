from datetime import datetime
from bs4 import BeautifulSoup
import requests

url = 'https://pogoda.mail.ru/prognoz/moskva/'
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')
temp = soup.find('div', class_='information__content__temperature').text
temp_second = soup.find('div', class_='information__content__additional__item').text
condition = soup.find('div', class_='information__content__additional information__content__additional_first').text

# Тут пришлось сделать такую махинацию. Убрать лишнюю кракозябру которая пришла из soup.
temp = ''.join(filter(lambda x: x != '\n' and x != '\t', temp))
temp_second = ''.join(filter(lambda x: x != '\n' and x != '\t', temp_second))
condition = ''.join(filter(lambda x: x != '\n' and x != '\t', condition))
print(temp)
print(temp_second)
print(condition)


def create_file(temp, temp_second, condition):
    time = datetime.now().strftime('%H:%M')
    with open('Temp.txt', 'w', encoding='utf-8') as file:
        file.write('{}  Температура в Москве {}\n'.format(time, temp))
        file.write('{}  {}\n'.format(time, temp_second))
        file.write('{}  {}\n'.format(time, condition))

def create_html(temp, temp_second, condition):
    style = 'style="font-size:30px; margin:20 0 0 0; color:lightblue; text-align:center;"'
    style2 = 'style="font-size:20px; margin:10 0 10 0; color:lightblue; text-align:center;"'
    html = '<html>\n <head></head>\n <body style="background-color: darkslategrey">\n'
    html += '    <div style="height:180px; width: 290px; margin:0 auto; margin-top:180px; border:1px dotted lightblue;"><p {}>Температура в Москве: {}</p>\n'\
        .format(style, temp)
    html += '    <p {}>{}</p>\n' \
        .format(style2, temp_second)
    html += '    <p {}>{}</p></div>\n' \
        .format(style2, condition)
    html += '  </body>\n</html>'

    with open('index.html', 'w') as page:
        page.write(html)
    return html

create_html(temp, temp_second, condition)
create_file(temp, temp_second, condition)