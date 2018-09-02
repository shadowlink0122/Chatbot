import random
from linebot.models import (TextSendMessage, )
import botengine as bt

def create_message(input):
    message = ''

    if len(message) == 0:
        message = '今はやめて...'

    return TextSendMessage(text=message)