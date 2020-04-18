from slackbot.bot import respond_to
from slackbot.bot import listen_to
import os

from plugins.weather import Weather
from plugins.wikipedia import Wikipedia

CITY_NUMBER = os.environ.get('CITY_NUMBER')
city_number = CITY_NUMBER
# 意味ないけどなんとなく...

weather = Weather()

# メンションに反応
@respond_to('.*今日の天気.*')
def weather_reply(message):
    weathers = weather.get_weather(city_number)
    w = weathers['forecasts'][0]
    message.reply('今日の天気は' + w['telop'] + 'だよ。\n' + w['image']['url'])
@respond_to('.*明日の天気.*')
def weather_reply(message):
    weathers = weather.get_weather(city_number)
    w = weathers['forecasts'][1]
    message.reply('明日の天気は' + w['telop'] + 'だよ。\n' + w['image']['url'])
@respond_to('^天気.*')
def weather_error(message):
    message.reply('天気が知りたけりゃ、「今日の」「明日の」をつけてくれい')
    message.react('thinking_face')

@respond_to('(.*)って[何|なに].*')
def wiki_reply(message, word):
    wiki = Wikipedia(word)
    if wiki.is_exists():
        summary = wiki.get_summary(1)
        message.reply('説明しよう!!「' + word + '」とは......\n' + summary + '\nである!!!\nもっと勉強したまえ^^\n' + wiki.get_url())
    else:
        message.reply('ぐぐれかす(曖昧すぎるか言葉が意味不明です)')

# メンションなしに反応
@listen_to('.*[OKD|okd].*')
def greeting(message):
    message.reply('呼んだ？')

@listen_to('.*寿司.*')
def sushi(message):
    message.react('sushi_rotation')
