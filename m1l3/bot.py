import discord
from bot_logic import gen_pass
from discord.ext import commands
import random
import os
import requests

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix = "$",intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("HI!")

@bot.command()
async def bye(ctx):
    await ctx.send("😞")

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))   

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def meme(ctx):
    with open("images/mem1.jpg", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)    

@bot.command()
async def meme_aleatorio(ctx):
    mem_alet = random.choice(os.listdir("images"))
    with open(f"images/{mem_alet}", "rb") as f:
        picture = discord.File(f)
    await ctx.send (file=picture)

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