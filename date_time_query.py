from datetime import datetime
import pytz

class DateTimeUtility:
    def __init__(self, timezone='UTC'):
        # Initialize the utility with a default timezone
        self.timezone = timezone

    def get_current_date(self):
        now = datetime.now(pytz.timezone('Europe/Budapest'))
        return [now.year, now.month, now.day]

    def get_current_time(self):
        now = datetime.now(pytz.timezone('Europe/Budapest'))
        return [now.hour, now.minute]

    def get_time_in_city(self, city_timezone:str):
        city_time = datetime.now(pytz.timezone(city_timezone))
        city_name = city_timezone.split("/")[1]
        return [city_name, city_time.hour, city_time.minute]
    
    def return_local_date(self):
        print(f"A mai dátum {self.get_current_date()[0]} {self.get_current_date()[1]}. hó {self.get_current_date()[2]} uram.")
    def return_local_time(self):
        print( f"A pontos idő {self.get_current_time()[0]} óra {self.get_current_time()[1]} perc uram.")
    def return_time_in_city(self,city_timezone:str):
        print( f"{self.get_time_in_city(city_timezone)[0]} helyi ideje {self.get_time_in_city(city_timezone)[1]} óra {self.get_time_in_city(city_timezone)[2]} perc uram.")
    

time_utility = DateTimeUtility()

time_utility.return_local_date()

time_utility.return_local_time()

# Africa
# America
# Antarctica
# Arctic
# Asia
# Atlantic
# Australia
# Europe
# Indian
# Pacific
time_utility.return_time_in_city('America/New_York')




