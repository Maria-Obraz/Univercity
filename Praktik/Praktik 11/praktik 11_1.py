import requests
from datetime import datetime
import json

def get_weather(city_name):
    api_key = 'c341e34f9b7c327502cde34aa7817c5f'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&lang=ru&appid={api_key}'
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def log_weather(city_name, weather_data):
    now = datetime.now().strftime("%H:%M:%S")
    log_data = f'[{now}] Запрос погоды в городе: {city_name}\n' \
               f'Температура: {weather_data["main"]["temp"]} °C, {weather_data["weather"][0]["description"].capitalize()}\n' \
               f'Влажность воздуха: {weather_data["main"]["humidity"]}%\n' \
               f'Скорость ветра: {weather_data["wind"]["speed"]} м/с\n' \
               f'Атмосферное давление: {weather_data["main"]["pressure"]} мм рт. ст.\n'
    with open('weather_logs.txt', 'a', encoding='utf-8') as f:
        f.write(log_data)

if __name__ == '__main__':
    city_name = input('Введите название города: ')
    weather_data = get_weather(city_name)
    log_weather(city_name, weather_data)
    print(f'Температура: {weather_data["main"]["temp"]} °C, {weather_data["weather"][0]["description"].capitalize()}')
    print(f'Влажность воздуха: {weather_data["main"]["humidity"]}%')
    print(f'Скорость ветра: {weather_data["wind"]["speed"]} м/с')
    print(f'Атмосферное давление: {weather_data["main"]["pressure"]} мм рт. ст.')