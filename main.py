import random
from linebot.models import (TextSendMessage, )
# import botengine

def create_message(input):
    love = ['好き', 'すき', 'スキ']
    unlove = ['嫌い', 'きらい', 'キライ']
    jankenstart = ['じゃんけん', 'ジャンケン']
    message = ''

    if len(message) == 0:
        message = input + '、と言いましたね？'

    return TextSendMessage(text=message)