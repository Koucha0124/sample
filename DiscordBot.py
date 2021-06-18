import discord
from discord.ext import commands

@bot.event
async def on_ready():
    print("起動完了")

@bot.command()
async def test(ctx):
    await ctx.send("test.ok!")

bot.run("TOKEN")
