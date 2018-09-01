import random

from linebot.models import TextSendMessage
import botengine

def create_message(input):

    message = make_reply(input)

    return TextSendMessage(text = message)