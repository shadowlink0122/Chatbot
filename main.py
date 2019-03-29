#!/usr/bin/env python
# -*- coding: utf-8 -*-

from linebot.models import (TextSendMessage, )
from botengine import make_reply

def create_message(text_message):
	message = ""
		
	# message = make_reply(text_message)

	if len(message) == 0:
		message = 'テスト中です'

	return TextSendMessage(text=message)