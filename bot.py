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
        while True:
            retorno = Gamoo().search_game() 
            if retorno != None:
                await message.channel.send(retorno)
            else:
                await message.channel.send("There is no more free games, come back tomorrow")
                break
        return

client.run(token)