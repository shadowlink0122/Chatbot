import random
from linebot.models import (TextSendMessage, )
import botengine

def create_message(input):

  message = botengine.make_reply(input)

  if message == "":
  	message = "Error : なんでだろう🤔\n				整備中です🙇‍♀️"

  return TextSendMessage(text=message)