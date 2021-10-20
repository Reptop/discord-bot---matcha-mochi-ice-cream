import discord
import os
import requests
import json 
from replit import db  

"so can we talk for min ooohhooo"

client = discord.Client()
my_secret = os.environ['TOKEN']

def tenki(): 
  response = ('api.openweathermap.org/data/2.5/weather?q={Portland}&appid={API key}')
  json_data = json.loads(response)
  fin = json_data
  return(fin)


def get_quote(): 
  response = requests.get("https://animechan.vercel.app/api/random")
  json_data = json.loads(response.text)
  quote = json_data
  return(quote)



@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  await client.change_presence(activity=discord.Game(name="Final Fantasy VII Remake"))

  @client.event
  async def on_message(message): 
    if message.author == client.user:
      return

    if message.content.startswith('$hello'):
      await message.channel.send('Hello!')
    
    if message.content.startswith('$cat'):
      await message.channel.send(file=discord.File('neko.gif'))

    if str(message.author) in ["Shakespeare#1494"]:
      MYid = '<@!888925448954871868>'
      await message.channel.send('%s Treat me to some fat ass on god' % MYid)

    if message.content.startswith('Reptop: quote') or message.content.startswith('$quote') or message.content.startswith('hithepig: quote') or message.content.startswith('$q'):
      quote = get_quote()
      await message.channel.send(quote)


client.run(my_secret)


