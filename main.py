import discord
import os
import requests
import json
import random
import numpy as np
import datetime
from matplotlib import pyplot as plt
"so can we talk for min ooohhooo"

"Fixes for next push: Fix the mental state tracker so that each np array point is added continously"
"And uh yeah thats about it"

client = discord.Client(intents=discord.Intents.default())
my_secret = os.environ['TOKEN']

triggers = [
        'im bad', 'i suck', 'i want death',
        'sadge', 'oof', 'damn bro'
    ]

limit = 2
x_axis = np.arange(2)
y_axis = np.arange(2)

def addPoint(scat, new_point):
  old_off = scat.get_offsets()
  new_off = np.concatenate([old_off,np.array(new_point)])
  
  scat.set_offsets(new_off)

  #scat.axes.figure.canvas.draw_idle()

def tenki(): 
  response = requests.get('https://api.openweathermap.org/data/2.5/weather?zip=97229,us&appid=ID')
  json_data = json.dumps(response.text, sort_keys=True, indent=4, separators=(',', ': ')) 
  data = json_data 
  return(data) 

def get_quote(): 
  response = requests.get("https://animechan.vercel.app/api/random")
  json_data = json.dumps(response.text, sort_keys=True, indent=4, separators=(',', ': ')) 
  quote = json_data
  return(quote)

def print_mental_state():

  #if nx and ny == 0:
    #return
  
  #os.remove("test.png")
    
  fig, ax = plt.subplots()  # Create a figure containing a single axes.
  
  plt.title('Mental State :(')
  ax.set_xlabel('Sanity')  # Add an x-label to the axes.
  ax.set_ylabel('Will To Live')  # Add a y-label to the axes.


#x = np.array([1, 3], [2, 6], [3, 7])

  # limit = limit + 1
  # print("limit: ", limit)

 # x = np.append(x,limit)
 # y = np.append(y,ny)

 #print(x)
  
  
 #ax.plot(x, y);  # Plot some data on the axes.
  
# function to show the plot
  filename =  "test.png"
  plt.savefig(filename)
  image = discord.File(filename)
  return image


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  await client.change_presence(activity=discord.Game(name="Final Fantasy VII Remake"))

@client.event
async def on_message(message):
  "using random number for stupid gif randomizer."
  "this is so stupid" 
  k = random.randint(0,50)
  #print(k)

  #nx = random.randint(1, 50)
  #ny = random.randint(1, 20)
 
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

  for i in triggers:
    if message.content == i:
      print("hello")
      print_mental_state()

  if (message.content.startswith('$woo')):
    img = print_mental_state()
    #await message.channel.send(file=discord.File('test.png'))
    
    await message.channel.send(file=img)
client.run(my_secret)





