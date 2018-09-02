import random
from linebot.models import (TextSendMessage, )
import botengine

def create_message(input):
<<<<<<< HEAD
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
=======
    message = botengine.make_reply(input)

    return TextSendMessage(text=message)
>>>>>>> 5a9efa352a49547fd9b8e966fa541ebc1215c55e
