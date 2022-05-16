import os

try: 
    import discord
except:
    os.system("title Downloading Discord Module")
    os.system("pip install discord")

try: 
    import discord
except:
    os.system("title Downloading Re Module")
    os.system("pip install re")

try: 
    import pystyle
except:
    os.system("title Downloading Pystyle Module")
    os.system("pip install pystyle")

import discord
import re
from pystyle import *

def has_numbers(inputString):
    return bool(re.search(r'\d', inputString))

class SELFBOT(discord.Client):
    global bps, token, prefix
    async def on_message(self, message):
        if(message.author!=self.user):
            return
        channels=[]
        if(prefix in message.content): 
            tmpStrConv = message.content.replace(prefix, '')
            tmpStrConv = tmpStrConv.strip()
            containsnumbers = has_numbers(tmpStrConv)
            if containsnumbers == True:
                MessagesToDEL = int(str(tmpStrConv))
            channels.append(message.channel)
        else:
            return
        for channel in channels:
            Write.Print(f"{channel}", Colors.red_to_purple, interval=0)
            if containsnumbers == True:
                Write.Print("Can't delete!\n", Colors.red_to_purple, interval=0) 
            else:
                async for msg in channel.history(limit=None):
                    if(msg.author==self.user):
                        try:
                            await msg.delete()
                            Write.Print(f"[!] {msg.content} got deleted\n", Colors.blue_to_cyan, interval=0)
                        except:
                            Write.Print(f"[X] {msg.content} didn't get deleted \n", Colors.blue_to_cyan, interval=0)

    token = Write.Input("Please input a Token: ", Colors.blue_to_cyan, interval=0)
    os.system("cls")
    prefix = Write.Input("Please input a prefix (leave blank for the default '#DEL'): ", Colors.blue_to_cyan, interval=0)
    bps = Write.Input("Please input a heartbeat timeout (leave blank for the default 86400): ", Colors.blue_to_cyan, interval=0)
    if bps == "":
        bps = 86400
    Write.Print(f"\nTo delete all messages in one channel, type: {prefix} in Discord, \nor delete a set amount of messages by adding a number after the prefix\n", Colors.red_to_purple, interval=0)

client=SELFBOT(heartbeat_timeout=bps, guild_subscriptions=False)
client.run(token, bot=False)