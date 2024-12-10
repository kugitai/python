import requests

url = "https://weather.tsukumijima.net/api/forecast/city/400010"

data = requests.get(url).json()
print('タイトル：', data['title'])
print('天気：', data['forecasts'][0]['telop'])
print('概況：',data['description']['text'])