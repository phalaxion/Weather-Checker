"""A simple weather checker that utilises the openweathermap API
for getting weather forecasts"""

import urllib.request as request
import json

def get_city(input_city):
    """Takes a search string as an input and returns any
    matches from city_list.json as a list"""

    # Get all matching cities from city_list json file
    with open("city_list.json", encoding="utf8") as f:
        city_list = json.load(f)
        matching_cities = [city for city in city_list if input_city.lower() in city["name"].lower()]
    return matching_cities

def get_weather(identifier):
    """Takes a city identifier given as part of the city
    details returned as part of get_city"""

    # Create a request for a forecast at the chosen location
    req = request.Request(
        "https://api.openweathermap.org/data/2.5/forecast?id=" +
        identifier+"&APPID=238080a58fd9b4bef78464108880d7e6&units=metric",
        data=None,
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; ' +
                              'Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
                }
    )

    # Open response and return the forecast
    with request.urlopen(req) as response:
        return json.loads(response.read().decode('utf-8'))
