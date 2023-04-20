import discord
import requests
import json
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

boticus_responses = [
    'Leave me alone',
    "I don't have the answers, why don't you ask Stuart",
    'It can probably be solved with a FUR LOOP',
    'Alen is your man for that',
    'How the hell would I know'
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'jen' in message.content:
        quote = get_quote()
        await message.channel.send(quote)

    if 'bot' in message.content:
        quote = random.choice(boticus_responses)
        await message.channel.send(quote)

    if message.content.startswith('!fur'):
        await message.channel.send(' A for-loop or for loop is a control flow statement for specifying iteration. Specifically, a for loop functions by running a section of code repeatedly until a certain condition has been satisfied!')

client.run('BOT_TOKEN')
