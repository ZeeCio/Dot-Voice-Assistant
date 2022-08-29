import requests
from engine import DOT

dot = DOT()


def weather_is(text):
    api_key = "a8f58b35b0fc5092dd94de27562e710a"
    weather_url = "http://api.openweathermap.org/data/2.5/weather?"
    data = text.split(" ")
    location = str(data[5])
    url = weather_url + "appid=" + api_key + "&q=" + location
    js = requests.get(url).json()

    if js["cod"] != "404":
        weather = js["main"]
        temp = round(weather["temp"] - 273.15)
        humidity = weather["humidity"]
        desc = js["weather"][0]["description"]
        message = "Here is the weather in " + location + " Today will be mostly " + str(desc) \
                  + ", humidity of " + str(humidity) + " percent " \
                  + ". The temperature is " + str(temp) + " degrees "

        print(message)
        return message
    else:
        return "City Not Found"
