from linebot.models import (TextSendMessage, )
# import botengine

def create_message(input):
	message = ""
		
	# message = botengine.make_reply(input)

	if len(message) == 0:
		message = 'ただ今メンテナンス中です\n改装が整うまでお待ちください'

	return TextSendMessage(text=message)