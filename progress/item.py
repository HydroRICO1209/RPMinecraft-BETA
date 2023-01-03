from discord.ext import commands
import discord

class DatabaseFunc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def fetchvalue(item, tablename, userid):
        return (await bot.db.fetch('SELECT $1 FROM $2 WHERE userid = $3', item, tablename, userid))[0][item]

#async def changevalue(item, tablename, userid, changes):
#   value = (await bot.db.fetch('SELECT $1 FROM $2 WHERE userid = $3', item, tablename, userid))[0][item]
#  value += changes