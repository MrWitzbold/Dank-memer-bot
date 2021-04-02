import discord
import datetime
import time
import asyncio
import random

client = discord.Client()
@client.event
async def on_ready():
    print("ready")
@client.event
async def on_message(message):
    commands_list = ["pls beg", "pls search", "pls hl", "pls trivia", "pls hunt", "pls fish", "pls pm", "pls use padlock"]

    commmands_that_require_items = False
    botter_id = "820162513873272833"

    if str(message.author.id) == "270904126974590976":
        print(message.content)
    if "Where do you want to search?" in str(message.content) and str("<@" + botter_id + ">") in str(message.content):
        await asyncio.sleep(1.5)
        item = str(message.content).split(",")[1].replace(",", "").replace("`", "")
        await message.channel.send(item)

    if "type `" in str(message.content).lower() and message.author.id == "270904126974590976":
        await asyncio.sleep(1.5)
        word = str(message.content).lower().split("type `")[1].replace("`", "")
        await asyncio.sleep(1)
        await message.channel.send(word)
    found_highlow = False
    found_name_hl = False
    embeds = message.embeds
    embed_with_hint = 0
    for embed in embeds:
        if "Your hint is " in str(embed.to_dict()):
            found_highlow = True
            embed_with_hint = str(embed.to_dict())
    if found_highlow:
        await asyncio.sleep(1.5)
        number = str(embed_with_hint.split("Your hint is ")[1].split(".")[0]).replace("*", "")
        print(number)
        if int(number) > 50:
            await message.channel.send("low")
        if int(number) < 50:
            await message.channel.send("high")
        if int(number) == 50:
            await message.channel.send("high")

    found_trivia = False
    trivia_embed = message.embeds
    for embed in embeds:
        await asyncio.sleep(1.5)
        if "trivia" in str(embed.to_dict()):
            choice = random.randint(0, 3)
            if choice == 0:
                await message.channel.send("a")
            if choice == 1:
                await message.channel.send("b")
            if choice == 2:
                await message.channel.send("c")
            if choice == 3:
                await message.channel.send("d")
    if "bank robbery" in str(message.content) and str(client.user.name) in str(message.content):
        await asyncio.sleep(1.5)
        await message.channel.send("pls use cell")
        await asyncio.sleep(2)
        await message.channel.send("p")
    if message.content == ";start" and str(message.author.id) == "664274363243036682":
        while True:
            sent_commands = ""
            if commmands_that_require_items is False:
                for i in range(0, 3):
                    random_command = random.randint(0, 3)
                    same_command = False
                    if str(random_command) not in sent_commands:
                        await message.channel.send(commands_list[random_command])
                    else:
                        same_command = True
                        while same_command:
                            random_command = random.randint(0, 3)
                            if str(random_command) not in sent_commands:
                                same_command = False
                                await message.channel.send(commands_list[random_command])
                    await asyncio.sleep(1 + random.randint(0, 1))
                    sent_commands += str(random_command) + ";"
                    print(sent_commands)
            if commmands_that_require_items:
                for i in range(0, len(commands_list)):
                    random_command = random.randint(0, len(commands_list))
                    same_command = False
                    if str(random_command) not in sent_commands:
                        await message.channel.send(commands_list[random_command])
                    else:
                        same_command = True
                        while same_command:
                            random_command = random.randint(0, len(commands_list))
                            if str(random_command) not in sent_commands:
                                same_command = False
                                await message.channel.send(commands_list[random_command])
                    if random_command == 1 or random_command == 2 or random_command == 3 or random_command == 6:
                        await asyncio.sleep(2)
                    else:
                        await asyncio.sleep(1 + random.randint(0, 2))
                    sent_commands += str(random_command) + ";"
                    print(sent_commands)
            await asyncio.sleep(35)




client.run("nah", bot = False)
