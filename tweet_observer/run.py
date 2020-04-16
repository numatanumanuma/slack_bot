from slacker import Slacker
from observer import Observer
import setting

API_TOKEN = setting.API_TOKEN
slack = Slacker(API_TOKEN)
channels = ['#bot_test']

observer = Observer()

if observer.checkUpdate():
    comment = observer.makeComment()
    for channel in channels:
        slack.chat.post_message(channel, comment, as_user=True)
