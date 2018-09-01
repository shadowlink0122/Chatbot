import random

from linebot.models import (TextSendMessage, )
import botengine

def create_message(comment):
    message = make_reply(comment)

    return TextSendMessage(text=message)
