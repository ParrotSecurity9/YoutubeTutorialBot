import discord
import random
from discord.ext import commands

intents = discord.Intents().all()
client = commands.Bot(command_prefix = "/", intents=intents)

@client.event
async def on_ready():
    print("Bot is online")

@client.event
async def on_member_join(member):
    print(f"{member} has joined the server")

@client.event
async def on_member_remove(member):
    print(f"{member} has left the server")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong {round(client.latency * 1000)}ms")

@client.command(aliases=["8ball", "test"])
async def _8ball(ctx, *, question):
    responses = ['My reply is no.',
                'It is certain.',
                'Cannot predict now.',
                'Very doubtful.',
                'It is decidedly so.',
                'Without a doubt.',
                'Ask again later.',
                'try again.',
                'Yes definitely.',
                'Better not tell you now.',
                'Outlook not so good.',
                'You may rely on it.',
                'Dont count on it.',
                'As I see it yes.',
                'Most Likely.',
                'Outlook good.',
                'Concentrate and ask again.',
                'Signs point to yes.']

    await ctx.send(f"Question: {question}\nMy response: {random.choice(responses)}")

client.run("Nzk4NDczNjM1ODYxMTAyNjEz.X_1ihQ.1TZkLvOnKgYhDPu86zkxHZBqgCQ")
