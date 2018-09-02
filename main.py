import random
from linebot.models import (TextSendMessage, )
import botengine as bt

def create_message(comment):
	message = "test message"
  # message = tb.make_reply(comment)

  if len(message) < 1:
  	message = "Error"

  return TextSendMessage(text=message)
