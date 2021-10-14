import requests
s_city = "Chelyabinsk,RU"
city_id = 1508291
appid = "defcc3d7b11ab47123a685f8e82a187a"
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print("Погода сейчас:", data['weather'][0]['description'])
    print("Температура сейчас:", data['main']['temp'])
    print("Температура минимальная:", data['main']['temp_min'])
    print("Температура максимальная:", data['main']['temp_max'])
except Exception as e:
    print("Exception (weather):", e)
    pass
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                 params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    for i in data['list']:
            print( i['dt_txt'], '{0:+3.0f}'.format(i['main']['temp']), i['weather'][0]['description'] )
except Exception as e:
    print("Exception (forecast):", e)
    pass