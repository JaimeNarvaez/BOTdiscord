import os
#print(os.listdir(r'C:\Users\JJNO\Documents\Kodland\3713\m1l3\images'))
import random
import discord
import requests
from bot_logic import gen_pass
from discord.ext import commands

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix= "$", intents=intents)

memes = os.listdir(r'C:\Users\JJNO\Documents\Kodland\3713\m1l3\images')

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def meme(ctx):
    meme_aleat = random.choice(memes)
    await ctx.send(f'Hi!!!')
    with open(f'C:/Users/JJNO/Documents/Kodland/3713/m1l3/images/{meme_aleat}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)  
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)          
bot.run("MTI3NTk3ODIzNzEwNDg4NTc4MQ.GdNLQ_.YV_5PTzt8woVfiQouwoZZsK_OfF-OrU32I9RfQ")    

