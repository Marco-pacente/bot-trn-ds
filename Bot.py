# bot.py
import os
from pydoc import cli
from unicodedata import name

import discord
import random
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

print(TOKEN)

#grazie reddit
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

citazioni_puglia = [
    "A chiang', alla chjes", "A Sciacquè la cap o' ciucc' s perde u timb e u sapaum", "A ce mor chi fongj fess ciuh chieng", "Ce scord pan e capp, mal sort 'ngapp", "Chi pèggre se fasce, u lupe se la mange", "Coji l'acqua quannu chiove", "Nesciune nasce ambaràte", "Vutt u' ciucc' andò vole u' patrom","Polentone di merda"
]

@bot.command(name = 'PING', help = 'la base')
async def PING(ctx):
    await ctx.send('PONG')

@bot.command(name = 'ping', help = 'la base funny')
async def ping(ctx):
    await ctx.send('pong')

@bot.command(name = 'pong', help = 'la base funny')
async def ping(ctx):
    await ctx.send('ping')

@bot.command(name = 'PONG', help = 'la base')
async def PING(ctx):
    await ctx.send('PING')

@bot.command(name = 'terrone', help = 'il meme')
async def terrone(ctx):
    messaggio = random.choice(citazioni_puglia)
    await ctx.channel.send(messaggio)

@bot.command(name = 'foto', help = 'le foto')
async def foto(ctx):
    try:
        dir = os.listdir('images/')
        foto = 'images/' + dir[random.randint(0, len(dir)-1)]
        print(foto)
        await ctx.channel.send(file = discord.File(foto))
    except FileNotFoundError('e'):
        await ctx.channel.send("scusa l'interprete è stupido non riesce a trovare una foto che è letteralmente nella stessa cartella")
        print('sorry')

@bot.command(name = 'musica', help = 'il meme')
async def musica(ctx):
    await ctx.send('https://youtu.be/90Fa9f338rE')

bot.run(TOKEN)