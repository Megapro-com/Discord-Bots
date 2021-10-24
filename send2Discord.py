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
DISCORD_TEST_URL = 'https://discord.com/api/webhooks/901831971943104563/xJ61gYmzCckEnMwQsbwYqwRqleDnHTTceBGGJRoKkj0cuW2kucy8Hs1y0TQ9VW5lsE1x'  

#send text message to discord channel
webhook = DiscordWebhook(url=DISCORD_TEST_URL, content='This is test message!')
response = webhook.execute()

#send picture or file to discord channel
path = "testPic.jpg"
filename = os.path.basename(path)
with open(os.path.normpath(path), "rb") as f:
    webhook = DiscordWebhook(url=DISCORD_TEST_URL)
    response =  webhook.add_file(file=f.read(), filename=filename)
    webhook.execute()

#Check your result from Megapro discord server
#Join Megapro Discord server: https://discord.gg/eENjUYWrVn
#gurus-bots-test channel: https://discord.com/channels/717060218131054664/901653994366201866/901659190089621595