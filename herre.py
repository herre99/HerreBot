import discord
from discord.ext import commands
import youtube_dl

# Crear el objeto Intents
intents = discord.Intents.default()

intents.all()

# Crear la instancia del bot con el objeto Intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready(ctx, arg):
    print(f'Bot conectado como {bot.user.name}')
    await ctx.send(arg)



@bot.command()
async def play(ctx, url):
    voice_channel = ctx.author.voice.channel
    voice_channel = discord.utils.get(ctx.guild.voice_channels, name=voice_channel.name)

    ydl_opts = {
        'format': 'bestaudio',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']

    voice_channel = await voice_channel.connect()
    voice_channel.play(discord.FFmpegPCMAudio(url2), after=lambda e: print('done', e))
    
@bot.command()
async def leave(ctx):
    await ctx.voice_channel.disconnect()

bot.run('MTIwMjY3MTk2MjE4MzMxMTM5MQ.GWPAmO.XElQnZ6yYP_J13-n4PxXTK_C17ST6R3KjpP6BU')
