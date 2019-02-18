import asyncio
import random                           #
import discord                          #
import requests                         #
from discord.ext import commands
from discord.ext.commands import Bot    #
from discord import Game                #
import datetime                         #

BOT_PREFIX = (";;", ".c ")
TOKEN = "NTQ2MjA1MDExNjA5MTI0ODY1.D0lECQ.f8SsnH7KsRaBgNQXUx6LfC8B78E"

client = Bot(command_prefix=BOT_PREFIX)

d = datetime.date.today()                                           # Date

@client.command(name='8ball',                                       # Y/N
                description="Answers yes or no.",
                brief="Answers yes or no.",
                aliases=['eightball', '8b'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'Yes',
        'No'
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@client.command(name='feeli',                                       # Ping that fuck
                aliases=['fee', 'f'],
                description="Pings Guntantrum/Feeli/Yulia/Kamille.",
                brief="Pings Guntantrum/Feeli/Yulia/Kamille",
                pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)                  # 5 second cooldown
async def fee():
    await client.say("<@163059809187397633>")

@client.command(name='ando',                                        # Impersonate Ando
                description="Impersonates Ando.",
                brief="asdf fdsa asdf fdsa asdf fdsa.",
                aliases='a',
                pass_context=True)
@commands.cooldown(3, 9, commands.BucketType.user)                  # 5 second cooldown
async def larousse():
    possible_responses = [
        'asdf',
        'fdsa',
        'AAAAA',
    ]
    await client.say(random.choice(possible_responses))

@client.event
async def on_command_error(error, ctx):
    # This prevents any commands with local handlers being handled here in on_command_error.
    if hasattr(ctx.command, 'on_error'):                            # e/c swap dies here
        return

    ignored = (commands.CommandNotFound, commands.UserInputError)

    # Allows us to check for original exceptions raised and sent to CommandInvokeError.
    # If nothing is found. We keep the exception passed to on_command_error.
    error = getattr(error, 'original', error)

    # Anything in ignored will return and prevent anything happening.
    if isinstance(error, ignored):
        return

    elif isinstance(error, commands.CommandOnCooldown):             # e/c/c/o dies here
        return await client.send_message(ctx.message.channel, "Command in cooldown.")

@client.command(name='dice',                                        # Roll n-sided die k times
                description="Rolls n-sided die.",
                brief="Rolls n-sided die.",
                aliases=['diceroll', 'dr'])
async def diceroll(n, k=1):
    if int(n) < 2:
        await client.say("Yeah nah. I need two or more choices.")
    elif int(n) >= 2 and k == 1:
        await client.say("Rolling " + n + "-sided die once.")
        po = range(1, int(n) + 1)
        await client.say("You rolled a " + str(random.choice(po)) + ".")
    elif int(n) >= 2 and k != 1:
        await client.say("Rolling " + n + "-sided die " + str(k) + " times.")
        j = 1
        values = []
        while j <= int(k):
            po = range(1, int(n) + 1)
            co = random.choice(po)
            values.append(co)
            j += 1
            if j > int(k):
                await client.say(values)

@client.command()                                                   # Bitcoin
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(url)
    value = response.json()['bpi']['USD']['rate']
    await client.say("Bitcoin price is: $" + value)

@client.command(name='fetchtime',
                description="Posts time.",
                brief="Posts local time.",
                aliases=['time', 'ft'])
async def fetchtime():
    t = datetime.datetime.now().time()
    await client.say(str(t.hour) + ":" + str(t.minute) + ":" + str(t.second))

@client.event                                                       # Impersonate Ando
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.content.startswith('fdsa'):
        msg = 'asdf'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('asdf'):
        msg = 'fdsa'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('AAAAA'):
        msg = 'aaaaa...!'.format(message)
        await client.send_message(message.channel, msg)
    await client.process_commands(message)

async def timekeeping():
    while True:
        t = datetime.datetime.now().time()
        if t.minute == 30:
            tks = client.get_server("530183926656925726")
            tkc = tks.get_channel("546223540425195571")
            await client.send_message(tkc, content="It's half past the hour.")
            await asyncio.sleep(30)
        await asyncio.sleep(30)

# @client.event
# async def on_ping(message):
#     if message.content == "<@546205011609124865>":
#         ping = "...".format(message)
#         await client.send_message(message.channel, ping)
#     await client.process_commands(message)
#
# @client.event
# async def on_ping2(message):
#     if message.content.startswith("@Plan C#4950"):
#         ping = "{0.author.mention}".format(message)
#         await client.send_message(message.channel, ping)
#     await client.process_commands(message)

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with Matt"), status=discord.Status.online)  # do_not_disturb
    print("Logged in as " + client.user.name)
    print("Ready.")
    ts = client.get_server("530183926656925726")
    tc = ts.get_channel("546223540425195571")
    await client.send_message(tc, content="Ready.")
    print('------')
    client.loop.create_task(timekeeping())
client.run(TOKEN)

# Remind me
# Reverse image search for pfp
# Translate text
# Translate text in image

# ctx.author => fetches username that used command
