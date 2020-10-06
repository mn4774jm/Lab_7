import requests
import os
from datetime import datetime
import logging

logging.basicConfig(filename='debug.log', level=logging.DEBUG, format=f'%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def main():
    location = get_user_input()
    weather = request_weather(location)
    forecast_output(weather)


def get_user_input():
    city = input('What city are you looking for? ').strip().lower()
    while not city:
        city = input('What city are you looking for? ').strip().lower()
        if not city:
            logging.debug(f'User has enter invalid data "{city}"')
    logging.info(f'User entered valid city "{city}"')

    country = input(f'What country is {city} in? (2 character country code): ').strip().lower()
    while not city:
        country = input(f'What country is {city} in? (2 character country code): ').strip().lower()
        if not city:
            logging.debug(f'User has enter invalid data "{country}"')
    logging.info(f'User entered valid country code "{country}"')
    return f'{city},{country}'


def request_weather(location):
    Key = os.environ.get('WEATHER_KEY')  # returns None if not found
    # provide params to a variable; will need to look at query requirements for each new api
    query = {'q': {location}, 'units': 'imperial', 'appid': Key}
    URL = f'https://api.openweathermap.org/data/2.5/forecast'
    data = requests.get(URL, params=query).json()
    if data['cod'] == '404':
        print('City not found')
    else:
        return data['list']


def forecast_output(forecast_items):
    for forecast in forecast_items:
        timestamp = forecast['dt']  # unix timestamp
        date = datetime.fromtimestamp(timestamp)
        temp = forecast['main']['temp']
        weather_description = forecast['weather'][0]['description']
        print(f'at {date} Weather: {weather_description} | Temp: {temp}F.')


if __name__ == '__main__':
    main()