import discord
from discord.ext import commands

intents = discord.Intents().all()

client = commands.Bot(command_prefix = "/", intents=intents)

@client.event
async def on_ready():
    print("Bot is online")

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

client.run("Nzk4NDczNjM1ODYxMTAyNjEz.X_1ihQ.h9C-7SrpODGOVmF3ih4sj0V0TJ8")