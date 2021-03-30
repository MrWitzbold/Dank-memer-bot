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
    if str(message.author.id) == "270904126974590976":
        print(message.content)
    if "Where do you want to search?" in str(message.content):
        item = str(message.content).split(",")[1].replace(",", "").replace("`", "")
        await message.channel.send(item)
    found_highlow = False
    embeds = message.embeds
    embed_with_hint = 0
    for embed in embeds:
        if "Your hint is " in str(embed.to_dict()):
            found_highlow = True
            embed_with_hint = str(embed.to_dict())
    if found_highlow:
        time.sleep(1)
        number = str(embed_with_hint.split("Your hint is ")[1].split(".")[0]).replace("*", "")
        print(number)
        if int(number) > 50:
            await message.channel.send("low")
        if int(number) < 50:
            await message.channel.send("high")
        if int(number) == 50:
            await message.channel.send("high")
    if message.content == ";start" and str(message.author.id) == "664274363243036682":
        while True:
            await message.channel.send("pls beg")
            await asyncio.sleep(1)
            await message.channel.send("pls hunt")
            await asyncio.sleep(1)
            await message.channel.send("pls fish")
            await asyncio.sleep(1)
            await message.channel.send("pls pm")
            await asyncio.sleep(2)
            await message.channel.send("i")
            await asyncio.sleep(1)
            await message.channel.send("pls use padlock")
            await asyncio.sleep(1)
            await message.channel.send("pls search")
            await asyncio.sleep(2)
            await message.channel.send("pls highlow")
            await asyncio.sleep(38)


client.run("nah", bot = False)
