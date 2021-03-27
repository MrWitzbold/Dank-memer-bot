import discord
import datetime
import time
import asyncio

client = discord.Client()
@client.event
async def on_ready():
    print("ready")
@client.event
async def on_message(message):
    if message.content == ";start" and str(message.author.id) == "664274363243036682":
        while True:
            await message.channel.send("pls beg")
            await asyncio.sleep(1)
            await message.channel.send("pls search")
            await asyncio.sleep(1.5)
            await message.channel.send("sewer")
            await asyncio.sleep(1)
            await message.channel.send("pls hunt")
            await asyncio.sleep(1)
            await message.channel.send("pls fish")
            await asyncio.sleep(1)
            await message.channel.send("pls pm")
            await asyncio.sleep(2)
            await message.channel.send("i")
            await asyncio.sleep(40)


client.run("nah", bot = True)
