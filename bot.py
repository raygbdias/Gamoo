import os, discord, json, random 

with open("token.json") as token:
    token = json.load(token)

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(token)