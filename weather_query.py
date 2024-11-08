import requests
from location_query import *
from datetime import datetime

KEY = "114e0884f014bde877c02193c5db72a5"
class WeatherQuery:
    #7 days
    url_local_forecast = f"http://api.openweathermap.org/data/2.5/forecast/daily?lat={get_location()[0]}&lon={get_location()[1]}&appid={KEY}&units=metric&cnt=7"
    #today
    url_current = f"https://api.openweathermap.org/data/2.5/weather?lat={get_location()[0]}&lon={get_location()[1]}&appid={KEY}&units=metric"
    url_air_pollution = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={get_location()[0]}&lon={get_location()[1]}&appid={KEY}"
    url_uv = f"http://api.openweathermap.org/data/2.5/uvi?lat={get_location()[0]}&lon={get_location()[1]}&appid={KEY}"

    air_pollution_response = requests.get(url_air_pollution)
    pollution_data_from_response = air_pollution_response.json()

    uv_response = requests.get(url_uv)
    uv_data_from_response = uv_response.json()

    forecast_response = requests.get(url_local_forecast)
    forecast_data_from_response = forecast_response.json()

    current_response = requests.get(url_current)
    current_data_from_response = current_response.json()

    def __init__(self):
        None
    def get_local_today(self,forecast_data=forecast_data_from_response, forecast_data_today=current_data_from_response, uv_data=uv_data_from_response, pollution_data=pollution_data_from_response):
        print(forecast_data, end="")
        print(forecast_data_today, end="")
        # today_data:dict = forecast_data["list"][0] #0 for today's data
        # current_weather = {
        #     "temperature": forecast_data_today['main']['temp'],
        #     "morning_temp" : today_data["temp"]["morn"],
        #     "temp_day": today_data['temp']['day'],
        #     "evening_temp" : today_data["temp"]["eve"],
        #     "temp_night": today_data['temp']['night'],
        #     "min_temp": today_data['temp']['min'],
        #     "max_temp": today_data['temp']['max'],

        #     "humidity": today_data['humidity'],

        #     "uv_index": uv_data['value'],

        #     "wind_speed": today_data['speed'],
        #     "wind_direction": today_data['deg'],

        #     "pressure": today_data['pressure'],
        #     "cloud_coverage": today_data['clouds'],

        #     "aqi": pollution_data['list'][0]['main']['aqi'],
        #     "co": pollution_data['list'][0]['components']['co'],
        #     "o3": pollution_data['list'][0]['components']['o3'],

        #     "rain_probability": today_data.get('rain', 'No rain expected'),
        #     "snow_volume": today_data.get('snow', 'No snow expected'),
        # }
        # print(current_weather, end="")
    def get_local_tomorrow(self, forecast_data=forecast_data_from_response):
        # Extract tomorrow's forecast
        tomorrow_data:dict = forecast_data['list'][1]  # The second item in the list is for tomorrow
        tomorrow_forecast = {
            "morning_temp" : tomorrow_data["temp"]["morn"],
            "temp_day": tomorrow_data['temp']['day'],
            "evening_temp" : tomorrow_data["temp"]["eve"],
            "temp_night": tomorrow_data['temp']['night'],
            "min_temp": tomorrow_data['temp']['min'],
            "max_temp": tomorrow_data['temp']['max'],

            "humidity": tomorrow_data['humidity'],
            "rain_probability": tomorrow_data.get('rain', 'No rain expected'),
            "snow_volume": tomorrow_data.get('snow', 'No snow expected'),

            "wind_speed": tomorrow_data['speed'],
            "wind_direction": tomorrow_data['deg'],
            "pressure": tomorrow_data['pressure'],
            "cloud_coverage": tomorrow_data['clouds'],
            
        }
    def get_local_week(self):
        None

    def get_global_today(self):
        None
    def get_global_tomorrow(self):
        None
    def get_global_week(self):
        None


wq = WeatherQuery()
wq.get_local_today()