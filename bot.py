import discord, json 
from data import Gamoo

with open("token.json") as token:
    token = json.load(token)

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} is ready to get you free games!!!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!help':
        await message.channel.send('list of commands goes in here')
        return
    if message.content == '!game':
        if Gamoo().search_game():
            while Gamoo().search_game():
                await message.channel.send(Gamoo().search_game())
        else:
            await message.channel.send("There is no more free games, come back tomorrow")
        return

client.run(token)