from linebot.models import (TextSendMessage, )
# import botengine

def create_message(input):
	message = ""
		
	message = botengine.make_reply(input)

	if len(message) == 0:
		message = '今はやめて...'

	return TextSendMessage(text=message)