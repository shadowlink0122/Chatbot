from linebot.models import (TextSendMessage, )
# import botengine

def create_message(input):
	message = ""
		
	# message = botengine.make_reply(input)

	if len(message) == 0:
		message = 'サーバ移行中\n改装が完了するまでお待ちください'

	return TextSendMessage(text=message)