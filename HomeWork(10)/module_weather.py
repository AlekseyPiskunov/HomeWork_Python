from bs4 import BeautifulSoup
import requests

# Парсим погоду (Moscow) (mail.ru)
def create_weather_moscow():
    url = 'https://pogoda.mail.ru/prognoz/moskva/'
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    temp = soup.find('div', class_='information__content__temperature').text
    temp_second = soup.find('div', class_='information__content__additional__item').text
    condition = soup.find('div', class_='information__content__additional information__content__additional_first').text

    # Тут пришлось сделать такую махинацию. Убрать лишнюю кракозябру которая пришла из soup.find
    temp = ''.join(filter(lambda x: x != '\n' and x != '\t', temp))
    temp_second = ''.join(filter(lambda x: x != '\n' and x != '\t', temp_second))
    condition = ''.join(filter(lambda x: x != '\n' and x != '\t', condition))
    weather = [temp, temp_second.capitalize(), condition.capitalize()]
    return weather

# Парсим погоду (St. Petersburg) (yandex.ru)
def create_weather_st_petersburg():
    url = 'https://yandex.ru/pogoda/?lat=59.93909836&lon=30.31587601'
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    temp = soup.find('div', class_='temp fact__temp fact__temp_size_s').text
    temp_second = soup.find('div', class_='term term_orient_h fact__feels-like').text
    condition = soup.find('div', class_='link__condition day-anchor i-bem').text
    temp_second = list(temp_second)
    temp_second.insert(13, ' ')
    temp_second = ''.join(temp_second)
    weather = [temp, temp_second, condition]
    return weather