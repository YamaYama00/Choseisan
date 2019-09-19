from slackbot.bot import respond_to #respond to @botname
from slackbot.bot import listen_to
from slackbot.bot import default_reply

@respond_to('test')
def mention_func(message):
    message.reply('i hate test')

@listen_to('こん')
def listen_func(message):
    message.send('にちは')

