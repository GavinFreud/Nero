import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='~')
startup_exts = ['commands','voice']

@bot.event
async def on_ready():
    print('logging in')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def help(ctx):
    embed = discord.Embed(title = "Nero Bot", description = "UMU! The commands I'll accept from you are: ")

    embed.add_field(name = "~add a b", value = "Gives the value of the addition of **a** and **b**")
    await ctx.send(embed = embed)


bot.run(Mzk0NjiMwMzUwMjA0MTc0MzM3.DSHHtg.M5N4Bt8WZvOyOeat1oy0BGY0DEI)
