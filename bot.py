#testing mode

from discord.ext import commands, tasks
import discord
from dataclasses import dataclass
import datetime

FILE_TOKEN = open("C:\\Users\Ethan\Desktop\stuySkyDiscordBot.txt")
print(FILE_TOKEN.read())

BOT_TOKEN = f"{FILE_TOKEN}"
CHANNEL_ID = 1418803172050468956

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

#outputs the date and time after running !date_time
@bot.command()
async def date_time(ctx): 
    date = datetime.datetime.now().strftime("%x")
    print("date is " + date)
    
    time = datetime.datetime.now().strftime("%H:%M:%S")
    print("time is " + time)

    await ctx.send(f"The date is {date} and the time is {time}.")
    
bot.run(BOT_TOKEN)