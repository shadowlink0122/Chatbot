import random
from linebot.models import (TextSendMessage, )
import botengine

def create_message(input):

  message = botengine.make_reply(input)
  message = "Test Message\nMaintenance now"

  if message == "":
  	message = "Error : なんでだろう🤔\n				整備中です🙇‍♀️"

  return TextSendMessage(text=message)