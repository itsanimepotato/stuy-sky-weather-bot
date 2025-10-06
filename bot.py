#testing mode

## WEATHER API SIDE
import requests

headers = {'StuySkyWeatherBot' : 'Ethan Cheung'}

STUY_LAT = 40.7127
STUY_LON = -74.0061

''' 

headers = {'StuySkyWeatherBot' : 'Ethan Cheung'}

endpoint = 'https://api.weather.gov/glossary'
response = requests.get(endpoint, headers = headers)
data = response.json()

# `features` contains the data we want.
print(data) 

'''

## DISCORD SIDE

from discord.ext import commands, tasks
import discord
from dataclasses import dataclass
import datetime

BOT_TOKEN = "MTQyNDUxMTg3Mzk3NzU0ODkwMA.GaUMX4.0OvFNenam5qie-4Sy3z7trprT_AUG72mAQJHYo"
CHANNEL_ID = 1418744998459084992

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

#outputs the date and time after running !date_time
@bot.command()
async def date_time(ctx): 
    date = datetime.datetime.now().strftime("%x")
    print("date is " + date)
    
    time = datetime.datetime.now().strftime("%H:%M:%S")
    print("time is " + time)

    await ctx.send(f"The date is {date} and the time is {time}.")
    
@bot.command()
async def info(ctx):
    datetimeinfo = "`!date_time` gives the current date and time \n"
    currentstuyweatherinfo = "`!currentstuyweather` gives the weather at Stuyvesant High School \n"
    pointforecastinfo = "`!pointforecast LATITUDE LONGITUDE` gives the weather at LATITUDE, LONGITUDE with no North South East West, like instead of 10N put 10\n"
    
    await ctx.send(f"{datetimeinfo}{currentstuyweatherinfo}{pointforecastinfo}")
    

## MIXED SIDE

@bot.command()
async def pointforecast(ctx, lat, lon): 
    
    #gets data at lat and lon coordinates
    endpoint = f'https://api.weather.gov/points/{lat},{lon}'
    print(endpoint)
    response = requests.get(endpoint, headers = headers)
    data = response.json()
    
    '''
    #gets all links about at pt (hourly daily etc)
    links = data["forecastGridData"]
    print(links)
    
    #gets link relating to daily forecast at pt
    forecast_link = data["properties"]["forecast"]
    print(forecast_link)
    
    #retrieves forecast data at coordinates
    forecast_response = requests.get(forecast_link, headers = headers)
    forecast_data = forecast_response.json()
    print(forecast_data)
    
    #gets most recently updated forecast for next period (for example: Monday, Monday Night, Tuesday, etc.)
    forecast = forecast_data["properties"]["periods"][0]
    
    timeOfDay = forecast["name"]
    date = datetime.datetime.now().strftime("%x")
    temp = forecast["temperature"]
    tempUnit = forecast["temperatureUnit"]
    windSpeed = forecast["windSpeed"]
    windDir = forecast["windDirection"]
    '''
    
    await ctx.send(f'The following information is about {timeOfDay} on {date} at {lat} latitude and {lon} longitude. The temperature is {temp}{tempUnit}. The wind speed is {windSpeed} coming from {windDir}.')   

    
@bot.command()
async def currentstuyweather(ctx):
    
    #gets data at stuy coordinates
    endpoint = f'https://api.weather.gov/points/{STUY_LAT},{STUY_LON}'
    print(endpoint)
    response = requests.get(endpoint, headers = headers)
    data = response.json()
    
    #gets all links about at stuy (hourly daily etc)
    links = data["properties"]
    print(links)
    
    #gets link relating to daily forecast at stuy
    forecast_link = data["properties"]["forecast"]
    print(forecast_link)
    
    #retrieves forecast data at stuy coordinates
    forecast_response = requests.get(forecast_link, headers = headers)
    forecast_data = forecast_response.json()
    print(forecast_data)
    
    #gets most recently updated forecast for next period (for example: Monday, Monday Night, Tuesday, etc.)
    forecast = forecast_data["properties"]["periods"][0]
    
    timeOfDay = forecast["name"]
    date = datetime.datetime.now().strftime("%x")
    temp = forecast["temperature"]
    tempUnit = forecast["temperatureUnit"]
    windSpeed = forecast["windSpeed"]
    windDir = forecast["windDirection"]
    
    await ctx.send(f'The following information is about {timeOfDay} on {date} at Stuy. The temperature is {temp}{tempUnit}. The wind speed is {windSpeed} coming from {windDir}.')   

    
#sends to bot in discord
bot.run(BOT_TOKEN)