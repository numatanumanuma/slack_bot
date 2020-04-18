from slackbot.bot import respond_to
from slackbot.bot import listen_to
import os

from plugins.weather import Weather

CITY_NUMBER = os.environ.get('CITY_NUMBER')
city_number = CITY_NUMBER
# 意味ないけどなんとなく...

weather = Weather()

# メンションに反応
@respond_to('.*天気.*')
def greeting_1(message):
    w = weather.get_weather(city_number)
    message.reply('今日の天気は' + w['forecasts'][0]['telop'] + 'だよ。')
 
# メンションなしに反応
@listen_to('.*OKD.*')
def greeting_2(message):
    message.reply('呼んだ？')
