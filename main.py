import ans
import time
import os
import random
from discord.ext import commands
bot = commands.Bot(command_prefix="-", help_command=None)

env = {
    "BOT_TOKEN": os.environ['BOT_TOKEN']
}

version = "1.0.1"
ips = []
stfu = False

@bot.event
async def on_ready():
  global stfu
  stfu = False

@bot.event
async def on_message(message):
  global messager
  await bot.process_commands(message)
  message.content = message.content.lower()
  messager = message.author
  if message.author.bot or stfu:
    return
  if message.content.startswith("-e"):
    await message.channel.send("https://cdn.discordapp.com/attachments/945230841372626954/983071545004023818/Mio_Honda_telling_you_to_shutup_lol.mp4 \n check out this vid!")
    return
  elif message.content.startswith("-"):
    return
  if ("bot") in message.content:
    current_messager = messager
    await message.channel.send(random.choice(ans.bot))
    CreateIp(random.randint(1,3))
    for ip in ips:
      await message.channel.send(ip)
    await message.channel.send(current_messager.mention + " " + random.choice(ans.ip))
    await message.channel.send(random.choice(ans.kys))
  if random.randint(1, 100) < 10:
    await message.channel.send(random.choice(ans.idk))
  elif random.randint(1, 100) > 90:
    await message.channel.send(random.choice(ans.positive))
  if message.content in ans.sup:
    await message.channel.send(random.choice(ans.sup))
  if message.content.startswith("ğ"):
    await message.channel.send(random.choice(ans.ğ))
  if ("kys") in message.content:
    await message.channel.send(random.choice(ans.kys))
  if ("sik") in message.content:
    message.content = message.content.replace("sik", "**SİK**")
    await message.channel.send(message.content+" "+random.choice(ans.secksemojis))
    await message.channel.send(random.choice(ans.isitsex))
  if ("lmao") in message.content:
    await message.channel.send(random.choice(ans.lmao))
  if ("uwu") in message.content or ("owo") in message.content or ("rawr") in message.content:
    await message.channel.send(random.choice(ans.cute))
  if message.content.startswith("kes") or message.content.startswith("sus"):
    await message.channel.send(random.choice(ans.agresif))
    return
  if ("?") in message.content:
    await message.channel.send(random.choice(ans.soru))
    return
  if ("ily") in message.content:
    if random.randint(1,10) < 5:
      await message.channel.send(ans.heartemoji)
    await message.channel.send(random.choice(ans.ily))
    return
  if (ans.gulentrollemoji) in message.content:
    await message.channel.send(ans.gulentrollemoji)
  if any(i in message.content for i in ans.kufur):
    current_messager = messager
    await message.add_reaction(emoji=random.choice(ans.middlefinger))
    await message.channel.send(str(current_messager.mention)+" "+random.choice(ans.kufurreaction))
    if random.randint(1, 10) > 5:
      CreateIp(random.randint(1,6))
      for ip in ips:
        await message.channel.send(ip)
      await message.channel.send(random.choice(ans.ip))
  if bot.user.mention in message.content:
    current_messager = messager
    await message.channel.send(random.choice(ans.ping))
    if random.randint(1, 100) > 50:
      await message.channel.send(random.choice(ans.howdoesitfeel)+current_messager)
  if (ans.coldemoji) in message.content:
    await message.channel.send("BING CHILLING "+ans.bingchillingemoji)
  if any(i in message.content for i in ans.gl):
    await message.channel.send(random.choice(ans.egegl)+" "+random.choice(ans.iltifat))
  if any(i in message.content for i in ans.kuzey):
    await message.channel.send(random.choice(ans.kuzey)+" "+random.choice(ans.iltifat))
  if ("omg") in message.content:
    await message.channel.send("omg")
  if ("ok") in message.content:
    await message.channel.send("ok")
  if ("idk") in message.content:
    await message.channel.send(message.content+random.choice(ans.either))
    return
  if ("bruh") in message.content:
    await message.channel.send(random.choice(ans.bruhreaction))
    return
  if any(i in message.content for i in ans.neden):
    await message.channel.send(random.choice(ans.bilmem))
    return
  if any(i in message.content for i in ans.horni):
    await message.channel.send(random.choice(ans.hornireaction))

@bot.command()
async def help(ctx):
  await ctx.send("2 commands: stfu & talk. That's it. Enjoy <3")

@bot.command()
async def stfu(ctx):
  global stfu
  if str(ctx.message.author) != ans.user_egegl:
    await ctx.message.add_reaction(emoji=random.choice(ans.middlefinger))
    await ctx.send(random.choice(ans.authfail))
    return
  await ctx.message.add_reaction(emoji=random.choice(ans.owner))
  stfu = True
  await ctx.send(random.choice(ans.stfu))

@bot.command()
async def talk(ctx):
  global stfu 
  if str(ctx.message.author) != ans.user_egegl:
    await ctx.message.add_reaction(emoji=random.choice(ans.middlefinger))
    await ctx.send(random.choice(ans.authfail))
    return
  stfu = False
  await ctx.send(random.choice(ans.ily))

@bot.command()
async def ping(ctx):
    await ctx.send("version **" + version + "**")

def CreateIp(index):
  ips.clear()
  for i in range(index):
    ip = ".".join(map(str, (random.randint(0, 255) for i in range(4))))
    ips.append(ip)

bot.run(env["BOT_TOKEN"])