import random
from linebot.models import (TextSendMessage, )
import botengine

def create_message(input):

  # message = botengine.make_reply(input)
  message = "Test Message\n" + input

  return TextSendMessage(text=message)