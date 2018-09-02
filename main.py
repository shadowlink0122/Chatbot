import random
from linebot.models import (TextSendMessage, )
import botengine as bt

def create_message(input):
	message = ""
  # message = tb.make_reply(input)

  if len(message) < 1:
  	message = "Error"

  return TextSendMessage(text=input)
