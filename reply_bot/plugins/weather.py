import json
import requests

class Weather:
    def __init__(self):
        None

    def get_weather(self, city_number):
        url = "http://weather.livedoor.com/forecast/webservice/json/v1?city=%s" % city_number
        # URLアクセスして情報を取得する
        response = requests.get(url)
        response.raise_for_status()
        # 取得したjsonデータを読み込む
        weather_data = json.loads(response.text)
        return weather_data
