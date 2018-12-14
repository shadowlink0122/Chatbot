from linebot.models import (TextSendMessage, )
import botengine

def create_message(input):
	message = ""
		
	# message = botengine.make_reply(input)

	if len(message) == 0:
		message = 'テスト中です'

	return TextSendMessage(text=message)