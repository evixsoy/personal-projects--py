
#asi nefunguje

import requests
while True:
    lokace = input("zadej lokaci:")

    key = "71da3f9e27844a4dae9171839242611"
    string= 'https://api.weatherapi.com/v1/current.json?key=' + key + '&q=' + lokace +'&aqi=no'
    r = requests.get(string).json()

    teplota = r['current']['temp_c']
    location = r['location']['name']
    date = r['location']['localtime']
    description = r['current']['condition']['text']

    print(location)
    print(date)
    print(f"{teplota}°C")
    print(description)