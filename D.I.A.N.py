import discord
from discord.ext import commands
from discord import Member 
from discord.ext.commands import has_permissions, MissingPermissions
import requests

intents = discord.Intents().all()
intents.members = True
client = commands.Bot(command_prefix='$', intents=intents)

@client.event
async def on_ready(): 
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name="Victory."))
    print ("She hates you.")
    print ("--------------")

@client.command()
async def Info(ctx):
    embed = discord.Embed(title=" ✨",color=0xF49726)
    embed.add_field(name="Command Categories :",value="🐸 `memes    :` Image generation with a memey twist.\n" + "🔧 `utility  :` Bot utility zone\n😏 `nsfw     :` Image generation with a memey twist.\n\nTo view the commands of a category, send `.help <category>`" ,inline=False)
    embed.set_footer(icon_url=ctx.author.avatar_url,text="Help requested by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)

@client.command()
async def hello(ctx):
    await ctx.send("Hey, how can i help")

@client.command()
async def uy(ctx):
    await ctx.send("Hello.")

@client.command()
async def Night(ctx):
    await ctx.send("yes, that's my projects name")

@client.command()
async def Identity(ctx):
    await ctx.send("hello, I'm Project Night, I function as a Music, Entertainment, Technical Use Bot")

@client.command()
async def Help(ctx):
    await ctx.send("Hello, To use my commands my prefix is $, contact Andrey if there are issues.")

@client.command()
async def Nethercom(ctx):
    await ctx.send("<@1002431877044510750>")

@client.event 
async def on_member_join(member):
    channel = client.get_channel(1107989241998364693)
    await channel.send("welcome to Glorious Night")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(1107989241998364693)
    await channel.send("cya cya")

@client.command()
async def tara_date(ctx):
    if (ctx.author.voice):
        channel = ctx.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("bru where")

@client.command()
async def wag_na(ctx):
    if (ctx.author.voice):
        channel = ctx.author.voice.channel
        await channel.disconnect()
    else:
        await ctx.send("O")

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"{member} has been kicked lmfao")

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("who are you to command me.")

@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"User {member} has been beamed fucking loser")

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("who are you to ask me that.")

@client.command()
async def Founder(ctx):
    embed = discord.Embed(title="Ellony is learning how to love!", url="https://www.youtube.com/watch?v=K4xLi8IF1FM", description="I'm very beautiful and loveable.", color=0xFFC0CB)
    embed.set_author(name=ctx.author.display_name)
    await ctx.send(embed=embed)

client.run('MTI3ODMyMzg2MDgzNTY2ODA5Mw.G1VEFH.n6FIO-d7jSfUAQd-kUQVB6V0zzVcCizC-Nutmk')