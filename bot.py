import discord
import datetime
import time
import asyncio
import random
import re
items = []
item_ammounts = []
client = discord.Client()
@client.event
async def on_ready():
    print("ready")
@client.event
async def on_message(message):
    global items
    global item_ammounts
    commands_list = ["pls beg", "pls search", "pls hl", "pls trivia", "pls hunt", "pls fish", "pls pm", "pls use padlock"]

    commmands_that_require_items = True
    botter_id = "716742725461868625"

    # Getting inventory items into a list
    found_inventory = False
    embeds = message.embeds
    full_embed_text = ""
    for embed in message.embeds:
        print("embed: " + str(embed.to_dict()))
        full_embed_text += str(embed.to_dict())
    if str(client.user.name) in str(full_embed_text) and "inventory" in str(full_embed_text):
        print("a")
        items_raw = re.findall(r'`.+?`', full_embed_text)
        item_ammounts = []
        items = []
        for i in range(0, len(items_raw)):
            items.append(str(items_raw[i]).replace("`", ""))
        item_ammounts_raw = re.findall(r'\*.+?\\', full_embed_text)
        for i in range(0, len(item_ammounts_raw)):
            if i % 2 == 0:
                item_ammounts.append(str(item_ammounts_raw[i]).split("─ ")[1].split("\\\\")[0].replace("\\", ""))
        print(items)
        print(item_ammounts_raw)
        print(item_ammounts)

    # Selling all the items in the items list
    if str(message.content).startswith(";sell page") and str(message.author.id) == botter_id:
        await message.delete()
        page = str(message.content).split(";sell page ")[1]
        await asyncio.sleep(1)
        await message.channel.send("pls inv " + page)
        await asyncio.sleep(1.5)
        for i in range(0, len(items)):
            await asyncio.sleep(2.5)
            await message.channel.send("pls sell " + items[i] + " " + item_ammounts[i])
    if "Where do you want to search?" in str(message.content) and str("<@" + botter_id + ">") in str(message.content):
        await asyncio.sleep(1)
        item = str(message.content).split(",")[1].replace(",", "").replace("`", "").replace(",", "")
        await message.channel.send(item)

    if "type `" in str(message.content).lower() and message.author.id == "270904126974590976":
        await asyncio.sleep(1)
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
        await asyncio.sleep(1)
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
        await asyncio.sleep(1)
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
        await asyncio.sleep(0.5)
        await message.channel.send("pls use cell")
        await asyncio.sleep(2)
        await message.channel.send("p")
    if message.content == ";start" and str(message.author.id) == botter_id:
        await message.delete()
        while True:
            random_command = 0
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
                    random_command = random.randint(0, len(commands_list)-1)
                    same_command = False
                    if str(random_command) not in sent_commands:
                        await message.channel.send(commands_list[random_command])
                        sent_commands += str(random_command) + ";"
                    else:
                        same_command = True
                        while same_command:
                            random_command = random.randint(0, len(commands_list)-1)
                            if str(random_command) not in sent_commands:
                                same_command = False
                                await message.channel.send(commands_list[random_command])
                                sent_commands += str(random_command) + ";"
                    if random_command == 6:
                        await asyncio.sleep(1)
                        await message.channel.send("i")
                    if random_command == 1 or random_command == 2 or random_command == 3 or random_command == 6:
                        await asyncio.sleep(2)
                    else:
                        await asyncio.sleep(1 + random.randint(0, 2))
            print(sent_commands)
            time = datetime.datetime.strptime("03/02/21 16:30", "%d/%m/%y %H:%M")
            if int(time.hour) == 23:
                await asyncio.sleep(2.5)
                await message.channel.send("pls dep all")
                await asyncio.sleep((8*60*60)-2.5)
            else:
                if random.randint(1, 5) == 2:
                    await asyncio.sleep(1.5)
                    await message.channel.send("pls dep all")
                if random.randint(1, 10) == 5:
                    await asyncio.sleep(15*60)
                else:
                    await asyncio.sleep(40)




client.run("nah", bot = False)
