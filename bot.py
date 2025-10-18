#testing mode

import requests
from discord.ext import commands, tasks
import discord
from dataclasses import dataclass

import datetime

import nasapy
import os
import random
import apodBackup

## NWS/NOAA API SIDE

headers = {'StuySkyWeatherBot' : 'StuySky'}

STUY_LAT = 40.7127
STUY_LON = -74.0061

#put this for commands needing the weather API

''' 
endpoint = 'https://api.weather.gov/INSERT_ENDPOINT_HERE'
response = requests.get(endpoint, headers = headers)
data = response.json()

print(data) 

'''

## NASA API SIDE
NASA_KEY = "vwwlK5uqo0BRhb4H0J6KRWgGailqnGK93lC5cdDT"
nasa = nasapy.Nasa(key=NASA_KEY)


## DISCORD SIDE

BOT_TOKEN = "MTQyNDUxMTg3Mzk3NzU0ODkwMA.GaUMX4.0OvFNenam5qie-4Sy3z7trprT_AUG72mAQJHYo"
CHANNEL_ID = 1418744998459084992

intents = discord.Intents.all()
activity = discord.Activity(type=discord.ActivityType.custom, name="and testing the code")
status = discord.Status.do_not_disturb
bot = commands.Bot(command_prefix="!", intents=intents, activity=activity, status=status, help_command=None)


## MIXED SIDE


# Commands with no API

@bot.command() 
async def info(ctx):
    _ = "`!_` \n"
    infoinfo = "`!info gives this list, the list of commands` \n"
    datetimeinfo = "`!date_time gives the current date and time` \n"
    currentstuyweatherinfo = "`!cstuy or !currentstuyweather gives the weather at Stuyvesant High School` \n"
    pointforecastinfo = "`!cpoint LATITUDE LONGITUDE gives the weather at LATITUDE, LONGITUDE, put lat and lon with no additions like !pointforecast 40.7127 -74.0061` \n"
    apodinfo = "`!apodinfo gives the astronomy picture of the day` \n"    
    
    await ctx.send(f"{infoinfo}\n{datetimeinfo}\n{currentstuyweatherinfo}\n{pointforecastinfo}\n{apodinfo}")

@bot.command()
async def logo(ctx):
    await ctx.send(file=discord.File('StuySkyLogo.png'))

#gives current date and time
@bot.command()
async def date_time(ctx): 
    date = datetime.datetime.now().strftime("%x")
    print("date is " + date)
    
    time = datetime.datetime.now().strftime("%H:%M:%S")
    print("time is " + time)
    
    await ctx.send(f"The date is {date} and the time is {time}.")
    

# Commands using the Weather API

#gives the weather at point lat, lon
@bot.command()
async def cpoint(ctx, lat, lon):
    try:
        #gets data at lat and lon coordinates
        endpoint = f'https://api.weather.gov/points/{lat},{lon}'
        print(lat)
        print(lon)
        print(endpoint)
        response = requests.get(endpoint, headers = headers)
        data = response.json()
        
        
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
        await ctx.send(f'The following information is about {timeOfDay} on {date} at {lat} latitude and {lon} longitude. The temperature is {temp}{tempUnit}. The wind speed is {windSpeed} coming from {windDir}.')   

    except:
        await ctx.send(f"Sorry, we don't have data for {lat}° latitude and {lon}° longitude right now.")

#gives the weather at stuy
@bot.command()
async def cstuy(ctx):   
    try:
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
        shortForecast = forecast["shortForecast"]
        
        await ctx.send(f'The following information is about {timeOfDay} on {date} at Stuy. The temperature is {temp}{tempUnit}. The wind speed is {windSpeed} coming from {windDir}. It should be {shortForecast}.')   
    except:
        await ctx.send(f"Sorry, we don't have data at Stuy right now.")

#gives the weather at stuy
@bot.command()
async def currentstuyweather(ctx):
    try:
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
        shortForecast = forecast["shortForecast"]
        
        await ctx.send(f'The following information is about {timeOfDay} on {date} at Stuy. The temperature is {temp}{tempUnit}. The wind speed is {windSpeed} coming from {windDir}. It should be {shortForecast}.')   
    except:
        await ctx.send(f"Sorry, we don't have data at Stuy right now.")


# Commands using NASA's APIs

#gives astronomy picture of the day
@bot.command()
async def apod(ctx):
    try:
        d = datetime.today().strftime('%Y-%m-%d')
        print(d)
        apod = nasa.picture_of_the_day(date=d, hd=True)
        print(apod)
        apod_json = apod.json()
        print(apod_json)
        image_url = apod_json['url']
        print(image_url)
        await ctx.send(image_url)
    except:
        basepath = './apodBackup'
        print(os.listdir(basepath))
        image = random.choice(os.listdir(basepath))
        print(image)
        
        n = 2
        for i in range(0,n):
            if i == 0:
                await ctx.send(f"Sorry, this is unavailable right now. Try one of these ones from the website: ")
            else:
                await ctx.send(file=discord.File(basepath+f"/{image}"))

#sends to bot in discord
bot.run(BOT_TOKEN)