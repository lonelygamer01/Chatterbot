import requests
def get_location():
    # Use ipinfo.io to get IP-based location data
    location_response = requests.get("https://ipinfo.io")
    location_data:str = location_response.json()
    
    # Extract latitude and longitude
    coordinates = location_data['loc'].split(',')
    latitude = coordinates[0]
    longitude = coordinates[1]
    
    return [latitude, longitude]