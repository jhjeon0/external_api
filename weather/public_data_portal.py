import requests
import json

api_key = ""

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
params ={'serviceKey' : api_key, 'pageNo' : '1', 'numOfRows' : '1000', 'dataType' : 'XML', 'base_date' : '20240513', 'base_time' : '0500', 'nx' : '55', 'ny' : '127' }
response = requests.get(url, params=params)
result = json.loads(response.text)

print(result)
