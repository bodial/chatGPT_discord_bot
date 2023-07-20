import discord
import openai
import config
from discord.ext import commands

client = discord.Client(intents=discord.Intents.all())
openai.api_key = "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"

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

def generate_response(prompt, num_responses=1):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        #max_tokens=1024,
        max_tokens=2500,
        n=num_responses,
        stop=None,
        timeout=15,
    )

    message = response.choices[0].text.strip()
    return message

##@client.event
##async def on_message(message):
##    if message.author == client.user:
##        return
##
##    response = generate_response(message.content)
##    print('вижу сообщение')
##    print(message)
##
##    await message.channel.send(response)

@client.event
async def on_ready():
    print('gpt online')

@client.command()
async def askme(ctx, *, message):
    print ('вижу askme')
    print(message)
##    if message.author == client.user:
##        return

    response = generate_response(message)
    print('получил ответ')

    await ctx.channel.send(response)

client.run(config.token)
