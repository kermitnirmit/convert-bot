import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import os
import time
import pymongo
import random
import string
from pymongo import MongoClient
from currency_converter import CurrencyConverter


MONGODB_URI = "mongodb://cookie1:cookie@ds229290.mlab.com:29290/cookiecount"
mongoc = MongoClient(MONGODB_URI, connectTimeoutMS=30000)
db = mongoc.get_default_database()
cookies = db.cookies
Client = discord.Client()
client = commands.Bot(command_prefix = "")
# c = CurrencyConverter()
@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(message):
    if message.author.id != "435229925503533057":
        if message.content.lower().startswith("conv"):
            if message.content.lower().endswith("cm"):
                end = len(message.content) - 2
                old = float(message.content[4:end])
                newF = old / 2.54
                toReturn = str(newF)
                await client.send_message(message.channel, message.content[4:end]+ "cm is " + toReturn + "in")
            if message.content.lower().endswith("in"):
                end = len(message.content) - 2
                old = float(message.content[4:end])
                newF = old * 2.54
                toReturn = str(newF)
                await client.send_message(message.channel, message.content[4:end]+ "in is " + toReturn + "cm")
            if message.content.lower().endswith("c"):
                end = len(message.content) - 1
                old = float(message.content[4:end])
                newF = (old * 1.8) + 32
                toReturn = str(newF)
                await client.send_message(message.channel, message.content[4:end]+ "C is " + toReturn + "F")
            if message.content.lower().endswith("f"):
                end = len(message.content) - 1
                old = float(message.content[4:end])
                newC = (old - 32) / 1.8
                toReturn = str(newC)
                await client.send_message(message.channel, message.content[4:end]+ "F is " + toReturn + "C")    
            if message.content.lower().endswith("mi"):
                end = len(message.content) - 2
                old = float(message.content[4:end])
                newC = old * 1.6
                toReturn = str(newC)
                await client.send_message(message.channel, message.content[4:end]+ "mi is " + toReturn + "km")
            if message.content.lower().endswith("miles"):
                end = len(message.content) - 5
                old = float(message.content[4:end])
                newC = old * 1.6
                toReturn = str(newC)
                await client.send_message(message.channel, message.content[4:end]+ "mi is " + toReturn + "km")
            if message.content.lower().endswith("km"):
                end = len(message.content) - 2
                old = float(message.content[4:end])
                newC = old * 0.62
                toReturn = str(newC)
                await client.send_message(message.channel, message.content[4:end]+ "km is " + toReturn + "mi")
            if message.content.lower().endswith("kg"):
                end = len(message.content) - 2
                old = float(message.content[4:end])
                newC = old * 2.21
                toReturn = str(newC)
                await client.send_message(message.channel, message.content[4:end]+ "kg is " + toReturn + "lbs")
            if message.content.lower().endswith("lbs"):
                end = len(message.content) - 3
                old = float(message.content[4:end])
                newC = old / 2.21
                toReturn = str(newC)
                await client.send_message(message.channel, message.content[4:end]+ "lbs is " + toReturn + "kg")    
        if message.content.lower().find("shut up nirmit") > -1:
            await client.send_message(message.channel, "https://media.giphy.com/media/3URfnnO4xuMaQ/giphy.gif")
        if message.content.lower().find("cookiecount") > -1:
            toReturn = str(getCookies())
            await client.send_message(message.channel, "I've given " + toReturn + " cookies so far")
        if message.content.lower().find("t know her") > -1 or message.content.lower().find("dk her") > -1:
            await client.send_message(message.channel, "But I do")
        if message.content.lower().find("big mood") > -1:
            serv = getServer()
            setCookies(serv, 3)
            await client.send_message(message.channel, "Y"+ ":cookie:"+ "U NEED A FEW C" + ":cookie:" + ":cookie:" + "KIES")
        elif message.content.lower().find("mood") > -1:
            serv = getServer()
            setCookies(serv, 1)
            await client.send_message(message.channel, "Here's a :cookie:")
        if message.content.lower().endswith("wh") or message.content.lower().endswith("i just") or message.content.lower().find("cecil") > -1:
            leng = random.randint(12,26)
            print(leng)
            toReturn = ""
            for x in range(1, leng):
                toReturn = toReturn + random.choice(string.ascii_lowercase)
            await client.send_message(message.channel, toReturn)
        if message.content.lower().startswith("help me mermet"):
            serv = getServer()
            setCookies(serv, 1)
            await client.send_message(message.channel, "Hi, I help with converting and mood boosting. \nI convert km/mi, kg/lbs, cm/in, and Celsius/Fahrenheit. \nTo convert, type: `conv 123F` \nto convert to Celsius and in that format for any other conversions. \n\n I also convert currencies. \nTo convert, type: `$$ 123 USD to EUR` to convert USD to EUR (for example). \n\nHere's a :cookie: for asking. Hope you like it! PM kermitnirmit if you need more help or have any suggestions!\n\n\nP.s. try typing cookiecount.")
        chance = random.randint(1,1000)
        if chance > 990:
            leng = random.randint(12,26)
            print(leng)
            toReturn = ""
            for x in range(1, leng):
                toReturn = toReturn + random.choice(string.ascii_lowercase)
            await client.send_message(message.channel, toReturn)
        elif message.author.id == "215984308303691777":
            if chance > 200:
                leng = random.randint(20,35)
            print(leng)
            toReturn = ""
            for x in range(1, leng):
                toReturn = toReturn + random.choice(string.ascii_lowercase)
            await client.send_message(message.channel, toReturn)
        if message.content.lower().find("despacito") > -1:
            await client.send_message(message.channel, "2")
        if message.author.id == "193934721921581057" and message.content.lower().find("hungry") > -1:
            await client.send_message(message.channel, "eat something")
        messagetext = message.content
        if messagetext.startswith("$$"):
            words = messagetext.split()
            # words should be ['$$', '12.121', 'USD' 'to/in/whatever', 'EUR']
            if len(words) != 5:
                pass
            else:
                toSend = currConvert(words)
                await client.send_message(message.channel, toSend)
def currConvert(words):
    c = CurrencyConverter("http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip")
    q, origV, origC, w, finalC = words
    origV = float(origV)
    try: 
        finalV = c.convert(origV, origC, finalC)
        rounded = round(finalV, 2)
        toReturn = str(origV) + " " + str(origC) + " is " + str(rounded) + " " + str(finalC)
        return toReturn
    except ValueError:
        return "Wrong currency names, try again."

def getServer():
    serv = cookies.find_one({"server":"ksas"})
    return serv
def getCookies():
    cook = cookies.find_one({"server":"ksas"})
    toReturn = cook['count'] 
    return toReturn
def setCookies(serv, inc):
    newC = getCookies() + inc
    update = {
        "count": newC
    }
    cookies.update_one({'_id': serv['_id']}, { '$set': update}, upsert=False)
client.run(os.environ['TOKEN'])