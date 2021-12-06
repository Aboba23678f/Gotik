import discord
from discord.ext import commands
from discord.ext.commands import Bot

bot = Bot(command_prefix ='.')
bot.remove_command('help')

@bot.event
async def on_ready():
	print(f'{bot.user} приконектился')

bot.run('OTE3Mzc5MDMyOTM5NjM4ODg0.Ya31zQ.LDmmsbcQoxh7WH0k3CEqnc9KXyU')