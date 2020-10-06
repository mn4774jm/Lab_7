import requests
import os
from datetime import datetime
import logging


def main():
    location = get_user_input()
    Key = os.environ.get('WEATHER_KEY')     # returns None if not found
    # provide params to a variable; will need to look at query requirements for each new api
    query = {'q': {location}, 'units': 'imperial', 'appid': Key}
    URL = f'https://api.openweathermap.org/data/2.5/forecast'

    data = requests.get(URL, params=query).json()
    if data['cod'] == '404':
        print('City not found')
    else:

        forecast_items = data['list']

        for forecast in forecast_items:
            timestamp = forecast['dt'] #unix timestamp
            date = datetime.fromtimestamp(timestamp)
            temp = forecast['main']['temp']
            weather_description = forecast['weather'][0]['description']
            print(f'at {date} Weather: {weather_description} | Temp: {temp}F.')

def get_user_input():
    city = input('What city are you looking for? ').strip().lower()
    country = input(f'What country is {city} in? (2 character country code): ').strip().lower()
    return f'{city},{country}'



if __name__ == '__main__':
    main()