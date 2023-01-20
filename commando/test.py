from discord.ext import commands
import discord
from progress.stats import *

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def test1(self, ctx, *, arg):
        dbfunc = self.bot.database_handler
        stats = Stats(ctx)
        await ctx.send(stats)
            
    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def test2(self, ctx, *, arg):
        dbfunc = self.bot.database_handler
        
            
async def setup(bot):
    await bot.add_cog(Test(bot))