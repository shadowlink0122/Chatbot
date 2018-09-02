import random

from linebot.models import (TextSendMessage, )
import botengine as bt

def create_message(comment):

    message = tb.make_reply(comment)

    return TextSendMessage(text=message)
