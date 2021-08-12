import discord
import os
import requests
import json 

client = discord.Client()
my_secret = os.environ['TOKEN']

"""functions for each API"""
def pokemon():
  callback = requests.get("https://pokeapi.co/api/v2/{endpoint}/")
  jd = json.loads(callback.text)
  final = jd
  return(final)

def get_quote(): 
  response = requests.get("https://animechan.vercel.app/api/random")
  json_data = json.loads(response.text)
  quote = json_data
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

  @client.event
  async def on_message(message): 
    if message.author == client.user:
      return

    if message.content.startswith('$hello'):
      await message.channel.send('Hello!')

    if message.content.startswith('$q'):
      quote = get_quote()
      await message.channel.send(quote)

    if message.content.startswith('$poke'):
      lorge = pokemon(); 
      await message.channel.send(lorge)


client.run(my_secret)


