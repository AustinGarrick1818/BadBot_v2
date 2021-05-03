# BadBot v2
# Created by: The Specialist @ discord

import os
import sys
import time
import string
import random
import discord
import asyncio
import pathlib
from os import path
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import MissingPermissions
#sys.path.insert(0, "modules")


token = open("data/bot_tokens/BadBot_v2.txt", "r").read()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='>', intents=intents)



@bot.event
async def on_ready():
	print(f'{bot.user}')
	print(f'{bot.user.id}')
	print(f'{discord.__version__}')



@bot.event
async def on_message(message):
   await bot.process_commands(message)

   if message.author == bot.user:
      return



@bot.command(name='demo', help='Test comand')
async def demo(ctx):
	#await ctx.message.delete()
	await ctx.send('All is working!')


@bot.command(name='logoff', help='Send bot offline')
async def logoff(ctx):
   #await ctx.message.delete()
   await ctx.send(f'Sending: {bot.user} offline...')
   await ctx.bot.logout()





# Bring the bot online
bot.run(token)