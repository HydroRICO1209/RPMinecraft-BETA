from discord.ext import commands
import discord

class Database:
    def __init__(self, bot):
        self.bot = bot

    async def fetchvalue(self, item, tablename, userid):
        string1 = f'SELECT $1 FROM {tablename} WHERE playerid = $3'
        return (await self.bot.db.fetchval(string1, str(item), int(userid)))[item]

#async def changevalue(item, tablename, userid, changes):
#   value = (await bot.db.fetch('SELECT $1 FROM $2 WHERE userid = $3', item, tablename, userid))[0][item]
#  value += changes