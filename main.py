import random

from linebot.models import (TextSendMessage, )

janken_flag = 1

def create_message(input):
    love = ['好き', 'すき', 'スキ']
    unlove = ['嫌い', 'きらい', 'キライ']
    jankenstart = ['じゃんけん', 'ジャンケン']
    message = ''

    for word in love:
        if input.find(word) >= 0:
            message = 'だよね。寺子屋大好き❤️'

    for word in unlove:
        if input.find(word) >= 0:
            message = 'は？ふざけんなよ！！'

    for word in jankenstart:
        if input.find(word) >= 0 or janken_flag ==1:
            if janken_flag != 1:
                message = 'グー・チョキ・パーのどれかを入力してね'
            else:
                janken_message(input)

    if len(message) == 0:
        message = input + '、と言いましたね？'

    return TextSendMessage(text=message)


def janken_message(input):

    janken = ['グー', 'チョキ', 'パー']

    for input in janken:
        if input not in janken:
            message = 'グー・チョキ・パーのどれかを入力してね'
        else:
            reply = random.choice(janken)
            message = reply

    return TextSendMessage(message)
