from bs4 import BeautifulSoup
import requests

url = 'https://pogoda.mail.ru/prognoz/moskva/'
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')
temp = soup.find('div', class_='information__content__temperature')
temp_second = soup.find('div', class_='information__content__additional__item')
condition = soup.find('div', class_='information__content__additional information__content__additional_first')

def create(temp, temp_second, condition):
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

create(temp.text, temp_second.text, condition.text)