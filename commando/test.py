from discord.ext import commands
import discord
from progress.item import *

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def test(self, ctx, *, arg):
        arglists = arg.split(" ")
        arglen = len(arglists)
        if arglen == 3:
            #item, tablename, userid
            var = await fetchvalue(arglists[0], arglists[1], int(arglists[2]))
            print(var)
        else:
            await ctx.send(f'arglen is only {arglen}, it should be 3 dumb')

async def setup(bot):
    await bot.add_cog(Test(bot))