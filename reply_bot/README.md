# reply_bot

~~~
pip3 install python-dotenv
pip3 install wikipedia
~~~

## 天気情報

[お天気Webサービス仕様](http://weather.livedoor.com/forecast/rss/primary_area.xml)

- 土浦
    080020

~~~json
# data['forecasts'][0]
    {
      'dateLabel': '今日',
      'telop': '晴れ',
      'date': '2018-12-19',
      'temperature': {
        'min': None,
        'max': {
          'celsius': '14',
          'fahrenheit': '57.2'
        }
      },
      'image': {
        'width': 50,
        'url': 'http://weather.livedoor.com/img/icon/1.gif',
        'title': '晴れ',
        'height': 31
      }
    },
~~~
