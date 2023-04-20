import openai
import discord
from discord.ext import commands

openai.api_key = "-"

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

messages = []

@bot.command()
async def 지피티(ctx, *, msg):
    messages.append({"role":"user", "content":msg})

    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=messages
    )
    chat_response = completion.choices[0].message.content
    await ctx.send(f'ChatGPT : {chat_response}', reference=ctx.message)

bot.run('-')
