from slackbot.bot import respond_to

@respond_to('Hello')
def reply_hello(message):
    message.reply('Hello')
