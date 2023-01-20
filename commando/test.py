from discord.ext import commands
import discord
from progress.stats import *

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def test1(self, ctx):
        dbfunc = self.bot.database_handler
        stats = await Stats(ctx)
        await ctx.send(stats['area'])
            
    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def test2(self, ctx, *, arg):
        dbfunc = self.bot.database_handler
        stats = await Stats(ctx)
        await ctx.send(stats[arg])
            
async def setup(bot):
    await bot.add_cog(Test(bot))