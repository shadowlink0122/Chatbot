import random
from linebot.models import (TextSendMessage, )
import botengine

def create_message(input):
  message = ''

  # for word in love:
  #     if input.find(word) >= 0:
  #         message = 'だよね。寺子屋大好き❤️'

  # for word in unlove:
  #     if input.find(word) >= 0:
  #         message = 'は？ふざけんなよ！！'

  if len(message) == 0:
    # message = botengine.make_reply(input)
    message = botengine.make_reply(input)

  return TextSendMessage(text=message)