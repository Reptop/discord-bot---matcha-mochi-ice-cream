import discord
import os
import requests
import json
import random
from io import StringIO

"so can we talk for min ooohhooo"

client = discord.Client()
my_secret = os.environ['TOKEN']


def tenki(): 
  response = requests.get('https://api.openweathermap.org/data/2.5/weather?zip=97229,us&appid=f203af71c732fbc42d6ee307a362abf5')
  json_data = json.dumps(response.text, sort_keys=True, indent=4, separators=(',', ': ')) 
  data = json_data 
  return(data) 

def get_quote(): 
  response = requests.get("https://animechan.vercel.app/api/random")
  json_data = json.dumps(response.text, sort_keys=True, indent=4, separators=(',', ': ')) 
  quote = json_data
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  await client.change_presence(activity=discord.Game(name="Final Fantasy VII Remake"))

@client.event
async def on_message(message):
  "using random number for stupid gif randomizer."
  "this is so stupid" 
  k = random.randint(0,50)
  print(k)
 
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')
    
  if message.content.startswith('$cat') and k > 25:
    await message.channel.send(file=discord.File('neko.gif'))
     
  if message.content.startswith('$cat') and k < 25:
    await message.channel.send(file=discord.File('neko1.gif'))
  
  if str(message.author) in ["Shakespeare#1494"]:
    MYid = '<@!888925448954871868>'
    await message.channel.send('%s Treat me to some fat ass on god' % MYid)

  if message.content.startswith('Reptop: quote') or message.content.startswith('$quote') or message.content.startswith('hithepig: quote'):
    quote = get_quote()
    await message.channel.send(quote)

  if (message.content.startswith('$weather')):
    get_weather = tenki()
    await message.channel.send(get_weather)


client.run(my_secret)




