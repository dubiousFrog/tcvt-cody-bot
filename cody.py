import discord

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents = intents)
guild = discord.Guild
messages =  []


print("Bot started")
@client.event
async def on_message(message):
    
    channelIDsToListen = [ 960336925812727858 ] # put the channels that you want to listen to here

    if message.channel.id in channelIDsToListen:

        if message.content != "" :
 
            messages.append(message.content)

        print("New message: " + message.content)
    
client.run('MTE0NDI5MDQ4ODY4MjI5MTIwMA.GgZu1f.RfbuasLW0KAnhTRu_DOQ3LXE5OinCxWGhuixbE')