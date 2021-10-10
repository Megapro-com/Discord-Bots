# -*- coding: utf-8 -*-
# @Time    : 2021/10/10
# @Author  : 
# @Email   : 
# @File    : send2Discord.py
# @Desc    : example of sending message to discord channel via webhook
# @Software: 

from discord_webhook import DiscordWebhook
import os

#define the channel webhook URL, replace below URL as yours
DISCORD_TEST_URL = 'https://discord.com/api/webhooks/888888888888888888/XXXXXXXXXXXXXXXXXXXXXXXXXXX_XXXXXXXXXXXXX_XXXXXXXXXXXXXXXXXXXXXXXXXXXX'  

#send text message to discord channel
webhook = DiscordWebhook(url=DISCORD_TEST_URL, content='hello world!')
response = webhook.execute()

#send picture or file to discord channel
path = "example.png"
filename = os.path.basename(path)
with open(os.path.normpath(path), "rb") as f:
    webhook = DiscordWebhook(url=DISCORD_TEST_URL)
    response =  webhook.add_file(file=f.read(), filename=filename)
    webhook.execute()