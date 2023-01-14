from discord.ext import commands
import discord
from progress.stats import *

class Area(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def area(self, ctx, arg: int):
        try:
            dbfunc = self.bot.database_handler
            userid = ctx.author.id
            area = await dbfunc.fetchValue('area', 'stats', userid)
            highestArea = await dbfunc.fetchValue('highest_area', 'stats', userid)
            if 1 <= arg <= 14:
                if arg <= highestArea:
                    await dbfunc.setIntValue('area', 'stats', userid, arg)
                    await ctx.send(f'**{ctx.author.name}** has moved to **AREA {arg}**')
                else:
                    await ctx.send(f'**{ctx.author.name}** fight more bosses to unlock this area :D')
            else:
                await ctx.send('404 area not found')
        except KeyError: #error handler
            await ctx.send(f'**{ctx.author.name}**, your account is either not created yet or not at the latest version. Try using `rpm start`')

async def setup(bot):
    await bot.add_cog(Area(bot))