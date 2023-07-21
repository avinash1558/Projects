import requests
from Speak import Speak
from time import sleep

def location():
    Speak("Wait sir, let me check")
    try:
        ipAdd = requests.get("https://api.ipify.org").text
        url = f"https://get.geojs.io/v1/ip/geo/{ipAdd}.json"
        location_req = requests.get(url)
        location_data = location_req.json()
        city = location_data['city']
        country = location_data['country']
        region = location_data['region']
        print(city)
        Speak(
            f"Sir i am not sure, but i think we are in {city} city and {region} region of {country} country")
        sleep(2)
        
    except Exception as e:
        Speak("Sorry sir, due to network issue i am not able to find where we are")
        sleep(2)

