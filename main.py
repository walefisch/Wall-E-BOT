import discord
import os
import requests
import json
import random
from discord.utils import get
from discord.ext import commands
from replit import db
from keep_aplive import keep_alive

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " ~" + json_data[0]['a']
  return(quote)

def get_meme():
  response = requests.get("https://reddit-meme-api.herokuapp.com/memes/")
  json_data = json.loads(response.text)
  meme = json_data['url']
  return(meme)

def get_cursed():
  response = requests.get("https://reddit-meme-api.herokuapp.com/cursed_images/")
  json_data = json.loads(response.text)
  cursed = json_data['url']
  return(cursed)

@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))

  await client.change_presence(activity=discord.Game('pls help'))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('pls help'):
    await message.channel.send('Hi! I am wall-e (very epic UwU) the commands that i currently understand are: pls deep, pls meme and pls cursed')

  if msg.startswith('pls deep'):
    quote = get_quote()
    await message.channel.send(quote)

  if msg.startswith('pls meme'):
    meme = get_meme()
    await message.channel.send(meme)

  if msg.startswith('pls cursed'):
    cursed = get_cursed()
    await message.channel.send(cursed)

  if msg.startswith('hurensohn'):
    await message.channel.send('geh nicht zur mutter')

  if msg.startswith('Hurensohn'):
    await message.channel.send('geh nicht zur mutter')

  if msg.startswith('https://discord.gg/'):
    await message.channel.send('delete ad or kick')

  if msg.startswith('Hs'):
    await message.channel.send('geh nicht zur mutter')

  if msg.startswith('hs'):
    await message.channel.send('geh nicht zur mutter')

  if msg.startswith('toxic'):
    await message.channel.send('no u')

keep_alive()
client.run(os.getenv('TOKEN'))