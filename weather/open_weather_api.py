import requests
import json

api_key = ""
lat = "37.49"
lot = "126.88"
lang = "kr"
city = "Seoul"

api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang={lang}&units=metric"

result = requests.get(api)
data = json.loads(result.text)


print(f"{data['name']}의 날씨입니다.")

"""
print(f"날씨는 {data["weather"][0]['description']}입니다.")
data["main"]["temp"]
data["main"]["feels_like"]
data["main"]["temp_min"]
data["main"]["temp_max"]
data["main"]["humidity"]
data["main"]["pressure"]
data["wind"]["deg"]
data["wind"]["speed"]
"""
