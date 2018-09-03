from linebot.models import (TextSendMessage, )
# import botengine

def create_message(input):
	message = "ご静聴ありがとうございました"
		
	# message = botengine.make_reply(input)

	if len(message) == 0:
		message = 'ただ今メンテナンス中\n改装が整うまでお待ちください'

	return TextSendMessage(text=message)