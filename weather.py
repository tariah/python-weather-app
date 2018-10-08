import urllib.request
import json


def get_weather(location):
    # Get woeid by making a call to /api/location/search
    link = "https://www.metaweather.com/api/location/search/?query=" + location
    url = urllib.request.urlopen(link)
    response = url.read().decode("utf8")
    json_data = json.loads(response)
    woeid = json_data[0]["woeid"]

    # Get the actual weather information with the woeid
    # gotten from the previous http call
    link = "https://www.metaweather.com/api/location/" + str(woeid)
    url = urllib.request.urlopen(link)
    response = url.read().decode("utf8")
    json_data = json.loads(response)
    consolidated_weather = json_data["consolidated_weather"]

    for data in consolidated_weather:
        print(data)
        print()

get_weather("lagos")
