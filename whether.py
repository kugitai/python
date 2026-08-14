import requests

url = "https://weather.tsukumijima.net/api/forecast"

params = {'city':400040}

data = requests.get(url,params=params).json()

print(f'{data['publicTimeFormatted']}現在の{data['title']}予報')
for i in range(2):
    print('日付：', data['forecasts'][i]['date'])
    print('天気：', data['forecasts'][i]['telop'])
    print(data['forecasts'][i]['image']['url'])
print('概況：',data['description']['text'])
