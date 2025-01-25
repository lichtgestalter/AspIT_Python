import httpx  # pip install httpx

KEY = "2a3891ce1248786a1398a888debb0368"  # ulsc@aspit.dk


def weather_now(city, key=KEY):
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&APPID=" + key
    response = httpx.get(url)
    weather = response.json()  # Deserialize json into a hierarchy of dictionaries and lists

    if weather["cod"] == "404":
        return "Unknown Location"

    print(f'{weather=}')
    print(f'{weather["weather"]=}')
    print(f'{weather["weather"][0]["main"]=}')
    print(f'{int(weather["main"]["temp"])=}')
    if weather["cod"] == 200:
        weather_report = city + ": " + weather["weather"][0]["main"] + ", " + str(int(weather["main"]["temp"])) + "°C"
    else:
        weather_report = "Unknown Location"
    return weather_report


if __name__ == "__main__":  # Executed when invoked directly
    print(weather_now("Helsinki", KEY))
    # print(weather_now("xxxxzzzyy", KEY))
